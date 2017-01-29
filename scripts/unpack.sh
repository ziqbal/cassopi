#!/bin/bash

echo "FIX"
exit

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..
APP=${PWD##*/}     

############################################################

cd ..
tar zxvf paparazzi.tar.gz
rm paparazzi.tar.gz