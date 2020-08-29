#! /bin/bash

pwd
ls

pip3 install -r requirements.txt

cd service1
python3 -m pytest --cov service1
cd ..
