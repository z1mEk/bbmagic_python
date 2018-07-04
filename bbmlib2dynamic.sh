#!/bin/sh
## prepare library bbmagic_lib_x.x.a to dynamic library bbmagic_lib_x.x.so

libv="1.2"

wget http://bbmagic.net/download/bin/bbmagic_lib_$libv.tar.gz
tar -zxvf bbmagic_lib_$libv.tar.gz
cd bbmagic_lib_$libv
ar -xv bbmagic_lib_$libv.a bbmagic_lib_$libv.o
wget http://bbmagic.net/download/bin/libbluetooth.a
gcc -shared -o bbmagic_lib_$libv.so bbmagic_lib_$libv.o libbluetooth.a
rm bbmagic_lib_$libv.a bbmagic_lib_$libv.o libbluetooth.a
cd ..
cp ./bbmagic_lib_$libv/bbmagic_lib_$libv.so bbmagic_lib_$libv.so
rm bbmagic_lib_$libv.tar.gz
rm -r ./bbmagic_lib_$libv
ls