#!/bin/bash

# Author: Thomas Renninger <trenn@suse.de>
# This code is covered and distributed under
# the General Public Licence v2

GIT_TAG=HEAD
VERSION=""
TOOL=""

function usage(){
    echo "$(basename $0) [ -k git_tag ] [ -v tag_to_use ] -t cpupower | turbostat | x86_perf_bias | intel-speed-select"
    echo
    echo "git_tag     Must be a valid kernel git tag, for example v3.1"
    echo "            if git_tag is not passed HEAD will be used which"
    echo "            may produce a package incompatible tarball name"
    echo "            BEST ALWAYS PASS AN EXISTING TAG"
    echo "            cpupower got introduced in 3.1-rc1"
    echo "tag_to_use  obs does not like -rcX as a version tag. Pass a verion"
    echo "            tag you like to use (e.g. 3.13 instead of 3.13-rc7"
    echo
    echo "export GIT_DIR= environment variable if the git repo is not the current directory"
    echo "For example: GIT_DIR=/path_to_git_repo/.git"
}

function parse_args()
{
    while getopts hv:k:t: name ; do
        case $name in
            v)
                VERSION="$OPTARG"
                ;;

            k)
                GIT_TAG="$OPTARG"
                ;;
            t)
		TOOL="$OPTARG"
		echo $TOOL
                ;;
            ?|h)
                usage
		exit 1
                ;;
	esac
    done
    shift $(($OPTIND -1))
}


