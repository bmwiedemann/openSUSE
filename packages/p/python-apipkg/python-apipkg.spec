#
# spec file for package python
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-apipkg%{psuffix}
Version:        1.5
Release:        0
Summary:        Namespace control and lazy-import mechanism
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/apipkg/
Source:         https://files.pythonhosted.org/packages/source/a/apipkg/apipkg-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pytest4.patch bsc#[0-9]+ mimi.vx@gmail.com
# Collected upstream fixes for gh#pytest-dev/apipkg#14 and
# gh#pytest-dev/apipkg#15
Patch0:         pytest4.patch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
With apipkg you can control the exported namespace of a
python package and greatly reduce the number of imports for your users.
It is a `small pure python module`_ that works on virtually all Python
versions, including CPython2.3 to Python3.1, Jython and PyPy.  It co-operates
well with Python's ``help()`` system, custom importers (PEP302) and common
command line completion tools.

Usage is very simple: you can require 'apipkg' as a dependency or you
can copy paste the <100 Lines of code into your project.

%prep
%autosetup -p1 -n apipkg-%{version}

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
PYTHONPATH=$(pwd)/src
%pytest
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG
%dir %{python_sitelib}/apipkg
%{python_sitelib}/apipkg/*
%{python_sitelib}/apipkg-%{version}-py%{python_version}.egg-info
%endif

%changelog
