#
# spec file for package eigen3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           eigen3
Version:        3.3.7
Release:        0
Summary:        C++ Template Library for Linear Algebra
License:        MPL-2.0 and LGPL-2.1+ and BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://eigen.tuxfamily.org/
Source0:        https://bitbucket.org/eigen/eigen/get/%{version}.tar.bz2#/%{name}-%{version}.tar.bz2
Patch0:         0001-Disable-Altivec-for-ppc64le.patch
Patch1:         0001-Do-stack-allignment-on-ppc.patch
# PATCH-FIX-OPENSUSE eigen_pkgconfig.patch asterios.dramis@gmail.com -- Fix pkg-config file includedir
Patch2:         eigen_pkgconfig.patch
# PATCH-FIX-OPENSUSE 01_install_FindEigen3.patch asterios.dramis@gmail.com -- Install FindEigen3.cmake
Patch3:         01_install_FindEigen3.patch
# PATCH-FIX-OPENSUSE eigen3-3.3.1-fixcmake.patch -- Fix double {prefix} as we use INCLUDE_INSTALL_DIR with {_includedir}
Patch4:         eigen3-3.3.1-fixcmake.patch
BuildRequires:  adolc-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  glew-devel
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  gsl-devel
%if 0%{?suse_version} > 1320
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if 0%{?suse_version} == 1315
BuildRequires:  libqt4-devel
%endif
BuildRequires:  mpfr-devel
BuildRequires:  pkg-config
BuildRequires:  sparsehash-devel
BuildRequires:  suitesparse-devel
BuildRequires:  superlu-devel
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(gl)
BuildArch:      noarch
%if 0%{?suse_version} > 1310
BuildRequires:  metis-devel
%endif

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package devel
Summary:        C++ Template Library for Linear Algebra
Group:          Development/Libraries/C and C++
# libeigen3-devel was last used at openSUSE 13.1 (version 3.2.0)
Provides:       libeigen3-devel = %{version}
Obsoletes:      libeigen3-devel < %{version}

%description devel
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms.

%package doc
Summary:        Documentation for the Eigen3 C++ Template Library for Linear Algebra
Group:          Documentation/HTML

%description doc
Documentation in HTML format for the Eigen3 C++ Template Library
for Linear Algebra

%prep
%setup -q -n eigen-eigen-323c052e1731
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' COPYING.MINPACK

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/Doxyfile.in

%build
%cmake \
 -DCMAKE_BUILD_TYPE=Release \
 -DINCLUDE_INSTALL_DIR=%{_includedir}/eigen3 \
 -DGOOGLEHASH_INCLUDES=%{_includedir}
make %{?_smp_mflags} all doc
rm -f doc/html/*.tgz `find doc -name _formulas.log`

%install
%cmake_install
%fdupes -s build/doc/html/

%files devel
%defattr(-,root,root,-)
%doc COPYING.*
%{_includedir}/eigen3/
%{_datadir}/eigen3/
%{_datadir}/pkgconfig/eigen3.pc
%{_datadir}/cmake/Modules/FindEigen3.cmake

%files doc
%defattr(-,root,root,-)
%doc build/doc/html/

%changelog
