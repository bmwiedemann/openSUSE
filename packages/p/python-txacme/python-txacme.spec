#
# spec file for package python-txacme
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
Name:           python-txacme
Version:        0.9.2
Release:        0
Summary:        Twisted implementation of the ACME protocol
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/twisted/txacme
Source0:        https://github.com/twisted/txacme/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Twisted >= 15.5.0}
BuildRequires:  %{python_module TxSNI}
BuildRequires:  %{python_module acme >= 0.21.0}
# extra
BuildRequires:  %{python_module apache-libcloud}
BuildRequires:  %{python_module attrs >= 17.4.0}
# cryptography is list in docs/conf.py
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module eliot >= 0.8.0}
# test
BuildRequires:  %{python_module fixtures >= 1.4.0}
BuildRequires:  %{python_module hypothesis < 4.0.0}
BuildRequires:  %{python_module hypothesis >= 3.20.0}
BuildRequires:  %{python_module josepy}
BuildRequires:  %{python_module pem >= 16.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module service_identity >= 17.0.0}
BuildRequires:  %{python_module testrepository >= 0.0.20}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools >= 2.1.0}
BuildRequires:  %{python_module treq >= 15.1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 15.5.0
Requires:       python-TxSNI
Requires:       python-acme >= 0.21.0
Requires:       python-apache-libcloud
Requires:       python-attrs >= 17.4.0
Requires:       python-cryptography
Requires:       python-eliot >= 0.8.0
Requires:       python-josepy
Requires:       python-pem >= 16.1.0
Requires:       python-pyOpenSSL >= 17.1.0
Requires:       python-treq >= 15.1.0
BuildArch:      noarch
%python_subpackages

%description
ACME is Automatic Certificate Management Environment, a protocol that allows clients and certificate authorities
to automate verification and certificate issuance.
The ACME protocol is used by the free Let's Encrypt Certificate Authority.

txacme is an implementation of the protocol for Twisted, the event-driven networking engine for Python.

%prep
%setup -q -n txacme-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# matchers - require testtools which are ATM broken, revisit in future
# client, util - randomly fails
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v src/txacme/test -k 'not (matchers or util or client)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
