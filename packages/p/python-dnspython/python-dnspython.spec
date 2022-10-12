#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-dnspython%{psuffix}
Version:        2.2.1
Release:        0
Summary:        A DNS toolkit for Python
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/rthalley/dnspython
Source:         https://files.pythonhosted.org/packages/source/d/dnspython/dnspython-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module typing}
# doh:
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module h2}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
# idna
BuildRequires:  %{python_module idna}
# dnssec
BuildRequires:  %{python_module cryptography}
# trio
BuildRequires:  %{python_module trio >= 0.14.0}
# curio
BuildRequires:  %{python_module sniffio >= 1.1}
BuildRequires:  %{python_module curio >= 1.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  netcfg
BuildRequires:  (python3-contextvars if python3-base < 3.7)
%endif
%if 0%{?python_version_nodots} < 37
Requires:       python-contextvars
%endif
# Requires despite optional: see description
# doh
Requires:       python-requests
Requires:       python-httpx
Requires:       python-requests-toolbelt
# idna
Requires:       python-idna >= 2.1
# dnssec
Requires:       python-cryptography
# trio
Suggests:       python-trio >= 0.14.0
# curio
Suggests:       python-sniffio >= 1.1
Suggests:       python-curio >= 1.2
# HTTP/2 support in httpx
Recommends:     python-h2
BuildArch:      noarch

%python_subpackages

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and
dynamic updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

The package requires dependencies necessary for these optional features:
- DNS over HTTPS (doh)
- IDNA
- DNSSEC
and suggest dependencies necessary for these optional features:
- trio
- curio
This optional feature is not available due to missing dependencies:
- wmi

%prep
%setup -q -n dnspython-%{version}
chmod -x examples/*
# https://github.com/rthalley/dnspython/pull/755
chmod -x dns/win32util.py

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md examples/
%{python_sitelib}/dns
%{python_sitelib}/dnspython-%{version}.dist-info
%endif

%changelog
