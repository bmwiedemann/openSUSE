#!/bin/bash -ex
rm -f nvml-[0-9.]*.tar.gz
VERSION=$(rpmspec --parse pmdk-convert.spec | egrep '^Version' | awk '{ print $NF}')
tar -xf pmdk-convert-$VERSION.tar.gz
cd pmdk-convert-$VERSION
rm -Rf build
mkdir -p build
cd build
cmake .. || true
cd ..
cp nvml-[0-9.]*.tar.gz ..
cd ../
FILELIST=(nvml-[0-9.]*.tar.gz)
osc add "${FILELIST[@]}"


SOURCES=""
SETUP=""
i=1
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
	i=$(($i + 1))
done

# Magical sed macro to replace the old content between the comment
# strings so we don't have to manually edit
# the nvml file list
sed -i -e '/## START_NVML_SETUP/,/## END_NVML_SETUP/!b;//!d;/## START_NVML_SETUP/a '"$SETUP" pmdk-convert.spec
sed -i -e '/## START_NVML_SOURCE/,/## END_NVML_SOURCE/!b;//!d;/## START_NVML_SOURCE/a '"$SOURCES" pmdk-convert.spec
