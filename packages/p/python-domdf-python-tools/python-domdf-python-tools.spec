#
# spec file for package python-domdf-python-tools
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
Name:           python-domdf-python-tools%{psuffix}
Version:        3.10.0
Release:        0
Summary:        Helpful functions for Python 🐍 🛠️
License:        MIT
URL:            https://github.com/domdfcoding/domdf_python_tools
Source:         https://github.com/domdfcoding/domdf_python_tools/archive/refs/tags/v%{version}.tar.gz#/domdf_python_tools-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/domdfcoding/domdf_python_tools/pull/137 Fix Python 3.14 test failures
# with one more fix from me (in the comments)
Patch0:         py314.patch
BuildRequires:  %{python_module hatch-requirements-txt}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coincidence}
BuildRequires:  %{python_module domdf-python-tools = %{version}}
BuildRequires:  %{python_module funcy}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-natsort >= 7.0.1
Requires:       python-typing-extensions >= 3.7.4.1
Suggests:       python-pytz >= 2019.1
BuildArch:      noarch
%python_subpackages

%description
Helpful functions for Python 🐍 🛠️

%prep
%autosetup -p1 -n domdf_python_tools-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Broken upstream
%pytest -k 'not (test_discover_entry_points)'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/domdf_python_tools
%{python_sitelib}/domdf_python_tools-%{version}.dist-info
%endif

%changelog
