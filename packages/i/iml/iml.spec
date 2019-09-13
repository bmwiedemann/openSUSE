#
# spec file for package iml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without openblas

Name:           iml
%define lname   libiml0
Version:        1.0.5
Release:        0
Summary:        An Integer Matrix Library
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://cs.uwaterloo.ca/~astorjoh/iml.html

Source:         https://www.cs.uwaterloo.ca/~astorjoh/%name-%version.tar.bz2
BuildRequires:  gmp-devel >= 3.1.1
%if %{with openblas}
BuildRequires:  openblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  cblas-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
IML package provides routines to solve nonsingular systems of linear
equations, solve any shape systems of linear equations, and perform
mod p matrix operations, such as computing row-echelon form,
determinant, rank profile, inverse of a mod p matrix.

%package -n %lname
Summary:        An Integer Matrix Library
Group:          System/Libraries

%description -n %lname
IML package provides routines to solve nonsingular systems of linear
equations, solve any shape systems of linear equations, and perform
mod p matrix operations, such as computing row-echelon form,
determinant, rank profile, inverse of a mod p matrix.

%package devel
Summary:        Development files for IML, an Integer Matrix Library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       gmp-devel >= 3.3.1

%description devel
IML package provides routines to solve nonsingular systems of linear
equations, solve any shape systems of linear equations, and perform
mod p matrix operations, such as computing row-echelon form,
determinant, rank profile, inverse of a mod p matrix.

This subpackage contains the include files and library links for   
developing against the IML library.

%prep
%autosetup -p1

%build
%configure --enable-shared --disable-static \
%if %{with openblas}
	   --with-cblas="-lopenblas" \
%else
	   --with-cblas="-lcblas -lblas" \
%endif
	   %{nil}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la
mkdir -p "$b/%_docdir"
mv "$b/%_datadir/iml" "$b/%_docdir/"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libiml.so.0*
%license COPYING

%files devel
%_includedir/iml.h
%_libdir/libiml.so
%_docdir/%name/

%changelog
