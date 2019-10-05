FROM ubuntu:18.04

############from pre###########

ENV DEBIAN_FRONTEND noninteractive

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt update --fix-missing  && \
    apt-get -y upgrade        && \
    apt install    -y sudo    && \ 
    apt update     -y         && \
	apt autoclean  -y         && \
    apt autoremove -y	      && \
	apt install -y ubuntu-desktop  && \
	apt install -y  \
	 			vim \
	 			firefox \
	 			openssh-server  \
	 			net-tools  \
	 			curl  && \
	apt  update -y 

################

RUN  sudo  echo  "deb http://packages.cloud.google.com/apt cloud-sdk-$(grep VERSION_CODENAME /etc/os-release | cut -d '=' -f 2) main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list

RUN  curl  https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN  sudo apt-get -y update 
RUN  sudo apt-get install -y google-cloud-sdk
     
## 

ENV USER=maxliu

RUN useradd  -m -s /bin/bash maxliu 
RUN usermod -aG sudo maxliu
RUN echo "maxliu ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/maxliu

RUN  echo "America/New_York" > /etc/timezone


USER maxliu 
WORKDIR /home/maxliu

########   vnc

RUN  sudo apt-get update -y && \
     sudo apt-get upgrade -y && \
	 sudo apt-get install -y \
			xfce4 \
			xfce4-goodies \
			tightvncserver
		
RUN  sudo apt-get update -y

RUN  sudo apt autoclean -y && \
     sudo apt autoremove -y 

RUN mkdir -p /home/maxliu/.vnc

ADD xstartup /home/maxliu/.vnc
ADD passwd /home/maxliu/.vnc
ADD .Xauthority /home/maxliu/

RUN sudo chown -R $USER:$USER ~/.cache/

RUN sudo chown maxliu:maxliu ~/.vnc/xstartup
RUN sudo chown maxliu:maxliu ~/.vnc/passwd
RUN sudo chown maxliu:maxliu ~/.Xauthority
RUN sudo chmod 600 ~/.vnc/passwd

############# install conda / jupyter

RUN sudo apt-get update --fix-missing && \
	sudo apt-get install -y wget bzip2 ca-certificates \
    		libglib2.0-0 libxext6 libsm6 libxrender1 \
    		git mercurial subversion \
    		tmux zstd \
			graphviz \
			unixodbc-dev iodbc

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p ~/conda && \
    rm ~/anaconda.sh 

RUN sudo ln -s ~/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". ~/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN mkdir -p  /home/maxliu/.jupyter/

RUN  /home/maxliu/conda/bin/jupyter notebook --generate-config

ADD entry_point.sh /opt/bin/

COPY jupyter_notebook_config.json  /home/maxliu/.jupyter/jupyter_notebook_config.json

RUN mkdir -p ~/tmp
ADD bashrc_max.txt /home/maxliu/tmp/

RUN ~/conda/bin/conda update -y --all

RUN ~/conda/bin/conda update -n base -c defaults conda -y --all

RUN ~/conda/bin/conda create -y -n py2 python=2.7 anaconda
RUN ~/conda/bin/conda create -y -n py3 python=3.6

RUN ~/conda/bin/conda update -n py2 -c defaults conda -y --all
RUN ~/conda/bin/conda update -n py3 -c defaults conda -y --all

RUN ~/conda/bin/conda install -y  ipykernel 

#############

RUN sudo apt install -y openjdk-8-jre-headless default-jre

 
RUN ~/conda/bin/conda config --add channels anaconda
RUN ~/conda/bin/conda config --append channels r
RUN ~/conda/bin/conda config --append channels fxmarc
RUN ~/conda/bin/conda config --append channels conda-forge 
RUN ~/conda/bin/conda config --append channels msys2

RUN ~/conda/bin/conda  install  -y -n py2  \
											ipykernel 

RUN ~/conda/bin/conda  install  -y -n py2 	pandasql \
											pandas-gbq 

