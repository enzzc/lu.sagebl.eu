#!/bin/python3

import os
from pathlib import Path
from tempfile import mkdtemp

src = 'src'
dest = 'www'
global_deps = ' '.join([
    'header.html',
    'footer.html',
])


with open('build.ninja', 'w') as f:
    f.write(f'''# Code generated. DO NOT EDIT.

rule md2html
  command = cmark $in | cat header.html - footer.html > $out
  description = $in -> $out

rule justhtml
  command = cat header.html $in footer.html > $out
  description = $in -> $out

''')
    for mdfile in Path(src).glob('**/*.md'):
        stem = mdfile.parent / mdfile.stem
        stem = str(stem).removeprefix(f'{src}/')
        if stem == 'index':
            print(f'Ignore {mdfile}')
            continue
        f.write(f'build {dest}/{stem}/index.html: md2html {mdfile}\n')

    for hfile in Path(src).glob('**/*.html'):
        stem = hfile.parent / hfile.stem
        stem = str(stem).removeprefix(f'{src}/')
        f.write(f'build {dest}/{stem}/index.html: justhtml {hfile}\n')

    indexfile = Path(src) / 'index.html'
    if indexfile.is_file():
        f.write(f'build {dest}/index.html: justhtml {indexfile}\n')

os.system('ninja')
