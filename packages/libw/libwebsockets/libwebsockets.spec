#
# spec file for package libwebsockets
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 22
Name:           libwebsockets
Version:        5.0.0
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
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(sqlite3)
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

%package evlib_ev
Summary:        Shared library for evlib_ev plugin
Group:          Development/Libraries/C and C++
Requires(pre):  %{name}%{sover} = %{version}

%description evlib_ev
This package contains the shared library for the evlib_ev plugin, which
lets applications drive libwebsockets from a libev event loop. Install it
only if an application asks for it.

%package evlib_event
Summary:        Shared library for evlib_event plugin
Group:          Development/Libraries/C and C++
Requires(pre):  %{name}%{sover} = %{version}

%description evlib_event
This package contains the shared library for the evlib_event plugin, which
lets applications drive libwebsockets from a libevent event loop. Install it
only if an application asks for it.

%package evlib_glib
Summary:        Shared library for evlib_glib plugin
Group:          Development/Libraries/C and C++
Requires(pre):  %{name}%{sover} = %{version}

%description evlib_glib
This package contains the shared library for the evlib_glib plugin, which
lets applications drive libwebsockets from a glib event loop. Install it
only if an application asks for it.

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
# This is upstream's LWS_WITH_DISTRO_RECOMMENDED feature set (the block at
# CMakeLists-implied-options.txt:93), spelled out option by option, minus
# LWS_WITH_LWSWS and LWS_WITH_PLUGINS_BUILTIN.
#
# It has to be spelled out rather than switched on with the one option,
# because that block assigns every option with a plain set(), which creates a
# normal variable that shadows the cache entry an -D on the command line would
# write. So with -DLWS_WITH_DISTRO_RECOMMENDED=ON, *nothing* it enables can be
# turned back off, and the two we need off both break the build:
#   - lwsws: upstream installs no unit file and no configuration for it, and
#     since 5.0.0 its install rule runs useradd for the system users lwsws and
#     lwsws-priv. Shipping it would need sysusers.d and a service file.
#     It also implies LWS_WITH_PLUGINS (implied-options:314).
#   - the bundled protocol plugins: demo protocols meant to be served by lwsws.
#     Each one calls require_lws_config(), which probes for features by
#     compiling against an *installed* libwebsockets.h, so it always fails in a
#     clean build root.
# Note this list does not track upstream automatically: check the block above
# against this one when updating, and decide per option rather than inheriting.
#
# DISABLE_WERROR because upstream adds -Werror unconditionally
# (CMakeLists.txt:1151). That turns any warning from a compiler newer than the
# one upstream tested into a build failure, which it already does here: the
# auth-dns zone signer ignores write() return values.
#
# LWS_WITH_HTTP3 defaults to ON in 5.0.0 (CMakeLists.txt:159-164, on whenever
# UDP is enabled), and CMakeLists.txt:281 then force-enables LWS_WITH_GNUTLS,
# because OpenSSL is not one of the backends it accepts for QUIC. GnuTLS does
# not sit alongside OpenSSL, it replaces it: the backends are an if/elseif
# chain in lib/tls/CMakeLists.txt. So just adding gnutls-devel would silently
# switch the TLS backend of every libwebsockets consumer in the distribution.
# Turning HTTP/3 off keeps OpenSSL and needs no extra dependency.
%cmake \
    -DLWS_WITH_HTTP2=ON \
    -DLWS_WITH_CGI=ON \
    -DLWS_WITH_HTTP_STREAM_COMPRESSION=ON \
    -DLWS_IPV6=ON \
    -DLWS_WITH_ZIP_FOPS=ON \
    -DLWS_WITH_SOCKS5=ON \
    -DLWS_WITH_RANGES=ON \
    -DLWS_WITH_ACME=ON \
    -DLWS_WITH_SYS_METRICS=ON \
    -DLWS_WITH_GLIB=ON \
    -DLWS_WITH_LIBUV=ON \
    -DLWS_WITH_LIBEV=ON \
    -DLWS_WITH_LIBEVENT=ON \
    -DLWS_WITH_EVLIB_PLUGINS=ON \
    -DLWS_WITHOUT_EXTENSIONS=OFF \
    -DLWS_ROLE_DBUS=ON \
    -DLWS_WITH_FTS=ON \
    -DLWS_WITH_THREADPOOL=ON \
    -DLWS_UNIX_SOCK=ON \
    -DLWS_WITH_HTTP_PROXY=ON \
    -DLWS_WITH_DISKCACHE=ON \
    -DLWS_WITH_LWSAC=ON \
    -DLWS_WITH_LEJP_CONF=ON \
    -DLWS_ROLE_RAW_PROXY=ON \
    -DLWS_WITH_GENCRYPTO=ON \
    -DLWS_WITH_CBOR=ON \
    -DLWS_WITH_COSE=ON \
    -DLWS_WITH_JOSE=ON \
    -DLWS_WITH_STRUCT_JSON=ON \
    -DLWS_WITH_STRUCT_SQLITE3=ON \
    -DLWS_WITH_SPAWN=ON \
    -DLWS_ROLE_MQTT=ON \
    -DLWS_WITH_SECURE_STREAMS=ON \
    -DLWS_WITH_SECURE_STREAMS_PROXY_API=ON \
    -DLWS_WITH_DIR=ON \
    -DLWS_WITH_SELFDNS=ON \
    -DLWS_WITHOUT_TESTAPPS=ON \
    -DLWS_WITHOUT_BUILTIN_GETIFADDRS=ON \
    -DLWS_WITHOUT_BUILTIN_SHA1=ON \
    -DLWS_WITH_STATIC=OFF \
    -DLWS_WITH_HTTP3=OFF \
    -DDISABLE_WERROR=ON
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

%files evlib_ev
%license LICENSE
%{_libdir}/libwebsockets-evlib_ev.so

%files evlib_event
%license LICENSE
%{_libdir}/libwebsockets-evlib_event.so

%files evlib_glib
%license LICENSE
%{_libdir}/libwebsockets-evlib_glib.so

%files devel
%license LICENSE
%doc README.* changelog
%{_includedir}/*
%{_libdir}/libwebsockets.so
%{_libdir}/pkgconfig/libwebsockets.pc
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%changelog
