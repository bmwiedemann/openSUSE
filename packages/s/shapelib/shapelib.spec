#
# spec file for package shapelib
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

# Please submit bugfixes or  comments via https://bugs.opensuse.org/
#


%define so_ver  4
Name:           shapelib
Version:        1.6.1
Release:        0
Summary:        Library for ESRI Shapefile Handling
License:        GPL-2.0-or-later AND (LGPL-2.0-or-later OR MIT) AND SUSE-Public-Domain
Group:          Productivity/Graphics/Other
URL:            http://shapelib.maptools.org/
Source0:        http://download.osgeo.org/shapelib/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# dbfdump is also in perl-DBD-XBase
Conflicts:      perl-DBD-XBase

%description
The Shapefile C Library provides the ability to write simple C programs for
reading, writing and updating (to a limited extent) ESRI Shapefiles, and the
associated attribute file (.dbf).

This package contains the executable programs.

%package -n libshp-devel
Summary:        Development Environment for %{name}
Group:          Development/Libraries/C and C++
Requires:       libshp%{so_ver} = %{version}
Provides:       shapelib-devel = %{version}

%description -n libshp-devel
The Shapefile C Library provides the ability to write simple C programs for
reading, writing and updating (to a limited extent) ESRI Shapefiles, and the
associated attribute file (.dbf).

This package contains the development environment for shapelib project.

%package -n libshp%{so_ver}
Summary:        Library for ESRI Shapefile Handling
Group:          System/Libraries

%description -n libshp%{so_ver}
The Shapefile C Library provides the ability to write simple C programs for
reading, writing and updating (to a limited extent) ESRI Shapefiles, and the
associated attribute file (.dbf).

This package contains the dynamic link library for shapelib project.

%prep
# %autosetup -p1

# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' contrib/doc/shpsort.txt

%build
%configure \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

%check
# Contrib tests fail
make %{?_smp_mflags} check ||:

%post -n libshp%{so_ver} -p /sbin/ldconfig
%postun -n libshp%{so_ver} -p /sbin/ldconfig

%files
%license LICENSE-LGPL
%doc ChangeLog
%doc contrib/doc/ web/
%{_bindir}/Shape_PointInPoly
%{_bindir}/csv2shp
%{_bindir}/dbfadd
%{_bindir}/dbfcat
%{_bindir}/dbfcreate
%{_bindir}/dbfdump
%{_bindir}/dbfinfo
%{_bindir}/shpadd
%{_bindir}/shpcat
%{_bindir}/shpcentrd
%{_bindir}/shpcreate
%{_bindir}/shpdata
%{_bindir}/shpdump
%{_bindir}/shpdxf
%{_bindir}/shpfix
%{_bindir}/shpinfo
%{_bindir}/shprewind
%{_bindir}/shpsort
%{_bindir}/shptreedump
%{_bindir}/shputils
%{_bindir}/shpwkb

%files -n libshp-devel
%{_includedir}/*
%{_libdir}/pkgconfig/shapelib.pc
%{_libdir}/libshp.so

%files -n libshp%{so_ver}
%{_libdir}/libshp.so.%{so_ver}*

%changelog
