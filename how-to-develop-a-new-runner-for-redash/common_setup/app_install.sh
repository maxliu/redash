#!/usr/bin/env bash

sudo apt update

sudo apt install -y git  vim tmux mc htop openssh-server python3-pip openconnect bridge-utils

rm -rf ~/.vim
cd ~
git clone https://github.com/maxliu/.vim.git
cd ~/.vim
bash ./cpCONF.sh

pip3 install matplotlib


cd ~

git config --global user.email 'xinyulrsm@gmail.com'

git config --global user.name 'maxliu'

git config --global credential.helper cache

git config --global credential.helper 'cache --timeout=3600000'

