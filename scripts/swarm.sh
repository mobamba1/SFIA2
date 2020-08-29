#! /bin/bash

ssh kenneth1521412@manager<< EOF
pwd
whoami
ls

sudo rm -r SFIA2
ls

git clone https://github.com/mobamba1/SFIA2.git
ls

EOF
