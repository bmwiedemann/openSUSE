#
# spec file for package cadsondemak-fonts
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

%define fontname     cadsondemak
Name:           cadsondemak-fonts
Version:        0.0+git.1535343411.3adc93a
Release:        0
License:        OFL-1.1
Summary:        Cadson Demak fonts
Url:            https://github.com/%{fontname}
Group:          System/X11/Fonts
Source:         %{fontname}.github.io-%{version}.tar.xz
Source1:        OFL.txt
Source2:        AUTHORS.txt
%reconfigure_fonts_prereq
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRequires:  %suseconfig_fonts_prereq
BuildRoot:      %{_tmppath}/%{fontname}.github.io-%{version}-build
BuildArch:      noarch

%description
Cadson Demak fonts are inspired from an old Thai font design, which give old traditional vibes but works well on modern design.

%prep
%setup -n %{fontname}.github.io-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 fonts/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%{_ttfontsdir}

%changelog
