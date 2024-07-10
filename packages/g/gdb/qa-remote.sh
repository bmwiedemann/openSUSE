#!/bin/sh

scriptdir=$(cd $(dirname $0); pwd -P)

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
	echo "Already have $c $arch, skipping"
	return
    fi

    if [ "$c" = "openSUSE_Leap_15.2" ]; then
	# Stale config, skip.
	return
    fi

    echo "Trying $c $arch"
    
    local dir
    dir=$pkgs/$c.$arch
    
    if [ ! -d $dir ]; then
	mkdir -p $dir
    fi

    rpm=$(echo $dir/gdb-testresults-*.*.rpm)
    rpm=$(for f in $rpm; do echo $f; done | grep -v nosrc)
    rpm=$(basename $rpm)
    if [ "$rpm" = "" ] || [ ! -f "$rpm" ]; then
	echo "Getting rpms"
	osc getbinaries -q -M testsuite -d $dir $c $arch
	rpm=$(echo $dir/gdb-testresults-*.rpm)
	rpm=$(for f in $rpm; do echo $f; done | grep -v nosrc)
	rpm=$(basename $rpm)
	echo "Got rpm: $rpm"
    else
	echo "Already have rpm: $rpm"	
    fi

    if [ ! -d $pkgs/gdb-testresults.$c.$arch ]; then
	(
	    echo "Extracting rpm: $rpm"
	    cd $dir
	    extract $rpm
	)
    else
	echo "Already extracted rpm: $rpm"
    fi

    if [ -d $dir/usr/share/doc/packages/gdb-testresults ]; then
	echo "Renaming"
	mkdir $root/binaries-testsuite.$c.$arch
	mv \
	    $dir/usr/share/doc/packages/gdb-testresults \
	    $root/binaries-testsuite.$c.$arch/gdb-testresults
    fi

    if [ -d $root/binaries-testsuite.$c.$arch/gdb-testresults ]; then
	echo "Cleaning up"
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

report_todo ()
{
    c="$1"
    arch="$2"
    status="$3"

    if [ "$c" = "SLE-10_SDK" ]; then
	# Stale config.
	return
    fi
    
    if [ "$c" = "SLE-11" ]; then
	# No longer supported, gdb requires more recent version of MPFR.
	return
    fi

    echo -e "Todo: $c\t$arch\t$status"
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
	osc results -M testsuite \
	    | grep -v succeeded \
	    | awk '{print $1, $2, $4}' \
	    | while read line; do
	    report_todo $line
	done
	;;

    3)
	m="$1"
	shift
	(
	    cd $root
	    bash $scriptdir/qa.sh $m
	)
	;;

    *)
	echo "Don't know how to handle arg: $n"
	exit 1
	;;
esac
