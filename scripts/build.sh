#! /bin/bash

pwd
ls


deactivate 
docker-compose down
docker rmi $(docker images -a -q)
#Docker --version
#docker-compose --version

#ansible --version



#docker images
#docker ps

ansible-playbook -i inventory.cfg playbook.yaml

docker-compose build

#sudo docker-compose build
#sudo docker images
#sudo docker system prune -f

#sudo docker images

docker login -u"$USER" -p"$PASS" 
docker images
whoami
docker-compose push


