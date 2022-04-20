#
# spec file for package python-social-auth-core
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017-2018 Matthias Fehring <buschmann23@opensuse.org>
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
%define modname social-core
Name:           python-social-auth-core
Version:        4.2.0
Release:        0
Summary:        Python Social Auth Core
License:        BSD-3-Clause
URL:            https://github.com/python-social-auth/social-core
Source:         https://github.com/python-social-auth/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module PyJWT >= 2.0.0}
BuildRequires:  %{python_module coverage >= 3.6}
BuildRequires:  %{python_module cryptography >= 2.1.1}
BuildRequires:  %{python_module defusedxml >= 0.5.0}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module oauthlib >= 1.0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jose >= 3.0.0}
BuildRequires:  %{python_module python3-openid >= 3.0.10}
BuildRequires:  %{python_module python3-saml >= 1.2.1}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module requests-oauthlib >= 0.6.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 2.0.0
Requires:       python-cryptography >= 2.1.1
Requires:       python-oauthlib >= 1.0.3
Requires:       python-python-jose >= 3.0.0
Requires:       python-requests >= 2.9.1
Requires:       python-requests-oauthlib >= 0.6.1
BuildArch:      noarch
Requires:       python-defusedxml >= 0.5.0
Requires:       python-python3-openid >= 3.0.10
Recommends:     python-python3-saml >= 1.2.1
%python_subpackages

%description
Python Social Auth is a social authentication/registration
mechanism with support for several frameworks and auth providers.

This is the core component of the python-social-auth ecosystem. It
implements the common interface to define new authentication backends to
third party services, implement integrations with web frameworks and
storage solutions.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# python3 only: assertRaisesRegexp -> assertRaisesRegex
# skipped tests are online based
rm -rf _build.python2
%pytest -k 'not (test_login or test_partial_pipeline)'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
