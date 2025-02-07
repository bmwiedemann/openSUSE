#
# spec file for package cpp-httplib
#
# Copyright (c) 2025 SUSE LLC
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


%define         sover 0.18
%define         libver 0_18
Name:           cpp-httplib
Version:        0.18.6
Release:        0
Summary:        A C++11 HTTP/HTTPS server and client library
License:        MIT
URL:            https://github.com/yhirose/cpp-httplib
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.pc
# https://github.com/yhirose/cpp-httplib/issues/2042
Patch0:         cpp-httplib-test-issue2004-online.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl) >= 3.0.0

%package -n lib%{name}%{libver}
Summary:        A C++11 HTTP/HTTPS library

%package devel
Summary:        A C++11 HTTP/HTTPS library
Requires:       lib%{name}%{libver} = %{version}

%description
This is a multi-threaded HTTP library with blocking I/O. There is no
support for non-blocking mode.

%description -n lib%{name}%{libver}
This is a multi-threaded HTTP library with blocking I/O. There is no
support for non-blocking mode.

%description devel
This is a multi-threaded HTTP library with blocking I/O. There is no
support for non-blocking mode.

It features built-in mappings, static file server, pre-routing and
post-routing handlers, and support for binding sockets to multiple
interfaces and any available port.

%prep
%autosetup -p1
chmod -x example/uploader.sh

# fix dynamically the version in the pkgconfig file
sed -i 's|Version: 0.0.0|Version: %{version}|g' %{SOURCE1}

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DHTTPLIB_REQUIRE_OPENSSL=ON \
  -DHTTPLIB_REQUIRE_ZLIB=ON \
  -DHTTPLIB_REQUIRE_BROTLI=ON \
  -DHTTPLIB_COMPILE=ON \
  -DHTTPLIB_TEST=ON
%cmake_build

%install
%cmake_install
install -Dm0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

#remove files
rm -r %{buildroot}%{_datadir}/{licenses/httplib,doc/packages/cpp-httplib}

%check
# OBS and chroot build environments does not provide internet
# connectivity, skip online tests to avoid failures
%ctest --parallel 1 --exclude-regex '(_Online$)'

%ldconfig_scriptlets -n lib%{name}%{libver}

%files -n lib%{name}%{libver}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc README.md example
%{_libdir}/lib%{name}.so
%{_includedir}/httplib.h
%{_libdir}/cmake/httplib
%{_libdir}/pkgconfig/%{name}.pc

%changelog
