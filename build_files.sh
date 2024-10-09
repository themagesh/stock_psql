#!/bin/bash

# Install dependencies
pip install setuptools
pip install -r requirements.txt

# Collect static files without user input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


