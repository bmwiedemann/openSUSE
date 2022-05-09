#
# spec file for package python-django-invitations
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
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-invitations
Version:        1.9.3
Release:        0
Summary:        Generic invitations app with support for Django-allauth
License:        GPL-3.0-only
URL:            https://github.com/bee-keeper/django-invitations
Source:         https://github.com/bee-keeper/django-invitations/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#bee-keeper/django-invitations#169
Patch0:         django-4.0.patch
# https://github.com/jazzband/django-invitations/blob/master/tests/basic/tests.py#L4
Patch1:         python-django-invitations-no-mock.patch
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module django-allauth}
BuildRequires:  %{python_module freezegun >= 0.3.5}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-django >= 3.1.2}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/basic/tests.py --ds=test_settings
%pytest tests/allauth/test_allauth.py --ds=test_allauth_settings

%files %{python_files}
%license LICENSE
%{python_sitelib}/invitations/
%{python_sitelib}/django_invitations-*.egg-info/

%changelog
