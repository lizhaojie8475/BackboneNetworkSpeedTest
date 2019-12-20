#! /bin/zsh
cd ~/Work/BackboneNetworkSpeedTest/Src

#~/Work/BackboneNetworkSpeedTest/venv/bin/python ./test.py insert;

for ((i=0; i<5; i++));
do
~/Work/BackboneNetworkSpeedTest/venv/bin/python ./test.py update;
done

