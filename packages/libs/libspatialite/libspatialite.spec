#
# spec file for package libspatialite
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


%define sover   7
%define libname %{name}%{sover}
Name:           libspatialite
Version:        4.3.0a
Release:        0
Summary:        Spatial SQLite
License:        MPL-1.1
Group:          Development/Libraries/C and C++
Url:            http://www.gaia-gis.it/spatialite/
Source:         http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM add define to use deprecated API
Patch1:         libspatialite-deprecated-proj-api.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libgeos-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3.7.3
BuildRequires:  pkgconfig(freexl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(zlib)

%description
The SpatiaLite extension enables SQLite to support spatial data too [aka
GEOMETRY], in a way conformant to OpenGis specifications.

%package -n %{libname}
Summary:        Spatial SQLite
Group:          System/Libraries

%description -n %{libname}
The SpatiaLite extension enables SQLite to support spatial data too [aka
GEOMETRY], in a way conformant to OpenGis specifications.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libspatialite.

%prep
%setup -q
%patch1 -p1

%build
%configure \
	--disable-static
make %{?_smp_mflags}

%check
# Don't fail build - two failures (reported to upstream)
make check %{?_smp_mflags} || :

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc README README.coverage
%{_libdir}/libspatialite.so.%{sover}*
%{_libdir}/mod_spatialite.so.%{sover}*

%files devel
%license COPYING
%doc README README.coverage
%{_includedir}/*
%{_libdir}/libspatialite.so
%{_libdir}/mod_spatialite.so
%{_libdir}/pkgconfig/spatialite.pc

%changelog
