#!/bin/bash

git fetch && git reset origin/main --hard > /dev/null
source env/bin/activate
pip3 install -r requirements.txt > /dev/null
systemctl daemon-reload
systemctl restart myportfolio
deactivate
