#
# spec file for package levmar
#
# Copyright (c) 2022 SUSE LLC
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


# Somewhat arbitrary SOVERSION. Bump whenever ABI changes, which has
# not happed for several years (since 2.6 release in 2011).
%define sover 2
%define libname liblevmar%{sover}
Name:           levmar
Version:        2.6
Release:        0
Summary:        Levenberg-Marquardt nonlinear least squares algorithm
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://users.ics.forth.gr/~lourakis/levmar/
Source:         http://users.ics.forth.gr/~lourakis/levmar/levmar-%{version}.tgz
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel

%description
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method

%package -n %{libname}
Summary:        Levenberg-Marquardt nonlinear least squares algorithm
Group:          Development/Libraries/C and C++

%description -n %{libname}
levmar is a native ANSI C implementation of the Levenberg-Marquardt
optimization algorithm.  Both unconstrained and constrained (under linear
equations, inequality and box constraints) Levenberg-Marquardt variants are
included.  The LM algorithm is an iterative technique that finds a local
minimum of a function that is expressed as the sum of squares of nonlinear
functions.  It has become a standard technique for nonlinear least-squares
problems and can be thought of as a combination of steepest descent and the
Gauss-Newton method.  When the current solution is far from the correct on,
the algorithm behaves like a steepest descent method: slow, but guaranteed
to converge.  When the current solution is close to the correct solution, it
becomes a Gauss-Newton method

%package devel
Summary:        Development files for levmar library, and demo program
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for the levmar library, and demo program.

%prep
%setup -q
dos2unix -k README.txt

# Make levmar shared lib
sed -i \
    -e 's:ADD_LIBRARY(levmar STATIC:ADD_LIBRARY(levmar SHARED:' \
    CMakeLists.txt

echo "set_target_properties(levmar PROPERTIES SOVERSION %{sover})" >> CMakeLists.txt
echo "target_link_libraries(levmar m blas lapack)" >> CMakeLists.txt

%build
# no install target/command, so CMake won't remove the RPATH on install
# instead, do not add it at all (i.e. during build)
%cmake \
  -DNEED_F2C:BOOL=false \
  -DCMAKE_SKIP_RPATH:bool=true \
  %{nil}
%cmake_build

%install
install -D -p -m 755 build/liblevmar.so %{buildroot}%{_libdir}/liblevmar.so.%{sover}
install -D -p -m 644 levmar.h %{buildroot}%{_includedir}/levmar.h
install -D -p -m 755 build/lmdemo %{buildroot}%{_bindir}/lmdemo
ln -s liblevmar.so.%{sover} %{buildroot}%{_libdir}/liblevmar.so

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.txt
%{_libdir}/liblevmar.so.%{sover}

%files devel
%{_includedir}/levmar.h
%{_libdir}/liblevmar.so
%{_bindir}/lmdemo

%changelog
