#!/usr/bin/bash

set -eu

VERSION=0.1
TARBALL_NAME=teluguvijayam-$VERSION
FONTS=(SyamalaRamana.ttf PottiSreeramulu.ttf ramabhadra.ttf dhurjati.ttf mallanna.ttf Ramaraja-Regular.ttf suranna.ttf TenaliRamakrishna-Regular.ttf TimmanaRegular.ttf Peddana-Regular.ttf Sree%20Krushnadevaraya.ttf Ponnala.ttf LakkiReddy.ttf RaviPrakash.ttf Gidugu.ttf Gurajada.ttf Suravaram.ttf NTR.ttf Mandali-Regular.ttf NATS.ttf)
CURDIR=$(pwd)
mkdir "$CURDIR"/"$TARBALL_NAME"

download_tarball(){
    download_url=$1
    download_filename=$2

    echo "Downloading $2..."
    wget -q "$download_url"/"$download_filename" -O \
        "$CURDIR/$TARBALL_NAME/$download_filename"
}

for file in ${FONTS[*]}; do
    download_tarball "https://siliconandhra.org/fonts/" "$file"
done

# Remove Special characters for some font names
cd $CURDIR/$TARBALL_NAME/
mv Sree%20Krushnadevaraya.ttf SreeKrushnadevaraya.ttf

echo "Creating the Tarball..."
tar --owner root --group root --mode a+rX -cvf - -C "$CURDIR"\
 "$TARBALL_NAME" | xz > "$CURDIR"/"$TARBALL_NAME".tar.xz

echo "Cleaning up..."
rm -rf "$CURDIR"/"$TARBALL_NAME"
