#
# spec file for package symmetrica
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


%define lname	libsymmetrica2
Name:           symmetrica
Version:        3.0.1
Release:        0
Summary:        C library for group theory
License:        MIT
Group:          Productivity/Scientific/Math
URL:            https://gitlab.com/sagemath/symmetrica
Source:         https://gitlab.com/sagemath/symmetrica/-/archive/%version/symmetrica-%version.tar.gz
Patch1:         return-value.patch
BuildRequires:  libtool

%description
Symmetrica is a C library with routines for group theory.

%package -n %lname
Summary:        C library for group theory
Group:          System/Libraries

%description -n %lname
Symmetrica is a C library with routines for the following applications, among
many others:

  * ordinary representation theory of the symmetric group and related groups
  * ordinary representation theory of the classical groups
  * modular representation theory of the symmetric group
  * projective representation theory of the symmetric group
  * combinatorics of tableaux
  * symmetric functions and polynomials
  * commutative and non commutative Schubert polynomials
  * operations of finite groups
  * ordinary representation theory of Hecke algebras of type An

%package devel
Summary:        Header files for Symmetrica, a library for group theory
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Symmetrica is a C library with routines for group theory.
This package contains header files.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static --docdir="%_defaultdocdir/%name"
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libsymmetrica.so.2*

%files devel
%license LICENSE
%_includedir/symmetrica*
%_libdir/libsymmetrica.so
%_defaultdocdir/%name/

%changelog
