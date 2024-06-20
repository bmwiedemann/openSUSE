#!/bin/bash

# Fedora Packages not copied:
#
skip_patches=(
    # Not applicable for openSUSE.
    gdb-add-index.patch
    gdb-6.3-rh-testversion-20041202.patch
    gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch
    gdb-6.8-bz466901-backtrace-full-prelinked.patch
    gdb-container-rh-pkg.patch

    # Fragile test-case, requires glibc to fail in a certain way.
    gdb-rhbz1156192-recursive-dlopen-test.patch

    # Obsolete.
    gdb-6.7-ppc-clobbered-registers-O2-test.patch
)

usage ()
{
    echo "usage: $(basename "$0") <fedora package dir> "
}

dir="$1"

if [ ! -f "$dir"/_patch_order ]; then
    usage
    exit 1
fi

mark1="^#Fedora Packages begin"
mark2="^#Fedora Packages end"
mark3="^#Fedora patching start"
mark4="^#Fedora patching end"

remove_current_patches ()
{
    # shellcheck disable=SC2207
    current_patches=($(awk "/$mark1/,/$mark2/{ print }" gdb.spec \
			   | grep Patch \
			   | awk '{print $2}'))

    for current_patch in "${current_patches[@]}"; do
	rm -f "$current_patch"
    done
}

skip ()
{
    local p
    p="$1"

    for skip_patch in "${skip_patches[@]}"; do
	if [ "$p" = "$skip_patch" ]; then
	    return 0
	fi
    done

    return 1
}

import_patches ()
{
    # Get the parts of gdb.spec that we want to keep unchanged.
    awk "NR==1,/$mark1/" gdb.spec \
	> gdb.spec.1
    awk "/$mark2/,/$mark3/" gdb.spec \
	> gdb.spec.3
    awk "/$mark4/,0" gdb.spec \
	> gdb.spec.5

    # Start generating the parts of gdb.spec that we want to change.
    f1=gdb.spec.2
    f2=gdb.spec.4
    rm -f $f1 $f2

    # Handle each fedora patch.
    skipped_patches=()
    n=1
    # shellcheck disable=SC2013
    for p in $(cat "$dir"/_patch_order); do
	if skip "$p"; then
	    echo "Skipped: $p"
	    skipped_patches=("${skipped_patches[@]}" "$p")

	    # Keep numbers the same as in fedora package.
	    n=$((n + 1))
	    continue
	fi

	cp "$dir"/"$p" .

	printf \
	    "%-16s%s\n" "Patch$n:" "$p" \
	    >> $f1

	echo \
	    "%patch -P $n -p1" \
	    >> $f2

	n=$((n + 1))
    done

    # Report which patches did not get skipped.
    for skip_patch in "${skip_patches[@]}"; do
	found=false
	for skipped_patch in "${skipped_patches[@]}"; do
	    if [ "$skip_patch" = "$skipped_patch" ]; then
		found=true
		break
	    fi
	done
	if ! $found; then
	    echo "Not skipped: $skip_patch"
	fi
    done

    # Assemble new gdb.spec.
    rm -f gdb.spec.new
    for n in $(seq 1 5); do
	cat gdb.spec."$n" \
	    >> gdb.spec.new
    done

    # Cleanup.
    for n in $(seq 1 5); do
	rm -f gdb.spec."$n"
    done

    # Update gdb.spec.
    mv gdb.spec.new gdb.spec
}

main ()
{
    remove_current_patches

    import_patches
}

main "$@"
