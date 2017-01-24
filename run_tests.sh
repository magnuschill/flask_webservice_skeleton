#!/usr/bin/env bash

# Uses python coverage to run all tests and aggregate coverage information
rm .coverage*
find ./tests -name "test_*.py" | xargs -n 1 coverage run -p --source APPLICATIONNAME
coverage combine
coverage report -m
