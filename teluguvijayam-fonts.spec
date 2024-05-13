#
# spec file for package teluguvijayam-fonts
#
# Copyright (c) 2020 SUSE LINUX Products GmbH, Nuernberg, Germany.
# 
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owner, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/

# Definitions
%define fontname teluguvijayam

Name:		teluguvijayam-fonts
Summary:	TrueType fonts for Telugu script (te)
License:	OFL-1.1
Group:		System/X11/Fonts
BuildArch:	noarch
Version:	0.1
Release:	1
Source0:		%{fontname}-%{version}.tar.xz
Source1:		create-archive.sh
BuildRequires:  fontpackages-devel 
BuildRequires:  tar
URL:		https://www.siliconandhra.org/fonts/

%description
This package provides following 20 fonts for Telugu script
which is used in Indian states of Andhra Pradesh & Telangana

  * Ponnala
  * RaviPrakash
  * LakkiReddy
  * Potti Sriramulu
  * Syamala Ramana
  * Gidugu
  * Gurajada
  * Suravaram
  * NTR
  * Mandali
  * NATS
  * SrikrushnaDevaraya
  * Peddana
  * Timmana
  * Tenali Ramakrishna
  * Suranna
  * Ramaraja
  * Mallana
  * Dhurjati
  * Ramabhadra

 These fonts are released by Departement of Information
 technology, Government of Andhra Pradesh.

Designer: Silicon Andhra

%prep
%setup -n %{fontname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}

# call fonts-config after installation or deinstallation of this package
%reconfigure_fonts_scriptlets

%files
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
