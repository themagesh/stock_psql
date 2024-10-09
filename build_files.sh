#!/bin/bash
echo 'BUILD START'
python3.12 -m venv venv 
 source venv/bin/activate
pip install -r requirements.txt
echo 'BUILD END'
# Install dependencies
pip install setuptools

echo 'colit'
# Collect static files without user input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


