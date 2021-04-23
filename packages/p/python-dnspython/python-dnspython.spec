#
# spec file for package python-dnspython
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-dnspython
Version:        2.1.0
Release:        0
Summary:        A DNS toolkit for Python
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/rthalley/dnspython
Source:         https://files.pythonhosted.org/packages/source/d/dnspython/dnspython-%{version}.zip
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
# SECTION tests
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module trio >= 0.14.0}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# /SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  netcfg
BuildRequires:  unzip
BuildRequires:  (python3-contextvars if python3-base < 3.7)
BuildRequires:  (python36-contextvars if python36-base)
Requires:       python-ecdsa
Requires:       python-pycryptodome
Requires:       python-requests-toolbelt
%if %{python_version_nodots} < 37
Requires:       python-contextvars
%endif
BuildArch:      noarch
Recommends:     python-cryptography
Recommends:     python-idna >= 2.1
Recommends:     python-trio >= 0.14.0
Recommends:     python-sniffio >= 1.1

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and
dynamic updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

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
# exclude the testcase which requires an unpackaged pickle file in the tests. see https://github.com/rthalley/dnspython/issues/622
%pytest -k 'not test_unpickle'

%files %{python_files}
%license LICENSE
%doc README.md examples/
%{python_sitelib}/dns/
%{python_sitelib}/dnspython-%{version}-py%{python_version}.egg-info

%changelog
