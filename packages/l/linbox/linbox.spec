#
# spec file for package linbox
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


%bcond_without openblas

Name:           linbox
%define lname   liblinbox0
Version:        1.7.0+git106
Release:        0
Summary:        C++ library for computation with matrices over ints and finite fields
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://linalg.org/
#Source:         https://github.com/linbox-team/linbox/releases/download/v%version/linbox-%version.tar.gz
Source:         https://github.com/linbox-team/linbox/archive/a253f54da0b82c7e85fd8ad144fdb572469961e3.tar.gz
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake >= 1.8
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  iml-devel
BuildRequires:  libm4ri-devel
BuildRequires:  libm4rie-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel
BuildRequires:  ntl-devel
%if %{with openblas}
BuildRequires:  openblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  cblas-devel
%endif
BuildRequires:  pkgconfig(fflas-ffpack) >= 2.5.0

%description
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package -n %lname
Summary:        C++ library for computation with matrices over ints and finite fields
Group:          System/Libraries

%description -n %lname
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

%package devel
Summary:        Development files for LinBox, a library for computation over finite fields
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
LinBox is a C++ template library for exact, high-performance linear
algebra computation with dense, sparse, and structured matrices over
the integers and over finite fields.

This subpackage contains the include files and library links for
developing against the Givaro library.

%prep
%autosetup -p1 -n %name-a253f54da0b82c7e85fd8ad144fdb572469961e3

%build
autoreconf -fi
%configure --disable-static \
%ifarch %ix86
	--disable-sse --disable-sse2 \
%endif
	--disable-sse3 --disable-ssse3 --disable-sse41 --disable-sse42 \
	--disable-avx --disable-avx2 --disable-fma --disable-fma4 \
	--without-archnative
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/liblinbox.so.0*

%files devel
%_bindir/*-config
%_includedir/%name/
%_libdir/liblinbox.so
%_libdir/pkgconfig/*.pc
%_mandir/man1/*.1*
%license COPYING*

%changelog
