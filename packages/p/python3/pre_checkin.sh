#!/bin/bash
# This script is called automatically during autobuild checkin.
#
#
#
# ...or is it? 
# it really doesn't seem so, you know. go run it manually.

master=python3-base.spec

# calculate version number from newest tar name
VERSION=`ls *.tar.xz | grep '^Python-' | tail -n 1 | sed -r 's/^Python-([0-9]+\.[0-9]+.[0-9a-z]+)\.tar.*$/\1/'`
if echo $VERSION | grep -q Python; then
    echo "Version is $VERSION and that's not right, fix the script."
    exit 1
fi
# VERSION = 3.3.0

Version=${VERSION/[a-z]*/}      # 3.3.0
tar_suffix=${VERSION#$Version}  # b1
a_version=(${Version//\./ })    # 3 3 0

python_version=${VERSION:0:3}                   # 3.3
python_version_abitag=${python_version//./}     # 33
python_version_soname=${python_version//./_}    # 3_3

if [ -n "$tar_suffix" ]; then
    Version=$Version~$tar_suffix           # 3.3.0~b1
    tarversion=$VERSION                    # 3.3.0b1
else
    tarversion="%{version}"
fi

# set Version for every spec
sed -i -r 's/(^Version:[ \t]+).*/\1'"$Version"'/' python3*.spec
# set tarversion for every spec
sed -i -r 's/(^%define[ \t]+tarversion[ \t]+).*/\1'$tarversion'/' python3*.spec

for varname in python_version{,_abitag,_soname}; do
    eval varvalue=\$$varname
    sed -i -r 's/(^%define[ \t]+'$varname'[ \t]+).*/\1'$varvalue'/' $master
done


# update baselibs
sed -i -r 's/^libpython.*$/libpython'$python_version_soname'm1_0/' baselibs.conf


# copy definition sections


sections="DEF PATCH PREP CONFIG"

for slave in python3.spec python3-doc.spec; do
{
    prev=1
    for section in $sections; do
        if ! grep -q "COMMON-$section" $slave; then
            echo "Skipping $section for $slave" > /dev/stderr
            continue
        fi
        begin="/COMMON-$section-BEGIN/"
        end="/COMMON-$section-END/"
        sed -n -e "${prev},${begin}p" $slave
        sed -n -e "${begin},${end}p" $master | head -n -1 | tail -n +2
        prev=$end
    done
    sed -n -e "${prev},\$p" $slave
} > $slave.tmp && mv $slave.tmp $slave
done

osc service localrun format_spec_file


# create import_failed.map from package definitions

MAPFILE=import_failed.map
function new_map_line () {
    if [ -z "$1" -o -z "$2" ]; then
        return
    fi
    if [ "$1" == "python3-base" ]; then
        return
    fi
    echo "$1:$2" >> $MAPFILE.tmp
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

mv $MAPFILE.tmp $MAPFILE

# run test inclusion check
python3 skipped_tests.py

# I really don't to keep all three *.changes files separate
cp python3-base.changes python3.changes
cp python3-base.changes python3-doc.changes
