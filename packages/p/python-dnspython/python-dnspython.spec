#
# spec file for package python-dnspython
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
Name:           python-dnspython
Version:        1.16.0
Release:        0
Summary:        A DNS toolkit for Python
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/rthalley/dnspython
Source:         http://dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
Source2:        http://dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz.asc
Source3:        python-dnspython.keyring
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
Requires:       python-ecdsa
Requires:       python-pycryptodome
BuildArch:      noarch
Recommends:     python-idna

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and
dynamic updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

dnspython originated at Nominum where it was developed to
facilitate the testing of DNS software. Nominum has generously
allowed it to be opened under a BSD-style licence.

%python_subpackages

%prep
%setup -q -n dnspython-%{version}
chmod -x examples/*

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
# Skip the resolver test suite as it requires Internet connection.
#test -f tests/test_resolver.py && rm tests/test_resolver.py
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md examples/
%{python_sitelib}/dns/
%{python_sitelib}/dnspython-%{version}-py%{python_version}.egg-info

%changelog
