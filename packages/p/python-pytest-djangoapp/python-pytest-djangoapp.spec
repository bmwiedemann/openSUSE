#
# spec file for package python-pytest-djangoapp
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


%{?sle15_python_module_pythons}
Name:           python-pytest-djangoapp
Version:        1.8.0
Release:        0
Summary:        Pytest plugin for Django pluggable application testing
License:        BSD-3-Clause
URL:            https://github.com/idlesign/pytest-djangoapp
Source:         https://github.com/idlesign/pytest-djangoapp/archive/refs/tags/v%{version}.tar.gz#/pytest_djangoapp-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module hatchling}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-pytest
Recommends:     python-ipdb
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A pytest plugin to help with Django pluggable application testing.

%prep
%autosetup -p1 -n pytest-djangoapp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/pytest_djangoapp
%{python_sitelib}/pytest_djangoapp-%{version}.dist-info

%changelog
