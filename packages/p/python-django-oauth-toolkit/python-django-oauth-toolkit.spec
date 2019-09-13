#
# spec file for package python-django-oauth-toolkit
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-oauth-toolkit
Version:        1.1.3
Release:        0
Summary:        OAuth2 Provider for Django
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/django-oauth-toolkit
Source:         https://github.com/jazzband/django-oauth-toolkit/archive/%{version}.tar.gz#/django-oauth-toolkit-%{version}.tar.gz
Patch0:         test-response-401.patch
BuildRequires:  %{python_module Django >= 1.11}	
BuildRequires:  %{python_module oauthlib >= 2.0.3}
BuildRequires:  %{python_module requests >= 2.13.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module djangorestframework}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-Django >= 1.11
Requires:       python-oauthlib >= 2.0.3
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
%setup -q -n django-oauth-toolkit-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=$(pwd)
%python_exec -m pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGELOG.md docs/*.rst docs/rest-framework/ docs/tutorial/ docs/views/
%{python_sitelib}/*

%changelog
