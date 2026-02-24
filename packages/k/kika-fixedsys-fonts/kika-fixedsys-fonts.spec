#
# spec file for package kika-fixedsys-fonts
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           kika-fixedsys-fonts
Version:        3.09.10
Release:        0
Summary:        The "Fixedsys Excelsior" font
License:        SUSE-Public-Domain
Group:          System/X11/Fonts
URL:            https://github.com/kika/fixedsys/
Source:         https://github.com/kika/fixedsys/releases/download/v%version/FSEX302.ttf
Source2:        https://github.com/kika/fixedsys/raw/master/README.md
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A TrueType (vector) font similar to Windows 2.x/3.x Fixedsys,
enhanced with Unicode symbols.

%prep
%setup -Tcq
cp -av %_sourcedir/README.md .

%build

%install
mkdir -pv "%buildroot/%_ttfontsdir"
cp -av %_sourcedir/*.ttf "%buildroot/%_ttfontsdir/"

%reconfigure_fonts_scriptlets

%files
%license README.md
%_ttfontsdir/

%changelog
