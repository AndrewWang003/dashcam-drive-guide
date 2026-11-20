"""Keep the code that all Matrix guides share identical in every guide repository.

    python3 tools/shared.py check ../other-guide     # report every shared block that differs (exit code 1)
    python3 tools/shared.py copy  ../other-guide     # copy this guide's shared blocks and files into the other guide

Run it from the root of a guide repository, with the other guide's repository beside it.

Shared blocks are marked in index.html, in CSS / JS comments or HTML comments:

    /* SHARED:name */ ... /* /SHARED:name */
    <!-- SHARED:name --> ... <!-- /SHARED:name -->

Everything between the two markers must be the same in every guide. A guide may leave a block out; it is then
reported but not an error. Shared files (the whole file is shared): GUIDE-PRINCIPLES.md and this script.

To change shared code: change it in one guide, test it there, run `copy` to each other guide, test those too,
and commit all of them in the same piece of work (GUIDE-PRINCIPLES.md section 9).
"""
import os, re, sys

FILES = ['GUIDE-PRINCIPLES.md', 'tools/shared.py']
PAGE = 'index.html'
BLOCK = re.compile(r'(/\*|<!--) SHARED:([\w-]+) (\*/|-->)(.*?)(/\*|<!--) /SHARED:\2 (\*/|-->)', re.S)


def blocks(text):
    out = {}
    for m in BLOCK.finditer(text):
        name = m.group(2)
        if name in out:
            sys.exit(f'{PAGE}: block {name} appears twice')
        out[name] = m
    return out


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ('check', 'copy'):
        sys.exit(__doc__)
    mode, other = sys.argv[1], sys.argv[2]
    here_page, other_page = read(PAGE), read(os.path.join(other, PAGE))
    mine, theirs = blocks(here_page), blocks(other_page)
    problems = []

    for name in sorted(set(mine) | set(theirs)):
        if name not in theirs:
            print(f'  {name}: only in this guide')
        elif name not in mine:
            print(f'  {name}: only in {other}')
        elif mine[name].group(4) != theirs[name].group(4):
            problems.append(name)
            print(f'  {name}: DIFFERENT')
        else:
            print(f'  {name}: same')
    for f in FILES:
        same = os.path.exists(os.path.join(other, f)) and read(f) == read(os.path.join(other, f))
        print(f'  {f}: {"same" if same else "DIFFERENT"}')
        if not same:
            problems.append(f)

    if mode == 'check':
        if problems:
            sys.exit(f'{len(problems)} shared part(s) differ: {", ".join(problems)}. '
                     'Decide which guide has the right version, then run copy from that guide.')
        print('all shared parts are the same')
        return

    # copy: replace each shared block in the other page with this guide's version (only blocks both pages have)
    text = other_page
    for name in [n for n in problems if n in mine and n in theirs]:
        m = blocks(text)[name]
        text = text[:m.start(4)] + mine[name].group(4) + text[m.end(4):]
    with open(os.path.join(other, PAGE), 'w', encoding='utf-8') as f:
        f.write(text)
    for f in FILES:
        os.makedirs(os.path.dirname(os.path.join(other, f)) or '.', exist_ok=True)
        with open(os.path.join(other, f), 'w', encoding='utf-8') as out:
            out.write(read(f))
    print(f'copied {len(problems)} part(s) to {other}. Test that guide, then commit both.')


if __name__ == '__main__':
    main()
