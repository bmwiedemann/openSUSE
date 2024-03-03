#!/bin/sh

commit="242f240b883b2515ccf2b4f82085f8484cd00a38"
fcitxcommit="fdf255839144638b9759b5ad98b5151fd28bb3ca"

set -e

for opt in $*; do
    case $opt in
        --without-mozc)    withoutmozc=1 ;;
        --without-fcitx)   withoutfcitx=1 ;;
        --without-zipcode) withoutzipcode=1 ;;
    esac
done


if [ -z $withoutmozc ]; then
    if [ ! -e mozc ]; then
        git clone --depth=1 https://github.com/google/mozc.git
        cd mozc
    else
        cd mozc
        git restore .
        git fetch
    fi

    git checkout $commit

    vermajor=`sed -n -e "s/MAJOR = \(.*\)/\1/p" src/data/version/mozc_version_template.bzl`
    verminor=`sed -n -e "s/MINOR = \(.*\)/\1/p" src/data/version/mozc_version_template.bzl`
    verbuild=`sed -n -e "s/BUILD_OSS = \(.*\)/\1/p" src/data/version/mozc_version_template.bzl`
    # REVISION is always 102 for Linux
    version=$vermajor.$verminor.$verbuild.102

    git archive --prefix=mozc-$version/ $commit | tar xC ../
    cd ..
    rm -r mozc-$version/src/third_party/*
    rm -r mozc-$version/docker
    tar --owner=0 --group=0 -cvJf mozc-$version.tar.xz mozc-$version
fi

if [ -z $withoutfcitx ]; then
    if [ ! -e fcitx-mozc ]; then
        git clone --depth=1 https://github.com/fcitx/mozc.git fcitx-mozc
        cd fcitx-mozc
    else
        cd fcitx-mozc
        git restore .
        git fetch
    fi

    git checkout $fcitxcommit

    git archive --format=tar $fcitxcommit \
    src/unix/fcitx src/unix/fcitx5 | \
    xz > ../fcitx-mozc-`echo $fcitxcommit | cut -c 1-8`.tar.xz
    cd ..
fi

if [ -z $withoutzipcode ]; then
    curl -O https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
    curl -O https://www.post.japanpost.jp/zipcode/dl/jigyosyo/zip/jigyosyo.zip
    kenallsha256=`sha256sum ken_all.zip | cut -d ' ' -f 1`
    jigyosyosha256=`sha256sum jigyosyo.zip | cut -d ' ' -f 1`
    sed -e "s/@kenallsha256@/$kenallsha256/" \
        -e "s/@jigyosyosha256@/$jigyosyosha256/" \
        < add-sha256sum-for-zipcode-archives.patch.in \
        > add-sha256sum-for-zipcode-archives.patch
fi
