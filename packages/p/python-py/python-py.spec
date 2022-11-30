#
# spec file
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


%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-py%{psuffix}
Version:        1.11.0
Release:        0
Summary:        Library with cross-python path, ini-parsing, io, code, log facilities
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/py
Source:         https://files.pythonhosted.org/packages/source/p/py/py-%{version}.tar.gz
# https://github.com/pytest-dev/py/pull/222
Patch0:         pr_222.patch
BuildRequires:  %{python_module apipkg}
BuildRequires:  %{python_module iniconfig}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
Requires:       python-apipkg
Requires:       python-iniconfig
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      %{oldpython}-py-docs
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module py = %{version}}
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
%autosetup -p1 -n py-%{version}

rm -rf py.egg-info
rm -f tox.ini
# https://github.com/pytest-dev/py/issues/162
rm -f testing/log/test_warning.py
rm -r py/_vendored_packages

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# In addition to PR 222, there are other tests failing due to changes in pytest 5 & 6
# https://github.com/pytest-dev/py/issues/209
%pytest -k 'not (test_getdimensions or test_format_excinfo or test_excinfo_repr or test_excinfo_str or test_syntaxerror_rerepresentation or test_len or test_power or test_comments)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/py
%{python_sitelib}/py-%{version}*-info
%endif

%changelog
