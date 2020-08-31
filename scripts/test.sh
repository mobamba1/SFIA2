#! /bin/bash


export DATABASE_URI="$DATABASE"
export SECRET_KEY="$SECRETKEY"
export SKEY="$SKEY"

pip3 install -r requirements.txt

cd service1
python3 -m pytest --cov service1
cd ..

cd service2
python3 -m pytest --cov service2
cd ..

cd service3
python3 -m pytest --cov service3
cd ..

cd service4
python3 -m pytest --cov service4
cd ..
