#!/bin/bash

git log --format='%aN <%aE>' | sort | uniq > AUTHORS.new
if ! cmp -s AUTHORS AUTHORS.new; then
    mv AUTHORS.new AUTHORS
    echo "AUTHORS file updated."
    exit 1
else
    rm AUTHORS.new
    echo "AUTHORS file is up-to-date."
    exit 0
fi
