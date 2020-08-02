#
# spec file for package gdouros-musica-fonts
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


Name:           gdouros-musica-fonts
Version:        3.17
Release:        0
Summary:        Font with Support for Unicode Musical Notation Symbols
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://greekfonts.teilar.gr
# Download source:
# http://users.teilar.gr/~g1951d/Musica.zip
Source0:        Musica-%{version}.zip
Source1:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Obsoletes:      musica-fonts < 3.11
Provides:       musica-fonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Musica covers the following scripts and symbols supported by The Unicode
Standard: Basic Latin, Greek and Coptic, some Punctuation and other Symbols,
Byzantine Musical Symbols, (Western) Musical Symbols and Archaic Greek
Musical Notation.

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
%doc README-SUSE Musica.pdf
%{_ttfontsdir}

%changelog
