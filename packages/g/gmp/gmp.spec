#
# spec file for package gmp
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gmp
Version:        6.2.0
Release:        0
Summary:        A library for calculating huge numbers
License:        GPL-3.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)
Group:          Development/Libraries/C and C++
URL:            https://gmplib.org/
Source0:        https://gmplib.org/download/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gmplib.org/download/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  pkgconfig

%description
GMP is a library for arbitrary precision arithmetic, operating on
signed integers, rational numbers, and floating-point numbers. There
is no practical limit to the precision except the ones implied by the
available memory in the machine GMP runs on.

%package -n libgmp10
Summary:        A library for calculating huge numbers
License:        LGPL-3.0-or-later OR GPL-2.0-or-later
Group:          System/Libraries

%description -n libgmp10
GMP is a library for arbitrary precision arithmetic, operating on
signed integers, rational numbers, and floating-point numbers.

%package -n libgmpxx4
Summary:        C++ bindings for the GNU MP Library
License:        LGPL-3.0-or-later OR GPL-2.0-or-later
Group:          System/Libraries
Requires:       libgmp10 >= %{version}

%description -n libgmpxx4
GMP is a library for arbitrary precision arithmetic, operating on
signed integers, rational numbers, and floating-point numbers.

This package contains C++ bindings for the GNU MP Library.

%package devel
Summary:        Include Files and Libraries for Development with the GNU MP Library
License:        GPL-3.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)
Group:          Development/Languages/C and C++
Requires:       libgmp10 = %{version}
Requires:       libgmpxx4 = %{version}
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description devel
These libraries are needed to develop programs which calculate with
huge numbers (integer and floating point).

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fexceptions"
%configure \
  --disable-static \
  --enable-cxx \
  --enable-fat
make %{?_smp_mflags}

%check
# do not disable "make check", FIX THE BUGS!
make %{?_smp_mflags} check

%install
%make_install
rm %{buildroot}%{_libdir}/libgmp.la
rm %{buildroot}%{_libdir}/libgmpxx.la

%post -n libgmp10 -p /sbin/ldconfig
%post -n libgmpxx4 -p /sbin/ldconfig
%postun -n libgmp10 -p /sbin/ldconfig
%postun -n libgmpxx4 -p /sbin/ldconfig
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files -n libgmp10
%license COPYING*
%{_libdir}/libgmp.so.10*

%files -n libgmpxx4
%{_libdir}/libgmpxx.so.4*

%files devel
%doc AUTHORS README NEWS
%doc demos
%{_infodir}/gmp.info*%{ext_info}
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so
%{_includedir}/gmp.h
%{_includedir}/gmpxx.h
%{_libdir}/pkgconfig/*.pc

%changelog
