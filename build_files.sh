#!/bin/bash
set -x

echo "Starting build process..."

# Activate the virtual environment
python3 -m venv venv

source venv/bin/activate

echo "Virtual environment activated."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Build steps completed."
chmod +x build_files.sh