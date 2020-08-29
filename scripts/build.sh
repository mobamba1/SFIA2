#! /bin/bash

pwd
ls

#docker rmi $(docker images -a -q)

deactivate 
docker-compose down

docker --version
docker-compose --version

ansible --version



docker images
docker ps

ansible-playbook -i inventory.cfg playbook.yaml

docker-compose build

sudo docker-compose build
sudo docker images
sudo docker system prune -f

sudo docker images
sudo docker login -u"kenneth1521412" -p"Mamama00)"
docker-compose push

