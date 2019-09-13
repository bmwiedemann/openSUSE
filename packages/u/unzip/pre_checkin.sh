#! /bin/sh

cp unzip.spec unzip-rcc.spec
cp unzip.changes unzip-rcc.changes

sed -i -e 's,Name: .*,Name: unzip-rcc,' unzip-rcc.spec
sed -i -e 's,%bcond_with rcc,%bcond_without rcc,' unzip-rcc.spec

osc service localrun format_spec_file

