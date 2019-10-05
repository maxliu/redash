#!/usr/bin/env bash

source build.config

docker build -t ${IMN}:${VER} \
		-t ${IMN}:latest  .

