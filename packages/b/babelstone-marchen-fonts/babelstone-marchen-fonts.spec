#
# spec file for package babelstone-marchen-fonts
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


Name:           babelstone-marchen-fonts
Version:        9.003
Release:        0
Summary:        BabelStone Font for Marchen script
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.babelstone.co.uk/Fonts/
Source0:        https://www.babelstone.co.uk/Fonts/Download/BabelStoneMarchen.ttf
Source1:        https://www.babelstone.co.uk/Fonts/BabelStoneOFL.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
BabelStone Marchen is a font for the sMar-chen script, which is based
on the deprecated experimental BabelStone Tibetan sMar-chen font. This
font uses the encoding specified by Unicode for Marchen script.

%prep
%autosetup -c -T
cp -a %{SOURCE0} .

%build
cp -a %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%license BabelStoneOFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/BabelStoneMarchen.ttf

%changelog
