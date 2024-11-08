#!/bin/bash

printf "# Credits\n\n" > CREDITS.md.new
git log --format='%aN <%aE>' | sort | uniq >> CREDITS.md.new
if ! cmp -s CREDITS.md CREDITS.md.new; then
    mv CREDITS.md.new CREDITS.md
    echo "CREDITS file updated."
    exit 1
else
    rm CREDITS.md.new
    echo "CREDITS file is up-to-date."
    exit 0
fi
