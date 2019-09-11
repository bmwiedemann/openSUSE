#
# spec file for package gdouros-akkadian-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gdouros-akkadian-fonts
#Provides:       locale(bg;el;ru;bg)
Version:        7.17
Release:        0
Summary:        Font with Support for Ancient Akkadian Scripts
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download source:
# http://users.teilar.gr/~g1951d/AkkadianAssyrian.zip
Source0:        AkkadianAssyrian-%{version}.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      akkadian-fonts < 2.56
Provides:       akkadian-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Akkadian covers the following scripts and symbols supported by
The Unicode Standard: Basic Latin, Greek and Coptic, some
Punctuation and other Symbols, Cuneiform, Cuneiform Numbers
 and Punctuation.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
install -m 0644 %{SOURCE1} .
mv "Akkadian Assyrian.pdf" Akkadian_Assyrian.pdf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Akkadian_Assyrian.pdf
%{_ttfontsdir}

%changelog
