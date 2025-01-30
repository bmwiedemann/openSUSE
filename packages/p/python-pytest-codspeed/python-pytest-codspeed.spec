#
# spec file for package python-pytest-codspeed
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
%{?sle15_python_module_pythons}
Name:           python-pytest-codspeed%{psuffix}
Version:        3.1.2
Release:        0
Summary:        A pytest plugin to create CodSpeed benchmarks
License:        MIT
URL:            https://github.com/CodSpeedHQ/pytest-codspeed
# gh#CodSpeedHQ/pytest-codspeed#70
ExclusiveArch:  x86_64 aarch64
Source:         https://files.pythonhosted.org/packages/source/p/pytest_codspeed/pytest_codspeed-%{version}.tar.gz
# PATCH-FIX-UPSTREAM make_tests_work.patch gh#CodSpeedHQ/pytest-codspeed#68 mcepl@suse.com
# add missing files
Patch0:         make_tests_work.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module cffi >= 1.17.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module rich >= 13.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  valgrind-devel
Requires:       python-cffi >= 1.17.1
Requires:       python-pytest >= 3.8
Requires:       python-rich >= 13.8.1
%if %{with test}
BuildRequires:  %{python_module pytest >= 3.8}
BuildRequires:  %{python_module pytest-codspeed = %{version}}
%endif
%python_subpackages

%description
A pytest plugin to create CodSpeed benchmarks.

%prep
%autosetup -p1 -n pytest_codspeed-%{version}

%build
%if %{without test}
export PYTEST_CODSPEED_FORCE_EXTENSION_BUILD=1
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
export PYTEST_CODSPEED_FORCE_VALGRIND_TESTS=1
%pytest
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/pytest_codspeed
%{python_sitearch}/pytest_codspeed-%{version}*-info
%exclude %{python_sitearch}/pytest_codspeed/instruments/valgrind/_wrapper/wrapper.[ch]
%endif

%changelog
