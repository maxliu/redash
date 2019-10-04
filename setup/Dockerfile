
FROM redash/redash:7.0.0.b18042

####

USER root

RUN sudo apt update -y
RUN sudo apt install -y unixodbc-dev iodbc vim mc sudo

RUN usermod -aG sudo redash
RUN echo "redash ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/redash

RUN  echo "America/New_York" > /etc/timezone

## delete /app
## volume (map) /app

####

USER redash

RUN pip install pyodbc

COPY __init__.py /app/redash/settings/

COPY odbcinst.ini /etc/odbcinst.ini

COPY libcacheodbc.so /app/libcacheodbc.so

ARG INCUBATOR_VER=unknown

COPY intersysiris.py /app/redash/query_runner

COPY intersysiris.png /app/client/app/assets/images/db-logos/intersysiris.png

COPY intersysiris.png /app/client/dist/images/db-logos/intersysiris.png
