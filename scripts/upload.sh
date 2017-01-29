#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..
APP=${PWD##*/}     


IP="192.168.1.13"
############################################################

scp /tmp/$APP.tar.gz pi@$IP:$APP.tar.gz 



ssh pi@$IP "sudo ./$APP/scripts/kill.sh"
ssh pi@$IP "tar zxvf $APP.tar.gz"
ssh pi@$IP "rm $APP.tar.gz"
