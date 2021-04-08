#!/bin/bash

cd /
sudo apt-get update
sudo apt-get install python python3 python3-pip -y
sudo pip3 install psutil
sudo wget https://raw.githubusercontent.com/TheMaster870/Device-Monitor/main/updateMonitor.py?token=ACBM5N7MUU42ZJ5Z4LYEIZ3AN33IO
FILE=/etc/rc.local
if [ -f "$FILE" ]
then
	sudo sed '$d' $FILE
	sudo echo "sudo python3 updateMonitor.py &" >> $FILE
	sudo echo "exit(0)" >> $FILE
else
	sudo touch $FILE
	sudo echo "#!/bin/sh" >> $FILE
	sudo echo "sudo python3 updateMonitor.py &" >> $FILE
	sudo echo "exit(0)" >> $FILE
	sudo chmod a+x $FILE
fi
