#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-mock%{psuffix}
Version:        4.0.3
Release:        0
Summary:        A Python Mocking and Patching Library for Testing
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://www.voidspace.org.uk/python/mock/
# no tests in PyPI sdist, use Github
Source:         https://github.com/testing-cabal/mock/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM mock-pr497-fixmixup-496.patch -- fix mixup of import, gh#/testing-cabal#496
Patch0:         https://github.com/testing-cabal/mock/pull/497.patch#/mock-pr497-fixmixup-496.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch

%python_subpackages

%description
mock is a Python module that provides a core Mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%prep
%autosetup -p1 -n mock-%{version}

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
%{python_sitelib}/mock
%{python_sitelib}/mock-%{version}*-info
%endif

%changelog
