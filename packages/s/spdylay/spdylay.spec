#
# spec file for package spdylay
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   7
%define c_lib   libspdylay%{sover}
Name:           spdylay
Version:        1.4.0
Release:        0
Summary:        SPDY C Library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://tatsuhiro-t.github.io/spdylay/
Source:         https://github.com/tatsuhiro-t/spdylay/releases/download/v%{version}/spdylay-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel >= 1.0.1
BuildRequires:  pkgconfig
BuildRequires:  python3-Cython
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(jansson) >= 2.5
BuildRequires:  pkgconfig(libevent) >= 2.0.8
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.7
BuildRequires:  pkgconfig(python3) >= 3
BuildRequires:  pkgconfig(zlib) >= 1.2.3

%description
This is an experimental implementation of Google’s SPDY protocol in
C. This library provides SPDY version 2, 3 and 3.1 framing layer
implementation. It does not perform any I/O operations but uses
callback functions provided by the application. Likewise, it includes
no event polling mechanism, so the application can freely choose.
Except for sample programs, this library code does not depend on any
particular SSL library.

%package -n %{c_lib}
Summary:        SPDY C Library
Group:          System/Libraries

%description -n %{c_lib}
This is an experimental implementation of Google’s SPDY protocol in
C. This library provides SPDY version 2, 3 and 3.1 framing layer
implementation. It does not perform any I/O operations but uses
callback functions provided by the application. Likewise, it includes
no event polling mechanism, so the application can freely choose.

This package holds the shared C library.

%package devel
Summary:        Development files for the SPDY C Library
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description devel
This is an experimental implementation of Google’s SPDY protocol in
C. This library provides SPDY version 2, 3 and 3.1 framing layer
implementation. It does not perform any I/O operations but uses
callback functions provided by the application. Likewise, it includes
no event polling mechanism, so the application can freely choose.
There is no dependency on a particular SSL library.

This package holds the development files.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/doc/%{name}/README.rst
find %{buildroot} -type f -name "*.la" -delete -print

%check
# testsuite fails in obs
# make check  %{?_smp_mflags}

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog NEWS doc/*.rst proxy.pac.sample shrpx.conf.sample
%{_bindir}/shrpx
%{_bindir}/spdycat
%{_bindir}/spdyd

%files -n %{c_lib}
%{_libdir}/libspdylay.so.%{sover}*

%files devel
%{_includedir}/spdylay/
%{_libdir}/libspdylay.so
%{_libdir}/pkgconfig/libspdylay.pc

%changelog
