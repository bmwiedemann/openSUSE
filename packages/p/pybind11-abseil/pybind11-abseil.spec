#
# spec file for package pybind11-abseil
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%{?sle15_python_module_pythons}
%define __builder ninja
%define python_subpackage_only 1
Name:           pybind11-abseil
Version:        202402.0
Release:        0
Summary:        Pybind11 bindings for the Abseil C++ Common Libraries
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11_abseil
Source:         %{url}/releases/download/v%{version}/pybind11_abseil-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- Based on patch from google-or-tools, rebased on pybind11-abseil 2002402.0
Patch0:         pybind11_abseil.patch
# PATCH-FIX-UPSTREAM use-system-packages-if-possible.patch badshah400@gmail.com -- Allow the use of system absl-cpp and pybind11 if available
Patch1:         use-system-packages-if-possible.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Install-headers-and-CMake-development-files.patch
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.24
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
BuildRequires:  cmake(absl)
BuildRequires:  cmake(pybind11) >= 2.11.0
# Section Tests need
BuildRequires:  %{python_module abseil}
BuildRequires:  %{python_module numpy}
# /Section
%python_subpackages

%description
%{name} provides adapters that make Abseil types work with Pybind11 bindings.

%package -n %{name}-devel
Summary:        Development files for pybind11_abseil
Requires:       cmake(absl)
Requires:       cmake(pybind11)

%description -n %{name}-devel
%{name} provides adapters that make Abseil types work with Pybind11 bindings.

This package provides the shared object files for developing against
pybind11_abseil independent of the python version in use.

%package -n python-pybind11_abseil
Summary:        Python version specific development files for pybind11_abseil
Requires:       python-abseil
Requires:       python-numpy

%description -n python-pybind11_abseil
%{name} provides adapters that make Abseil types work with Pybind11 bindings.

This package provides the python version specific shared objects to develop
applications against pybind11_abseil.

%prep
%autosetup -p1 -n pybind11_abseil-%{version}

%build
%{python_expand pushd . # build
%cmake \
  -DCMAKE_INSTALL_PYDIR=%{$python_sitearch} \
  -DPython_EXECUTABLE=%{_bindir}/python%{$python_version} \
  %{nil}
%cmake_build
popd
}

%install
%{python_expand # install
%cmake_install
}

%check
# test fails on x86: https://github.com/pybind/pybind11_abseil/issues/22
%ifnarch %{ix86}
%{python_expand # tests
%ctest
}
%endif

%files -n %{name}-devel
%license LICENSE
%doc README.md
%{_includedir}/pybind11_abseil/
%{_libdir}/cmake/pybind11_abseil/
%{_libdir}/lib*.a

%files %{python_files pybind11_abseil}
%license LICENSE
%doc README.md
%{python_sitearch}/pybind11_abseil/

%changelog
