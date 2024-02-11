#
# spec file for package python-django-request
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


Name:           python-django-request
Version:        1.6.3
Release:        0
Summary:        Django statistics app
License:        BSD-2-Clause
URL:            https://github.com/django-request/django-request
Source:         https://github.com/django-request/django-request/archive/%{version}.tar.gz#/django-request-%{version}.tar.gz
# gh#django-request/django-request#241
Patch0:         set-timezone-for-day-tests.patch
Patch1:         do-not-fail-on-day-one-of-month.patch
# PATCH-FIX-UPSTREAM https://github.com/django-request/django-request/pull/276 Fixed test_week() when first Sunday of the year is on January, 7th.
Patch2:         test_week.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 2.2
Requires:       python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
django-request is a statistics module for django.
It stores requests in a database for admins to see,
it can also be used to get statistics on who is online etc.

%prep
%autosetup -p1 -n django-request-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.test_settings
%python_exec -m django test -v 2

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/request
%{python_sitelib}/django_request-%{version}.dist-info

%changelog
