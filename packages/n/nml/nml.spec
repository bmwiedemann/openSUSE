#
# spec file for package nml
#
# Copyright (c) 2021 SUSE LLC
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


Name:           nml
Version:        0.5.3
Release:        0
Summary:        NewGRF Meta Language
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            http://dev.openttdcoop.org/projects/nml
Source:         https://github.com/OpenTTD/nml/releases/download/%{version}/%{name}-%{version}.tar.gz
# Backport fixed pcx images for regression tests (gh#OpenTTD/nml!188, deb#980641)
Source1:        https://github.com/OpenTTD/nml/raw/07c5a4de27fec1383d2657aa51a092b1d2c658fe/regression/arctic_railwagons.pcx
Source2:        https://github.com/OpenTTD/nml/raw/07c5a4de27fec1383d2657aa51a092b1d2c658fe/regression/opengfx_generic_trams1.pcx
Source3:        https://github.com/OpenTTD/nml/raw/07c5a4de27fec1383d2657aa51a092b1d2c658fe/regression/opengfx_trains_start.pcx
Source99:       nml-rpmlintrc
BuildRequires:  gcc
BuildRequires:  python3-devel
# We need the required packages also on building for regression tests:
BuildRequires:  python3-Pillow
BuildRequires:  python3-ply
BuildRequires:  python3-setuptools
Requires:       python3-Pillow
Requires:       python3-ply
Requires:       python3-setuptools
Provides:       nmlc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A tool to compile nml files to grf or nfo files, making newgrf coding easier.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} regression

%build
make
make extensions

%install
python3 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

install -D -m0644 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#setuptools should not be a requirement on running, so we install the nmlc wrapper from source
install -m0755 nmlc %{buildroot}%{_bindir}/nmlc

# The actual python code is not being installed?!?
mkdir -p %{buildroot}%{python3_sitelib}/nml
cp -rp nml/* %{buildroot}%{python3_sitelib}/nml/

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1*
%{python3_sitearch}/*
%{python3_sitelib}/%{name}/

%changelog