RUN ~/conda/bin/conda  install  -y -n py2  selenium \
											gspread=0.6.2 \
											path.py=11.0 \
											google-api-python-client=1.7.8 \
											celery=4.1.0 \
											kombu=4.1.0 \
											oauth2client 

RUN ~/conda/bin/conda  install  -y -n py2 	sentry-sdk \
											jaydebeapi \
											pandas-profiling  \
											google-cloud-sdk \
											psycopg2 \
											yaml \
											pyyaml \
											implicit \
											lightgbm \
											xgboost \
											altair \
											catboost \
											vega_datasets \
											vega3 \
											vega \
											flower \
											pyodbc
											
RUN ~/conda/bin/conda install -c moustik -n py2  weasyprint=0.30

RUN ~/conda/bin/conda  install  -y -n py3 anaconda \
											ipykernel \
											pandasql \
											pandas-gbq \
											selenium  \
											oauth2client \
											sentry-sdk \
                                            jaydebeapi \
											pandas-profiling \
											google-cloud-sdk \
											psycopg2 \
											yaml \
											celery \
											flower \
											pyyaml \
											implicit \
											lightgbm \
											xgboost \
											altair \
											catboost \
											vega_datasets \
											vega3 \
											vega \
											gspread=0.6.2 \
											google-api-python-client \
											r-essentials r-base r-irkernel  rpy2 \
											tensorflow keras pydot  \ 
											graphviz 

											
											
											# libpython

RUN ~/conda/bin/conda  install  -y -n py3	 mkl-service  \
											pymc3 \
											arviz  \
											pandas-datareader \
											pyodbc
											


RUN ~/conda/envs/py2/bin/python -m ipykernel install --user --name py2 --display-name "py2"
RUN ~/conda/envs/py3/bin/python -m ipykernel install --user --name py3 --display-name "py3"

# RUN ~/conda/bin/conda update -y --all
#########################################################


ADD add_R_packages.R /tmp

ENV PATH "/home/maxliu/conda/bin:$PATH"
ENV PATH /home/maxliu/mycode/Marketing_study:$PATH
ENV PATH /home/maxliu/mycode/Marketing_study/driver:$PATH
ENV PATH "/home/maxliu/mycode/:$PATH"

ENV PYTHONPATH "/home/maxliu/mycode:$PYTHONPATH"
ENV PYTHONPATH "/home/maxliu/mycode/util:$PYTHONPATH"
ENV PYTHONPATH "/home/maxliu/mycode/scikitchart:$PYTHONPATH"
ENV PYTHONPATH "/home/maxliu/mycode/edx2bigquery:$PYTHONPATH"

RUN ~/conda/envs/py3/bin/Rscript /tmp/add_R_packages.R

#########################################################

RUN ["/bin/bash", "-c", "echo -e 'arcEnergy1\narcEnergy1\n' | sudo passwd root"]

RUN ["/bin/bash", "-c", "echo -e 'maxliu:arcEnergy1' | sudo chpasswd"]

RUN ["/bin/bash", "-c", "cat ~/tmp/bashrc_max.txt >> ~/.bashrc"]

RUN ["/bin/bash", "-c", "source ~/.bashrc"]


#########################################################

RUN git config --global user.email "xinyulrsm@gmail.com"  && \
	git config --global user.name "xinyu max liu"
#########################################################

RUN sudo chmod +x /home/maxliu/.vnc/xstartup

#########################################################

RUN sudo apt  -y update 


#########################################

COPY entry_point.sh /opt/bin/
COPY odbcinst.ini /etc/odbcinst.ini

RUN sudo mkdir -p /app
COPY libcacheodbc.so /app/libcacheodbc.so

RUN  sudo chmod +x /opt/bin/entry_point.sh

ENTRYPOINT ["/opt/bin/entry_point.sh"]


######## END ############################################

