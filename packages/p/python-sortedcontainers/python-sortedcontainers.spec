#
# spec file for package python-sortedcontainers
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
Name:           python-sortedcontainers%{psuffix}
Version:        2.3.0
Release:        0
Summary:        Sorted container data types
License:        Apache-2.0
URL:            https://github.com/grantjenks/python-sortedcontainers
Source:         https://github.com/grantjenks/python-sortedcontainers/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
%endif
%python_subpackages

%description
SortedContainers is an Apache2 licensed containers library, written in
pure-Python, and fast as C-extensions.

Python's standard library is great until you need a sorted container type. Many
will attest that you can get really far without one, but the moment you **really
need** a sorted list, dict, or set, you're faced with a dozen different
implementations, most using C-extensions without great documentation and
benchmarking.

SortedContainers takes all of the work out of Python sorted types - making your
deployment and use of Python easy. There's no need to install a C compiler or
pre-build and distribute custom extensions. Performance is a feature and testing
has 100% coverage with unit tests and hours of stress.

%prep
%setup -q -n python-sortedcontainers-%{version}
rm -rf sortedcontainers.egg-info

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest tests
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%endif

%changelog
