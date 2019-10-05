
FROM redash/redash:preview

# FROM redash/redash:7.0.0.b18042
####

USER root

RUN sudo apt update -y
RUN sudo apt install -y unixodbc-dev iodbc
RUN sudo pip install  pandas-gbq 

RUN echo  "deb http://packages.cloud.google.com/apt cloud-sdk-$(grep VERSION_CODENAME /etc/os-release | cut -d '=' -f 2) main" |  tee /etc/apt/sources.list.d/google-cloud-sdk.list

RUN  curl  https://packages.cloud.google.com/apt/doc/apt-key.gpg |  apt-key add -
RUN   apt-get -y update 
RUN   apt-get install -y google-cloud-sdk



# RUN usermod -aG sudo redash
# RUN echo "redash ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/redash

# RUN  echo "America/New_York" > /etc/timezone

RUN pip install pyodbc

USER redash


COPY odbcinst.ini /etc/odbcinst.ini

ARG INCUBATOR_VER=unknown

COPY libcacheodbc.so /app/libcacheodbc.so

COPY intersysiris.png /app/client/app/assets/images/db-logos/

COPY intersysiris.png /app/client/dist/images/db-logos/
