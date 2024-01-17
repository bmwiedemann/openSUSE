#
# spec file for package mingw64-mpfr
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


Name:           mingw64-mpfr
Version:        3.1.4
Release:        0
Summary:        The MPFR multiple-precision floating-point library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://mpfr.org/
# upstream removed the file unfortunately
#Source:         http://mpfr.org/mpfr-current/mpfr-%{version}.tar.xz
Source:         mpfr-%{version}.tar.xz
#!BuildIgnore: post-build-checks
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-gmp-devel
BuildRequires:  xz
%_mingw64_package_header_debug
BuildArch:      noarch
# bugzilla.opensuse.org/1184052
#!BuildIgnore:  mingw64(libstdc++-6.dll)
#!BuildIgnore:  mingw64(libgcc_s_seh-1.dll)

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit
mantissa).

%package -n mingw64-libmpfr4
Summary:        MPFR multiple-precision floating-point computation shared library
Group:          System/Libraries
Obsoletes:      mingw64-libmpfr
Provides:       mingw64-libmpfr

%description -n mingw64-libmpfr4
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%package devel
Summary:        MPFR multiple-precision floating-point library development files
Group:          Development/Libraries/C and C++
Requires:       mingw64(lib:gmp)

%description devel
MPFR multiple-precision floating-point library development files.

%_mingw64_debug_package

%prep
%autosetup -p1 -n mpfr-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw64_cache}
%{_mingw64_configure} \
      --enable-shared \
      --disable-static \
      --enable-thread-safe

%{_mingw64_make} %{?_smp_mflags} || %{_mingw64_make}

%install
%make_install

%files -n mingw64-libmpfr4
%{_mingw64_bindir}/libmpfr-4.dll

%files devel
%{_mingw64_libdir}/libmpfr.dll.a
%{_mingw64_includedir}/mpfr.h
%{_mingw64_includedir}/mpf2mpfr.h
%{_mingw64_infodir}
%exclude %{_mingw64_infodir}/dir*
%{_mingw64_datadir}/doc/mpfr

%changelog
