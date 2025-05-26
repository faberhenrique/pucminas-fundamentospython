#!/bin/bash
black .
isort .
autoflake --in-place --remove-unused-variables --remove-all-unused-imports -r .