#! /bin/sh
# when updating from an older version of the overlay package
# move added/modified overlay files to the new location.
error=0

src=/usr/share/warewulf/overlays
dst=/var/lib/warewulf/overlays

test -d $src || exit 0

for i in $(find -P $src -maxdepth 1 -mindepth 1 -type d)
do
    d=$(basename -s "" $i)
    if [ ! -d $dst/$d ]
    then
	mkdir -p /var/lib/warewulf/overlays/$d/rootfs || { error=1; continue; }
    elif [ ! -d $dst/$d/rootfs ]
    then
	mkdir -p $dst/$d/rootfs || { error=1; continue; }
    fi
    for j in $(find -P $src/$d -not -type d)
    do
	D=$(dirname $j)
	D=${D##$src/$d}
	f=$(basename -s ".rpmsave" $j)
	if [ ! -d $dst/$d/rootfs/$D ]
	then
	    mkdir -p $dst/$d/rootfs/$D || { error=1; continue; }
	fi
	if [ ! -e $dst/$d/rootfs/$D/$f ]
	then
	    mv $j $dst/$d/rootfs/$D/$f
	elif [ ! -e $dst/$d/rootfs/$D/$f.rpmsave ]
	then
	    mv $j $dst/$d/rootfs/$D/$f.rpmsave
	else
	    error=1
	fi
    done
done
if [ $error -gt 0 ]
then
    echo "Cannot copy all files - check $src manually" >&2
else
    find -P $src -type d -delete
fi

