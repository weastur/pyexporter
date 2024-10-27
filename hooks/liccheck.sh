#!/bin/bash

set -e

uv pip freeze > requirements.txt
liccheck -l PARANOID
