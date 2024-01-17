#
# spec file for package python-napalm-arubaos-switch
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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
%define skip_python36 1
Name:           python-napalm-arubaos-switch
Version:        0.2.0
Release:        0
License:        MIT
Summary:        NAPALM - ArubaOS network driver
URL:            https://github.com/napalm-automation-community/napalm-arubaos-switch/
Group:          Development/Languages/Python
Source:         https://github.com/napalm-automation-community/napalm-arubaos-switch/archive/%{version}.tar.gz#/napalm-arubaos-switch-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh/napalm-automation-community/napalm-arubaos-switch/commit/ebd48e46 the driver needs to return the speed as float instead of an integer
Patch0:         float-speed.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 3.3.0}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module netutils}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-json-report}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module textfsm >= 1.1.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-napalm >= 3.3.0
Requires:       python-netaddr
Requires:       python-requests
Requires:       python-requests-toolbelt
Requires:       python-textfsm >= 1.1.0
BuildArch:      noarch
%python_subpackages

%description
ArubaOS driver support for NAPLAM network automation.
This Drivers uses the REST interface.

%prep
%setup -q -n napalm-arubaos-switch-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
# Remove test from sitelib
%python_expand rm -R %{buildroot}%{$python_sitelib}/test/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
skip_tests="test_traceroute"
# gh#napalm-automation-community/napalm-arubaos-switch#20
skip_tests+=" or test_method_signatures or test_get_facts"
%pytest -k "not (${skip_tests})"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/napalm_arubaos_switch*
%{python_sitelib}/napalm_arubaoss

%changelog
