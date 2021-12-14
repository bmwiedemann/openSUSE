#
# spec file for package fflas-ffpack
#
# Copyright (c) 2021 SUSE LLC
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

Name:           fflas-ffpack
%define lname	libfflas0
Version:        2.5.0
Release:        0
Summary:        Finite Field Linear Algebra Subroutines
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://linbox-team.github.io/fflas-ffpack/

#Git-Clone:	https://github.com/linbox-team/fflas-ffpack
Source:         https://github.com/linbox-team/fflas-ffpack/releases/download/v%version/fflas-ffpack-%version.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 3.1.1
BuildRequires:  libtool >= 2.2
%if %{with openblas}
BuildRequires:  openblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  cblas-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(givaro) >= 4.1.2

%description
The FFLAS-FFPACK library provides functionalities for dense linear
algebra over word size prime finite field.

%package devel
Summary:        Development files for FFLAS-FFPACK
Group:          Development/Libraries/C and C++

%description devel
The FFLAS-FFPACK library provides functionalities for dense linear
algebra over word size prime finite field.

This subpackage contains the include files for
developing against the fflas-ffpack library.

%package doc
Summary:        API documentation for FFLAS-FFPACK
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The FFLAS-FFPACK library provides functionalities for dense linear
algebra over word size prime finite field.

This subpackage contains the Doxygen-generated HTML documentation for
the FFLAS-FFPACK API.

%prep
%autosetup -p1

#Do not compile in DATE and TIME
sed '/HTML_TIMESTAMP/s/YES/NO/' -i doc/Doxyfile

%build
# tarball strangely created; wants to rerun aclocal-1.15.
autoreconf -fi

trap "cat config.log; exit 1" ERR
%configure \
	--with-blas-cflags=" " \
%if %{with openblas}
	--with-blas-libs="-lopenblas" \
%else
	--with-blas-libs="-lcblas -lblas" \
%endif
	--enable-doc --with-docdir="%_docdir/%name" \
	--disable-simd --without-archnative
trap "" ERR
%make_build

%install
%make_install
rm -f "%buildroot/%_docdir/%name/fflas-ffpack-html/INSTALL"
perl -i -lpe 's{^#!/usr/bin/env bash$}{#!/bin/bash}g' %buildroot/%_bindir/*-config
%fdupes %buildroot/%_prefix

%files devel
%doc ChangeLog
%license COPYING.LESSER
%_bindir/fflas-ffpack-config
%_includedir/fflas-ffpack/
%_libdir/pkgconfig/ff*.pc

%files doc
%_docdir/%name/

%changelog
