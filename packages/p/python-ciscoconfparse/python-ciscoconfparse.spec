#
# spec file for package python-ciscoconfparse
#
# Copyright (c) 2022 SUSE LLC
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
%bcond_without python2
Name:           python-ciscoconfparse
Version:        1.6.52
Release:        0
Summary:        Library for parsing, querying and modifying Cisco IOS-style configurations
License:        GPL-3.0-or-later
URL:            https://github.com/mpenning/ciscoconfparse
Source:         https://files.pythonhosted.org/packages/source/c/ciscoconfparse/ciscoconfparse-%{version}.tar.gz
BuildRequires:  %{python_module dnspython >= 2.1.0}
BuildRequires:  %{python_module loguru >= 0.6.0}
BuildRequires:  %{python_module passlib >= 1.7.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml >= 0.10.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-ipaddr >= 2.1.11
BuildRequires:  python2-mock
%endif
Requires:       python-dnspython >= 2.1.0
Requires:       python-loguru >= 0.6.0
Requires:       python-toml >= 0.10.2
%ifpython2
Requires:       python-ipaddr >= 2.1.11
%endif
BuildArch:      noarch
%python_subpackages

%description
ciscoconfparse is a Python library, which parses through Cisco IOS-style
(and other vendor) configurations.  It can:

- Audit existing router / switch / firewall / wlc configurations
- Retrieve portions of the configuration
- Modify existing configurations
- Build new configurations

The library examines an IOS-style config and breaks it into a set of linked
parent / child relationships.  You can perform complex queries about these
relationships.

%prep
%autosetup -p1 -n ciscoconfparse-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no online dns (and /etc/resolv.conf) available
#%%pytest -k "not (test_dns_lookup or test_reverse_dns_lookup)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ciscoconfparse
%{python_sitelib}/ciscoconfparse-%{version}-py%{python_version}.egg-info

%changelog
