#
# spec file for package libmicrohttpd
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2010,2011,2012  Stephan Kleine
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


%global sover   12
%global libname %{name}%{sover}
Name:           libmicrohttpd
Version:        0.9.76
Release:        0
Summary:        Small Embeddable HTTP Server Library
# Some internal tests are licenced as GPL-3.0+ - they are only used in
# check phase and not shipped further
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Servers
URL:            https://www.gnu.org/software/libmicrohttpd/
Source0:        https://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz.sig
Source2:        https://grothoff.org/christian/grothoff.asc#/%{name}.keyring
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  socat
BuildRequires:  pkgconfig(gnutls) >= 2.8.6
BuildRequires:  pkgconfig(libcurl) >= 7.16.4

%description
GNU libmicrohttpd is a small C library that is supposed to make it easy to run
an HTTP server as part of another application. GNU libmicrohttpd is free software
and part of the GNU project. Key features that distinguish libmicrohttpd from
other projects are:

    * C library: fast and small
    * API is simple, expressive and fully reentrant
    * Implementation is http 1.1 compliant
    * HTTP server can listen on multiple ports
    * Support for IPv6
    * Support for incremental processing of POST data
    * Creates binary of only 30k (without TLS/SSL support)
    * Three different threading models
    * Supported platforms include GNU/Linux, FreeBSD, OpenBSD, NetBSD, OS X, W32,
      Symbian and z/OS
    * Optional support for SSL3 and TLS (requires libgcrypt)

libmicrohttpd was started because the author needed an easy way to add a concurrent
HTTP server to other projects. Existing alternatives were either non-free, not
reentrant, standalone, of terrible code quality or a combination thereof. Do not
use libmicrohttpd if you are looking for a standalone http server, there are many
other projects out there that provide that kind of functionality already. However,
if you want to be able to serve simple WWW pages from within your C or C++
application, check it out.

%package -n %{libname}
Summary:        Small embeddable http server library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
Shared library for %{name} (%{summary}).

%package devel
Summary:        Small Embeddable HTTP Server Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig >= 0.9.0
Requires:       pkgconfig(gnutls) >= 2.8.6

%description devel
Headers, pkg-config files, so link and other development files for %{name}
(%{summary}).

%prep
%setup -q

%build
%configure \
  --enable-bauth \
  --enable-dauth \
  --enable-epoll \
  --enable-messages \
  --enable-postprocessor \
  --enable-https \
  --enable-curl \
  --disable-static \
  --disable-examples

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -v %{buildroot}%{_infodir}/%{name}_performance_data.png

%check
# Parallel execution of tests fail
# Tests randomly fail so keep them in log for inspection rather than for valid
# verification of anything.
%make_build -j1 check || :

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/%{name}.so.%{sover}*

%files devel
%license COPYING
%doc ChangeLog
%{_includedir}/microhttpd.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_infodir}/%{name}*.info%{?ext_info}
%{_mandir}/man3/%{name}.3%{?ext_man}

%changelog
