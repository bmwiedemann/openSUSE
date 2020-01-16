#
# spec file for package js-technology-fonts
#
# Copyright (c) 2019 SUSE LLC
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

%define fontname     js-technology
%define fontrepo     thai-font-collection
Name:           js-technology-fonts
Version:        0.0+git.1515043414.01c39b7
Release:        0
License:        GPL-2.0+
Summary:        JS Technology fonts
Url:            https://github.com/jeffmcneill/thai-font-collection
Group:          System/X11/Fonts
Source:         %{fontrepo}-%{version}.tar.xz
%reconfigure_fonts_prereq
BuildRequires:  fontpackages-devel
BuildRequires:  %suseconfig_fonts_prereq
BuildRoot:      %{_tmppath}/%{fontrepo}-%{version}-build
BuildArch:      noarch

%description
JS Technology fonts were initially created to support Thai language for desktop publishing in Windows operating system. 
Which was later adapted for sewing machine patterns.

%prep
%setup -n %{fontrepo}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 downloadable-free-thai-fonts/js-technology/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%{_ttfontsdir}

%doc downloadable-free-thai-fonts/js-technology/README.md

%changelog
