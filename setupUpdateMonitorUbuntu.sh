#!/bin/bash

cd /
sudo apt-get update
sudo apt-get install python python3 python3-pip -y
sudo pip3 install psutil
sudo wget https://raw.githubusercontent.com/TheMaster870/Device-Monitor/main/updateMonitor.py?token=ACBM5N7MUU42ZJ5Z4LYEIZ3AN33IO
read -p "Open Startup Applications and add 'sudo python3 /home/drew/Desktop/updateMonitor.py' in command."
echo "Rebooting..."
sudo reboot
