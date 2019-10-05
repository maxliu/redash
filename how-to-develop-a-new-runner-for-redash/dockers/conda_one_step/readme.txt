

docker-compose up -d







docker exec -it my_py bash

  git config --global user.email "xinyulrsm@gmail.com"
  git config --global user.name "xinyu max liu"


6) run the following in terminal for gbq credentials:  <== need login to ubuntu computer
    $$ gcloud auth application-default login

    or 

    gcloud auth application-default login --no-launch-browser


1) start jupyter
	./jus3.sh

2) run tableau scheduled jobs
	cd ~/mycode/celeryJobs/tableau
	source activate py3  or conda activate py3
	./runSche.sh

3) run github scheduled jobs

	## might need this
	## sudo chmod 400  /home/maxliu/mycode/redashBI/keys/redahsBI

	conda activate py2   ##!!! NOT PY3 "click" is not working on py3

	cd ~/mycode/celeryJobs/github
	eval $(ssh-agent -s)
	ssh-add ~/mycode/redashBI/keys/redahsBI
	./runSche.sh

4) run cameo celery job

	conda activate py2
	~/conda/envs/py2/bin/pip install -I path.py==7.7.1
	cd ~/mycode/CAMEO
	celery -A cameo2RCelery worker -l INFO --concurrency=2 --time-limit=36000 --maxtasksperchild=10  -f celery.log

5) run flower
	cd ~/mycode/CAMEO
	conda activate py2
	flower -A cameo2RCelery --port=5555




