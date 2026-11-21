#!/bin/bash

export LC_ALL=C

master=python*.spec

# create import_failed.map from package definitions
pkgname=$(grep python_pkg_name $master |grep define |awk -F' ' '{print $3}')
MAPFILE=import_failed.map
function new_map_line () {
    package=$1
    package=$(echo $1 |sed -e "s:%{python_pkg_name}:$pkgname:")
    modules=$2
    if [ -z "$package" -o -z "$modules" ]; then
        return
    fi
    if [[ "$package" =~ "-base" ]]; then
        return
    fi
    echo "$package:$modules" >> $MAPFILE.tmp
}

for spec in *.spec; do
    basename=${spec%.spec}
    package=
    modules=
    while read line; do
        case $line in
            "%files -n "*)
                new_map_line $package "$modules"
                package=${line#"%files -n "}
                modules=
                ;;
            "%files "*)
                new_map_line $package "$modules"
                package=$basename-${line#"%files "}
                modules=
                ;;
            "%files")
                new_map_line $package "$modules"
                package=$basename
                modules=
                ;;
            "%{sitedir}/config-"*)
                # ignore
                ;;
            "%{sitedir}/"*)
                word=${line#"%{sitedir}/"}
                if ! echo $word | grep -q /; then
                    modules="$modules $word"
                fi
                ;;
            "%{dynlib "*"}")
                word=${line#"%{dynlib "}
                word=${word%"}"}
                modules="$modules $word"
                ;;
        esac
    done < $spec
    new_map_line $package "$modules"
done

cat $MAPFILE.tmp |sort -u > $MAPFILE
rm $MAPFILE.tmp

# run test inclusion check
tar xJf Python-*.xz 
python3 skipped_tests.py

# generate baselibs.conf
VERSION=$(grep ^Version $master|awk -F':' '{print $2}' |sed -e 's/ //g')
python_version=${VERSION:0:3}                   # 3.3
python_version_abitag=${python_version//./}     # 33
python_version_soname=${python_version//./_}    # 3_3
echo "$pkgname-base" > baselibs.conf
echo "$pkgname" >> baselibs.conf
echo "libpython$python_version_soname-1_0" >> baselibs.conf

