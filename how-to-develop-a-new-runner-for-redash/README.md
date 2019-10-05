# how-to-develop-a-new-runner-for-redash 

## scrach

``` shell

# install git

	sudo apt install git -y

	git clone https://github.com/maxliu/redash.git

	cd redash

	cd how-to-develop-a-new-runner-for-redash-to-develop/common_setup

	./app_install.sh
	./docker_install.sh
	./drive_map.sh

	copy daemon.json and restart docker

```

## DEV env

``` shell

	cd ~/redash
	
	cp following files to ~/redash

		libcacheodbc.so
		odbcinst.ini
		toISC.sh   ## connect to 
		user/      ## password.txt for iris
		test_iris.sh
		build.sh
		create_tables.sh
		

    modify following files at ~/redash
		
		Dockerfile
		docker-compose.yml

	for iris query runner

		modify redash/setting/__init__.py
		add redash/query_runners/intersysiris.py
        modify requirements_all_ds.txt		

		
	./build.sh

	docker-compose up 
	
	./create_tables.sh

	might need the following command
		docker stop $(docker ps -a -q)
		docker rm  $(docker ps -a -q)

```

## PROD env

``` shell


```



ref: [redash_dev](https://redash.io/help/open-source/dev-guide/docker)


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
