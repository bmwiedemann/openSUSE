#
# spec file for package python-django-invitations
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-django-invitations
Version:        2.0.0
Release:        0
Summary:        Generic invitations app with support for Django-allauth
License:        GPL-3.0-only
URL:            https://github.com/bee-keeper/django-invitations
Source:         https://github.com/bee-keeper/django-invitations/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM configure-django.patch gh#jazzband/django-invitations!235 mcepl@suse.com
# Add missing configuration settings
Patch0:         configure-django.patch
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-allauth}
BuildRequires:  %{python_module freezegun >= 0.3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-django >= 3.1.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Recommends:     python-django-allauth
BuildArch:      noarch
%python_subpackages

%description
Generic invitations app with support for Django-allauth.

%prep
%autosetup -p1 -n django-invitations-%{version}
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/basic/tests.py --ds=test_settings
%pytest tests/allauth/test_allauth.py --ds=test_allauth_settings

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/invitations
%{python_sitelib}/django_invitations-%{version}*-info

%changelog
