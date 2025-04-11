#
# spec file for package meslo-lg-fonts
#
# Copyright (c) 2025 SUSE LLC
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


Name:           meslo-lg-fonts
Version:        1.2.2
Release:        0
Summary:        Meslo LG Font Family
License:        Apache-2.0
Group:          System/X11/Fonts
URL:            https://github.com/andreberg/Meslo-Font
# Upstream source 1.2.1:
# https://github.com/andreberg/Meslo-Font/archive/v1.2.1.tar.gz
# Downstream source 1.2.2:
# https://github.com/regularhunter/Meslo-Font/archive/1.2.2.tar.gz
Source0:        Meslo_LG_v%{version}.zip
Source1:        README.md
Source2:        COPYING
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Recommends:     meslo-lg-dz-fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Meslo LG is a customized version of Apple's Menlo-Regular font (which is
a customized Bitstream Vera Sans Mono).

%prep
%setup -qn "Meslo_LG_v%{version}"
cp %{SOURCE1} .
cp %{SOURCE2} .
# %%doc doesn't work with spaces. Let's rename the file.
mv -f "About Meslo LG v%{version}.pdf" About_Meslo_LG_v%{version}.pdf

%build

%install
mkdir -p "%{buildroot}/%{_ttfontsdir}"
install -Dpm 644 *.ttf "%{buildroot}/%{_ttfontsdir}/"

%reconfigure_fonts_scriptlets

%files
%doc About_Meslo_LG_v%{version}.pdf COPYING README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
