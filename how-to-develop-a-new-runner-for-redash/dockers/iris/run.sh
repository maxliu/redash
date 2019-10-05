#!/usr/bin/env bash

## this one works
#docker run -it --rm --expose=51773 -p 52773:52773 -p 1883:1883 -p 1978:1978  --name iris intersystemsdc/irisdemo-demo-appointmentsms:stable


## https://hub.docker.com/r/intersystemsdc/irisdemo-base-irisb-community
docker run -it --rm -p 51773:51773  -p 52773:52773 -p 1883:1883 -p 1978:1978 --volume $(pwd)/user/:/durable --env ISC_DATA_DIRECTORY=/durable/iris  --name iris intersystemsdc/irisdemo-base-irisb-community:2019.3.0.306.0-community  --password-file /durable/password.txt








# docker run --name my-iris -d --publish 9091:51773 --publish 9092:52773 --volume /home/maxliu/:/durable --env ISC_DATA_DIRECTORY=/durable/iris store/intersystems/iris:2019.1.0.511.0-community --password-file /durable/password/password.txt 

# # http://localhost:9092/csp/sys/UtilHome.csp
# # http://localhost:52773/csp/sys/UtilHome.csp
