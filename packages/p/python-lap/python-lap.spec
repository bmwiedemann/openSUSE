#
# spec file for package python-lap
#
# Copyright (c) 2025 SUSE LLC
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

Name:           python-lap%{psuffix}
Version:        0.5.12
Release:        0
Summary:        Linear Assignment Problem solver (LAPJV/LAPMOD)
License:        BSD-2-Clause
URL:            https://github.com/gatagat/lap
Source:         https://files.pythonhosted.org/packages/source/l/lap/lap-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module Cython >= 0.29.32}
BuildRequires:  %{python_module numpy >= 1.21.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 67.8.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module lap = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-timeout}
# /SECTION
%endif
BuildRequires:  fdupes
Requires:       python-numpy >= 1.21.6
%python_subpackages

%description
Linear Assignment Problem solver (LAPJV/LAPMOD).

%prep
%autosetup -p1 -n lap-%{version}

%build
%if !%{with test}
export CFLAGS="%{optflags}"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
mkdir testing
cp -rf lap/tests testing
pushd testing
%pytest_arch
popd
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/lap
%{python_sitearch}/lap-%{version}.dist-info
%endif

%changelog
