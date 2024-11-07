#!/bin/bash

printf "# Authors\n\n" > AUTHORS.md.new
git log --format='%aN <%aE>' | sort | uniq >> AUTHORS.md.new
if ! cmp -s AUTHORS.md AUTHORS.md.new; then
    mv AUTHORS.md.new AUTHORS.md
    echo "AUTHORS file updated."
    exit 1
else
    rm AUTHORS.md.new
    echo "AUTHORS file is up-to-date."
    exit 0
fi
