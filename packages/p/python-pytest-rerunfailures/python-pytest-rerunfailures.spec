#
# spec file for package python-pytest-rerunfailures
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
Name:           python-pytest-rerunfailures
Version:        9.1.1
Release:        0
Summary:        A pytest plugin to re-run tests
License:        MPL-2.0
URL:            https://github.com/pytest-dev/pytest-rerunfailures
Source:         https://files.pythonhosted.org/packages/source/p/pytest-rerunfailures/pytest-rerunfailures-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 40.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 5.0
Requires:       python-setuptools >= 40.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 5.0}
# /SECTION
%python_subpackages

%description
The pytest-rerunfailures package is a plugin for py.test that re-runs
tests to eliminate intermittent failures.

%prep
%setup -q -n pytest-rerunfailures-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_rerunfailures.py*
%pycache_only %{python_sitelib}/__pycache__/pytest_rerunfailures*
%{python_sitelib}/pytest_rerunfailures-%{version}*-info

%changelog
