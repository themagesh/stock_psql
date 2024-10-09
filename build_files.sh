#!/bin/bash
echo 'BUILD START'
python3 -m venv venv 
source venv/bin/activate
python3 -m pip install -r requirements.txt
echo 'BUILD END'
# Install dependencies
python3 -m pip install setuptools

echo 'colit'
# Collect static files without user input
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput


