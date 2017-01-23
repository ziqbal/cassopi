
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/..
APP=${PWD##*/}     

############################################################

rm -rf f.lock

cd ..

rm -rf /tmp/$APP.tar.gz

tar zcvf /tmp/$APP.tar.gz $APP