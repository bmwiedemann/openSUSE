#
# spec file for package mingw32-mpfr
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mingw32-mpfr
Version:        3.1.2
Release:        0
Summary:        The MPFR multiple-precision floating-point library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://mpfr.org/
# upstream removed the file unfortunately
#Source:         http://mpfr.org/mpfr-current/mpfr-%{version}.tar.xz
Source:         mpfr-%{version}.tar.xz
#!BuildIgnore: post-build-checks
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-gmp-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw32_package_header_debug
BuildArch:      noarch

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit
mantissa).

%package -n mingw32-libmpfr4
Summary:        MPFR multiple-precision floating-point computation shared library
Group:          System/Libraries
Obsoletes:      mingw32-libmpfr
Provides:       mingw32-libmpfr

%description -n mingw32-libmpfr4
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%package devel
Summary:        MPFR multiple-precision floating-point library development files
Group:          Development/Libraries/C and C++
Requires:       mingw32(lib:gmp)

%description devel
MPFR multiple-precision floating-point library development files.

%_mingw32_debug_package

%prep
%setup -q -n mpfr-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}
%{_mingw32_configure} \
	--enable-shared --disable-static \
	--enable-thread-safe

%{_mingw32_make} %{?_smp_mflags} || %{_mingw32_make}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files -n mingw32-libmpfr4
%defattr(755,root,root,755)
%{_mingw32_bindir}/libmpfr-4.dll

%files devel
%defattr(644,root,root,755)
%{_mingw32_libdir}/libmpfr.dll.a
%{_mingw32_includedir}/mpfr.h
%{_mingw32_includedir}/mpf2mpfr.h
%{_mingw32_infodir}
%exclude %{_mingw32_infodir}/dir*
%{_mingw32_datadir}/doc/mpfr

%changelog
