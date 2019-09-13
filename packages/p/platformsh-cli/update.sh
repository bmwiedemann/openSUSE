#!/bin/bash

# rerun _service
rm *.xz
osc service dr

# extract tarball, install composer dependencies, recompress, remove directory
name=$(basename $(pwd))
tar xf $name-*.tar.xz
cd $name-*/
composer install --no-interaction --no-dev
composer licenses > ../licenses.txt
php ../extensions.php > ../extensions.txt
source_dir=$(basename $(pwd))
cd ..
tar --directory=$source_dir -cJf $name-vendor.tar.xz vendor
rm -r $source_dir

osc addremove
