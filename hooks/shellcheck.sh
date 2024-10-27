#!/bin/bash

set -e

find . -type f -name '*.sh' -exec shellcheck {} +
