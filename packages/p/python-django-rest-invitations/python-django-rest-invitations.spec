#
# spec file for package python-django-rest-invitations
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-django-rest-invitations
Version:        0.1.2
Release:        0
Summary:        A set of Django REST API endpoints to handle invitations
License:        GPL-3.0-only
URL:            https://github.com/fmarco/django-rest-invitations
Source:         https://github.com/fmarco/django-rest-invitations/archive/%{version}.tar.gz#/django-rest-invitations-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#fmarco/django-rest-invitations#17
Patch0:         django-4.0.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-django-invitations >= 1.9.3
Requires:       python-djangorestframework >= 3.10
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module django-invitations >= 1.9.3}
BuildRequires:  %{python_module djangorestframework >= 3.10}
BuildRequires:  %{python_module pytest-django}
# /SECTION
%python_subpackages

%description
A set of Django REST API endpoints to handle invitations.

%prep
%autosetup -p1 -n django-rest-invitations-%{version}
sed -i -e 's:==:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec manage.py test

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/*

%changelog
