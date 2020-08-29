#! /bin/bash

pwd
ls

export DATABASE_URI='mysql+pymysql://root:root@34.105.217.36:3306/coordinate'
export SECRET_KEY=sdfkjf
export SKEY=alkdfnsuf

deactivate 
docker-compose down
docker rmi $(docker images -a -q)
#Docker --version
#docker-compose --version

mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc

pip install --user ansible

ansible --version
/home/jenkins/.local/bin/ansible --version
/home/jenkins/.local/bin/ansible-playbook -i inventory.cfg playbook.yaml


#docker images
#docker ps

ansible-playbook -i inventory.cfg playbook.yaml

docker-compose build
docker-compose up -d


#sudo docker-compose build
#sudo docker images
#sudo docker system prune -f

#sudo docker images

docker login -u"$USER" -p"$PASS" 
docker images
whoami
docker-compose push


