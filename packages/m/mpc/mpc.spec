#
# spec file for package mpc
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 3
Name:           mpc
Version:        1.4.1
Release:        0
Summary:        Multiple-precision complex shared library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.multiprecision.org/mpc/
Source0:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmp) >= 5.0.0
BuildRequires:  pkgconfig(mpfr) >= 4.1.0

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package -n libmpc%{sover}
Summary:        MPC multiple-precision complex shared library
Group:          Development/Libraries/C and C++

%description -n libmpc%{sover}
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package devel
Summary:        MPC multiple-precision complex library development files
Group:          Development/Libraries/C and C++
Requires:       libmpc%{sover} = %{version}

%description devel
MPC multiple-precision complex library development files.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure \
	--disable-static \
	%{nil}
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libmpc%{sover}

%files -n libmpc%{sover}
%license COPYING.LESSER
%{_libdir}/libmpc.so.%{sover}{,.*}

%files devel
%license COPYING.LESSER
%doc AUTHORS NEWS
%{_infodir}/mpc.info%{?ext_info}
%{_libdir}/libmpc.so
%{_includedir}/mpc.h
%{_libdir}/pkgconfig/mpc.pc

%changelog
