#
# spec file for package nghttp2
#
# Copyright (c) 2023 SUSE LLC
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


%global soname  libnghttp2
%global sover   14
%global soname_asio libnghttp2_asio
%global sover_asio 1
%global flavor @BUILD_FLAVOR@%{nil}
Name:           nghttp2
Version:        1.53.0
Release:        0
Summary:        Implementation of Hypertext Transfer Protocol version 2 in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nghttp2.org/
Source:         https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%ifnarch ppc %{arm}
BuildRequires:  pkgconfig(jemalloc)
%endif

%description
This is an implementation of Hypertext Transfer Protocol version 2.

The framing layer of HTTP/2 is implemented as a form of reusable C library.
On top of that, we have implemented HTTP/2 client, server and proxy. We
have also developed load test and benchmarking tool for HTTP/2.

HPACK encoder and decoder are available as public API.

%package -n %{soname}-%{sover}
Summary:        Shared library for nghttp2
Group:          System/Libraries

%description -n %{soname}-%{sover}
Shared C libraries for implementation of Hypertext Transfer Protocol
version 2.

%package -n python3-nghttp2
Summary:        Python3 bindings for nghttp2
Group:          Development/Libraries/Python

%description -n python3-nghttp2
Python bindings for implementation of Hypertext Transfer Protocol version
2.

%package -n %{soname}-devel
Summary:        Development files for nghttp2
Group:          Development/Languages/C and C++
Requires:       %{soname}-%{sover} = %{version}
Provides:       %{name}-devel

%description -n %{soname}-devel
Development files for usage with libnghttp2, which implements
Hypertext Transfer Protocol version 2.

%package doc
Summary:        Documentation for nghttp2
Group:          Documentation/HTML

%description doc
Documentation for nghttp2, which includes a shared C library,
HTTP/2 client, server and proxy.

%prep
%setup -q -n nghttp2-%{version}
# fix python shebang
sed -i -e 's:#!%{_bindir}/env python:#!%{_bindir}/python3:g' script/fetch-ocsp-response

%build
autoreconf -fiv
%configure \
  --disable-static        \
  --disable-silent-rules  \
  --enable-app            \
  %{nil}
%make_build all

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# Do not ship theis
rm -rf %{buildroot}%{_datadir}/doc/nghttp2

# None of applications using these man pages are built.
rm -rf %{buildroot}%{_mandir}/man1/* \
  doc/manual/html/.buildinfo

%check
# One test fails if python-sphinx is not present
%make_build check ||:

%ldconfig_scriptlets -n %{soname}-%{sover}

%files
%{_bindir}/deflatehd
%{_bindir}/inflatehd
%{_bindir}/h2load
%{_bindir}/nghttp
%{_bindir}/nghttpd
%{_bindir}/nghttpx
%{_datadir}/%{name}/

%files -n %{soname}-%{sover}
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{soname}-devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/%{name}*.h
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc

%changelog
