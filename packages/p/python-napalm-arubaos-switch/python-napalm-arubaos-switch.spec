#
# spec file for package python-napalm-arubaos-switch
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
Name:           python-napalm-arubaos-switch
Version:        0.1.1
Release:        0
License:        MIT
Summary:        NAPALM - ArubaOS network driver
Url:            https://github.com/napalm-automation-community/napalm-arubaos-switch/
Group:          Development/Languages/Python
Source:         https://github.com/napalm-automation-community/napalm-arubaos-switch/archive/v%{version}.tar.gz#/napalm-arubaos-switch-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 2.0.0}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module textfsm >= 1.1.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-napalm >= 2.0.0
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# There are no tests yet

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/napalm_arubaos_switch*
%{python_sitelib}/napalm_arubaoss

%changelog
