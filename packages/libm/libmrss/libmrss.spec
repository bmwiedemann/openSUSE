#
# spec file for package libmrss
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 0
Name:           libmrss
Version:        0.19.4
Release:        0
Summary:        RSS Parsing Library
License:        LGPL-2.1-only
URL:            https://github.com/bakulf/libmrss/
Source:         https://github.com/bakulf/libmrss/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(nxml)

%description
libmRSS is a C library for parsing, writing, and creating RSS (Rich Site
Summary, Really Simple Syndication, and RDF Site Summary) and ATOM files or
streams. The formats supported are: RSS 0.91, RSS 0.92, RSS 1.0, RSS 2.0, ATOM
0.3, and ATOM 1.0.

%package -n %{name}%{sover}
Summary:        RSS Parsing Library

%description -n %{name}%{sover}
libmRSS is a C library for parsing, writing, and creating RSS (Rich Site
Summary, Really Simple Syndication, and RDF Site Summary) and ATOM files or
streams. The formats supported are: RSS 0.91, RSS 0.92, RSS 1.0, RSS 2.0, ATOM
0.3, and ATOM 1.0.

This package contains the shared library.

%package devel
Summary:        Headers and development package for libmrss
Requires:       %{name}%{sover} = %{version}

%description devel
libmRSS is a C library for parsing, writing, and creating RSS (Rich Site
Summary, Really Simple Syndication, and RDF Site Summary) and ATOM files or
streams. The formats supported are: RSS 0.91, RSS 0.92, RSS 1.0, RSS 2.0, ATOM
0.3, and ATOM 1.0.

%prep
%autosetup -p1
touch NEWS

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build test

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/libmrss.so.%{sover}{,.*}

%files devel
%license COPYING
%{_libdir}/pkgconfig/mrss.pc
%{_libdir}/libmrss.so
%{_includedir}/mrss.h

%changelog
