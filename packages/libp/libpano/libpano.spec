#
# spec file for package libpano
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with java

Name:           libpano
Version:        2.9.21
Release:        0
Summary:        Panorama Tools Back-End Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://panotools.sourceforge.net/
Source:         https://sourceforge.net/projects/panotools/files/libpano13/libpano13-%{version}/libpano13-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with java}
BuildRequires:  java-devel
%endif
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)

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
%cmake \
  %{?with_java:-DSUPPORT_JAVA_PROGRAMS:Bool=ON} \
  %{nil}
%cmake_build

%install
%cmake_install
# No way to disable static library build, delete it
rm %{buildroot}/%{_libdir}/libpano*.a
# Install documentation manually
rm -Rf %{buildroot}/%{_prefix}/share/pano13/doc

%post -n libpano13-3 -p /sbin/ldconfig
%postun -n libpano13-3 -p /sbin/ldconfig

%files -n libpano13-3
%license COPYING
%{_libdir}/libpano13.so.*

%files utils
%doc doc/{Optimize,stitch}.txt doc/PT*.readme
%{_bindir}/*
%{_mandir}/man?/*.*

%files devel
%doc README AUTHORS
%{_includedir}/pano13
%{_libdir}/libpano13.so
%{_libdir}/pkgconfig/libpano13.pc

%changelog
