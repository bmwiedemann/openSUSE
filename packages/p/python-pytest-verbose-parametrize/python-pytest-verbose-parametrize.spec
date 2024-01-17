#
# spec file for package python-pytest-verbose-parametrize
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
%bcond_without python2
Name:           python-pytest-verbose-parametrize
Version:        1.7.0
Release:        0
Summary:        More descriptive output for parametrized pytest tests
License:        MIT
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-verbose-parametrize/pytest-verbose-parametrize-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Iterable-collections.patch gh#man-group/pytest-plugins#197 mcepl@suse.com
# Python 3.10 finally really killed collections class, which are now in
# collections.abc
Patch0:         Iterable-collections.patch
# PATCH-FEATURE-UPSTREAM pytest-fixtures-pr171-remove-mock.patch -- gh#man-group#pytest-plugins#171
Patch1:         pytest-fixtures-pr171-remove-mock.patch
# https://github.com/man-group/pytest-plugins/issues/209
Patch2:         python-pytest-verbose-parametrize-no-six.patch
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python2-mock
%endif
# /SECTION
%python_subpackages

%description
More descriptive output for parametrized py.test tests.

%prep
%autosetup -p1 -n pytest-verbose-parametrize-%{version}

# we can't do integration tests as py2 and py3 can be different versions
# and the script simply calls $bindir/pytest
rm tests/integration/test_verbose_parametrize.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_verbose_parametrize.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_verbose_parametrize*.pyc
%{python_sitelib}/pytest_verbose_parametrize-%{version}*-info

%changelog
