#!/bin/sh
#
# makespec.sh VERSION < kernel-firmware.spec.in > kernel-firmware.spec
#

export LANG=C
version="$1"

topics=$(awk '{print $1}' topicdefs | sort)

define_subpackage () {
    local topic="$1"
    local desc=$(grep '^'"$topic"'[[:space:]]' topicdefs | sed -e's/^[a-zA-Z0-9-]*[[:space:]]*//')
    echo "%package $topic"
    echo "Summary:        Kernel firmware files for $desc"
    echo "Group:          System/Kernel"
    echo "Requires(post): /usr/bin/mkdir /usr/bin/touch"
    echo "Requires(postun):/usr/bin/mkdir /usr/bin/touch"
    echo "Requires(post): dracut >= 049"
    echo "Conflicts:      kernel < 5.3"
    echo "Conflicts:      kernel-firmware < %{version}"
    echo "Conflicts:      kernel-firmware-uncompressed"
    echo "%if 0%{?suse_version} >= 1550"
    echo "# make sure we have post-usrmerge filesystem package on TW"
    echo "Conflicts:      filesystem < 84"
    echo "%endif"
    grep "^${topic}:" topicprovs | sed -e's/^[^ \t]*:[[:space:]]*//g'
    sh ./get_supplements.sh $topic
    echo
    echo "%description $topic"
    echo "This package contains compressed kernel firmware files for"
    echo "$desc."
    echo
}

define_post () {
    local l="$*"
    if [ -z "$l" -a -f uncompressed-post ]; then
	cat uncompressed-post
	return 0
    fi
    if [ -n "$l" -a -f "$l"-post ]; then
	cat "$l"-post
	return 0
    fi
    test -n "$l" && l=" $l"
    echo "%post$l"
    echo "%{?regenerate_initrd_post}"
    echo
    echo "%postun$l"
    echo "%{?regenerate_initrd_post}"
    echo
    echo "%posttrans$l"
    echo "%{?regenerate_initrd_posttrans}"
}

sed -e"s/@@VERSION@@/$version/g" | while read line; do
    if [ "$line" = "@@ALLPROVS@@" ]; then
	sed -e's/^[^ \t]*:[[:space:]]*//g' topicprovs
	continue
    fi
    if [ "$line" = "@@SUBPKGLIST@@" ]; then
	for t in $topics; do
	    echo "Requires:       %{name}-$t"
	done
	continue
    fi
    if [ "$line" = "@@SUBPKGPROVS@@" ]; then
	for t in $topics; do
	    echo "Provides:       %{name}-$t = %{version}"
	done
	continue
    fi
    if [ "$line" = "@@SUBPACKAGES@@" ]; then
	for t in $topics; do
	    define_subpackage $t
	done
	continue
    fi
    case "$line" in
	@@POST@@*)
	    define_post $(echo "$line" | sed -e's/^@@POST@@ *//')
	    continue;;
    esac
    if [ "$line" = "@@SUBPKGPOSTS@@" ]; then
	for t in $topics; do
	    echo
	    define_post $t
	done
	continue
    fi
    if [ "$line" = "@@SUBPKGFILES@@" ]; then
	for t in $topics; do
	    echo "%files -f files-$t $t"
	    echo
	done
	continue
    fi
    echo "$line"
done

exit 0
