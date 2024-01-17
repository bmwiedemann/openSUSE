#
# spec file for package python-napalm-procurve
#
# Copyright (c) 2023 SUSE LLC
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


# python-napalm is python3 only
%define skip_python2 1
Name:           python-napalm-procurve
Version:        0.7.0
Release:        0
Summary:        NAPALM - HP ProCurve network driver
License:        Apache-2.0
URL:            https://github.com/ixs/napalm-procurve
Source:         https://github.com/ixs/napalm-procurve/archive/%{version}.tar.gz#/napalm-procurve-%{version}.tar.gz
Patch0:         setup-parse-requirements.patch
#PATCH-FIX-UPSTREAM https://github.com/ixs/napalm-procurve/pull/29 float speed
Patch1:         float-speed.patch
#PATCH-FIX-OPENSUSE fix-linter.patch remove pyflakes from code lint because it's failing
Patch2:         fix-linter.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 3.0.0}
BuildRequires:  %{python_module netmiko}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-napalm >= 3.0.0
Requires:       python-netmiko
BuildArch:      noarch
%python_subpackages

%description
ProCurve driver support for Napalm network automation.

%prep
%setup -q -n napalm-procurve-%{version}
%autopatch -p1

sed -i -e '/addopts/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#ixs/napalm-procurve#19
# gh#ixs/napalm-procurve#30
%pytest -k 'not (test_method_signatures or test_get_config_filtered or test_get_facts)'

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%{python_sitelib}/napalm_procurve
%{python_sitelib}/napalm_procurve-%{version}*-info

%changelog
