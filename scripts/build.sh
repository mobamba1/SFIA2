#! /bin/bash

pwd
ls

deactivate 
sudo docker-compose down

docker --version
docker-compose --version

/home/jenkins/.local/bin/ansible --version

sudo docker images
