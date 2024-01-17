#
# spec file for package wslay
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


%define sover   0
%define c_lib   lib%{name}%{sover}
Name:           wslay
Version:        1.1.1
Release:        0
Summary:        WebSocket library in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/tatsuhiro-t/wslay
Source0:        https://github.com/tatsuhiro-t/wslay/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- NOTE: It can only be used on Leap >= 15.3 and Tumbleweed
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150300
Patch0:         0001-Fix-sphinx-3.3-errors.patch
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cunit-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(nettle) >= 2.4

%description
Wslay is a WebSocket library written in C. It implements the protocol version
13 described in RFC 6455. This library offers 2 levels of API: event-based API
and frame-based low-level API. For event-based API, it is suitable for
non-blocking reactor pattern style. You can set callbacks in various events.
For frame-based API, you can send WebSocket frame directly. Wslay only supports
data transfer part of WebSocket protocol and does not perform opening handshake
in HTTP.

Wslay supports:

Text/Binary messages.
Automatic ping reply.
Callback interface.
External event loop.

Wslay does not perform any I/O operations for its own. Instead, it offers
callbacks for them. This makes Wslay independent on any I/O frameworks, SSL,
sockets, etc. This makes Wslay portable across various platforms and the
application authors can choose freely I/O frameworks.

%package -n %{c_lib}
Summary:        WebSockets C Library
Group:          System/Libraries

%description -n %{c_lib}
Wslay is a WebSocket library written in C. It implements the protocol version
13 described in RFC 6455. This library offers 2 levels of API: event-based API
and frame-based low-level API. For event-based API, it is suitable for
non-blocking reactor pattern style. You can set callbacks in various events.
For frame-based API, you can send WebSocket frame directly. Wslay only supports
data transfer part of WebSocket protocol and does not perform opening handshake
in HTTP.

This package holds the shared C library.

%package devel
Summary:        Development files for the wslay WebSockets library
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description devel
Wslay is a WebSocket library written in C. It implements the protocol version
13 described in RFC 6455. This library offers 2 levels of API: event-based API
and frame-based low-level API. For event-based API, it is suitable for
non-blocking reactor pattern style. You can set callbacks in various events.
For frame-based API, you can send WebSocket frame directly. Wslay only supports
data transfer part of WebSocket protocol and does not perform opening handshake
in HTTP.

This package holds the development files.

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
export CFLAGS="%{optflags} -fpermissive"
export CXXFLAGS="%{optflags} -fpermissive"
autoreconf -fiv
%configure \
  --disable-silent-rules \
  --disable-static \
  --docdir=%{_docdir}
# documentation building fails with parallel build
%make_build -j1

%install
%make_install
# do not ship these
find %{buildroot} -type f -name "*.la" -delete -print
pushd %{buildroot}%{_bindir}/
  for i in * ; do mv $i wslay-$i ; done
popd

%check
%make_build check

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README README.rst
%{_bindir}/wslay*

%files -n %{c_lib}
%{_libdir}/libwslay.so.%{sover}*

%files devel
%{_mandir}/man3/*
%{_includedir}/wslay/
%{_libdir}/libwslay.so
%{_libdir}/pkgconfig/libwslay.pc

%changelog
