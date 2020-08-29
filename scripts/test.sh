#! /bin/bash

pwd
ls

pip3 install -r requirements.txt

cd service1
pytest --cov service1
cd ..
