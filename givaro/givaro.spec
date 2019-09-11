#
# spec file for package givaro
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


Name:           givaro
%define lname   libgivaro9
Version:        4.0.4
Release:        0
Summary:        C++ library for arithmetic and algebraic computations
License:        CECILL-B
Group:          Productivity/Scientific/Math
Url:            http://givaro.forge.imag.fr/

#Git-Clone:	https://github.com/linbox-team/givaro
Source:         https://github.com/linbox-team/givaro/archive/v%version.tar.gz
Patch1:         givaro-doc-no-build-time.patch
Patch2:         reproducible.patch
# Old doxygen does not properly handle symlink recursion
BuildRequires:  doxygen >= 1.5.7.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 3.1.1
BuildRequires:  graphviz
BuildRequires:  libtool >= 2.2
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Givaro is a C++ library for arithmetic and algebraic computations.

Its main features are implementations of the basic arithmetic of many
mathematical entities: Primes fields, Extensions Fields, Finite
Fields, Finite Rings, Polynomials, Algebraic numbers, Arbitrary
precision integers and rationals (C++ wrappers over gmp) It also
provides data-structures and templated classes for the manipulation
of basic algebraic objects, such as vectors, matrices (dense, sparse,
structured), univariate polynomials (and therefore recursive
multivariate).

It contains different program modules and is fully compatible with
the LinBox linear algebra library and the KAAPI kernel for
Adaptative, Asynchronous Parallel and Interactive programming.

%package -n %lname
Summary:        C++ library for arithmetic and algebraic computations
Group:          System/Libraries

%description -n %lname
Givaro is a C++ library for arithmetic and algebraic computations.

Its main features are implementations of the basic arithmetic of many
mathematical entities: Primes fields, Extensions Fields, Finite
Fields, Finite Rings, Polynomials, Algebraic numbers, Arbitrary
precision integers and rationals. It also provides data-structures
and templated classes for the manipulation of basic algebraic
objects, such as vectors, matrices (dense, sparse, structured),
univariate polynomials (and therefore recursive multivariate).

%package devel
Summary:        Development files for Givaro, an algorithmic-algebraic computation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Givaro is a C++ library for arithmetic and algebraic computations.

Its main features are implementations of the basic arithmetic of many
mathematical entities: Primes fields, Extensions Fields, Finite
Fields, Finite Rings, Polynomials, Algebraic numbers, Arbitrary
precision integers and rationals.

This subpackage contains the include files and library links for   
developing against the Givaro library.

%package doc
Summary:        API documentation for the Givaro library, in HTML
Group:          Documentation/HTML
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description doc
Givaro is a C++ library for arithmetic and algebraic computations.

Its main features are implementations of the basic arithmetic of many
mathematical entities: Primes fields, Extensions Fields, Finite
Fields, Finite Rings, Polynomials, Algebraic numbers, Arbitrary
precision integers and rationals.

This subpackage contains the Doxygen-generated HTML documentation for
the Givaro API.

%prep
%setup -q
%patch -P 1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure --disable-static --enable-doc --with-docdir="%_docdir/%name" \
	--enable-silent-rules --disable-simd
chmod a+x givaro-config
make %{?_smp_mflags}

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la
%fdupes -s %buildroot/%_docdir/%name/givaro-html/

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libgivaro.so.*
%doc COPYRIGHT COPYING

%files devel
%defattr(-,root,root)
%_bindir/givaro-config
%_bindir/givaro-makefile
%_includedir/givaro-config.h
%_includedir/givaro/
%_includedir/gmp++/
%_includedir/recint/
%_libdir/libgivaro.so
%_libdir/pkgconfig/givaro.pc

%files doc
%defattr(-,root,root)
%dir %_docdir/%name/
%exclude %_docdir/%name/givaro-html/INSTALL
%_docdir/%name/givaro.html
%_docdir/%name/givaro-html/

%changelog
