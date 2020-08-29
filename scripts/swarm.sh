#! /bin/bash

ssh kenneth1521412@manager<< EOF

export DATABASE_URI='mysql+pymysql://root:root@34.105.217.36:3306/coordinate'
export SECRET_KEY=sdfkjf
export SKEY=alkdfnsuf

docker stack rm SFIA2
docker rmi $(docker images -a -q)

pwd
whoami
ls

sudo rm -r SFIA2
ls

git clone https://github.com/mobamba1/SFIA2.git
ls

cd SFIA2


docker login -u"$USER" -p"$PASS"
docker pull kenneth1521412/service1
docker pull kenneth1521412/service2
docker pull kenneth1521412/service3
docker pull kenneth1521412/service4

docker stack deploy --compose-file docker-compose.yaml SFIA2
docker stack services SFIA2

EOF
