#
# spec file for package int10h-oldschoolpc-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.0
Release:        0
Summary:        Remakes of old computer hardware fonts
License:        CC-BY-SA-4.0
Group:          System/X11/Fonts
URL:            http://int10h.org/oldschool-pc-fonts/

Source:         http://int10h.org/oldschool-pc-fonts/download/ultimate_oldschool_pc_font_pack_v1.0.zip
Source8:        ratio.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This fontpack contains remakes of various type styles
from text-mode era PCs — in modern Unicode-compatible TrueType form
(plus straight bitmap versions). The main focus is on hardware
character sets: the kind that's located in a ROM and shown by default
when working in text (or graphics) mode.

[ Classic hardware text mode stretches the fonts to fit the screen!
To recreate the same visuals of that, a stretch factor must be
applied. For details, see ratio.txt inside the package. ]

%prep
%setup -Tcqa0
cp "%_sourcedir/ratio.txt" .

%build
iconv -f cp437 -t utf-8 <README.NFO | perl -i -pe 's{\r}{}g' >readme.txt
mv LICENSE.TXT license.txt

%install
c="%buildroot/%_ttfontsdir"
mkdir -p "$c"
install -pm 0644 */*.ttf "$c/"

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc readme.txt license.txt ratio.txt
%_ttfontsdir/

%changelog
