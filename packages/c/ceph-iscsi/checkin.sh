#!/bin/bash
#
# checkin.sh
#
# This script automates generation of a new tarball and spec file from a
# git clone or repo+branch combination for the "ceph-iscsi" package
# in OBS.
#

set -x

PROJECT="ceph-iscsi"
DEFAULT_REPO="https://github.com/SUSE/$PROJECT.git"
DEFAULT_BRANCH="ses6"
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
    echo "    Repo defaults to $DEFAULT_REPO"
    echo "    Branch defaults to $DEFAULT_BRANCH"
    exit 1
}

function _error_exit {
    echo >&2 $1
    exit $2
}

function _check_clone {
    local OPT="$1"
    if [ -z "$OPT" ] ; then
        _error_exit "Empty string sent to internal function _check_clone"
    fi
    if [ -e "$OPT/$PROJECT.spec" ] ; then
        echo "$OPT looks like a $PROJECT clone; using it"
    else
        _error_exit "$OPT does not appear to be a $PROJECT clone" 1
    fi
}

GETOPT=$(getopt -o b:e:hr: --long "branch:,existing:,help,repo:" \
       -n 'checkin.sh' -- "$@")
test "$?" -eq 0 || _error_exit "Terminating..." 1
eval set -- "$GETOPT"

REPO="$DEFAULT_REPO"
BRANCH="$DEFAULT_BRANCH"
while true ; do
    case "$1" in
        -b|--branch)   BRANCH="$2"   ; shift 2 ;;
        -h|--help)     usage ;; # does not return
        -r|--repo)     REPO="$2"     ; shift 2 ;;
        --) shift ; break ;;
        *) echo "Internal error" ; exit 1 ;;
    esac
done

echo "Will make pristine, temporary clone of repo ->$REPO<- branch ->$BRANCH<-"
#TMPDIR=$(mktemp -d --tmpdir=$BASEDIR)
TMPDIR=$(mktemp -d)
TMPDIR+="/clone"
mkdir $TMPDIR
echo "Created temporary temporary $TMPDIR"
git clone --branch $BRANCH $REPO $TMPDIR
CLONE="$TMPDIR"
_check_clone "$CLONE"

echo "Running \"osc rm *gz\" to nuke previous tarball"
if type osc > /dev/null 2>&1 ; then
    osc rm *gz
else
    _error_exit "osc not installed - cannot continue" 1
fi
if stat --printf='' *.gz 2>/dev/null ; then
    _error_exit "There are still files ending in gz in the current directory - clean up yourself!" 1
fi

THIS_DIR=$(pwd)
pushd $CLONE
if [ ! -d .git ]; then
    echo "no .git present.  run this from the base dir of the git checkout."
    exit 1
fi
GIT_SHA1=$(git describe --long --tags | cut -d"-" -f3)
echo "Extracting spec file"
VERSION=$(grep ^Version *spec | sed -r "s/^Version:\s+//")
VERSION="${VERSION}+$(date +%s).${GIT_SHA1}"
sed -i -e 's/^Version:.*/Version:        '$VERSION'/' $PROJECT.spec
sed -i -e 's#^Source0:.*#Source0:        %{name}-%{version}.tar.gz#' $PROJECT.spec
sed -i -e '/Source0/a %if 0%{?suse_version}\nSource98:       checkin.sh\nSource99:       README-checkin.txt\nExclusiveArch:  x86_64 aarch64 ppc64le s390x\n%endif' $PROJECT.spec
sed -i -e '/BuildArch:\s\+noarch/d' $PROJECT.spec
sed -i -e 'N;/^\n$/D;P;D;' $PROJECT.spec  # collapse multiple adjacent newlines down to a single newline
cp $PROJECT.spec $THIS_DIR
echo "Version number is ->$VERSION<-"
cd ..
mv clone "$PROJECT-$VERSION"
echo "Creating tarball"
tar cvfz $THIS_DIR/$PROJECT-$VERSION.tar.gz --exclude .git "$PROJECT-$VERSION"
popd

echo "Running \"osc add *gz\" to register the new tarball"
osc add *gz

if [ -n "$TMPDIR" ] ; then
    echo "Nuking the temporary clone"
    rm -rf $TMPDIR
fi

#echo "Running pre_checkin.sh (if you touch the ceph.changes file after running this script, re-run pre_checkin.sh manually)"
#if [ -f "pre_checkin.sh" ] ; then
#    bash pre_checkin.sh
#else
#    echo "WARNING: no pre_checkin.sh script found!"
#fi

echo "Done! Run \"osc ci --noservice\" to commit."
