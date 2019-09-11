#
# spec file for package xano-mincho-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xano-mincho-fonts
Version:        20040509
Release:        0
Summary:        Japanese "XANO-Mincho-U32" TrueType font JIS X 0213:2004
License:        SUSE-Xano
Group:          System/X11/Fonts
Url:            http://www.asahi-net.or.jp/~sd5a-ucd/freefonts/XANO-mincho/
# original archive was in .zip format. Converted to .tar.bz2 to save some
# space in the .src.rpm file  The original archive also contained a .otf file.
# This file is removed to save some more space in the .src.rpm file.
# The .otf file contains only glyphs from the BMP and even in the BMP it contains
# fewer glyphs than the .ttf file. On top of that, the hinting in the .otf file
# seems to less good than the hinting in the .ttf file.
Source0:        xano-mincho-20040509.tar.bz2
BuildRequires:  fontpackages-devel
Provides:       scalable-font-ja
Provides:       xano-mincho = %{version}
Provides:       locale(ja)
Obsoletes:      xano-mincho <= 20040509
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Japanese "XANO-Mincho-U32" TrueType font JIS X 0213:2004

%prep
%setup -n xano-mincho-%{version}

%build
for i in README.txt
do
    iconv -f SHIFT-JIS -t UTF-8 < $i > $i.UTF-8
    mv $i.UTF-8 $i
done

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc README.txt license.txt
%{_ttfontsdir}

%changelog
