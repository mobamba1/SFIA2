#! /bin/bash

#pwd
#ls

#export DATABASE_URI='mysql+pymysql://root:root@34.105.217.36:3306/coordinate'
#export SECRET_KEY=sdfkjf
#export SKEY=alkdfnsuf

#deactivate 
#docker-compose down
#docker rmi $(docker images -a -q)
#Docker --version
#docker-compose --version

#mkdir -p ~/.local/bin
#echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
#source ~/.bashrc

ssh kenneth1521412@sfia2
pwd
ls
cd SFIA2
export DATABASE_URI="$DATABASE"
export SECRET_KEY="$SECRETKEY"
export SKEY="$SKEY"
deactivate
docker-compose down
docker rmi $(docker images -a -q)


ansible --version



#docker images
#docker ps
/home/kenneth1521412/.local/bin/ansible --version

/home/kenneth1521412/.local/bin/ansible-playbook -i inventory.cfg playbook.yaml

docker-compose build
docker-compose up -d

#this is a comment
#sudo docker-compose build
#sudo docker images
#sudo docker system prune -f

#sudo docker images

docker login -u"$USER" -p"$PASS" 
docker images
whoami
docker-compose push


