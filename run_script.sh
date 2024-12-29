#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Installing pip3..."
    python3 -m ensurepip --upgrade
fi

VENV_DIR="myvenv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR"
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

if [ -f "requirements.txt" ]; then
    echo "Installing packages from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please make sure it's present in the project directory."
    exit 1
fi

echo "Virtual environment setup complete!"

echo "Installing system dependencies..."
sudo apt install -y xdg-utils
sudo apt install -y firefox
sudo apt install -y fim

echo "System dependencies installed!"
