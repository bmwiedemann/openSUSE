#
# spec file for package python-django-request
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-django-request
Version:        1.5.6
Release:        0
Summary:        Django statistics app
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-request/django-request
Source:         https://github.com/django-request/django-request/archive/%{version}.tar.gz#/django-request-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-python-dateutil
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
django-request is a statistics module for django.
It stores requests in a database for admins to see,
it can also be used to get statistics on who is online etc.

%prep
%setup -q -n django-request-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.test_settings
%python_exec -m django test -v 2

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
