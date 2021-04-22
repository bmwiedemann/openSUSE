#
# spec file for package libpano
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libpano
Version:        2.9.20
Release:        0
Summary:        Panorama Tools Back-End Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://panotools.sourceforge.net/
Source:         https://sourceforge.net/projects/panotools/files/libpano13/libpano13-%{version}/libpano13-%{version}.tar.gz
BuildRequires:  java-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
Library and utilities for working with panoramas.

%package -n libpano13-3
Summary:        Panorama Tools Back-End Library
Group:          Development/Libraries/C and C++

%description -n libpano13-3
Library and utilities for working with panoramas.

%package utils
Summary:        Panorama Tools Utilities
Group:          Productivity/Graphics/Other

%description utils
Utilities for working with panoramas.

%package devel
Summary:        Panorama Tools Back-End Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libpano13-3 = %{version}
Recommends:     %{name}-utils

%description devel
Development files for library for working with panoramas.

%prep
%setup -q -n libpano13-%{version}

%build
autoreconf -fi
%configure \
  --with-java=%{java_home}
%make_build

%install
%make_install
#Axe Libs.private from .pc files, which do not behave as expected
sed -i -e '/^Libs.private/d' %{buildroot}%{_libdir}/pkgconfig/libpano13.pc
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libpano13-3 -p /sbin/ldconfig
%postun -n libpano13-3 -p /sbin/ldconfig

%files -n libpano13-3
%license COPYING
%{_libdir}/libpano13.so.*

%files utils
%doc doc/{Optimize,stitch}.txt tools/README.PTmender
%{_bindir}/*
%{_mandir}/man?/*.*

%files devel
%doc README AUTHORS ChangeLog
%{_includedir}/pano13
%{_libdir}/libpano13.so
%{_libdir}/pkgconfig/libpano13.pc

%changelog
