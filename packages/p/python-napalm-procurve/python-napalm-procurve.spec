#
# spec file for package python-napalm-procurve
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
# python-napalm is python3 only
%define skip_python2 1
Name:           python-napalm-procurve
Version:        0.5.0
Release:        0
Summary:        NAPALM - HP ProCurve network driver
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ixs/napalm-procurve
Source:         https://github.com/ixs/napalm-procurve/archive/%{version}.tar.gz#/napalm-procurve-%{version}.tar.gz
Patch0:         napalm3.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 2.4.0}
BuildRequires:  %{python_module netmiko}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-napalm >= 2.4.0
Requires:       python-netmiko
BuildArch:      noarch
%python_subpackages

%description
ProCurve driver support for Napalm network automation.

%prep
%setup -q -n napalm-procurve-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Although the napalm3.patch fixes the methods signatures in test_method_signatures (to preserve compatibility), 
# there is no support for get_config(sanitized=True)
%pytest -k "not test_get_config_sanitized"

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%{python_sitelib}/*

%changelog
