#!/bin/bash
set -e

# Check if python and pip are installed
if ! command -v python &> /dev/null
then
    echo "python could not be found. Make sure you have specified a Python runtime in vercel.json."
    exit 1
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip could not be found. Make sure you have specified a Python runtime in vercel.json."
    exit 1
fi

# Install dependencies
pip3 install setuptools
pip3 install -r requirements.txt

# Collect static files without user input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


