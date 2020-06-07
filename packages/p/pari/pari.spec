#
# spec file for package pari
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


# See
# http://pari.math.u-bordeaux.fr/archives/pari-dev-1211/msg00006.html
# for details on the SO versioning.

Name:           pari
%define sover  6
%define lname   libpari-gmp-tls%sover
Version:        2.11.4
Release:        0
Summary:        Computer Algebra System for computations in Number Theory
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://pari.math.u-bordeaux.fr/
#Git-Clone:	https://pari.math.u-bordeaux.fr/git/pari.git
#Git-Web:	https://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi
Source:         https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%version.tar.gz
Source2:        https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%version.tar.gz.asc
Patch1:         pari-nodate.diff
BuildRequires:  fltk-devel
BuildRequires:  gmp-devel
BuildRequires:  libX11-devel
BuildRequires:  readline-devel
BuildRequires:  xorg-x11-proto-devel

%description
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%package gp
Summary:        Frontend to the PARI Computer Algebra System
Group:          Productivity/Scientific/Math

%description gp
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%package -n %lname
Summary:        Computer Algebra System library for fast computations in Number Theory
# This is used by the data packages to avoid having a too-old version of libpari:
Group:          System/Libraries
Provides:       libpari-gmp = %version

%description -n %lname
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%package devel
Summary:        Development files for the PARI CAS
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
PARI/GP is a computer algebra system designed for fast computations
in number theory (factorizations, algebraic number theory, elliptic
curves), but also contains a large number of other useful functions
to compute with mathematical entities such as matrices, polynomials,
power series, algebraic numbers etc., and a lot of transcendental
functions.

%prep
%autosetup -p1

%build
./Configure --prefix="%_prefix" \
	--bindir="%_bindir" --includedir="%_includedir" \
	--libdir="%_libdir" \
	--sysdatadir="%_libdir" --datadir="%_datadir/%name" \
	--mt=pthread
make %{?_smp_mflags} all \
	CFLAGS="%optflags -fno-strict-aliasing" \
	STRIP=true

%install
%make_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files gp
%_bindir/*
%_datadir/%name
%_libdir/%name.cfg
%_mandir/man*/*

%files -n %lname
%if 0%{?sle_version} <= 150000 && !0%{?is_opensuse}
%dir %_licensedir
%endif
%license COPYING
%_libdir/libpari-gmp-tls.so.%version
%_libdir/libpari-gmp-tls.so.%sover

%files devel
%doc examples/
%doc CHANGES CHANGES-* NEW README
%_includedir/pari/
%_libdir/libpari.so

%changelog
