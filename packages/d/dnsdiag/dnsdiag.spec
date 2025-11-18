#
# spec file for package dnsdiag
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


%define pythons python3
%bcond_with test
Name:           dnsdiag
Version:        2.9.1
Release:        0
Summary:        DNS request auditing toolset
License:        BSD-3-Clause
Group:          Development/Languages/Python
#Git-Clone:     https://github.com/farrokhi/dnsdiag.git
URL:            https://dnsdiag.org/
Source:         https://github.com/farrokhi/dnsdiag/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        dnseval.1
Source2:        dnsping.1
Source3:        dnstraceroute.1
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-aioquic >= 1.2.0
Requires:       python3-cryptography >= 42.0.5
Requires:       python3-cymruwhois >= 1.6
Requires:       python3-dnspython >= 2.8.0
Requires:       python3-h2 >= 4.1.0
Requires:       python3-httpx >= 0.27.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  python3-cymruwhois >= 1.6
BuildRequires:  python3-dnspython >= 2.6.1
BuildRequires:  python3-pytest
%endif

%description
A set of tools to perform basic audits on DNS requests and responses
to make sure DNS is working as expected. Dnsping can be used to
measure the response time of a given DNS server for arbitrary
requests. Just like a traditional ping utility, it provides similar
functionality for DNS requests.

Dnstraceroute can be used to trace the path a DNS request takes to
its destination. Its purpose is to detect whether a request is
redirected or hijacked. This can be done by comparing different DNS
queries being sent to the same DNS server using dnstraceroute and
observe if there is any difference between the path.

dnseval evaluates multiple DNS resolvers and helps choosing the best
DNS server for the network. It is recommended to use one's own DNS
resolver as opposed to a third-party DNS server. dnseval can compare
different DNS servers from a performance (latency) and reliability
(loss) point of view for when DNS forwarders need to be used instead
of a resolver.

%prep
%autosetup -n dnsdiag-%{version}
sed -e '/^#!\//, 1d' -i *.py dnsdiag/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -d -m0755 %{buildroot}%{_mandir}/man1/
install -m0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} -t %{buildroot}%{_mandir}/man1/

%check
%if %{with test}
%pytest
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/dnseval
%{_bindir}/dnstraceroute
%{_bindir}/dnsping
%{_mandir}/man1/dnseval.1%{?ext_man}
%{_mandir}/man1/dnstraceroute.1%{?ext_man}
%{_mandir}/man1/dnsping.1%{?ext_man}
%{python_sitelib}/dnseval.py
%{python_sitelib}/dnsping.py
%{python_sitelib}/dnstraceroute.py
%{python_sitelib}/dnsdiag
%{python_sitelib}/dnsdiag-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
