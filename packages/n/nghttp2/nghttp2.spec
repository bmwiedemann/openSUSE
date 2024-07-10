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
%global flavor @BUILD_FLAVOR@%{nil}
Name:           nghttp2
Version:        1.62.1
Release:        0
Summary:        Implementation of Hypertext Transfer Protocol version 2 in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nghttp2.org/
Source0:        https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz
Source1:        https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz.asc
Source2:        nghttp2.keyring
Source3:        baselibs.conf
%if 0%{?suse_version} && 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl) >= 1.1.1
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
Provides:       %{name}-devel = %{version}

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
%autosetup -p1 -n nghttp2-%{version}

%build
%if 0%{?suse_version} && 0%{?suse_version} == 1500
export CC=/usr/bin/gcc-13
export CXX=/usr/bin/g++-13
%endif
%configure \
  --disable-static        \
  --disable-silent-rules  \
  --enable-app            \
  %{nil}
%make_build all

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print


# Do not ship this
rm -rf %{buildroot}%{_datadir}/doc/nghttp2

# None of applications using these man pages are built.
rm -rf %{buildroot}%{_mandir}/man1/* \
  doc/manual/html/.buildinfo

# https://build.opensuse.org/request/show/1212476
%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/fetch-ocsp-response
%endif


%check
%make_build check

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
