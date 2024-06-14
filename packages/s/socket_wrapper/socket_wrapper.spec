#
# spec file for package socket_wrapper
#
# Copyright (c) 2024 SUSE LLC
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


############################# NOTE ##################################
#
# This is a special library. You are not able to link this library.
# Do NOT create library package or a devel package!
#
############################# NOTE ##################################

Name:           socket_wrapper
Version:        1.4.3
Release:        0
Summary:        A library passing all socket communications through Unix sockets
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://cwrap.org/
#
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        socket_wrapper.keyring
Source3:        %{name}-rpmlintrc
#
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  cmake(cmocka)

%description
socket_wrapper helps client/server software development to gain functional test
coverage. It can run several instances of a software stack on the same machine
and perform functional testing of network configurations locally.

To use it, set the following environment variables:

LD_PRELOAD=libsocket_wrapper.so
SOCKET_WRAPPER_DIR=/path/to/swrap_dir

%package -n libsocket_wrapper_noop0
Summary:        A library providing dummies for socket_wrapper

%description -n libsocket_wrapper_noop0
Applications with the need to call socket_wrapper_enabled() should link against
-lsocket_wrapper_noop in order to resolve the symbol at link time.

%package -n libsocket_wrapper_noop-devel
Summary:        Development headers for libsocket_wrapper_noop
Requires:       libsocket_wrapper_noop0 = %{version}

%description -n libsocket_wrapper_noop-devel
Development headers for applications with the need to call
socket_wrapper_enabled().

%prep
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON

%make_build VERBOSE=1

%install
%cmake_install

%check
%ctest

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libsocket_wrapper_noop0 -p /sbin/ldconfig

%postun -n libsocket_wrapper_noop0 -p /sbin/ldconfig

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libsocket_wrapper.so.*
%{_mandir}/man1/socket_wrapper.1*
%{_libdir}/libsocket_wrapper.so
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config-version.cmake
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc

%files -n libsocket_wrapper_noop0
%{_libdir}/libsocket_wrapper_noop.so.*

%files -n libsocket_wrapper_noop-devel
%{_includedir}/socket_wrapper.h
%{_libdir}/libsocket_wrapper_noop.so
%{_libdir}/cmake/socket_wrapper/socket_wrapper_noop-config*.cmake
%{_libdir}/pkgconfig/socket_wrapper_noop.pc

%changelog
