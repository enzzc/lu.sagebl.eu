# lu.sagebl.eu: source and generator

This repository contains the source code of the website, as well as the _ad hoc_
static website generator.
This static website generator is a bit special.

First, pages are written
as plain HTML fragments (without header or footer), e.g.:

```html
<main>
  <article>
    <h1>Hello, World!</h1>
    <p>
      ...
      ...
    </p>
  </article>
</main>
```

Second, `build.py` only produces a `build.ninja` file which describes the
dependency graph. The [Ninja build system](https://ninja-build.org/) then
generates the final HTML files into `www/` (The `src/` hierarchy is mapped into
`www/`.)

Dependencies:
 * Python 3
 * `ninja`
 * `inotifywait` (if `hot-reload.sh` is used)
 * Basic UNIX tools such as `cat`, `sed`, etc.

## Usage

Edit `src/something.html`, then run:

```console
$ ./build.py
```

Then push the content of `www/` to the adequate destination.

### Hot-reload

```console
$ ./hot-reload.sh
```
