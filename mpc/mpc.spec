#
# spec file for package mpc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mpc
Version:        1.1.0
Release:        0
Summary:        MPC multiple-precision complex shared library
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            http://www.multiprecision.org/mpc/
Source0:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       mpfr-devel
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}

%description devel
MPC multiple-precision complex library development files.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_libdir}/libmpc.la

%post -n libmpc3 -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n libmpc3 -p /sbin/ldconfig

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -n libmpc3
%defattr(-,root,root)
%{_libdir}/libmpc.so.3*

%files devel
%defattr(-,root,root)
%doc AUTHORS NEWS COPYING.LESSER
%{_infodir}/mpc.info.gz
%{_libdir}/libmpc.a
%{_libdir}/libmpc.so
%{_includedir}/mpc.h

%changelog
