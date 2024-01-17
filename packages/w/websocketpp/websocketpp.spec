#
# spec file for package websocketpp
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


Name:           websocketpp
Version:        0.8.2
Release:        0
Summary:        C++ WebSocket Protocol Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.zaphoyd.com/websocketpp
Source0:        https://github.com/zaphoyd/websocketpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        websocketpp.pc
# PATCH-FIX-UPSTREAM - https://github.com/zaphoyd/websocketpp/pull/888
Patch0:         Update-websocketpp-configVersion.cmake.patch
BuildRequires:  cmake >= 2.6
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildArch:      noarch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
WebSocket++ is a header-only C++ library
that implements RFC6455, the WebSocket protocol. It allows integrating
WebSocket client and server functionality into C++ programs. It uses
interchangeable network transport modules including one based on C++
iostreams and one based on Boost Asio.

%package devel
Summary:        Development files for websocketpp, a C++ WebSocket Protocol Library
Group:          Development/Libraries/C and C++

%description devel
WebSocket++ is a header-only C++ library
that implements RFC6455, the WebSocket protocol. It allows integrating
WebSocket client and server functionality into C++ programs. It uses
interchangeable network transport modules including one based on C++
iostreams and one based on Boost Asio.

%prep
%setup -q
%patch0 -p1

%build
%if 0%{?suse_version} >= 1310
%cmake
%else
mkdir build
pushd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON
%endif
make %{?_smp_mflags}

%install
%if 0%{?suse_version} >= 1310
%cmake_install
%else
pushd build
%make_install
%endif
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pkgconfig/websocketpp.pc

%files devel
%license COPYING
%doc changelog.md readme.md roadmap.md
%{_includedir}/websocketpp
%{_prefix}/lib/cmake
%{_prefix}/lib/cmake/websocketpp
%{_datadir}/pkgconfig/websocketpp.pc

%changelog
