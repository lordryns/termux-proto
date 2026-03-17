#!/data/data/com.termux/files/usr/bin/bash

set -e

clear

echo "Updating repo"

export DEBIAN_FRONTEND=noninteractive

pkg upgrade -y -o Dpkg::Options::="--force-confnew"

sleep 1
clear

echo "installing python..."
pkg install python

sleep 1
clear

echo "Running setup script..."
python setup.py

sleep 1
clear

echo "Done!"
