#
# spec file for package python-zope.interface
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%global modname zope.interface
%{?sle15_python_module_pythons}
Name:           python-zope.interface%{psuffix}
Version:        6.4.post2
Release:        0
Summary:        Interfaces for Python
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.interface
Source:         https://files.pythonhosted.org/packages/source/z/zope.interface/%{modname}-%{version}.tar.gz
# needed for tests that try to compile things
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module zope.event}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testing}
%endif
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
%python_subpackages

%description
This package is intended to be independently reusable in any Python
project. It is maintained by the Zope Toolkit project.

This package provides an implementation of object interfaces for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the Design By Contract methodology support in Python.

%prep
%setup -q -n %{modname}-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand rm %{buildroot}%{$python_sitearch}/zope/interface/_zope_interface_coptimizations.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
cd src
%pyunittest zope/interface/{common/,}tests/test_*.py
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt COPYRIGHT.txt
%doc CHANGES.rst README.rst
%{python_sitearch}/zope.interface-%{version}*-info
%{python_sitearch}/zope.interface-%{version}*-nspkg.pth
%dir %{python_sitearch}/zope
%{python_sitearch}/zope/interface

%endif

%changelog
