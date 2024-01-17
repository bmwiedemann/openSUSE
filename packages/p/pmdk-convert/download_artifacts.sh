#!/bin/bash -ex
rm -f nvml-[0-9.]*.tar.gz [0-9.]*.tar.gz
VERSION=$(rpmspec --parse pmdk-convert.spec | egrep '^Version' | awk '{ print $NF}')
tar -xf pmdk-convert-$VERSION.tar.gz
cd pmdk-convert-$VERSION
rm -Rf build
mkdir -p build
cd build
cmake .. || true
cd ..
cp [0-9.]*.tar.gz ..
cd ../
FILELIST=([0-9.]*.tar.gz)
osc add "${FILELIST[@]}"


SOURCES=""
SETUP=""
i=1

cp pmdk-convert-$VERSION/CMakeLists.txt pmdk-convert-$VERSION/CMakeLists.txt.orig

for file in "${FILELIST[@]}"; do
	# Remove tests bins from the tarball as they may contain binaries that mess up ClamAV
	dir=$(tar -tf $file | head -n 1 | awk '{ print $NF}')
	if [ -d $dir ]; then
		rm -Rf $dir
	fi
	tar --same-permissions -xf $file
	find $dir/src/test -name "*.bin" -exec rm {} \;
	rm -f $file
	tar --owner=root --group=root -czf  $file $dir
	SOURCES+="Source$i:        $file\n"
	SETUP+="cp %{S:$i} .\ntar -xf %{S:$i}\n"

	VER=$(basename $file .tar.gz | sed -e 's/^nvml-//')
	# And now time for some very ugly hacking to regenerate the hash in CMakeLists.txt so
	# the patched tarball will not be redownloaded again...
	VERSTR=$(egrep "set\(VER.* $VER\)" pmdk-convert-$VERSION/CMakeLists.txt.orig | sed -e 's/.*(\(VER[0-9]*\) .*/\1/')
	HASH=$(sha256sum $file | awk '{ print $1 }')

	sed -i -e 's/\(get_pmdk(${'$VERSTR'} \)[0-9a-f]* /\1'$HASH' /' pmdk-convert-$VERSION/CMakeLists.txt
	i=$(($i + 1))
done

diff -u pmdk-convert-$VERSION/CMakeLists.txt.orig pmdk-convert-$VERSION/CMakeLists.txt > cmake_hash.patch

# Magical sed macro to replace the old content between the comment
# strings so we don't have to manually edit
# the nvml file list
sed -i -e '/## START_NVML_SETUP/,/## END_NVML_SETUP/!b;//!d;/## START_NVML_SETUP/a '"$SETUP" pmdk-convert.spec
sed -i -e '/## START_NVML_SOURCE/,/## END_NVML_SOURCE/!b;//!d;/## START_NVML_SOURCE/a '"$SOURCES" pmdk-convert.spec
