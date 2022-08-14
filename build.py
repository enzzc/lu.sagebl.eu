#!/usr/bin/env python3

import os
import re
from pathlib import Path

src = 'src'
dest = 'www'

header = 'header.html'
footer = 'footer.html'

default_title = "Lu's Website"


pattern = re.compile(r'<h1>(.+)</h1>')

with open('build.ninja', 'w') as f:
    f.write(f'''# Code generated. DO NOT EDIT.

rule justhtml
  command = cat $in | sed 's/:TITLE/$title/g' > $out
  description = $in -> $out

''')
    for hfile in Path(src).glob('**/*.html'):
        stem = hfile.parent / hfile.stem
        stem = str(stem).removeprefix(f'{src}/')
        if stem == 'index':
            continue

        # Fetch title (first <h1>)
        content = hfile.read_text(encoding='utf-8')
        m = pattern.findall(content)
        if not m:
            title = default_title
        else:
            title = m[0].strip()

        f.write(f'build {dest}/{stem}/index.html: justhtml {header} {hfile} {footer}\n  title = {title}\n')

    indexfile = Path(src) / 'index.html'
    if indexfile.is_file():
        f.write(f'build {dest}/index.html: justhtml {header} {indexfile} {footer}\n  title = Home\n')

os.system('ninja')
