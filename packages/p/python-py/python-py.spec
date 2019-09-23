#
# spec file for package python-py
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-py%{psuffix}
Version:        1.8.0
Release:        0
Summary:        Library with cross-python path, ini-parsing, io, code, log facilities
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/py
Source:         https://files.pythonhosted.org/packages/source/p/py/py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      %{oldpython}-py-docs
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
The py lib is a Python development support library featuring
the following tools and modules:

* py.path:  uniform local and svn path objects
* py.apipkg:  explicit API control and lazy-importing
* py.iniconfig:  easy parsing of .ini files
* py.code: dynamic code generation and introspection
* py.path:  uniform local and svn path objects

%prep
%setup -q -n py-%{version}

rm -rf py.egg-info
rm -f tox.ini
# https://github.com/pytest-dev/py/issues/162
rm -f testing/log/test_warning.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_exec %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# the passing is because upstream does not care about the results for now and
# pinned pytest 3 in the repo (as this module is deprecated)
# https://github.com/pytest-dev/py/issues/209
%pytest || :
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
