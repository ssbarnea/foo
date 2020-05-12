#!/bin/bash
set -x

for PYTHON in $(which python3.8 python3.7 python3.6); do
    export PINNED_PYTHON=`$PYTHON --version`
    echo "Testing pinning $PYTHON with tox:"
    tox --discover "$PYTHON" -re devel
done
