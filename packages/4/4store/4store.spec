#
# spec file for package 4store
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


%define major   0
Name:           4store
Version:        1.1.6
Release:        0
Summary:        RDF Storage and SPARQL Query Engine
License:        GPL-3.0-or-later
URL:            https://4store.github.io
Source:         https://github.com/4store/4store/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         invalid-define.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(rasqal)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
4store was designed by Steve Harris and developed at Garlik to underpin
their Semantic Web applications. It has been providing the base platform
for around 3 years. At times holding and running queries over databases of
15GT, supporting a Web application used by thousands of people.

%package -n lib4store%{major}
Summary:        4store RDF Storage Library

%description -n lib4store%{major}
This package provides 4store RDF storage shared library.

%package -n lib4store-devel
Summary:        4store RDF Storage Development Files
Requires:       lib4store%{major} = %{version}

%description -n lib4store-devel
This package provides 4store RDF storage development files.

%prep
%setup -q
%patch0 -p1

%build
# configure script is not shipped since v1.1.6, generation is required
echo %{version} > .version && ./autogen.sh
# needed for building with gcc10
export CFLAGS="%{optflags} -fcommon"
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
sed -i 's:%{_bindir}/env bash:/bin/bash:' %{buildroot}%{_bindir}/4s-*
sed -i 's:%{_bindir}/env perl:%{_bindir}/perl:' %{buildroot}%{_bindir}/4s-*

%post -n lib4store%{major} -p /sbin/ldconfig
%postun -n lib4store%{major} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/4s-*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files -n lib4store%{major}
%{_libdir}/lib4store.so.*

%files -n lib4store-devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/%{name}
%{_libdir}/lib4store.so
%{_libdir}/pkgconfig/*

%changelog
