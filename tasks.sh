#!/bin/bash

# activate the project virtual environment
source venv/bin/activate

# execute the test suite.
pytest

# return exit code 0 if all tests passed, or 1 if something went wrong.
if [ $? -eq 0 ]; then
    echo "Passed tests successfully"
    exit 0
else
    echo "Tests failed or encountered an error."
    exit 1
fi