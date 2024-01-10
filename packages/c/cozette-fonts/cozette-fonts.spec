#
# spec file for package cozette-fonts
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


%define fontname    Cozette
Name:           cozette-fonts
Version:        1.23.1
Release:        0
Summary:        A bitmap programming font
License:        MIT
Group:          System/X11/Fonts
URL:            https://github.com/slavfox/Cozette
Source0:        https://github.com/slavfox/Cozette/releases/download/v.%{version}/CozetteFonts-v-1-23-1.zip
Source1:        https://raw.githubusercontent.com/slavfox/Cozette/v.%{version}/README.md
Source2:        https://raw.githubusercontent.com/slavfox/Cozette/v.%{version}/CHANGELOG.md
BuildRequires:  %{suseconfig_fonts_prereq}
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A bitmap font with great coverage of all the glyphs
that might encounter in the terminal.

%prep
%setup -q -n %{fontname}Fonts
cp %{SOURCE1} .
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
find . -name "*.ttf" -execdir install -m 0644 {} %{buildroot}%{_ttfontsdir}/ \;

%reconfigure_fonts_scriptlets

%files
%{_ttfontsdir}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
