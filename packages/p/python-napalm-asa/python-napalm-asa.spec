#
# spec file for package python-napalm-asa
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
# skip py2 as napalm dropped py2
%define skip_python2 1
Name:           python-napalm-asa
Version:        0.1.1
Release:        0
Summary:        NAPALM - Cisco ASA Driver network driver
License:        Apache-2.0
URL:            https://github.com/napalm-automation-community/napalm-asa
Source:         https://github.com/napalm-automation-community/napalm-asa/archive/v0.1.1.tar.gz#/napalm-asa-%{version}.tar.gz
Patch0:         napalm3.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-napalm >= 2.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 2.0.0}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Cisco ASA Driver implementation for the NAPALM Network Automation Project.
This driver makes use of the Cisco ASA REST API. The REST API is only
available from software version 9.3.2 and up, and on the 5500-X series,
ASAv, ASA on Firepower and ISA 3000 platforms.

%prep
%setup -q -n napalm-asa-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Although the napalm3.patch fixes the methods signatures in test_method_signatures (to preserve compatibility), 
# there is no support for get_config(sanitized=True)
# test_get_interfaces has obsolete model
%pytest -k "not (test_get_config_sanitized or (test_get_interfaces and not test_get_interfaces_))"

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%{python_sitelib}/*

%changelog
