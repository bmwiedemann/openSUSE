#
# spec file for package babelstone-ogham-fonts
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


Name:           babelstone-ogham-fonts
Version:        20220314
Release:        0
Summary:        BabelStone Font for Ogham Script
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.babelstone.co.uk/Fonts/
Source0:        https://www.babelstone.co.uk/Fonts/Download/BabelStoneOghamFonts.zip
Source1:        https://www.babelstone.co.uk/Fonts/BabelStoneOFL.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A set of twelve Unicode Ogham fonts in seven font families, representing
a variety of different styles of Ogham letters found in manuscripts and
on Ogham stone inscriptions.

%prep
%autosetup -c -T -a0

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
