#
# spec file for package python-oauthlib
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
Name:           python-oauthlib
Version:        3.1.0
Release:        0
Summary:        A Generic Implementation of the OAuth Request-Signing Logic
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/oauthlib/oauthlib
Source:         https://files.pythonhosted.org/packages/source/o/oauthlib/oauthlib-%{version}.tar.gz
Patch:          o_switch_to_unitest_mock.patch
BuildRequires:  %{python_module PyJWT >= 1.0.0}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 1.0.0
Requires:       python-blinker
Requires:       python-cryptography
BuildArch:      noarch
%python_subpackages

%description
A generic, spec-compliant, thorough implementation of the OAuth request-signing
logic.

OAuth often seems complicated and difficult-to-implement. There are several
prominent libraries for signing OAuth requests, but they all suffer from one or
both of the following:

1. They predate the OAuth 1.0 spec, AKA RFC 5849.
2. They predate the OAuth 2.0 spec, AKA RFC 6749.
3. They assume the usage of a specific HTTP request library.

OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object. Use it to graft OAuth support onto your
favorite HTTP library. If you're a maintainer of such a library, write a thin
veneer on top of OAuthLib and get OAuth support for very little effort.

%prep
%setup -q -n oauthlib-%{version}
%patch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%dir %{python_sitelib}/oauthlib
%{python_sitelib}/oauthlib/*
%dir %{python_sitelib}/oauthlib-%{version}-py*.egg-info
%{python_sitelib}/oauthlib-%{version}-py*.egg-info/*

%changelog
