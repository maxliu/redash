#!/usr/bin/env bash


docker build --build-arg INCUBATOR_VER=$(date +%s) -t redash/redash:liu2 .
