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



# cd ~

# git clone https://github.com/getredash/redash.git

# remove old one

# cd ~/redash
# sudo apt update -y
# sudo apt-get remove docker docker-engine docker.io containerd runc

# 	# update
# 	sudo apt-get update -y

# 	# Install packages to allow apt to use a repository over HTTPS
# 	sudo apt-get install \
# 		    apt-transport-https \
# 		    ca-certificates \
# 		    curl \
# 		    gnupg-agent \
# 		    software-properties-common -y

# 	# Add Docker’s official GPG key
# 	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 	sudo apt-key fingerprint 0EBFCD88

# 	# Use the following command to set up the stable repository.
# 	sudo add-apt-repository \
# 		   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
# 		   $(lsb_release -cs) \
# 		   stable"

# 	# update again
# 	sudo apt-get update

# 	# install
# 	sudo apt-get install docker-ce docker-ce-cli containerd.io


# 	# add user to docker group so that don't have to use 'sudo' everytime
# 	sudo groupadd docker
# 	sudo usermod -aG docker $USER

# 	sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 	sudo chmod +x /usr/local/bin/docker-compose