function export_cpupower() {

    echo "Exporting cpupower from kernel version $GIT_TAG"

    if [ "$VERSION" = "" ];then
	# convert - to . as package versions do not allow -
	if [ $# -eq 1 ];then
	    VERSION="${GIT_TAG/-/.}"
            # remove leading v
	    VERSION="-${VERSION#v}"
	elif [ $# -eq 2 ];then
	    VERSION="${2/-/.}"
            # remove leading v
	    VERSION="-${VERSION#v}"
	elif [ $# -gt 2 ];then
	    usage
	    exit 1
	fi
    fi

    # Tried to do this with one git archive command, but
    # --remote= param seem not to be configured for kernel.org gits
set -x
    git archive --format=tar $GIT_TAG tools/power/cpupower |tar -x
set +x
    mv tools/power/cpupower cpupower-${VERSION}
    tar -cvjf cpupower-${VERSION}.tar.bz2 cpupower-${VERSION}
    popd
    mv "$DIR/cpupower-${VERSION}".tar.bz2 .
    echo cpupower-${VERSION}.tar.bz2
}

function export_turbostat() {

    git archive --format=tar $GIT_TAG tools/power/x86/turbostat |tar -x

    if [ -z "$TURBOSTAT_VERSION" ];then
	TURBOSTAT_VERSION=$(grep "turbostat version" tools/power/x86/turbostat/turbostat.c |grep fprintf  |sed 's/.*turbostat version \([0-9][0-9].[0-9][0-9].[0-9][0-9]\).*/\1/')
    fi
    TURBOSTAT_VERSION=$(echo "-$TURBOSTAT_VERSION")
    mv tools/power/x86/turbostat turbostat${TURBOSTAT_VERSION}
    git checkout $GIT_TAG include/uapi/linux/const.h
    git checkout $GIT_TAG include/vdso/bits.h
    git checkout $GIT_TAG include/vdso/const.h
    git checkout $GIT_TAG arch/x86/include/asm/msr-index.h
    git checkout $GIT_TAG arch/x86/include/asm/intel-family.h
    mkdir -p turbostat${TURBOSTAT_VERSION}/include/uapi/linux
    mkdir -p turbostat${TURBOSTAT_VERSION}/include/vdso
    cp include/uapi/linux/const.h turbostat${TURBOSTAT_VERSION}/include/uapi/linux/const.h
    cp include/vdso/bits.h turbostat${TURBOSTAT_VERSION}/include/vdso/bits.h
    cp include/vdso/const.h turbostat${TURBOSTAT_VERSION}/include/vdso/const.h
    cp arch/x86/include/asm/intel-family.h turbostat${TURBOSTAT_VERSION}
    cp arch/x86/include/asm/msr-index.h turbostat${TURBOSTAT_VERSION}
    tar -cvjf turbostat${TURBOSTAT_VERSION}.tar.bz2 turbostat${TURBOSTAT_VERSION}
    popd
    mv "$DIR/turbostat${TURBOSTAT_VERSION}".tar.bz2 .
    echo turbostat${TURBOSTAT_VERSION}.tar.bz2
}

function export_x86_perf_bias() {

set -x
    git archive --format=tar $GIT_TAG tools/power/x86/x86_energy_perf_policy |tar -x

    if [ -z "$PERF_BIAS_VERSION" ];then
	PERF_BIAS_VERSION=$(grep 'printf("x86_energy_perf_policy .* (C) Len Brown <len.brown@intel.com' tools/power/x86/x86_energy_perf_policy/x86_energy_perf_policy.c |sed 's/.*x86_energy_perf_policy \([0-9][0-9].[0-9][0-9].[0-9][0-9]\).*/\1/')
    fi
    PERF_BIAS_VERSION=$(echo "-$PERF_BIAS_VERSION")
    mv tools/power/x86/x86_energy_perf_policy x86_energy_perf_policy${PERF_BIAS_VERSION}
set +x
    git checkout $GIT_TAG arch/x86/include/asm/msr-index.h
    cp arch/x86/include/asm/msr-index.h x86_energy_perf_policy${PERF_BIAS_VERSION}
    tar -cvjf x86_energy_perf_policy${PERF_BIAS_VERSION}.tar.bz2 x86_energy_perf_policy${PERF_BIAS_VERSION}
    popd
    mv "$DIR/x86_energy_perf_policy${PERF_BIAS_VERSION}".tar.bz2 .
    echo x86_energy_perf_policy${PERF_BIAS_VERSION}.tar.bz2

}

function export_intel-speed-select {

    set -x
    git archive --format=tar $GIT_TAG tools/power/x86/intel-speed-select |tar -x

    if [ -z "$SPEED_SELECT_VERSION" ];then
	SPEED_SELECT_VERSION=$(sed -n -e 's#static const char \*version_str = "v\(.*\)";#\1#p' tools/power/x86/intel-speed-select/isst-config.c)
    fi
    SPEED_SELECT_VERSION=$(echo "-$SPEED_SELECT_VERSION")
    mv tools/power/x86/intel-speed-select intel-speed-select${SPEED_SELECT_VERSION}
    set +x
    git checkout $GIT_TAG include/uapi/linux/isst_if.h
    mkdir -p intel-speed-select${SPEED_SELECT_VERSION}/include/linux
    cp include/uapi/linux/isst_if.h intel-speed-select${SPEED_SELECT_VERSION}/include/linux
    tar -cvjf intel-speed-select${SPEED_SELECT_VERSION}.tar.bz2 intel-speed-select${SPEED_SELECT_VERSION}
    popd
    mv "$DIR/intel-speed-select${SPEED_SELECT_VERSION}".tar.bz2 .
    echo intel-speed-select${SPEED_SELECT_VERSION}.tar.bz2
}

parse_args $*

DIR=`mktemp -d`
pushd "$DIR"

if [ "$GIT_DIR" = "" ];then
    export GIT_DIR=/archteam/trenn/git/linux-2.6/.git
fi

case $TOOL in
    cpupower)
        export_cpupower
        ;;
    turbostat)
        export_turbostat
        ;;
    x86_perf_bias)
	export_x86_perf_bias
        ;;
    intel-speed-select)
	set -x
	export_intel-speed-select
	;;
    *)
	echo "You have to provide the tool you want to export cpupower|turbostat|x86_energy_perf_bias|intel-speed-select"
	usage
	rm -rf "$DIR"
	exit 1
	;;
esac
rm -rf "$DIR"
