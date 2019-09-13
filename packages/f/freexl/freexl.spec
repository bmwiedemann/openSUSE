#
# spec file for package freexl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover   1
%define libname lib%{name}%{sover}
Name:           freexl
Version:        1.0.5
Release:        0
Summary:        Library to extract valid data from within an Excel
License:        MPL-1.1 OR GPL-2.0+ OR LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            https://www.gaia-gis.it/fossil/freexl/index
Source:         http://www.gaia-gis.it/gaia-sins/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
FreeXL is an open source library to extract valid data from within an Excel
(.xls) spreadsheet.

%package -n %{libname}
Summary:        Shared library for FreeXL
Group:          System/Libraries

%description -n %{libname}
FreeXL is an open source library to extract valid data from within an Excel
(.xls) spreadsheet.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel
Requires:       pkgconfig

%description devel
This package contains all necessary include files and libraries needed to
compile and develop applications that use libspatialite.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n lib%{name}1
%doc AUTHORS COPYING README
%{_libdir}/libfreexl.so.%{sover}*

%files devel
%doc AUTHORS COPYING README
%{_includedir}/freexl.h
%{_libdir}/libfreexl.so
%{_libdir}/pkgconfig/freexl.pc

%changelog
