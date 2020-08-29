#! /bin/bash


export DATABASE_URI='mysql+pymysql://root:root@34.105.217.36:3306/coordinate'
export SECRET_KEY=sdfkjf
export SKEY=alkdfnsuf

pip3 install -r requirements.txt

cd service1
python3 -m pytest --cov service1
cd ..
