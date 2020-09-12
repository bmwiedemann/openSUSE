#
# spec file for package ulfius
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018-2020, Martin Hauke <mardnh@gmx.de>
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


%define _lto_cflags %{nil}
%define sover 2_6
Name:           ulfius
Version:        2.6.9
Release:        0
Summary:        Web Framework for REST Applications in C
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/babelouest/ulfius
Source:         https://github.com/babelouest/ulfius/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jansson) >= 2.4
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.51
BuildRequires:  pkgconfig(liborcania) >= 2.1.0
BuildRequires:  pkgconfig(libyder) >= 1.4.12

%description
The library is based on GNU libmicrohttpd for the backend web server, jansson
for the json manipulation library, and libcurl for the HTTP/SMTP client API.

It can be used to create web applications in C programs.

%package -n libulfius%{sover}
Summary:        Web Framework for REST Applications in C
Group:          System/Libraries

%description -n libulfius%{sover}
The library is based on GNU libmicrohttpd for the backend web server, jansson
for the json manipulation library, and libcurl for the HTTP/SMTP client API.

It can be used to create web applications in C programs.

%package devel
Summary:        Header files for ulfius
Group:          Development/Libraries/C and C++
Requires:       libcurl-devel
Requires:       libgnutls-devel
Requires:       libjansson-devel
Requires:       libmicrohttpd-devel
Requires:       libulfius%{sover} = %{version}
Requires:       orcania-devel
Requires:       yder-devel

%description devel
Development and header files for libulfius.

%package -n uwsc
Summary:        Ulfius WebSocket Client
Group:          Productivity/Networking/Web/Utilities

%description -n uwsc
A simple command-line websocket client program.

%prep
%setup -q

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    -DCMAKE_INSTALL_PREFIX:PATH=/
%make_build

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc/

%post   -n libulfius%{sover} -p /sbin/ldconfig
%postun -n libulfius%{sover} -p /sbin/ldconfig

%files -n libulfius%{sover}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/libulfius.so.*

%files devel
%doc API.md
%{_includedir}/ulfius.h
%{_includedir}/ulfius-cfg.h
%{_libdir}/libulfius.so
%{_libdir}/pkgconfig/libulfius.pc

%files -n uwsc
%{_bindir}/uwsc
%{_mandir}/man1/uwsc.1%{?ext_man}

%changelog
