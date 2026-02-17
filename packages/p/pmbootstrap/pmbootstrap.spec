#
# spec file for package pmbootstrap
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Jianhua Lu <lujianhua000@gmail.com>
# Copyright (c) 2024 Zhang Bingwu <xtexchooser@duck.com>
# Copyright (c) 2023, Tomáš Čech <sleep_walker@opensuse.org>
# Copyright (c) 2021-2025, Martin Hauke <mardnh@gmx.de>
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


%define         pythons %{primary_python}
%define         commit 888d8b4a2733af411e81d3c36b2a5945ed1e3467
Name:           pmbootstrap
Version:        3.9.0
Release:        0
Summary:        Sophisticated chroot/build/flash tool to develop and install postmarketOS
License:        GPL-3.0-or-later
URL:            https://postmarketos.org
Source0:        https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module gnureadline}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  kpartx
BuildRequires:  openssl
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
Sophisticated chroot/build/flash tool to develop and install postmarketOS

%prep
%autosetup -n %{name}-%{version}-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install
export SOURCE_DATE_EPOCH=$(date +%s)
python3 -m compileall -q -f %{buildroot}%{python3_sitelib}/pmb
python3 -O -m compileall -q -f %{buildroot}%{python3_sitelib}/pmb

%fdupes -s %{buildroot}%{python3_sitelib}

%check
# fails on non x86_64 https://gitlab.postmarketos.org/postmarketOS/pmbootstrap/-/issues/2500
# using shell test because package is noarch
arch="$(uname -m)"
if [ "$arch" = 'x86_64' ]
then
  %pytest -k "not test_pkgrepo_pmaports and not test_random_valid_deviceinfos"
else
  echo "Skipping tests due to architecture $arch."
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/pmbootstrap
%{python_sitelib}/%{name}-%{version}.dist-info
%{python_sitelib}/pmb
%exclude %{python3_sitelib}/pmb/**/__pycache__/*

%changelog
