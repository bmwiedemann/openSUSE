#
# spec file for package python-kasa
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-kasa
Version:        0.0~git1580219900.15b0c8c
Release:        0
Summary:        Python API for TP-Link Kasa Smarthome products
License:        GPL-3.0-or-later
URL:            https://github.com/python-kasa/python-kasa
Source0:        python-kasa-%{version}.tar.xz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module voluptuous}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Runtime requires
Requires:       python-click >= 7.0
Requires:       python-pytest-asyncio
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This package contains the python module for interfacing with TP-Link smart devices: Plugs, Power Strips, Wall switches and bulbs.
Use 'kasa' binary.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/kasa
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/python-kasa/python-kasa/issues/27
#%%pytest

%post
%python_install_alternative kasa

%postun
%python_uninstall_alternative kasa

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/kasa
%dir %{python_sitelib}/kasa
%{python_sitelib}/kasa/*
%{python_sitelib}/*.egg-info*

%changelog
