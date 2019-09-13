#
# spec file for package libopenraw
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libopenraw
Version:        0.1.3
Release:        0
Summary:        A library to decode digital camera RAW files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libopenraw.freedesktop.org/
Source0:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
Source1:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source99:       baselibs.conf

BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.21
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel >= 1.31.1
%endif

%description
libopenraw is a library that aim at decoding digital camera RAW files.

%package -n libopenraw1
Summary:        A library to decode digital camera RAW files
Group:          Development/Libraries/C and C++

%description -n libopenraw1
libopenraw is a library that aim at decoding digital camera RAW files.

%package -n gdk-pixbuf-loader-libopenraw
Summary:        A library to decode digital camera RAW files -- gdk-pixbuf loader
Group:          Development/Libraries/C and C++
Supplements:    packageand(libopenraw1:gdk-pixbuf)
%{gdk_pixbuf_loader_requires}

%description -n gdk-pixbuf-loader-libopenraw
libopenraw is a library that aim at decoding digital camera RAW files.

This package provides a libopenraw-based gdk-pixbuf loader.

%package -n libopenraw-devel
Summary:        A library to decode digital camera RAW files
Group:          Development/Libraries/C and C++
#include gdk-pixbuf/gdk-pixbuf.h
Requires:       gdk-pixbuf-devel
Requires:       libopenraw1 = %{version}

%description  -n libopenraw-devel
libopenraw is a library that aim at decoding digital camera RAW files.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --with-pic
make V=1 %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libopenraw1 -p /sbin/ldconfig
%postun -n libopenraw1 -p /sbin/ldconfig
%post -n gdk-pixbuf-loader-libopenraw
%{gdk_pixbuf_loader_post}

%postun -n gdk-pixbuf-loader-libopenraw
%{gdk_pixbuf_loader_postun}

%files -n libopenraw1
%license COPYING
%doc README TODO ChangeLog
%{_libdir}/*.so.*

%files -n gdk-pixbuf-loader-libopenraw
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libopenraw_pixbuf.so

%files -n libopenraw-devel
%{_libdir}/*.so
%dir %{_includedir}/libopenraw-0.1
%{_includedir}/libopenraw-0.1/*
%{_libdir}/pkgconfig/*.pc

%changelog
