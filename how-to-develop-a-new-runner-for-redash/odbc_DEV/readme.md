
# setup DEV environment

## basic ideas

## steps
```
cd ~

git clone https://github.com/maxliu/redash.git

cd ~/redash
git checkout [brach_name] # for example 'test_DEV_env'

cd ~

git clone https://github.com/maxliu/how-to-develop-a-runner-for-redash.git
```

# in tmux window - fileSync
``` sh
    ./cp_init_setting.sh

    manually modify __init__.py
    manually modify .gitignor
    ## manually modify docker-compose.yml

    ./file_sync.sh
```
# in tmux window - docker

``` sh
    cd ~/redash

    docker-compose build --no-cache

    docker-compose up -d

    docker-compose run --rm server create_db && docker-compose run --rm postgres psql -h postgres -U postgres -c "create database tests"
```
## might need the following (if do this the settings in redash will be gone <- danger)

    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)

## test
localhost:5000

mofify the files on ~/how-to-develop-a-runner-for-redash/odbc_DEV

git checkout aaa_liu_dev redash/query_runner/intersysiris.py redash/settings/__init__.py  requirements_all_ds.txt


```
