#
# spec file for package fifth-leg-font
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fifth-leg-font
Version:        0.6
Release:        0
%define pkgname   opensuse-font-fifth-leg
Summary:        Font for the openSUSE Brand
License:        OFL-1.1
Group:          System/X11/Fonts
Source:         %{pkgname}-%{version}.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Fifth Leg font is the font used for openSUSE branded material.

%prep
%setup -q -c

%build
#bnc#840414
sed -i 's:musichal\.cz:musichall\.cz:' COPYING

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}/
dos2unix COPYING

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%changelog
