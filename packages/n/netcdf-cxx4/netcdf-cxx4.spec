#
# spec file for package netcdf-cxx4
#
# Copyright (c) 2025 SUSE LLC
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


%define sover 1
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

ExcludeArch:    s390 s390x i586 %arm

%define libname(s:)   libnetcdf_c++4%{?-s:-%{-s*}}

Name:           netcdf-cxx4
Version:        4.3.1
%global _ver 4_3_1
Release:        0
Summary:        C++ library for the Unidata network Common Data Form version 4
License:        NetCDF
Group:          Productivity/Scientific/Other
URL:            https://www.unidata.ucar.edu/software/netcdf/
Source0:        https://downloads.unidata.ucar.edu/netcdf-cxx/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix build with netcdf 4.9.3 https://github.com/Unidata/netcdf-cxx4/pull/162
Patch1:         a43d6d4d415d407712c246faca553bd951730dc1.patch
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(netcdf)

%description
NetCDF4 (network Common Data Form) is a set of software libraries and
machine-independent data formats that support the creation, access, and sharing
of array-oriented scientific data.

This package provides the C++ API.

%package -n %{libname -s %{sover}}
Summary:        C++ library for the Unidata network Common Data Form version 4
Group:          System/Libraries
Provides:       libnetcdf%{sover}:%{_libdir}/libnetcdf_c++.so.%{sover}

%description -n %{libname -s %{sover}}
NetCDF4 (network Common Data Form) is a set of software libraries and
machine-independent data formats that support the creation, access, and sharing
of array-oriented scientific data.

This package provides the C++ API.

%package -n %{libname}-devel
Summary:        Development files for netcdf_c++
Group:          Development/Libraries/C and C++
Provides:       libnetcdf-devel:%{_libdir}/libnetcdf_c++.so
Requires:       %{libname -s %{sover}} = %{version}
Obsoletes:      %{name}-tools < %{version}
Provides:       %{name}-tools = %{version}

%description -n %{libname}-devel
This package contains the netcdf_c++4 header files and shared devel libs.

%prep
%setup -q -n %{name}-%{version}
%patch -P1 -p1

%build
%configure \
     --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libnetcdf_c++4.la

%check
make check || {
	cat cxx4/test-suite.log
	exit 1
}

%ldconfig_scriptlets -n %{libname -s %{sover}}

%files -n %{libname -s %{sover}}
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_libdir}/libnetcdf_c++4.so.%{sover}
%{_libdir}/libnetcdf_c++4.so.%{sover}.*

%files -n %{libname}-devel
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_includedir}/nc*.h
%{_includedir}/netcdf
%{_bindir}/ncxx4-config
%{_libdir}/pkgconfig/netcdf-cxx4.pc
%{_libdir}/libnetcdf_c++4.so
# Do not add plugins for now
%exclude %{_libdir}/libh5bzip2.*

%changelog
