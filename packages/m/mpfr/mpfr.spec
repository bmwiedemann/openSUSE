#
# spec file for package mpfr
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


Name:           mpfr
Version:        4.1.1
Release:        0
Summary:        The GNU multiple-precision floating-point library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.mpfr.org/
Source0:        https://www.mpfr.org/mpfr-%{version}/mpfr-%{version}.tar.xz
Source1:        https://www.mpfr.org/mpfr-%{version}/mpfr-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit
mantissa).

%package -n libmpfr6
Summary:        The GNU multiple-precision floating-point shared library
Group:          Development/Libraries/C and C++

%description -n libmpfr6
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%package devel
Summary:        Development files for the GNU multiple-precision floating-point library
Group:          Development/Libraries/C and C++
Requires:       gmp-devel
Requires:       libmpfr6 = %{version}
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}

%description devel
Development files for the GNU multiple-precision floating-point library.

The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%prep
%setup -q

%build
%configure \
%ifarch %{sparc} hppa
	--disable-thread-safe \
%else
 	--enable-thread-safe \
%endif
	--enable-shared \
	--disable-static \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# installed via macro
rm %{buildroot}%{_docdir}/mpfr/COPYING*

%post -n libmpfr6 -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n libmpfr6 -p /sbin/ldconfig

%files -n libmpfr6
%license COPYING*
%{_libdir}/libmpfr.so.6*

%files devel
%license COPYING*
%doc %{_docdir}/mpfr
%{_infodir}/mpfr.info%{?ext_info}
%{_libdir}/libmpfr.so
%{_includedir}/mpf2mpfr.h
%{_includedir}/mpfr.h
%{_libdir}/pkgconfig/mpfr.pc

%changelog
