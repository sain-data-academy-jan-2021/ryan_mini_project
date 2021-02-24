#!/bin/bash

set -eu

if pytest -v
then
git add ${1}
git commit -m "${2}"

else
echo "Test Failed!!! Canceling Commit"
fi
