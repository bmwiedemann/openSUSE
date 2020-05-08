#!/bin/sh
# This expects to be run from the package dir
# and will build a single package
set -x
project=${project:-`cat ../.project 2>/dev/null`}
project=${project:-openSUSE:Factory}
set -e
repo=${repo:-standard}
arch=${arch:-x86_64}
pkg=$(basename $(pwd))
mkdir -p .osc
echo "$project" > .osc/_project
echo "$pkg" > .osc/_package
prjconf=.osc/_buildconfig-$repo-$arch
buildinfo=.osc/_buildinfo-$repo-$arch
cat > $prjconf <<EOPRJCONF
%define _project openSUSE:Factory
%define _repository standard
Macros:
%vendor obs://build.opensuse.org/openSUSE:Factory
%_download_url http://download.opensuse.org/repositories
%_project openSUSE:Factory
%distribution openSUSE:Factory
%_project openSUSE:Factory
%_repository standard
:Macros
EOPRJCONF
cat ../../_/_project/_config >> $prjconf
#osc buildinfo > $buildinfo

osc build --noservice "$@"
