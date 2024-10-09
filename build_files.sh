#!/bin/bash
set -e

# Check if python and pip are installed
if ! command -v python &> /dev/null
then
    echo "python could not be found. Make sure you have specified a Python runtime in vercel.json."
    exit 1
fi

if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Make sure you have specified a Python runtime in vercel.json."
    exit 1
fi

# Install requirements
pip install -r requirements.txt

# Your other build commands...


# Install dependencies
pip install setuptools
pip install -r requirements.txt

# Collect static files without user input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


