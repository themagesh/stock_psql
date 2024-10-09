#!/bin/bash
set -e

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Django collectstatic
python manage.py collectstatic --noinput

