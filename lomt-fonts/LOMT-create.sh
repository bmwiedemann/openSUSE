#!/bin/sh -ex
#
# Creates the LOMT tarball from all the single repositories.
#

url="git://github.com/theleagueof";
fonts="league-gothic blackout knewave ostrich-sans fanwood linden-hill
	league-script-number-one raleway prociono orbitron
	goudy-bookletter-1911 sorts-mill-goudy chunk sniglet junction";
if [ -z "$SKIP_GIT" ]; then
	mkdir -p git;
	pushd git;
	for i in $fonts; do
		if [ -d "$i" ]; then
			pushd "$i";
			git pull;
			popd;
		else
			git clone "$url/$i";
		fi;
	done;
	popd;
fi;

#
#	Copy files from git to "LOMT"
#
rm -Rf LOMT;
mkdir LOMT;
pushd git/;
find $fonts -maxdepth 1 -type f "(" -name "*.otf" -o -name "*.ttf" ")" \
	-exec cp -a "{}" ../LOMT/ ";";
for i in $fonts; do
	cp -a "$i/readme.markdown" "../LOMT/$i.markdown";
	cp -af "$i"/Open*Font*markdown ../LOMT/;
done;
popd; # git/

#
#	Remove duplicate fonts
#
for i in LOMT/*.otf; do
	rm -f "${i%.otf}.ttf";
done;
rm -f LOMT/OFLGoudyStMTT*.ttf;
