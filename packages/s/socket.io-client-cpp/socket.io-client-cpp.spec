#
# spec file for package socket.io-client-cpp
#
# Copyright (c) 2023 SUSE LLC
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 1
%define libname libsioclient
Name:           socket.io-client-cpp
Version:        3.1.0
Release:        0
Summary:        Socket.IO C++ Client
License:        MIT
URL:            https://github.com/socketio/socket.io-client-cpp
Source:         https://github.com/socketio/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(RapidJSON)
BuildRequires:  cmake(websocketpp)
BuildRequires:  pkgconfig(asio)

%description
C++11 implementation of Socket.IO client

%package -n %{libname}%{sover}
Summary:        Socket.IO C++ Client

%description -n %{libname}%{sover}
C++11 implementation of Socket.IO client

%package devel
Summary:        Development files for libm2k
Requires:       %{libname}%{sover} = %{version}

%description devel
Development files for Socket.IO client

%prep
%autosetup -p1
chmod -x README.md LICENSE

%build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}%{sover}

%files -n %{libname}%{sover}
%license LICENSE
%doc API.md CHANGELOG.md README.md
%{_libdir}/%{libname}.so.*
%{_libdir}/%{libname}_tls.so.*

%files devel
%license LICENSE
%{_includedir}/sio_*.h
%{_libdir}/%{libname}*.so

%changelog
