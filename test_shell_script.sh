#!/bin/bash

set -eu

if pytest
then
git add test_shell_script.sh
git commit -m "${1}"

else
echo "Test Failed!!! Canceling Commit"
fi
