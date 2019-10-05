# how-to-develop-a-new-runner-for-redash 

ref: [redash_dev](https://redash.io/help/open-source/dev-guide/docker)

steps and resources for developing a new query runner for redash


## get / clone a new Ubuntu 18.04 VM
```shell
	$ sudo apt install -y git  vim-nox tmux mc htop 
```

## install Docker to Ubuntu [link](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
	
```shell
	# remove old one
	$ sudo apt-get remove docker docker-engine docker.io containerd runc
	
	# update
	$ sudo apt-get update
	
	# Install packages to allow apt to use a repository over HTTPS
	$ sudo apt-get install \
		    apt-transport-https \
		    ca-certificates \
		    curl \
		    gnupg-agent \
		    software-properties-common
		    
	# Add Docker’s official GPG key
	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	$ sudo apt-key fingerprint 0EBFCD88
	
	# Use the following command to set up the stable repository.
	$ sudo add-apt-repository \
		   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
		   $(lsb_release -cs) \
		   stable"
	
	# update again
	$ sudo apt-get update
	
	# install
	$ sudo apt-get install docker-ce docker-ce-cli containerd.io
	
	# add user to docker group so that don't have to use 'sudo' everytime
	$ sudo groupadd docker
	$ sudo usermod -aG docker $USER

	# reboot	
	$ sudo reboot
	
	# run the command to test 
	$ docker ps 
	
```

## install docker-compose to Ubuntu 18.04 [link](https://docs.docker.com/compose/install/)

```shell
	$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	
	$ sudo chmod +x /usr/local/bin/docker-compose
	
	# test
	$ docker-compose --version
	
	# might need the following
	$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

```

## install node.js  [link](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04)

```shell
	$ sudo apt update
	$ sudo apt install nodejs
```

## install npm packages
```shell
	$ npm install
	$ npm run build
	
	# if work on front end code, run below
	$ npm run start
```

## Clone the Git repository then modify files
```shell
	cd ~
	git colone https://github.com/maxliu/how-to-develop-a-new-runner-for-redash.git
	cd ~
	git clone https://github.com/getredash/redash.git
	
	cd how-to-develop-a-new-runner-for-redash
	
	cp intersyscache.py ~/redash/redash/query_runner
	cp intersyscache_test.py ~/redash/redash/query_runner
	cp intersystems-jdbc-3.0.0.jar   ~/redash
	cp cache-jdbc-2.0.0.jar    ~/redash
	
	cp re*.txt  ~/redash
	
	cp Dockerfile   ~/redash
	cp docker-compose.yml   ~/redash
	
	## add the following to ~/redash/redash/settings/__init__.py in the default_query_runners session
	
		'redash.query_runner.intersyscache'
	
```

## build new docker image and create docker services
```shell
	$ cd redash
	$ docker build -t redash_jvm .
	
	# use the command below to chekc to see if the image is created
	$ docker images
	
	$ docker-compose up
```

## create tabels 
```shell
	# Create tables
	$ docker-compose run --rm server create_db

	# Create database for tests
	$ docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"

```

## rebuild if add new packages
```shell
	$ docker-compose build worker  or $ docker-compose build --no-cache worker
	$ docker-compose build server  or $ docker-compose build --no-cache server
```

## check 
	localhost:5000
	
## use ipynb help development
	
	need conda docker
	ref : Intersystems_cache_on_redash-Copy5.ipynb

## detailed steps (in tmux_config_redash.sh)

```shell
#!/usr/bin/env bash

# /home/max/dropbox/mycode/0_python_learn/my_learn/my_dockerfiles



cd ~/redash

tmux  new-session -n 'images' -d 'watch -n 1 docker images && bash' \; \
      split-window -v 'docker images && bash' \; \
      select-pane -t 0 \; \
      split-window -h ' ~/my_dockerfiles/watch_size.sh  && bash' \; \
      resize-pane -R 45 \; \
      select-pane -t 2 \; \
      \
      new-window -n 'control' 'watch -n 1 docker ps -a ' \; \
      split-window -v 'docker ps -a && bash' \; \
      split-window -v 'docker ps -a && bash' \; \
      \
      new-window -n 'r-server' 'cd ~/redash && docker-compose up && bash' \; \
      split-window -v 'sleep 60 && docker exec -it redash_server_1 bash  ' \; \
      \
      new-window -n 'iris' 'cd ~/my_dockerfiles/latest/iris && ./run.sh && bash' \; \
      split-window -v 'sleep 60 &&  docker exec -it iris  bash && bash' \; \
      \
      new-window -n 'conda' 'cd ~/my_dockerfiles/latest/ubuntu18_desktop_vnc_conda_pks1_redash && ./run.sh && bash' \; \
      split-window -v 'sleep 60 && docker exec -it conda_for_redash  bash ' \; \
      \
      new-window -n 'tables' 'sleep 90 && ~/my_dockerfiles/latest/iris/create_tables.sh && bash' \; \
      \
      attach
