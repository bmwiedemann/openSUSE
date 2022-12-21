#
# spec file for package mpc
#
# Copyright (c) 2022 SUSE LLC
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


Name:           mpc
Version:        1.3.1
Release:        0
Summary:        multiple-precision complex shared library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.multiprecision.org/mpc/
Source0:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmp) >= 5.0.0
BuildRequires:  pkgconfig(mpfr) >= 4.1.0

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package -n libmpc3
Summary:        MPC multiple-precision complex shared library
Group:          Development/Libraries/C and C++

%description -n libmpc3
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package devel
Summary:        MPC multiple-precision complex library development files
Group:          Development/Libraries/C and C++
Requires:       libmpc3 = %{version}
Requires:       pkgconfig(gmp) >= 5.0.0
Requires:       pkgconfig(mpfr) >= 4.1.0
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}

%description devel
MPC multiple-precision complex library development files.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libmpc3 -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n libmpc3 -p /sbin/ldconfig

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -n libmpc3
%defattr(-,root,root)
%license COPYING.LESSER
%{_libdir}/libmpc.so.3*

%files devel
%defattr(-,root,root)
%license COPYING.LESSER
%doc AUTHORS NEWS
%{_infodir}/mpc.info%{?ext_info}
%{_libdir}/libmpc.a
%{_libdir}/libmpc.so
%{_includedir}/mpc.h

%changelog
