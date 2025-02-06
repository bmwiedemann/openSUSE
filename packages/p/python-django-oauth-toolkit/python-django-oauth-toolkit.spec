#
# spec file for package python-django-oauth-toolkit
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-django-oauth-toolkit
Version:        1.7.0
Release:        0
Summary:        OAuth2 Provider for Django
License:        BSD-2-Clause
URL:            https://github.com/jazzband/django-oauth-toolkit
Source:         https://github.com/jazzband/django-oauth-toolkit/archive/%{version}.tar.gz#/django-oauth-toolkit-%{version}.tar.gz
Patch0:         stop-using-pk-to-reference-tokens.patch
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  %{python_module jwcrypto >= 0.8.0}
BuildRequires:  %{python_module oauthlib >= 3.1.0}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module requests >= 2.13.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-jwcrypto >= 0.8.0
Requires:       python-oauthlib >= 3.1.0
Requires:       python-requests >= 2.13.0
Conflicts:      python-django-oauth
BuildArch:      noarch
%python_subpackages

%description
If you are facing one or more of the following:
* Your Django app exposes a web API you want to protect with OAuth2 authentication,
* You need to implement an OAuth2 authorization server to provide tokens management for your infrastructure,

Django OAuth Toolkit can help you providing out of the box all the endpoints, data and logic needed to add OAuth2 capabilities to your Django projects. Django OAuth Toolkit makes extensive use of the excellent OAuthLib, so that everything is rfc-compliant.

%prep
%autosetup -p1 -n django-oauth-toolkit-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=$(pwd)
%pytest -k 'not (test_response_when_auth_server_response_return_404 or test_clear_expired_tokens_with_tokens)'

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGELOG.md docs/*.rst docs/rest-framework/ docs/tutorial/ docs/views/
%{python_sitelib}/*

%changelog
