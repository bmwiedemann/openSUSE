#
# spec file for package babelstone-han-fonts
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


Name:           babelstone-han-fonts
Version:        15.0.4
Release:        0
Summary:        BabelStone font for Han Script
License:        SUSE-Arphic
# Change to Arphic-1999 after openSUSE's rpmlint gets synced
# https://github.com/spdx/license-list-XML/issues/1404
Group:          System/X11/Fonts
URL:            http://www.babelstone.co.uk/Fonts/
Source0:        http://babelstone.co.uk/Fonts/Download/BabelStoneHan.zip
Source1:        LICENSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
BabelStone Han is a dual-width Unicode Han font in Song/Ming style
with G-source glyphs used in the People's Republic of China.

%prep
%autosetup -c -T -a0

%build
cp -a %{SOURCE1} .

%install
install -Dm 0644 -t %{buildroot}%{_ttfontsdir}/ *.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/BabelStoneHan.ttf

%changelog
