#
# spec file for package python-django-perf-rec
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-django-perf-rec
Version:        4.26.0
Release:        0
Summary:        Keep detailed records of the performance of your Django code
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/adamchainz/django-perf-rec
Source:         https://github.com/adamchainz/django-perf-rec/archive/refs/tags/%{version}.tar.gz#/django-perf-rec-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
Requires:       python-PyYAML
Requires:       python-sqlparse >= 0.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module sqlparse >= 0.4.0}
# /SECTION
%python_subpackages

%description
Keep detailed records of the performance of your Django code.

%prep
%setup -q -n django-perf-rec-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
export DJANGO_SETTINGS_MODULE=tests.settings
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
