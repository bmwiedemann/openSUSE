#
# spec file for package python-social-auth-core
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
%define modname social-core
Name:           python-social-auth-core
Version:        3.4.0
Release:        0
Summary:        Python Social Auth Core
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://github.com/python-social-auth/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# Missing test data https://github.com/python-social-auth/social-core/pull/351
Source1:        https://raw.githubusercontent.com/python-social-auth/social-core/master/social_core/tests/backends/data/saml_config.json
Patch0:         remove-unittest2.patch
# PATCH-FEATURE-UPSTREAM resolve_depreciations.patch gh#python-social-auth/social-core#500 mcepl@suse.com
# Remove deprecation warnings
Patch1:         resolve_depreciations.patch
BuildRequires:  %{python_module PyJWT >= 1.4.0}
BuildRequires:  %{python_module Unidecode >= 1.1.1}
BuildRequires:  %{python_module coverage >= 3.6}
BuildRequires:  %{python_module cryptography >= 2.1.1}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oauthlib >= 1.0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jose >= 3.0.0}
BuildRequires:  %{python_module python3-saml}
BuildRequires:  %{python_module rednose >= 0.4.1}
BuildRequires:  %{python_module requests >= 2.9.1}
BuildRequires:  %{python_module requests-oauthlib >= 0.6.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-python-openid >= 2.2.5
%endif
BuildRequires:  python3-defusedxml >= 0.5.0
BuildRequires:  python3-python3-openid >= 3.0.10
Requires:       python-PyJWT >= 1.4.0
Requires:       python-Unidecode >= 1.1.1
Requires:       python-cryptography >= 2.1.1
Requires:       python-oauthlib >= 1.0.3
Requires:       python-python-jose >= 3.0.0
Requires:       python-requests >= 2.9.1
Requires:       python-requests-oauthlib >= 0.6.1
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%ifpython2
Requires:       python2-python-openid >= 2.2.5
%endif
%ifpython3
Requires:       python3-defusedxml >= 0.5.0
Requires:       python3-python3-openid >= 3.0.10
Recommends:     python-python3-saml
%endif
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

cp %{SOURCE1} social_core/tests/backends/data/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# python3 only: assertRaisesRegexp -> assertRaisesRegex
# skipped tests are online based
rm -rf _build.python2
python3 -m pytest -v -k 'not (test_login or test_partial_pipeline)'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
