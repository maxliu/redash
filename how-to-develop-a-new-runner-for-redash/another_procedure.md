# install redash dev env to ubuntu 18

if needed, map host folder to vm. if map doesn't work, reinstall VMwareTolls

## setup 

```bash

cd ~

git clone https://github.com/maxliu/redashlrsm.git

cd redashlrsm/setup/dockers/liu2_DEV


./app_install.sh


./setup.sh

sudo reboot



./redash_restart.sh

cd redashlrsm/setup/dockers/liu2_PROD_4

./toISC.sh ## vpn to ISC

localhost:5000 for load redash BI 

```

## development

do steps above

tmux -1:
  sudo atom then open ~/redashlrsm
  modify intersysiris.py and intersystem_test.py

tmux -2
  cd redashlrsm/setup/dockers/liu2_DEV
  run ./test_iris.sh or in_docker.sh for debug intersysiris.py

tmux-3
  cd cd redashlrsm/setup/dockers/iris
  ./run.sh # to start iris instance
 
tmux-4 
  watch -n 1 'ifconfig | grep -B1 inet'
  








# old




ln -s "/mnt/hgfs/Dropbox (MIT)/mycode/0_python_learn/my_learn/my_dockerfiles/latest" latest


modify source code

save py, png, ini or ohter files to ~/redashlrsm/setup/

run ```docker build -t redash/redash:liu2 . ```

run  ```docker-compose down```

run  ```docker-compose up```

```bash

cd ~

ln -s "/mnt/hgfs/Dropbox (MIT)/mycode/0_python_learn/my_learn/my_dockerfiles/latest" latest

git clone https://github.com/maxliu/redashlrsm.git

cd redashlrsm/setup/dockers/liu2_DEV

./app_install.sh

./setup.sh

sudo reboot

docker-compose up

# use sudo atom to modify intersysiris.py and intersysiris_test.py

docker exec -it redash_server_1 bash

(in docker)cd /liu2_DEV
(in docker)python intersystemiris_test.py
if works

./build.sh

# in another window
docker-compose down && docker-compose up

goto localhost:5000 to test



```



#old steps leave here for reference





cd ~

ln -s "/mnt/hgfs/Dropbox (MIT)/mycode/0_python_learn/my_learn/my_dockerfiles/latest" latest

cd latest

./docker_isntall.sh

sudo reboot

cd ~/redash

npm install

docker-compose up -d

### Create tables
```
$ docker-compose run --rm server create_db
```
### Create database for tests
```
$ docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"

$ npm run build

$ npm run start

check localhost:5000








install git 

```
$ cd ~

$ git clone https://github.com/getredash/redash.git

$ cd redash

$ cd setup

$ ./setup.sh  ## run $ sudo chmod +x setup.sh  first if needed

$ sudo usermod -aG docker $USER

$ sudo reboot

$ cd ~/redash

$ sudo install nodejs

$ sudo install npm

$ npm install npm@3.10.10

$ npm install

$ docker-compose up -d
```

### Create tables
```
$ docker-compose run --rm server create_db
```
### Create database for tests
```
$ docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"
```

```
$ npm run build

$ npm run start
```
if changed python code

```
$ docker-compose build worker
$ docker-compose build server
```

$ ln -s "/mnt/hgfs/Dropbox (MIT)/mycode" mycode

$ ln -s "/mnt/hgfs/Dropbox (MIT)" dropbox

$ln -s "/mnt/hgfs/Dropbox (MIT)/mycode/0_python_learn/my_learn/isc_cache" isc_cache

$ ln -s "/mnt/hgfs/Dropbox (MIT)/mycode/0_python_learn/my_learn/my_dockerfiles/latest" latest


$ ../latest/conda_one_step/ build and run
$../latest/iris/run.sh



## ref

[Docker Based Developer Installation Guide](https://redash.io/help/open-source/dev-guide/docker)


