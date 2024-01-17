#
# spec file for package bitstream-vera-fonts
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


%define fontname     bitstream-vera
Name:           bitstream-vera-fonts
Version:        1.10
Release:        0
Summary:        Bitstream Vera(tm) Truetype fonts
License:        Bitstream-Vera
Group:          System/X11/Fonts
URL:            https://www.gnome.org/fonts/
Source:         https://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/%{version}/ttf-%{fontname}-%{version}.tar.bz2
BuildRequires:  fontpackages-devel
# FIXME: This causes a rpmlint warning; change <= to < once there's a new upstream version
Obsoletes:      %{fontname} <= 1.10
Provides:       %{fontname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The package contains the "Vera" truetype fonts from Bitstream Inc.

%prep
%setup -q -n ttf-%{fontname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,755)
%doc COPYRIGHT.TXT RELEASENOTES.TXT README.TXT local.conf
%{_ttfontsdir}

%changelog
