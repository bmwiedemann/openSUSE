#
# spec file for package redhat-overpass-fonts
#
# Copyright (c) 2023 SUSE LLC
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


%global desc Overpass is a (sans-serif) font family inspired by Highway Gothic.
Name:           redhat-overpass-fonts
Version:        3.0.5
Release:        0
Summary:        A font family inspired by Highway Gothic
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://overpassfont.org/
Source0:        https://github.com/RedHatOfficial/Overpass/releases/download/v%{version}/overpass-%{version}.zip
Source1:        https://github.com/RedHatOfficial/Overpass/raw/master/OFL.txt
Source2:        https://github.com/RedHatOfficial/Overpass/raw/master/AUTHORS.txt
Source3:        https://github.com/RedHatOfficial/Overpass/raw/master/CONTRIBUTORS.txt
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
%{desc}

This package contains the proportional variants in OpenType format.

%package -n redhat-overpass-mono-fonts
Summary:        Overpass Mono typeface

%description -n redhat-overpass-mono-fonts
%{desc}

This package contains the monospace variants in OpenType format.

%prep
%autosetup -n Overpass-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .
chmod 0644 overpass*-specimen.pdf README.md

%build

%install
install -dm0755 %{buildroot}%{_ttfontsdir}
mv desktop-fonts/*/*.otf "%{buildroot}/%{_ttfontsdir}/"

%reconfigure_fonts_scriptlets
%reconfigure_fonts_scriptlets -n redhat-overpass-mono-fonts

%files
%doc README.md {AUTHORS,CONTRIBUTORS}.txt overpass-specimen.pdf
%license OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/overpass-[^m]*.otf

%files -n redhat-overpass-mono-fonts
%doc README.md {AUTHORS,CONTRIBUTORS}.txt overpass-mono-specimen.pdf
%license OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/overpass-mono-*.otf

%changelog
