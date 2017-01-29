#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..
APP=${PWD##*/}     

IP="192.168.1.13"
############################################################

ssh pi@$IP 'tar zcvf tmp.tar.gz /tmp/*.jpg'
scp pi@$IP:tmp.tar.gz /tmp/tmp.tar.gz
ssh pi@$IP 'rm tmp.tar.gz'
cd /tmp/
tar zxvf tmp.tar.gz
open tmp

