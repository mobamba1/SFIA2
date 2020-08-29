#! /bin/bash

pwd
ls

docker rmi $(docker images -a -q)

deactivate 
docker-compose down

docker --version
docker-compose --version

ansible --version

sudo docker login


docker images
docker ps

ansible-playbook -i inventory.cfg playbook.yaml

docker-compose build

sudo docker-compose build
sudo docker images
sudo docker system prune -f

sudo docker images
sudo docker login
sudo docker-compose push
