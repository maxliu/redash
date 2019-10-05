#!/usr/bin/env bash

sudo /etc/init.d/ssh start
vncserver :1 -geometry 1280x800 -depth 24 

cd /home/maxliu/mycode

# /home/maxliu/mycode/jus3.sh

bash