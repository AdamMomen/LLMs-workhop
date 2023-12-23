#!/bin/bash

# Function to install pyenv
install_pyenv() {
  curl https://pyenv.run | $SHELL
}

# Function to install Python 3.11.0 using pyenv
install_python() {
  pyenv install 3.11.0
  pyenv global 3.11.0
}

# Function to install virtualenv
install_virtualenv() {
  if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt update
    sudo apt install -y virtualenv
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install virtualenv
  else
    echo "Unsupported OS for this script"
  fi
}

# Function to create and activate a virtual environment
create_virtualenv() {
  virtualenv venv -p $(pyenv which python)
  source venv/bin/activate
}

# Function to install dependencies from requirements.txt
install_requirements() {
  if [[ -f requirements.txt ]]; then
    pip install -r requirements.txt
  else
    echo "requirements.txt not found"
  fi
}

# Check OS and execute commands
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo "Detected Linux OS"
  install_pyenv
  install_python
  install_virtualenv
  create_virtualenv
  install_requirements
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Detected macOS"
  install_pyenv
  install_python
  install_virtualenv
  create_virtualenv
  install_requirements
elif [[ "$OSTYPE" == "msys"* ]]; then
  echo "Detected Windows OS. Please run the appropriate commands manually."
else
  echo "Unsupported OS"
fi

echo "Setup complete."

