#
# spec file for package libwebsockets
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 19
Name:           libwebsockets
Version:        4.3.5
Release:        0
Summary:        A WebSockets library written in C
# base64-decode.c and ssl-http2.c is under MIT license with FPC exception.
# sha1-hollerbach is under BSD
# Test suite is licensed as Public domain (CC-zero)
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://libwebsockets.org
Source:         https://github.com/warmcat/libwebsockets/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(zlib)

%description
Libwebsockets covers some features for people making embedded
HTTP/WebSocket servers or clients.

%package -n %{name}%{sover}
Summary:        A WebSockets library written in C
Group:          Development/Libraries/C and C++
Requires:       %{name}-evlib_uv = %{version}

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

%package evlib_uv
Summary:        Shared library for evlib_uv plugin
Group:          Development/Libraries/C and C++
Requires(pre):  %{name}%{sover} = %{version}
Provides:       %{name}-evlib-uv = %{version}
Obsoletes:      %{name}-evlib-uv < %{version}

%description evlib_uv
This package contains the shared library for evlib_uv plugin.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the WebSockets library.

%prep
%autosetup -p1

%build
%cmake \
    -DLWS_WITHOUT_TESTAPPS=ON \
    -DLWS_WITHOUT_BUILTIN_GETIFADDRS=ON \
    -DLWS_WITHOUT_BUILTIN_SHA1=ON \
    -DLWS_WITH_STATIC=OFF \
    -DLWS_WITHOUT_TESTAPPS=ON \
    -DLWS_WITH_LIBUV=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/pkgconfig/libwebsockets_static.pc

%check
%ctest

%ldconfig_scriptlets -n libwebsockets%{sover}

%files -n libwebsockets%{sover}
%license LICENSE
%{_libdir}/libwebsockets.so.%{sover}

%files evlib_uv
%license LICENSE
%{_libdir}/libwebsockets-evlib_uv.so

%files devel
%license LICENSE
%doc README.* changelog
%{_includedir}/*
%{_libdir}/libwebsockets.so
%{_libdir}/pkgconfig/libwebsockets.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%changelog
