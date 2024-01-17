#
# spec file for package python-napalm-asa
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


%define skip_python2 1
Name:           python-napalm-asa
%define base_version 0.1.1
Version:        20180525.8c54a85
Release:        0
Summary:        NAPALM - Cisco ASA Driver network driver
License:        Apache-2.0
URL:            https://github.com/napalm-automation-community/napalm-asa
# Source:         https://github.com/napalm-automation-community/napalm-asa/archive/v%%{version}.tar.gz#/napalm-asa-%%{version}.tar.gz
Source:         napalm-asa-%{version}.tar.xz
# PATCH-FIX-UPSTREAM napalm-py23_compat.patch gh#napalm-automation-community/napalm-asa#35 mcepl@suse.com
# Make tests pass even when we removed napalm.base.utils.py23_compat
Patch0:         py23_compat.patch
# PATCH-FIX-UPSTREAM pylama.patch gh#napalm-automation-community/napalm-asa#36 mcepl@suse.com
# Fix problems discovered by pylama
Patch1:         pylama.patch
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-napalm >= 2.5.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 4.0.0}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Cisco ASA Driver implementation for the NAPALM Network Automation Project.
This driver makes use of the Cisco ASA REST API. The REST API is only
available from software version 9.3.2 and up, and on the 5500-X series,
ASAv, ASA on Firepower and ISA 3000 platforms.

%prep
%autosetup -p1 -n napalm-asa-%{version}

sed -i -E '/--cov/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#napalm-automation-community/napalm-asa#34
skip_tests="test_get_facts or test_get_interfaces "
skip_tests+=" or test_method_signatures or test_traceroute"
skip_tests+=" or test_get_config_filtered or test_get_config_sanitized"
%pytest -k "not (${skip_tests})"

%files %{python_files}
%license LICENSE
%doc README.md CONTRIBUTING AUTHORS
%{python_sitelib}/napalm_asa
%{python_sitelib}/napalm_asa-%{base_version}*-info

%changelog
