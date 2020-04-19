#
# spec file for package python-pyfakefs
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-pyfakefs%{psuffix}
Version:        4.0.2
Release:        0
Summary:        Fake file system that mocks the Python file system modules
License:        Apache-2.0
URL:            https://github.com/jmcgeheeiv/pyfakefs
Source:         https://github.com/jmcgeheeiv/pyfakefs/archive/v%{version}.tar.gz#/python-pyfakefs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest >= 2.8.6}
BuildRequires:  %{pythons}
%endif
%python_subpackages

%description
pyfakefs implements a fake file system that mocks the Python file system
modules. Using pyfakefs, your tests operate on a fake file system in
memory without touching the real disk. The software under test requires
no modification to work with pyfakefs.

%prep
%setup -q -n pyfakefs-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/pyfakefs/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=C.UTF-8
%python_expand PYTHONPATH=$(pwd) $python -m pyfakefs.tests.all_tests
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES* README*
%license COPYING*
%{python_sitelib}/*
%endif

%changelog
