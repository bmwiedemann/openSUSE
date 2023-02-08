#!/bin/bash
#
# checkin.sh
#
# This script automates generation of a new tarball and spec file from a
# git clone or repo+branch combination for the "ceph" package in OBS.
#

set -x

BASEDIR=$(pwd)

function usage {
    set +x
    echo "Usage:"
    echo "  ${0} [-h,--help] [-e,--existing CLONE]"
    echo "             [-r,--repo REPO] [-b,--branch BRANCH]"
    echo ""
    echo "Options:"
    echo "    --existing  Use existing ceph clone CLONE"
    echo "    --repo      Make a fresh clone of ceph repo REPO"
    echo "    --branch    Use branch BRANCH with fresh clone"
    echo ""
    echo "Notes:"
    echo "    If existing clone is given, repo and branch are ignored."
    echo "    Repo defaults to https://github.com/SUSE/ceph.git"
    echo "    Branch defaults to ses7p"
    exit 1
}

function _error_exit {
    echo >&2 $1
    exit $2
}

function _check_ceph_clone {
    local OPT="$1"
    if [ -z "$OPT" ] ; then
        _error_exit "Empty string sent to internal function _check_ceph_clone"
    fi
    if [ -e "$OPT/make-dist" ] ; then
        echo "$OPT looks like a ceph clone; using it"
    else
        _error_exit "$OPT does not appear to be a ceph clone" 1
    fi
}

function _verify_git_describe {
    git describe --match 'v*'
    echo "Does this version number looks sane? y/[N]"
    read a
    if [ "x$a" != "xy" ] ; then
        _error_exit "Aborting!" 1
    fi
}

GETOPT=$(getopt -o b:e:hr: --long "branch:,existing:,help,repo:" \
       -n 'checkin.sh' -- "$@")
test "$?" -eq 0 || _error_exit "Terminating..." 1
eval set -- "$GETOPT"

EXISTING=""
REPO="https://github.com/SUSE/ceph.git"
BRANCH="ses7p"
while true ; do
    case "$1" in
        -b|--branch)   BRANCH="$2"   ; shift 2 ;;
        -e|--existing) EXISTING="$2" ; shift 2 ;;
        -h|--help)     usage ;; # does not return
        -r|--repo)     REPO="$2"     ; shift 2 ;;
        --) shift ; break ;;
        *) echo "Internal error" ; exit 1 ;;
    esac
done

if [ -n "$EXISTING" ] ; then
    if [ ! -d "$EXISTING" ] ; then
        _error_exit "Alleged directory ->$EXISTING<- is not a directory" 1
    fi
    if [ ! -r "$EXISTING" ] ; then
        _error_exit "I cannot read directory ->$EXISTING<-" 1
    fi
    if [ ! -w "$EXISTING" ] ; then
        _error_exit "I cannot write to directory ->$EXISTING<-" 1
    fi
    if [ ! -x "$EXISTING" ] ; then
        _error_exit "I cannot cd to directory ->$EXISTING<-" 1
    fi
    CLONE="$EXISTING"
else
    echo "Will make fresh clone of repo ->$REPO<- branch ->$BRANCH<-"
    # TMPDIR=$(mktemp -d --tmpdir=$BASEDIR)  # does not work due to http://tracker.ceph.com/issues/39556
    TMPDIR=$(mktemp -d)
    echo "Created temporary temporary $TMPDIR"
    git clone --progress --branch $BRANCH $REPO $TMPDIR
    CLONE="$TMPDIR"
fi
_check_ceph_clone "$CLONE"

pushd $CLONE
#_verify_git_describe
if [ -z "$TMPDIR" ] ; then
    echo "Deleting stale tarballs from previous runs"
    rm -rf *.bz2
fi
echo "Running make-dist inside clone"
export DASHBOARD_FRONTEND_LANGS="ALL"
./make-dist
popd

echo "Running \"osc rm *bz2\" to nuke previous tarball"
if type osc > /dev/null 2>&1 ; then
    osc rm *bz2
else
    _error_exit "osc not installed - cannot continue" 1
fi

if stat --printf='' *.bz2 2>/dev/null ; then
    _error_exit "There are still files ending in bz2 in the current directory - clean up yourself!" 1
fi

echo "Copying new spec file and tarball from $CLONE"
cp $CLONE/ceph.spec $CLONE/ceph*bz2 .

if [ -n "$TMPDIR" ] ; then
    echo "Nuking the clone"
    rm -rf $TMPDIR
fi

echo "Running \"osc add *bz2\" to register the new tarball"
osc add *bz2

echo "Running pre_checkin.sh (if you touch the ceph.changes file after running this script, re-run pre_checkin.sh manually)"
if [ -f "pre_checkin.sh" ] ; then
    bash pre_checkin.sh
else
    echo "WARNING: no pre_checkin.sh script found!"
fi

echo "Done! Run \"osc ci --noservice\" to commit."
