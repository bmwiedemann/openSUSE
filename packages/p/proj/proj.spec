#
# spec file for package proj
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


%define gridver 1.8
%define sover   15
%define libname lib%{name}%{sover}
Name:           proj
Version:        6.2.0
Release:        0
Summary:        Cartographic projection software
License:        MIT
Group:          Productivity/Scientific/Other
URL:            https://proj.org/
Source0:        http://download.osgeo.org/proj/%{name}-%{version}.tar.gz
Source1:        http://download.osgeo.org/proj/%{name}-datumgrid-%{gridver}.zip
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  sqlite3
BuildRequires:  unzip
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
Provides:       libproj = %{version}

%description
This package offers the commandline tools for performing respective
forward and inverse transformation of cartographic data to or from cartesian
data with a wide range of selectable projection functions.

%package -n %{libname}
Summary:        Cartographic projection software
Group:          Development/Libraries/C and C++

%description -n %{libname}
This package the library for performing respective
forward and inverse transformation of cartographic data to or from cartesian
data with a wide range of selectable projection functions.

%package devel
Summary:        Development files for PROJ
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       libproj-devel = %{version}
Obsoletes:      libproj-devel < %{version}

%description devel
This package contains libproj and the appropriate header files and man pages.

%prep
%setup -q
cd data
unzip -o %{SOURCE1}

%build
%configure \
  --with-external-gtest \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# Tests dont work on i586 and noone cares
%ifnarch %{ix86}
make %{?_smp_mflags} check
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc NEWS AUTHORS README ChangeLog
%defattr(0755,root,root)
%{_bindir}/cs2cs
%{_bindir}/cct
%{_bindir}/gie
%{_bindir}/geod
%{_bindir}/invgeod
%{_bindir}/invproj
%{_bindir}/proj
%{_bindir}/projinfo
%defattr(0644,root,root)
%{_mandir}/man1/cs2cs.1%{?ext_man}
%{_mandir}/man1/geod.1%{?ext_man}
%{_mandir}/man1/proj.1%{?ext_man}
%{_mandir}/man1/cct.1%{?ext_man}
%{_mandir}/man1/gie.1%{?ext_man}
%{_mandir}/man1/projinfo.1%{?ext_man}
%{_datadir}/proj/

%files -n %{libname}
%license COPYING
%{_libdir}/libproj.so.%{sover}*

%files devel
%{_includedir}/*.h
%{_includedir}/proj
%{_includedir}/proj_json_streaming_writer.hpp
%{_libdir}/libproj.so
%{_libdir}/pkgconfig/proj.pc
%{_mandir}/man3/geodesic.3%{?ext_man}
%{_mandir}/man3/pj_init.3%{?ext_man}

%changelog
