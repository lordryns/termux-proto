#!/data/data/com.termux/files/usr/bin/bash

set -e

clear

echo "Welcome to termux-proto!"
sleep 1
echo "Updating repo"

export DEBIAN_FRONTEND=noninteractive

pkg upgrade -y -o Dpkg::Options::="--force-confnew"

sleep 1
clear

echo "installing python..."
pkg install python git -y

pip install questionary

sleep 1
clear

if [ ! -d ".git" ]; then
  git clone https://github.com/lordryns/termux-proto.git
  cd termux-proto
fi

echo "Running setup script..."
python setup.py

sleep 1
clear

echo "Done!"
