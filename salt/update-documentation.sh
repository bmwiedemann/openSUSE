#!/bin/bash
#
# Update html.tar.bz2 documentation tarball
# Author: Bo Maryniuk <bo@suse.de>
#

NO_SPHINX_PARAM="--without-sphinx"

function build_virtenv() {
    virtualenv --system-site-packages $1
    source $1/bin/activate
    pip install --upgrade pip
    if [ -z "$2" ]; then
	pip install -I Sphinx
    fi
}

function check_env() {
    if [[ -z "$1" || "$1" != "$NO_SPHINX_PARAM" ]] && [ ! -z "$(which sphinx-build 2>/dev/null)" ]; then
	cat <<EOF
You've installed Spinx globally. But it might be outdated or
clash with the version I am going to install into the temporary
virtual environment from PIP.

Please consider to remove Sphinx from your system, perhaps?
Or pass me "$NO_SPHINX_PARAM" param so I will try reusing yours
and see what happens. :)

EOF
	exit 1;
    fi

    for cmd in "make" "quilt" "virtualenv" "pip"; do
	if [ -z "$(which $cmd 2>/dev/null)" ]; then
	    echo "Error: '$cmd' is still missing. Install it, please."
	    exit 1;
	fi
    done
}

function quilt_setup() {
    quilt setup salt.spec
    cd $1
    quilt push -a
}

function build_docs() {
    cd $1
    make html
    rm _build/html/.buildinfo
    cd _build/html
    chmod -R -x+X *
    cd ..
    tar cvf - html | bzip2 > $2/html.tar.bz2
}

function write_changelog() {
    mv salt.changes salt.changes.previous
    TIME=$(date -u +'%a %b %d %T %Z %Y')
    MAIL=$1
    SEP="-------------------------------------------------------------------"
    cat <<EOF > salt.changes
$SEP
$TIME - $MAIL

- Updated html.tar.bz2 documentation tarball.

EOF
    cat salt.changes.previous >> salt.changes
    rm salt.changes.previous
}

if [ -z "$1" ]; then
    echo "Usage: $0 <your e-mail> [--without-sphinx]"
    exit 1;
fi

check_env $2;

START=$(pwd)
V_ENV="sphinx_doc_gen"
V_TMP=$(mktemp -d)

for f in "salt.spec" "salt*tar.gz"; do
    cp -v $f $V_TMP
done

cd $V_TMP;
build_virtenv $V_ENV $2;

SRC_DIR="salt-$(cat salt.spec | grep ^Version: | cut -d: -f2 | sed -e 's/[[:blank:]]//g')";
quilt_setup $SRC_DIR
build_docs doc $V_TMP

cd $START
mv $V_TMP/html.tar.bz2 $START
rm -rf $V_TMP

echo "Done"
echo "---------------"
