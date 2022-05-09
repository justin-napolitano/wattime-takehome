#!/bin/bash
#doitscript

git pull && make clean && make html && git add . && git commit && git push
