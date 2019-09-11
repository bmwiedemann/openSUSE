#
# spec file for package libwebsockets
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


%define sover 13
Name:           libwebsockets
Version:        3.0.0
Release:        0
Summary:        A WebSockets library written in C
# base64-decode.c and ssl-http2.c is under MIT license with FPC exception.
# sha1-hollerbach is under BSD
# Test suite is licensed as Public domain (CC-zero)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libwebsockets.org
Source:         https://github.com/warmcat/libwebsockets/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-norpmtools.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
Libwebsockets covers some features for people making embedded
HTTP/WebSocket servers or clients.

%package -n %{name}%{sover}
Summary:        A WebSockets library written in C
Group:          System/Libraries

%description -n %{name}%{sover}
Libwebsockets covers some features for people making embedded
HTTP/WebSocket servers or clients.

* HTTP(S) serving and client operation
* WS(S) serving and client operation
* HTTP(S) APIs for file transfer and upload
* HTTP POST form handling (including multipart)
* Cookie-based sessions
* Account management (including registration, email verification,
  lost password, etc.)
* SSL PFS support

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the WebSockets library.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
    -DWITHOUT_TESTAPPS=1 \
    -DLWS_USE_LIBEV=OFF \
    -DLWS_WITHOUT_BUILTIN_GETIFADDRS=ON \
    -DLWS_USE_BUNDLED_ZLIB=OFF \
    -DLWS_WITHOUT_BUILTIN_SHA1=ON \
    -DLWS_WITH_STATIC=OFF \
    -DLWS_WITHOUT_TESTAPPS=ON
make %{?_smp_mflags}

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/pkgconfig/libwebsockets_static.pc
rm -rf %{buildroot}%{_datadir}/libwebsockets-test-server/

%post -n libwebsockets%{sover} -p /sbin/ldconfig
%postun -n libwebsockets%{sover} -p /sbin/ldconfig

%files -n libwebsockets%{sover}
%license LICENSE
%{_libdir}/libwebsockets.so.%{sover}

%files devel
%doc README.* changelog
%{_includedir}/*
%{_libdir}/libwebsockets.so
%{_libdir}/pkgconfig/libwebsockets.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/Libwebsockets*.cmake

%changelog
