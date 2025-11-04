#
# spec file for package eigen3
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


%global pkgname eigen3
%global srcname eigen

# The OpenGL support test fails
%bcond_with opengl_test

# Tests fail for different reasons within the test-suite itself; disable for now
# See e.g. https://gitlab.com/libeigen/eigen/-/issues/2088, https://gitlab.com/libeigen/eigen/-/issues/2092
# Also balloons the resources required: > 32 GiB disk space + >= 12 GiB memory
%bcond_with tests

# Docs for version 3.4.1 do not build with doxygen 1.14.0 or later: https://gitlab.com/libeigen/eigen/-/issues/2976
# So, we do not build them but just extract a pre-generated doc tarball from upstream and package its contents

%define major_ver 3.4
%define api_docdir %{_docdir}/%{name}/api

Name:           eigen3
Version:        %{major_ver}.1
Release:        0
Summary:        C++ Template Library for Linear Algebra
License:        BSD-3-Clause AND LGPL-2.1-only AND MPL-2.0 AND LGPL-2.1-or-later
URL:            http://eigen.tuxfamily.org/
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/%{srcname}-%{version}.tar.bz2
Source1:        https://libeigen.gitlab.io/eigen/docs-%{major_ver}/eigen-doc.tgz#/%{srcname}-doc-%{major_ver}.tar.bz2
Patch0:         0001-Disable-Altivec-for-ppc64le.patch
Patch1:         0001-Do-stack-allignment-on-ppc.patch
%if %{with tests}
# SECTION Patches to fix tests
# PATCH-FIX-UPSTREAM eigen3-googlehash-detection.patch badshah400@gmail.com -- GoogleHash needs C++11 std to compile test code and be succesfully detected
Patch9:         eigen3-googlehash-detection.patch
# PATCH-FIX-UPSTREAM eigen3-fix-forward_adolc-unit-test.patch badshah400@gmail -- Prevent conflict of std::min/max with eigen's macros by importing eigen test-suite's main.h header only after all system headers have been included
Patch10:        eigen3-fix-forward_adolc-unit-test.patch
# /SECTION
%endif
BuildRequires:  adolc-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gmp-devel
BuildRequires:  gsl-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  metis-devel
BuildRequires:  mpfr-devel
BuildRequires:  pkg-config
BuildRequires:  sparsehash-devel
BuildRequires:  suitesparse-devel
BuildRequires:  superlu-devel
%if %{with opengl_test}
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
BuildRequires:  pkgconfig(gl)
%endif
BuildArch:      noarch

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package devel
Summary:        C++ Template Library for Linear Algebra
# libeigen3-devel was last used at openSUSE 13.1 (version 3.2.0)
Provides:       libeigen3-devel = %{version}
Obsoletes:      libeigen3-devel < %{version}

%description devel
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package doc
Summary:        Documentation for the Eigen3 C++ Template Library for Linear Algebra
BuildArch:      noarch

%description doc
Documentation in HTML format for the Eigen3 C++ Template Library
for Linear Algebra

%prep
%autosetup -p1 -b1 -n %{srcname}-%{version}

# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' COPYING.MINPACK

%build
%cmake \
 -DCMAKE_SKIP_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
 -DEIGEN_BUILD_BLAS:BOOL=OFF \
 -DEIGEN_BUILD_LAPACK:BOOL=OFF \
 -DEIGEN_TEST_CXX11:Bool=%{?with_tests:ON}%{!?with_tests:OFF} \
 -DEIGEN_TEST_OPENMP:Bool=%{?with_tests:ON}%{!?with_tests:OFF} \
 -DINCLUDE_INSTALL_DIR:PATH=include/eigen3 \
 %{nil}

%cmake_build all %{?with_tests:buildtests}

%install
%cmake_install

# Install bundled docs
mkdir -p %{buildroot}%{api_docdir}
cp -r ../eigen-doc/* %{buildroot}%{api_docdir}
%fdupes %{buildroot}%{api_docdir}

%if %{with tests}
%check
# Run with a fixed seed to prevent random failures: https://gitlab.com/libeigen/eigen/-/issues/2088
export EIGEN_SEED=100
# Repeat each test once to reduce time spent, since we use a fixed seed anyway
export EIGEN_REPEAT=1
%ctest
%endif

%files devel
%license COPYING.*
%{_includedir}/eigen3/
%{_datadir}/eigen3/
%{_datadir}/pkgconfig/eigen3.pc

%files doc
%dir %{_docdir}/%{name}
%doc %{api_docdir}

%changelog
