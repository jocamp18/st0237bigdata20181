1. utilizar distribución cloudera CDH QuickStart en Docker

IP host: 192.168.10.115
ubuntu server 16.04

      $ sudo apt-get install docker

      $ sudo docker pull cloudera/quickstart:latest

      $ sudo docker images

      REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
      cloudera/quickstart   latest              4239cd2958c6        17 months ago       6.336 GB

      $ sudo docker run --hostname=quickstart.cloudera --privileged=true -t -i -p 8080 4239cd2958c6 /usr/bin/docker-quickstart -d
