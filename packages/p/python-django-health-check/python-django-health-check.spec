#
# spec file for package python-django-health-check
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
%define skip_python2 1
Name:           python-django-health-check
Version:        3.14.0
Release:        0
Summary:        Run checks on Django and is dependent services
License:        MIT
URL:            https://github.com/KristianOellegaard/django-health-check
Source:         https://github.com/KristianOellegaard/django-health-check/archive/%{version}.tar.gz#/django-health-check-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module celery}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
BuildArch:      noarch
%python_subpackages

%description
This project checks for various conditions and provides reports when anomalous
behavior is detected.

Services checked include databases, caches, queue servers, celery processes, etc.

%prep
%setup -q -n django-health-check-%{version}
# setuptools-scm fails for GitHub archives
sed -i 's/use_scm_version=True/version="%{version}"/' setup.py

# do not nedlessly pull extra deps
sed -i -e '/sphinx/d;/pytest-runner/d;/--cov[-=]/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
