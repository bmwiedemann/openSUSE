#
# spec file for package babelstone-han-fonts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           babelstone-han-fonts
Version:        8.0.2
Release:        0
Summary:        Font for Han Script
License:        SUSE-Arphic
Group:          System/X11/Fonts
Url:            http://www.babelstone.co.uk/Fonts/
Source0:        http://babelstone.co.uk/Fonts/BabelStoneHan.zip
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
%setup -q -c -T -a0

%build
cp -a %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc LICENSE
%{_ttfontsdir}

%changelog

