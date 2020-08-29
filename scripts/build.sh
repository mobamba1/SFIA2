#! /bin/bash

pwd
ls

deactivate 
docker-compose down

docker --version
docker-compose --version

ansible --version

docker login


docker images
docker ps

ansible-playbook -i inventory.cfg playbook.yaml

docker-compose build
docker-compose push
