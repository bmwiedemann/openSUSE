#
# spec file for package python-napalm-procurve
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-napalm-procurve
Version:        0.4.0
Release:        0
License:        Apache-2.0
Summary:        NAPALM - HP ProCurve network driver
Url:            https://github.com/ixs/napalm-procurve
Group:          Development/Languages/Python
Source:         https://github.com/ixs/napalm-procurve/archive/%{version}.tar.gz#/napalm-procurve-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 2.4.0}
BuildRequires:  %{python_module netmiko}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pylama}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%{python_sitelib}/*

%changelog
