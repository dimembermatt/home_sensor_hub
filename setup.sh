# !/bin/bash
# Setup instructions for (1) configuring the RPI0, (2) setting up relevant drivers, (3) installing relevant sensor libraries, and (4) establishing the sensing routines.

# We're starting in the root directory of the RPI0
cd ~
pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py

# Create and load in the venv
python -m venv venv
source ./venv/bin/activate

# Install sensor drivers
pip3 install adafruit-circuitpython-sgp30
pip3 install adafruit-circuitpython-apds9960
pip3 install adafruit-circuitpython-ahtx0