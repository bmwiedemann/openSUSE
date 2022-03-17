#
# spec file for package python-pytest-djangoapp
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
Name:           python-pytest-djangoapp
Version:        0.15.2
Release:        0
Summary:        Pytest plugin for Django pluggable application testing
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/idlesign/pytest-djangoapp
Source:         https://files.pythonhosted.org/packages/source/p/pytest-djangoapp/pytest-djangoapp-%{version}.tar.gz
# PATCH-FIX-UPSTREAM django_4.patch gh#idlesign/pytest-djangoapp#23 mcepl@suse.com
# this patch makes things totally awesome
Patch0:         django_4.patch
BuildRequires:  %{python_module setuptools}
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

# gh#idlesign/pytest-djangoapp#4
mv ./pytest_djangoapp/tests/conftest.py .

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/pytest_djangoapp/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
