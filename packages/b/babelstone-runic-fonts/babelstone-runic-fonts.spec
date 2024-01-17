#
# spec file for package babelstone-runic-fonts
#
# Copyright (c) 2022 SUSE LLC
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


Name:           babelstone-runic-fonts
Version:        20131112
Release:        0
Summary:        Font for Runic Script
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.babelstone.co.uk/Fonts/
Source0:        https://www.babelstone.co.uk/Fonts/Download/BabelStoneAngloSaxon.zip
Source1:        https://www.babelstone.co.uk/Fonts/BabelStoneOFL.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A set of six Runic fonts that each cover the subset of 34 characters
in the Unicode Runic block that are used in Frisian and Anglo-Saxon
inscriptions from the 5th to 11th centuries.

%prep
%setup -q -c -T -a0

%build
cp -a %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%license BabelStoneOFL.txt
%{_ttfontsdir}

%changelog
