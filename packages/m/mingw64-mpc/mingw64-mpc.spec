#
# spec file for package mingw64-mpc
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mingw64-mpc
Version:        1.0.2
Release:        0
Summary:        MPC multiple-precision complex library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.multiprecision.org/mpc/
Source:         ftp://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
#!BuildIgnore: post-build-checks
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-pkg-config
BuildRequires:  mingw64-gmp-devel
BuildRequires:  mingw64-mpfr-devel
%_mingw64_package_header_debug
BuildArch:      noarch
# bugzilla.opensuse.org/1184052
#!BuildIgnore:  mingw64(libstdc++-6.dll)
#!BuildIgnore:  mingw64(libgcc_s_seh-1.dll)

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package -n mingw64-libmpc3
Summary:        MPC multiple-precision complex library
Group:          System/Libraries
Obsoletes:      mingw64-libmpc
Provides:       mingw64-libmpc

%description -n mingw64-libmpc3
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package devel
Summary:        MPC multiple-precision complex library development files
Group:          Development/Libraries/C and C++
Requires:       mingw64(lib:mpfr)

%description devel
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. This
package contains the library development files.

%_mingw64_debug_package

%prep
%autosetup -p1 -n mpc-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw64_cache}
%{_mingw64_configure} \
	--enable-shared --disable-static

%{_mingw64_make} %{?_smp_mflags} || %{_mingw64_make}

%install
%make_install

%files -n mingw64-libmpc3
%{_mingw64_bindir}/libmpc-3.dll

%files devel
%{_mingw64_libdir}/libmpc.dll.a
%{_mingw64_includedir}/mpc.h
%{_mingw64_infodir}
%exclude %{_mingw64_infodir}/dir*

%changelog
