#!/bin/bash

reponame="javaee-jsp-api"
pkgname="javax.servlet.jsp-api"

version=`grep Version: *spec | sed -e 's/Version:\s*\(.*\)/\1/'`
version="$version`sed -n 's/%global\s\+reltag\s\+/-/p' *.spec`"
echo $version

test ! -d $reponame
git clone https://github.com/javaee/$reponame
cd $reponame
git checkout -b tag-${pkgname}-${version} ${pkgname}-${version}
git archive --format=tar --prefix=${pkgname}-${version}/ HEAD:api \
    | xz >../${pkgname}-${version}.tar.xz
