#!/bin/bash

# macro: translate_suse_desktop
#
#     Used to add translation to a SUSE specifc .desktop files.
#

set -o errexit
intltool-merge /usr/share/translate-suse-desktop $1.in $1 -d -u
mkdir -p suse_translate_desktop
cd suse_translate_desktop
ln ../$1.in .
intltool-extract --type=gettext/ini $1.in
xgettext --default-domain=$APPLICATION --add-comments --keyword=_ --keyword=N_ --keyword=U_ $1.in.h -o ${1%.desktop}.pot
RPM_OTHER_DIR=${RPM_BUILD_DIR%/BUILD*}/OTHER
if test -f $RPM_OTHER_DIR/translate-suse-desktop.tar.gz ; then
    X=r
else
    X=c
fi
tar ${X}f $RPM_OTHER_DIR/translate-suse-desktop.tar.gz ${1%.desktop}.pot
echo "Wrote ${1%.desktop}.pot to $RPM_OTHER_DIR/translate-suse-desktop.gz"
echo "with for https://github.com/openSUSE/suse-desktop-translations translatable by"
echo "https://l10n.opensuse.org/projects/suse-desktop-translations/"
