#!/bin/sh

pwd=$(pwd -P)

root=$pwd/tmp-qa-local
logs=$root/logs
pkgs=$root/pkgs

configs="
openSUSE_Leap_15.4
openSUSE_Leap_15.3
openSUSE_Factory
SLE-15
SLE-12
SLE-11
"

usage ()
{
    echo "usage: $0 <1-4>"
    echo "1: Cleanup"
    echo "2: Do local builds without testsuite"
    echo "3: Do local builds with testsuite"
    echo "4: Verify local testsuite results"
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

acquire_sudo_rights ()
{
	# Acquire sudo rights.
	sudo --validate

	# Keep sudo rights alive.
	while true; do
	    sleep 100
	    sudo --validate --non-interactive
	    kill -0 "$$" 2>/dev/null || exit
	done &
}

archs="x86_64 i586"

have_combo ()
{
    arch="$1"
    c="$2"

    if [ "$arch" = "i586" ]; then
	case $c in
            SLE-12|SLE-15)
		return 1
		;;
	esac
    fi
    return 0
}

case "$n" in
    1)
	cleanup
	;;

    2)
	acquire_sudo_rights

	rm -Rf $logs/$n
	mkdir -p $logs/$n

	for arch in $archs; do
	    for c in $configs; do
		if ! have_combo $arch $c; then
		    continue
		fi
		osc build \
		    --clean \
		    --no-verify \
		    --trust-all-projects \
		    --no-service \
		    $c $arch \
		    > $logs/$n/LOG.$c.$arch \
		    2>&1

		if [ $? -eq 0 ]; then
		    echo PASS: $c $arch
		else
		    echo FAIL: $c $arch
		fi

		sudo rm -Rf /var/tmp/build-root/$c-$arch
	    done
	done
	;;

    3)
	acquire_sudo_rights

	rm -Rf $logs/$n
	mkdir -p $logs/$n

	for arch in $archs; do
	    for c in $configs; do
		if ! have_combo $arch $c; then
		    continue
		fi
		mkdir -p $pkgs/$c.$arch
		osc build \
		    --clean \
		    --no-verify \
		    --trust-all-projects \
		    --no-service \
		    -k $pkgs/$c.$arch \
		    -M testsuite \
		    $c $arch \
		    > $logs/$n/LOG.$c.$arch \
		    2>&1
		if [ $? -eq 0 ]; then
		    ok=true
		else
		    ok=false
		fi

		rpm=gdb-testresults-12.1-0.$arch.rpm
		if [ -f $pkgs/$c.$arch/$rpm ]; then
		    (
			cd $pkgs/$c.$arch
			extract gdb-testresults-12.1-0.$arch.rpm
		    )
		    mv \
			$pkgs/$c.$arch/usr/share/doc/packages/gdb-testresults \
			$pkgs/gdb-testresults.$c.$arch
		    rm -Rf $pkgs/$c.$arch
		else
		    ok=false
		fi

		if $ok; then
		    echo PASS: $c $arch
		else
		    echo FAIL: $c $arch
		fi

		sudo rm -Rf /var/tmp/build-root/$c-$arch
	    done
	done
	;;

    4)
	for arch in $archs; do
	    for c in $configs; do
		if ! have_combo $arch $c; then
		    continue
		fi
		echo "CONFIG: $c $arch"
		case $c in
		    openSUSE_Factory)
			bash qa.sh -local -factory $pkgs/gdb-testresults.$c.$arch
			;;
		    SLE-12)
			bash qa.sh -local -sle12 $pkgs/gdb-testresults.$c.$arch
			;;
		    SLE-11)
			bash qa.sh -local -sle11 $pkgs/gdb-testresults.$c.$arch
			;;
		    *)
			bash qa.sh -local $pkgs/gdb-testresults.$c.$arch
			;;
		esac
	    done
	done
	;;

    *)
	echo "Don't know how to handle arg: $n"
	exit 1
	;;
esac
