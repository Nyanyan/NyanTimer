#!/bin/sh

for file in *; do
    eval "git rm --cached ${file}"
    echo "git rm --cached ${file}"
done
