#!/bin/zsh

cd ~/Work/BackboneNetworkSpeedTest

cd Data
git rm -r splitedDNS
mkdir -p splitedDNS

cd ~/Work/BackboneNetworkSpeedTest/Src/Tools
python ./SplitFile.py -i china_dns.txt -o splitedDNS -n $1
