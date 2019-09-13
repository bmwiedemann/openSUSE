#! /bin/sh
arch=$1
flavors=
for flavor in $(ls /usr/src/linux-obj/$arch 2>/dev/null); do
    if [ "$flavor" = um ]; then
        continue
    fi
    flavors="$flavors $flavor"
done
echo $flavors
