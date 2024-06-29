#
# spec file for package armadillo
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


%define soname libarmadillo14
Name:           armadillo
Version:        14.0.0
Release:        0
Summary:        C++ matrix library with interfaces to LAPACK and ATLAS
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://arma.sourceforge.net/
Source:         https://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  arpack-ng-devel
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig
BuildRequires:  superlu-devel >= 5.2

%description
Armadillo is a C++ linear algebra library (matrix maths).
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.

%package     -n %{soname}
Summary:        C++ matrix library with interfaces to LAPACK and ATLAS
Group:          System/Libraries

%description -n %{soname}
Armadillo is a C++ linear algebra library (matrix maths).
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate)
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.

This package provides the shared libraries for armadillo.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
Armadillo is a C++ linear algebra library (matrix maths).
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.

This package provides the documentation for armadillo.

%package        devel
Summary:        Development headers and documentation for the Armadillo C++ library
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}
Requires:       arpack-ng-devel
Requires:       blas-devel
Requires:       lapack-devel
Requires:       libstdc++-devel
Requires:       superlu-devel >= 4.3
Recommends:     %{name}-doc

%description    devel
Armadillo is a C++ linear algebra library (matrix maths).
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.

This package contains files necessary for development using the
Armadillo C++ library. It contains header files, example programs,
and user documentation (reference guide).

%prep
%setup -q
#Convert DOS end-of-line to UNIX end-of-line
sed -i 's/\r$//' README.md
sed -i 's/\r$//' examples/README.txt
sed -i 's/\r$//' LICENSE.txt
sed -i 's/\r$//' NOTICE.txt
for i in `ls examples/*.cpp`; do sed -i 's/\r$//' $i; done

%build
%cmake -DBUILD_SMOKE_TEST:BOOL=ON
%cmake_build

%install
%cmake_install
rm -f examples/Makefile.cmake
rm -rf examples/example1_win64.*
rm -rf examples/example2_win64.*
rm -rf examples/lib_win64

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%{_libdir}/*.so.*

%files doc
%doc armadillo_*.pdf
%doc NOTICE.txt README.md index.html examples/ docs.html
%license LICENSE.txt

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/armadillo
%{_includedir}/armadillo_bits/
%{_datadir}/Armadillo/

%changelog
