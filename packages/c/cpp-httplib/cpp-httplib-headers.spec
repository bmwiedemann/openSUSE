#
# spec file for package cpp-httplib-headers
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


Name:           cpp-httplib-headers
Version:        0.11.4
Release:        0
Summary:        A C++11 header-only HTTP/HTTPS library
License:        MIT
URL:            https://github.com/yhirose/cpp-httplib
Source0:        cpp-httplib-%{version}.tar.gz
BuildRequires:  meson >= 0.47.0

%package devel
Summary:        A C++11 header-only HTTP/HTTPS library
Conflicts:      cpp-httplib-devel
Provides:       cpp-httplib-devel-static = %{version}
BuildArch:      noarch

%description
This is a multi-threaded HTTP library with blocking I/O. There is no
support for non-blocking mode.

%description devel
This is a multi-threaded HTTP library with blocking I/O. There is no
support for non-blocking mode.

It features built-in mappings, static file server, pre-routing and
post-routing handlers, and support for binding sockets to multiple
interfaces and any available port.

%prep
%setup -q -n cpp-httplib-%{version}
# For avoid c++ compiler check
sed -i "7s/.*/version: '%{version}',/" meson.build

%build
%meson -Dcpp-httplib_openssl=disabled -Dcpp-httplib_brotli=disabled \
       -Dcpp-httplib_zlib=disabled

%install
%meson_install

%files devel
%{_includedir}/httplib.h
%{_datadir}/pkgconfig/cpp-httplib.pc
%doc README.md
%license LICENSE

%changelog
