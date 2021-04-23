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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-pathlib2%{?psuffix}
Version:        2.3.5
Release:        0
Summary:        Object-oriented filesystem paths
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mcmtroffaes/pathlib2
Source:         https://files.pythonhosted.org/packages/source/p/pathlib2/pathlib2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module scandir}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testsuite}
%endif
%ifpython2
Requires:       python-scandir
%endif
%ifpython2
Provides:       %{oldpython}-pathlib2 = %{version}
Obsoletes:      %{oldpython}-pathlib2 <= %{version}
%endif
%python_subpackages

%description
The goal of pathlib2 is to provide a backport of
`standard pathlib <http://docs.python.org/dev/library/pathlib.html>`_
module which tracks the standard library module,
so all the newest features of the standard pathlib can be
used also on older Python versions.

%prep
%autosetup -n pathlib2-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export PYTHONPATH="$PWD"
%python_exec tests/test_pathlib2.py
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.rst
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*
%endif

%changelog
