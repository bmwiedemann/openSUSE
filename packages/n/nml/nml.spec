#
# spec file for package nml
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        0.8.1
Release:        0
Summary:        NewGRF Meta Language
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            http://dev.openttdcoop.org/projects/nml
Source:         https://github.com/OpenTTD/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
# We need the required packages also on building for regression tests:
BuildRequires:  python3-Pillow >= 3.4
BuildRequires:  python3-ply
Requires:       python3-Pillow >= 3.4
Requires:       python3-ply
Provides:       nmlc = %{version}

%description
A tool to compile nml files to grf or nfo files, making newgrf coding easier.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%python3_pyproject_wheel

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python3_sitearch}
make -C regression

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitearch}
%fdupes %{buildroot}%{python3_sitelib}

install -D -m0644 docs/nmlc.1 %{buildroot}%{_mandir}/man1/nmlc.1

#setuptools should not be a requirement on running, so we install the nmlc wrapper from source
install -m0755 nmlc %{buildroot}%{_bindir}/nmlc
# Fix script interpreter
sed -i 's@^#!\s*/usr/bin/env python3@#!/usr/bin/python3@' %{buildroot}%{_bindir}/nmlc

# The actual python code is not being installed?!?
mkdir -p %{buildroot}%{python3_sitelib}/nml
cp -rp nml/* %{buildroot}%{python3_sitelib}/nml/
# Remove devel file
rm %{buildroot}%{python3_sitelib}/nml/_lz77.c

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_bindir}/nmlc
%{_mandir}/man1/nmlc.1*
%{python3_sitelib}/%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/nml_lz77.cpython-*-linux-gnu.so
%{python3_sitearch}/%{name}-%{version}.dist-info

%changelog
