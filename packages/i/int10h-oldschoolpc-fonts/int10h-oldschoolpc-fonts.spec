#
# spec file for package int10h-oldschoolpc-fonts
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           int10h-oldschoolpc-fonts
Version:        2.1
Release:        0
Summary:        Remakes of old computer hardware fonts
License:        CC-BY-SA-4.0
Group:          System/X11/Fonts
URL:            http://int10h.org/oldschool-pc-fonts/

Source:         https://int10h.org/oldschool-pc-fonts/download/oldschool_pc_font_pack_v2.1_FULL.zip
Source8:        ratio.txt
BuildRequires:  fontpackages-devel
BuildRequires:  lcdf-typetools
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
This fontpack contains remakes of various type styles from text-mode
era PCs — in modern Unicode-compatible TrueType form (plus straight
bitmap versions). The main focus is on hardware character sets: the
kind that's located in a ROM and shown by default when working in
text (or graphics) mode.

[ Classic hardware text mode stretches the fonts to fit the screen!
To recreate the same visuals of that, a stretch factor must be
applied. For details, see ratio.txt inside the package. ]

%package stretched
Summary:        Pre-stretched versions of int10h-oldschoolpc-fonts
Group:          System/X11/Fonts
Conflicts:      %name < %version
Conflicts:      %name > %version
%reconfigure_fonts_prereq

%description stretched
This package contains aspect-corrected and non-corrected-but-stretched
variants of the main font files.

%prep
%setup -Tcqa0
cp "%_sourcedir/ratio.txt" .

%build
iconv -f cp437 -t utf-8 <README.NFO | perl -i -pe 's{\r}{}g' >readme.txt
mv LICENSE.TXT license.txt

%install
mkdir mxs
mv */Mx*-2[xy]*.ttf mxs/

c="%buildroot/%_sharedir/fontconfig/conf.avail"
tt="%buildroot/%_ttfontsdir"
mkdir -p "$c" "$tt"

genalias()
{
	echo "<?xml version='1.0'?>"
	echo '<!DOCTYPE'" fontconfig SYSTEM 'fonts.dtd'>"
	echo "<fontconfig>"
	for i in "$@"; do
		mx="$(otfinfo -i "$i" | perl -lne 'if(/^Family:\s*(.*)/){$_=$1;s{&}{&amp;}g;print}')"
		px="Px${mx:2}"
		echo "<alias><family>$px</family><prefer><family>$mx</family></prefer></alias>"
	done
	echo "</fontconfig>"
}

genalias mxs/Mx*.ttf >31-int10h-stretch-alias.conf
mv mxs/*.ttf "$tt/"
genalias */Mx*.ttf >31-int10h-alias.conf
mv */Ac*.ttf */Mx*.ttf "$tt/"
%install_fontsconf 31-int10h-alias.conf
%install_fontsconf 31-int10h-stretch-alias.conf

%reconfigure_fonts_scriptlets
%reconfigure_fonts_scriptlets -n %name-stretched

%files
%license license.txt
%doc readme.txt ratio.txt
%_ttfontsdir/Mx*
%exclude %_ttfontsdir/*-2x.ttf
%exclude %_ttfontsdir/*-2y.ttf
%dir %_sysconfdir/fonts
%dir %_sysconfdir/fonts/conf.d
%files_fontsconf_availdir
%files_fontsconf_file -l 31-int10h-alias.conf

%files stretched
%dir %_ttfontsdir/
%_ttfontsdir/Ac*
%_ttfontsdir/Mx*-2x.ttf
%_ttfontsdir/Mx*-2y.ttf
%dir %_sysconfdir/fonts
%dir %_sysconfdir/fonts/conf.d
%files_fontsconf_availdir
%files_fontsconf_file -l 31-int10h-stretch-alias.conf

%changelog
