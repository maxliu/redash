#!/usr/bin/env bash

source build.config

docker rm conda_test

docker run -it \
  --name conda \
	-p 9988:8888 -p 9991:5901  -p 9922:22 \
	-v ~/dropbox:/home/maxliu/dropbox \
	-v ~/dropbox/mycode:/home/maxliu/mycode  \
	-v ~/redashlrsm:/home/maxliu/mycode/0_python_learn/my_learn/isc_cache/dev/redash  \
	 ${IMN}:latest


# 	-v /home:/home/maxliu/mycode  \
# -v ~/mycode:/home/maxliu/mycode \
