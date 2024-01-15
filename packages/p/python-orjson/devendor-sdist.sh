#!/bin/sh
file=$(find . -maxdepth 1 -name 'orjson-*.tar.gz' -print | sort -rn | tail -1)
echo "Removing the cargo vendoring from upstream ${file}"
dir=${file%.tar.gz}
tar -x -z -f $file
rm ${dir}/Cargo.lock
rm -r ${dir}/include/cargo
rm -r ${dir}/.cargo
outfile=${dir}-devendored.tar.xz
echo "Repackaging to ${outfile}"
tar -c -J -f ${outfile} ${dir}
