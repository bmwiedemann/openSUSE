#
# spec file for package cozette-fonts
#
# Copyright (c) 2020 SUSE LLC
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

%define ttf_fontdir %{_datadir}/fonts/truetype
%define fontname    Cozette
%define fontversion    1.9.2
Name:           cozette-fonts
Version:        1.9.2+git.1601275698.ea2ec2b
Release:        0
Summary:        A bitmap programming font
License:        MIT
Group:          System/X11/Fonts
URL:            https://github.com/slavfox/Cozette
Source0:        Cozette-%{version}.tar.xz
Source1:        %{url}/releases/download/v.%{fontversion}/CozetteVector.otf
BuildRequires:  %{suseconfig_fonts_prereq}
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A bitmap font with great coverage of all the glyphs
that might encounter in the terminal.

%prep
%setup -q -n %{fontname}-%{version} 

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%{_ttfontsdir}

%license LICENSE
%doc CHANGELOG.md README.md

%changelog
