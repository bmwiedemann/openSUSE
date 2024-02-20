#
# spec file for package python-cramjam
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
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

# Adjust the version in _service and use `rm -rf cramjam; osc service runall` in order to update
%define modname cramjam
Name:           python-cramjam%{psuffix}
Version:        2.8.1
Release:        0
Summary:        Thin Python bindings to de/compression algorithms in Rust
License:        MIT
URL:            https://github.com/milesgranger/cramjam
Source:         %{modname}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module maturin >= 0.13}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
# SECTION test dependencies
%if %{with test}
BuildRequires:  %{python_module %{modname} = %{version}}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module memory_profiler}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
%python_subpackages

%description
Extremely thin Python bindings to de/compression algorithms in Rust.
Allows for using algorithms such as Snappy, without any system dependencies.

%prep
%setup -q -n %{modname}-%{version} -a1

%build
%if %{without test}
pushd %{modname}-python
%pyproject_wheel
%endif

%install
%if %{without test}
pushd %{modname}-python
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
pushd %{modname}-python
%pytest_arch --ignore benchmarks
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}.dist-info
%endif

%changelog
