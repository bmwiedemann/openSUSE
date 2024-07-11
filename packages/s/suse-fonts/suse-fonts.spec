#
# spec file for package suse-fonts
#
# Copyright (c) 2024 SUSE LLC
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


Name:           suse-fonts
Version:        0~20240710
Release:        0
Summary:        SUSE font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/SUSE/suse-font
# Fetched from https://github.com/SUSE/suse-font/actions/runs/9857187979
Source0:        %{name}-%{version}.zip
Source1:        https://raw.githubusercontent.com/SUSE/suse-font/main/OFL.txt
Source2:        https://raw.githubusercontent.com/SUSE/suse-font/main/README.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
SUSE is a sans serif typeface designed by René Bieder, embodying a unique
hybrid between geometric and monospaced features. It captures the essence of
SUSE, a company renowned for its open-source solutions. This versatile typeface
family includes the following styles: Thin, ExtraLight, Light, Regular, Medium,
SemiBold, Bold, and ExtraBold.

%prep
%setup -q -c -T -a0
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 fonts/otf/*.otf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc README.md
%{_ttfontsdir}

%changelog
