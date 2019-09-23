#
# spec file for package python-mock
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-mock%{psuffix}
Version:        3.0.5
Release:        0
Summary:        A Python Mocking and Patching Library for Testing
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://www.voidspace.org.uk/python/mock/
# no tests in sdis
# Source:         https://files.pythonhosted.org/packages/source/m/mock/mock-%{version}.tar.gz
Source:         https://github.com/testing-cabal/mock/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 17.1}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-funcsigs
%endif
%ifpython2
Requires:       python-funcsigs >= 1
%endif
%python_subpackages

%description
mock is a Python module that provides a core Mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%prep
%setup -q -n mock-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*
%endif

%changelog
