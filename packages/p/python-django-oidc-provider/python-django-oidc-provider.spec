#
# spec file for package python-django-oidc-provider
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


Name:           python-django-oidc-provider
Version:        0.7.0
Release:        0
Summary:        OpenID Connect Provider implementation for Django
License:        MIT
URL:            https://github.com/juanifioren/django-oidc-provider
Source:         https://github.com/juanifioren/django-oidc-provider/archive/v%{version}.tar.gz#/django-oidc-provider-%{version}.tar.gz
# PATCH-FIX-UPSTREAM django4.patch gh#juanifioren/django-oidc-provider#399 mcepl@suse.com
# Django 4 doesn't have ugettext_lazy function
Patch1:         django4.patch
# https://github.com/juanifioren/django-oidc-provider/issues/401
Patch2:         python-django-oidc-provider-no-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-pyjwkest >= 1.3.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module psycopg2}
BuildRequires:  %{python_module pyjwkest >= 1.3.0}
BuildRequires:  %{python_module pytest >= 3.6.4}
BuildRequires:  %{python_module pytest-django}
# /SECTION
%python_subpackages

%description
OpenID Connect Provider implementation for Django.

%prep
%autosetup -p1 -n django-oidc-provider-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#juanifioren/django-oidc-provider#400
%pytest -k 'not test_makemigrations_output'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/oidc_provider
%{python_sitelib}/django_oidc_provider-%{version}*-info

%changelog
