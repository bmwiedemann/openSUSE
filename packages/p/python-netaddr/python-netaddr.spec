#
# spec file for package python-netaddr
#
# Copyright (c) 2020 SUSE LLC
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
#%%bcond_without test
Name:           python-netaddr
Version:        0.7.19
Release:        0
Summary:        Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/drkjam/netaddr
Source:         https://files.pythonhosted.org/packages/source/n/netaddr/netaddr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%setup -q -n netaddr-%{version}
sed -i "1d" netaddr/{ip/iana,eui/ieee,tests/__init__}.py # Fix non-executable scripts

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/netaddr
%fdupes %{buildroot}

%if %{with test}
%check
%python_exec setup.py test
%endif

%post
%python_install_alternative netaddr

%postun
%python_uninstall_alternative netaddr

%files %{python_files}
%{python_sitelib}/*
%{_bindir}/netaddr-%{python_bin_suffix}
%python_alternative %{_bindir}/netaddr
%license LICENSE
%doc AUTHORS CHANGELOG COPYRIGHT README.md

%changelog
