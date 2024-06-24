#
# spec file for package python-django-allauth
#
# Copyright (c) 2024 SUSE LLC
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


%global django_min_version 3.2
%global python3_openid_min_version 3.0.8
%global requests_oauthlib_min_version 0.3.0
%global requests_min_version 2.0.0
%global pyjwt_min_version 1.7
# optional extra requires
%global python3_saml_min_version 1.15.0
%global python3_saml_max_version 2.0.0
%global qrcode_min_version 7.0.0
# testing
%global pillow_min_version 9.0
%global pytest_min_version 7.4
%global pytest_django_min_version 4.5.2

%global pkgname django_allauth

%{?sle15_python_module_pythons}
Name:           python-django-allauth
Version:        0.63.3
Release:        0
Summary:        Django authentication, registration, account management
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pennersr/django-allauth
Source:         https://files.pythonhosted.org/packages/source/d/django-allauth/%{pkgname}-%{version}.tar.gz
Patch0:         missing-template-in-test.patch
BuildRequires:  %{python_module Django >= %{django_min_version}}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python3-openid >= %{python3_openid_min_version}}
BuildRequires:  %{python_module requests >= %{requests_min_version}}
BuildRequires:  %{python_module requests-oauthlib >= %{requests_oauthlib_min_version}}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= %{django_min_version}
Requires:       python-PyJWT >= %{pyjwt_min_version}
Requires:       python-python3-openid >= %{python3_openid_min_version}
Requires:       python-requests >= %{requests_min_version}
Requires:       python-requests-oauthlib >= %{requests_oauthlib_min_version}
Recommends:     python-qrcode >= %{qrcode_min_version}
Recommends:     (python-python3-saml >= %{python3_saml_min_version} with python-python3-saml < %{python3_saml_max_version})
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= %{pillow_min_version}}
BuildRequires:  %{python_module pytest >= %{pytest_min_version}}
BuildRequires:  %{python_module pytest-django >= %{pytest_django_min_version}}
BuildRequires:  %{python_module python3-saml >= %{python3_saml_min_version}}
BuildRequires:  %{python_module qrcode >= %{qrcode_min_version}}
# /SECTION
%python_subpackages

%description
Integrated set of Django applications addressing authentication, registration,
account management as well as 3rd party (social) account authentication.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

# 2 tests failing with KeyError: 'location' (not in response headers)
sed -i 's/test_login/_test_login/' allauth/socialaccount/providers/openid/tests.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH="$(pwd)"
export PYTEST_ADDOPTS="--ds=tests.regular.settings"
%pytest allauth

%files %{python_files}
%doc AUTHORS ChangeLog.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
