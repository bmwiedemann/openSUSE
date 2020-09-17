#
# spec file for package z3
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


%define sover 4_8
Name:           z3
Version:        4.8.9
Release:        0
Summary:        Theorem prover from Microsoft Research
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://github.com/Z3Prover/z3/wiki
Source0:        https://github.com/Z3Prover/z3/archive/z3-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  python3-devel

%description
Z3 is a Satisfiability Modulo Theories (SMT) solver and integrates
several decision procedures: Linear real and integer arithmetic,
fixed-size bit vectors, uninterpreted functions, extensional arrays,
quantifiers and model generation.

%package -n libz3-%{sover}
Summary:        Library for the Z3 SMT theorem prover
Group:          System/Libraries

%description -n libz3-%{sover}
Z3 is a Satisfiability Modulo Theories (SMT) solver and integrates
several decision procedures.

This subpackage contains the Z3 runtime library needed for Z3 and
other projects.

%package devel
Summary:        Development files for Z3
Group:          Development/Languages/C and C++
Requires:       libz3-%{sover} = %{version}

%description devel
Development files for the Z3 library.

%package -n python3-%{name}
Summary:        Python bindings for Z3
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python3-%{name}
Python bindings for the Z3 library.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%define __builder ninja
%cmake \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DZ3_BUILD_LIBZ3_SHARED=true \
  -DZ3_USE_LIB_GMP=true \
  -DZ3_BUILD_PYTHON_BINDINGS=true \
  -DZ3_INSTALL_PYTHON_BINDINGS=true \
  -DZ3_ENABLE_EXAMPLE_TARGETS=false \
%if 0%{?suse_version} >= 1550
  -DZ3_LINK_TIME_OPTIMIZATION=true
%else
  -DZ3_LINK_TIME_OPTIMIZATION=false
%endif

%cmake_build

%install
%cmake_install

%post -n libz3-%{sover} -p /sbin/ldconfig
%postun -n libz3-%{sover} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.md RELEASE_NOTES
%{_bindir}/z3

%files -n libz3-%{sover}
%{_libdir}/libz3.so.*

%files devel
%{_includedir}/z3*.h
%{_libdir}/libz3.so
%{_libdir}/pkgconfig/z3.pc
%dir %{_libdir}/cmake/z3/
%{_libdir}/cmake/z3/Z3Config.cmake
%{_libdir}/cmake/z3/Z3ConfigVersion.cmake
%{_libdir}/cmake/z3/Z3Targets*

%files -n python3-%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*py

%changelog
