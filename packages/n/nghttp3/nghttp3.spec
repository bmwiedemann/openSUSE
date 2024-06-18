#
# spec file for package nghttp3
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


%global soname  libnghttp3
%global sover   9
Name:           nghttp3
Version:        1.4.0
Release:        0
Summary:        Implementation of Hypertext Transfer Protocol version 3 in C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nghttp2.org/nghttp3/
Source0:        https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz
Source1:        https://github.com/ngtcp2/nghttp3/releases/download/v%{version}/nghttp3-%{version}.tar.xz.asc
Source2:        nghttp3.keyring
Source3:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cunit)

%description
nghttp3 is an implementation of RFC 9114 HTTP/3 mapping over QUIC and RFC 9204 QPACK in C.

It does not depend on any particular QUIC transport implementation.

This library implements RFC 9114 HTTP/3. It does not support server push.

The following extensions have been implemented:

Extensible Prioritization Scheme for HTTP
Bootstrapping WebSockets with HTTP/3

%package -n %{soname}-%{sover}
Summary:        Shared library for nghttp3
Group:          System/Libraries

%description -n %{soname}-%{sover}
Shared C libraries for implementation of Hypertext Transfer Protocol
version 3.

%package -n %{soname}-devel
Summary:        Development files for nghttp3
Group:          Development/Languages/C and C++
Requires:       %{soname}-%{sover} = %{version}
Provides:       %{name}-devel = %{version}

%description -n %{soname}-devel
Development files for usage with libnghttp3, which implements
Hypertext Transfer Protocol version 3.

%prep
%setup -q -n nghttp3-%{version}

%build
%configure \
  --disable-static        \
  --disable-silent-rules  \
  --enable-lib-only       \
  --with-cunit            \
  %{nil}
%make_build all

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# Do not ship this
rm -rf %{buildroot}%{_datadir}/doc/nghttp3

# None of applications using these man pages are built.
rm -rf %{buildroot}%{_mandir}/man1/* \
  doc/manual/html/.buildinfo

%check
%make_build check

%ldconfig_scriptlets -n %{soname}-%{sover}

%files -n %{soname}-%{sover}
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{soname}-devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc

%changelog
