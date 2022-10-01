#!/bin/sh

pwd=$(pwd -P)

root=$pwd/tmp-qa-remote
pkgs=$root/pkgs

usage ()
{
    echo "usage: $0 <1-2>"
    echo "       $0 <3> <1-5>"
    echo "1: Cleanup"
    echo "2: Get remote testsuite results"
    echo "3: Verify remote testsuite result"
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi

n="$1"
shift

extract ()
{
    local package
    package="$1"

    rpm2cpio "$package" \
        | cpio -idmv \
	       > /dev/null \
	       2>&1
}

get_item ()
{
    c="$1"
    arch="$2"

    if [ -d $root/binaries-testsuite.$c.$arch/gdb-testresults ]; then
	return
    fi

    if [ "$c" = "openSUSE_Leap_15.2" ]; then
	# Stale config, skip.
	return
    fi
    
    local dir
    dir=$pkgs/$c.$arch
    
    if [ ! -d $dir ]; then
	mkdir -p $dir
    fi

    rpm=$(echo $dir/gdb-testresults-12.1-*.*.rpm)
    rpm=$(for f in $rpm; do echo $f; done | grep -v nosrc)
    if [ ! -f $rpm ]; then
	osc getbinaries -q -M testsuite -d $dir $c $arch
    fi

    if [ ! -d $pkgs/gdb-testresults.$c.$arch ]; then
	(
	    cd $dir
	    extract $rpm
	)
    fi

    if [ -d $dir/usr/share/doc/packages/gdb-testresults ]; then
	mkdir $root/binaries-testsuite.$c.$arch
	mv \
	    $dir/usr/share/doc/packages/gdb-testresults \
	    $root/binaries-testsuite.$c.$arch/gdb-testresults
    fi

    if [ -d $root/binaries-testsuite.$c.$arch/gdb-testresults ]; then
	rm -Rf $dir
    fi
}

cleanup ()
{
    if [ -d $root ]; then
	echo "About to remove dir $root"
	echo "Press ^C to abort, enter to continue"
	read
    fi
    rm -Rf $root
    mkdir -p $root
}

case "$n" in
    1)
	cleanup
	;;

    2)
	osc results -M testsuite \
	    | grep succeeded \
	    | awk '{print $1, $2}' \
	    | while read line; do
	    get_item $line
	done
	;;

    3)
	m="$1"
	shift
	(
	    cd $root
	    bash $pwd/qa.sh $m
	)
	;;

    *)
	echo "Don't know how to handle arg: $n"
	exit 1
	;;
esac
