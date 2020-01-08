#
# spec file for package mingw32-mpc
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


Name:           mingw32-mpc
Version:        1.0.2
Release:        0
Summary:        MPC multiple-precision complex library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.multiprecision.org/mpc/
Source:         ftp://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
#!BuildIgnore: post-build-checks
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-pkg-config
BuildRequires:  mingw32-gmp-devel
BuildRequires:  mingw32-mpfr-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw32_package_header_debug
BuildArch:      noarch

%description
MPC is a C library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding of the
result.  It is built upon and follows the same principles as MPFR.

%package -n mingw32-libmpc3
Summary:        MPC multiple-precision complex library
Group:          System/Libraries
Obsoletes:      mingw32-libmpc
Provides:       mingw32-libmpc

%description -n mingw32-libmpc3
MPC is a C library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding of the
result.  It is built upon and follows the same principles as MPFR.

%package devel
Summary:        MPC multiple-precision complex library development files
Group:          Development/Libraries/C and C++
Requires:       mingw32(lib:mpfr)

%description devel
MPC is a C library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding of the
result.  This package contains the library development files.

%_mingw32_debug_package

%prep
%setup -q -n mpc-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}
%{_mingw32_configure} \
	--enable-shared --disable-static

%{_mingw32_make} %{?_smp_mflags} || %{_mingw32_make}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files -n mingw32-libmpc3
%defattr(755,root,root,755)
%{_mingw32_bindir}/libmpc-3.dll

%files devel
%defattr(644,root,root,755)
%{_mingw32_libdir}/libmpc.dll.a
%{_mingw32_includedir}/mpc.h
%{_mingw32_infodir}
%exclude %{_mingw32_infodir}/dir*

%changelog
