#
# spec file for package python-netaddr
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-netaddr
Version:        1.3.0
Release:        0
Summary:        Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/netaddr/netaddr
Source:         https://files.pythonhosted.org/packages/source/n/netaddr/netaddr-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module iniconfig}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pluggy}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with:
    - IPv4 and IPv6 addresses and subnets (including CIDR notation);
    - MAC (Media Access Control) addresses in multiple formats;
    - IEEE EUI-64, OUI and IAB identifiers;
    - a user friendly IP glob-style format.

Included are routines for:
    - generating, sorting and summarizing IP addresses;
    - converting IP addresses and ranges between various different formats;
    - performing set based operations on groups of IP addresses and subnets;
    - arbitrary IP address range calculations and conversions;
    - querying IEEE OUI and IAB organisational information;
    - querying of IP standards related data from key IANA data sources.

%prep
%autosetup -p1 -n netaddr-%{version}
sed -i "1{\@/usr/bin/env python@d}" netaddr/{cli,ip/iana,eui/ieee}.py # Fix non-executable scripts

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/netaddr
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative netaddr

%postun
%python_uninstall_alternative netaddr

%files %{python_files}
%license LICENSE.rst
%doc AUTHORS.rst CHANGELOG.rst COPYRIGHT.rst README.rst
%{python_sitelib}/netaddr*
%{_bindir}/netaddr-%{python_bin_suffix}
%python_alternative %{_bindir}/netaddr

%changelog
