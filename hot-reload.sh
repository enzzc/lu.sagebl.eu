#!/bin/bash
inotifywait -m src -e CLOSE_WRITE | while read -r f; do [[ "$f" =~ "\.html$" ]] && ./build.py; done
