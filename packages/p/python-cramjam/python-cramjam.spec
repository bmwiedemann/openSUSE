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
%{?sle15_python_module_pythons}
Name:           python-cramjam%{psuffix}
Version:        2.9.1
Release:        0
Summary:        Thin Python bindings to de/compression algorithms in Rust
License:        MIT
URL:            https://github.com/milesgranger/cramjam
Source:         %{modname}-%{version}.tar.xz
Source1:        vendor.tar.xz
# PATCH-FEATURE-OPENSUSE cramjam-opensuse-config.patch code@bnavigator.de -- Use system libraries and avoid static linking
Patch0:         cramjam-opensuse-config.patch
# PATCH-FIX-UPSTREAM cramjam-issue193-test_variants.patch gh#milesgranger/cramjam#193
Patch1:         cramjam-issue193-test_variants.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module maturin >= 0.13}
BuildRequires:  %{python_module pip}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(blosc2)
BuildRequires:  pkgconfig(libisal)
BuildRequires:  pkgconfig(libzstd)
# SECTION test dependencies
%if %{with test}
BuildRequires:  %{python_module %{modname} = %{version}}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module memory_profiler}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
%python_subpackages

%description
Extremely thin Python bindings to de/compression algorithms in Rust.
Allows for using algorithms such as Snappy, without any system dependencies.

%prep
%autosetup -p1 -n %{modname}-%{version} -a1

%build
%if %{without test}
export ZSTD_SYS_USE_PKG_CONFIG=1
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
%pytest_arch -n auto --ignore benchmarks
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}.dist-info
%endif

%changelog
