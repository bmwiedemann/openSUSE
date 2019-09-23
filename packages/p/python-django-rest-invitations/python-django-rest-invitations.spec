#
# spec file for package python-django-rest-invitations
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-django-rest-invitations
Version:        0.1.1
Release:        0
Summary:        A set of Django REST API endpoints to handle invitations
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            http://github.com/fmarco/django-rest-invitations
Source:         https://github.com/fmarco/django-rest-invitations/archive/%{version}.tar.gz
Patch0:         fix-test-middleware-classes.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-django-invitations >= 1.9.2
Requires:       python-djangorestframework >= 3.7.7
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module django-invitations >= 1.9.2}
BuildRequires:  %{python_module djangorestframework >= 3.7.7}
BuildRequires:  %{python_module pytest-django}
# /SECTION
%python_subpackages

%description
A set of Django REST API endpoints to handle invitations.

%prep
%setup -q -n django-rest-invitations-%{version}
%patch0 -p1

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
