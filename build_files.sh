#!/bin/bash
set -e

# Activate virtual environment
source venv/bin/activate

echo 'BUILD START'
python manage.py collectstatic --noinputn --clear
pip install -r requirements.txt
echo 'BUILD END'