#
# spec file for package python-ciscoconfparse
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-ciscoconfparse
Version:        1.4.10
Release:        0
Summary:        Library for parsing, querying and modifying Cisco IOS-style configurations
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/mpenning/ciscoconfparse
Source:         https://files.pythonhosted.org/packages/source/c/ciscoconfparse/ciscoconfparse-%{version}.tar.gz
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module ipaddr}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-ipaddress
BuildRequires:  python2-mock
Requires:       python-colorama
Requires:       python-dnspython
Requires:       python-ipaddr
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
%setup -q -n ciscoconfparse-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/ciscoconfparse
%{python_sitelib}/ciscoconfparse-%{version}-py%{python_version}.egg-info

%changelog
