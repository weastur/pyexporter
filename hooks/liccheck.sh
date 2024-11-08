#!/bin/bash

set -e

uv pip freeze > requirements.txt
uv run liccheck -l PARANOID
