#! /bin/bash

vers=$(cat csound.spec|grep "Version:        "|cut -b 17-23)
rm -f *.tar.*
wget https://github.com/csound/csound/archive/${vers}.tar.gz || exit 1
echo "\n\nUnpacking tarball\n"
tar -xf ${vers}.tar.gz
echo "Removing undistibutable files\n"
rm -f csound-${vers}/Opcodes/scansyn*
echo "Creating distributable tarball\n"
tar -acf csound-${vers}-distibutable.tar.xz csound-${vers}
echo "Cleaning up\n"
rm -rf csound-${vers} ${vers}.tar.gz
if ! test -e ${vers}.tar.gz;
then
echo "success"
osc ar
exit 0
else
echo "error"
exit 1
fi
