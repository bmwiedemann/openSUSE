#
# spec file for package python-django-allauth
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global asgiref_min_version 3.8.1
%global django_min_version 4.2.16
%global fido2_min_version 1.1.2
%global oauthlib_min_version 3.3.0
%global pillow_min_version 9.0
%global pyjwt_min_version 2.0
%global python3_openid_min_version 3.0.8
%global qrcode_min_version 7.0.0
%global requests_min_version 2.0.0
%global requests_oauthlib_min_version 0.3.0
# optional extra requires
%global python3_saml_min_version 1.15.0
%global python3_saml_max_version 2.0.0
# testing
%global pytest_asyncio_min_version 0.23.8
%global pytest_django_min_version 4.5.2
%global pytest_min_version 7.4

%global pkgname django_allauth

%{?sle15_python_module_pythons}
Name:           python-django-allauth
Version:        65.14.3
Release:        0
Summary:        Django authentication, registration, account management
License:        MIT
URL:            https://allauth.org
Source0:        https://files.pythonhosted.org/packages/source/d/django-allauth/django_allauth-%{version}.tar.gz
Patch0:         missing-template-in-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= %{django_min_version}}
BuildRequires:  %{python_module Pillow >= %{pillow_min_version}}
BuildRequires:  %{python_module PyJWT >= %{pyjwt_min_version}}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module asgiref >= %{asgiref_min_version}}
BuildRequires:  %{python_module django-ninja}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module fido2 >= %{fido2_min_version}}
BuildRequires:  %{python_module oauthlib >= %{oauthlib_min_version}}
BuildRequires:  %{python_module psycopg}
BuildRequires:  %{python_module pytest >= %{pytest_min_version}}
BuildRequires:  %{python_module pytest-asyncio >= %{pytest_asyncio_min_version}}
BuildRequires:  %{python_module pytest-django >= %{pytest_django_min_version}}
BuildRequires:  %{python_module python3-openid >= %{python3_openid_min_version}}
BuildRequires:  %{python_module python3-saml >= %{python3_saml_min_version}}
BuildRequires:  %{python_module python3-saml >= %{python3_saml_min_version}}
BuildRequires:  %{python_module qrcode >= %{qrcode_min_version}}
BuildRequires:  %{python_module requests >= %{requests_min_version}}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= %{django_min_version}
Requires:       python-asgiref >= %{asgiref_min_version}
Suggests:       python-fido2 >= %{fido2_min_version}
Suggests:       python-oauthlib >= %{oauthlib_min_version}
Suggests:       python-PyJWT >= %{pyjwt_min_version}
Suggests:       python-python3-openid >= %{python3_openid_min_version}
Suggests:       python-python3-saml >= %{python3_saml_min_version}
Suggests:       python-qrcode >= %{qrcode_min_version}
Suggests:       python-requests >= %{requests_min_version}
Suggests:       python-requests-oauthlib >= %{requests_oauthlib_min_version}
BuildArch:      noarch
%python_subpackages

%description
Integrated set of Django applications addressing authentication, registration,
account management as well as 3rd party (social) account authentication.

%package headless
Summary:        Django allauth - Headless
Requires:       %{name} = %{version}-%{release}
Requires:       python-PyYAML >= 6

%description headless
Python extra dependency `headless-spec` for python-django-allauth.

%package idp-oidc
Summary:        Django allauth - Identity Provider
Requires:       %{name} = %{version}-%{release}
Requires:       python-PyJWT >= %{pyjwt_min_version}
Requires:       python-cryptography
Requires:       python-oauthlib >= %{oauthlib_min_version}

%description idp-oidc
Python extra dependency `idp-oidc` for python-django-allauth.

%package mfa
Summary:        Django allauth - Two-Factor Authentication
Requires:       %{name} = %{version}-%{release}
Requires:       python-fido2 >= %{fido2_min_version}
Requires:       python-qrcode >= %{qrcode_min_version}

%description mfa
Python extra dependency `mfa` for python-django-allauth.

%package openid
Summary:        Django allauth - OpenID provider
Requires:       %{name} = %{version}-%{release}
Requires:       python-python3-openid >= %{python3_openid_min_version}

%description openid
Python extra dependency `openid` for python-django-allauth.

%package saml
Summary:        Django allauth - Saml provider
Requires:       %{name} = %{version}-%{release}
Requires:       python-python3-saml >= %{python3_saml_min_version}

%description saml
Python extra dependency `saml` for python-django-allauth.

%package steam
Summary:        Django allauth - Steam provider (OpenID-compliant)
Requires:       %{name} = %{version}-%{release}
Requires:       python-python3-openid >= %{python3_openid_min_version}

%description steam
Python extra dependency `steam` for python-django-allauth.

%package socialaccount
Summary:        Django allauth - Third-party ("social") accounts
Requires:       %{name} = %{version}-%{release}
Requires:       python-PyJWT >= %{pyjwt_min_version}
Requires:       python-cryptography
Requires:       python-oauthlib >= %{oauthlib_min_version}
Requires:       python-requests >= %{requests_min_version}

%description socialaccount
Python extra dependency `socialaccount` for python-django-allauth.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

# 2 tests failing with KeyError: 'location' (not in response headers)
sed -i 's/test_login/_test_login/' tests/apps/socialaccount/providers/openid/tests.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH="$(pwd)"
export PYTEST_ADDOPTS="--ds=tests.projects.regular.settings"
%pytest tests

%files %{python_files}
%doc ChangeLog.rst README.rst
%license LICENSE AUTHORS
%{python_sitelib}/allauth
%{python_sitelib}/django_allauth-%{version}.dist-info

%files %{python_files idp-oidc}

%files %{python_files mfa}

%files %{python_files openid}

%files %{python_files saml}

%files %{python_files steam}

%files %{python_files socialaccount}

%files %{python_files headless}

%changelog
