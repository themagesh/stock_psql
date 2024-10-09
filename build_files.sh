#!/bin/bash
echo 'BUILD START'
python3.12 -m venv venv 
 source venv/bin/activate
python3.12 -m pip install -r requirements.txt
echo 'BUILD END'
# Install dependencies
python3.12 -m pip install setuptools

echo 'colit'
# Collect static files without user input
python3.12 manage.py makemigrations
python3.12 manage.py migrate
python3.12 manage.py collectstatic --noinput


