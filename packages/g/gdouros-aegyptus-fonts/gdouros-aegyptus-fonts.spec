#
# spec file for package gdouros-aegyptus-fonts
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


Name:           gdouros-aegyptus-fonts
Version:        6.17
Release:        0
Summary:        Fonts with Support for Ancient Egyptian Hieroglyphs
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download source:
# http://users.teilar.gr/~g1951d/Aegyptus.zip
Source0:        Aegyptus-%{version}.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      aegyptus-fonts < 5.01
Provides:       aegyptus-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Aegyptus allocates Egyptian Hieroglyphs, in Plane 15 of the UCS. The main
sources of glyphs are «Hieroglyphica», PIREI, 2000 and the work of Alan
Gardiner. The font also covers Basic Latin, Egyptian Transliteration
characters, the Hieratic alphabet, Coptic, Meroitic, the Gardiner set
supported by Unicode, et al. The Gardiner set (redesigned with a thicker
line) is also available in the small font Gardiner.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
install -m 0644 %{SOURCE1} .

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE Aegyptus.pdf
%{_ttfontsdir}

%changelog
