#
# spec file for package double-conversion
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


%define lib_ver 3
Name:           double-conversion
Version:        3.1.5
Release:        0
Summary:        Binary-decimal and decimal-binary routines for IEEE doubles
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/google/double-conversion
Source0:        https://github.com/google/double-conversion/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python

%description
Double-conversion provides binary-decimal and decimal-binary routines
for IEEE double-precision floating point numbers. The library
consists of conversion routines that have been extracted from the V8
JavaScript engine.

%package     -n lib%{name}%{lib_ver}
Summary:        Binary-decimal and decimal-binary routines for IEEE doubles
Group:          System/Libraries

%description -n lib%{name}%{lib_ver}
Double-conversion provides binary-decimal and decimal-binary routines
for IEEE double-precision floating point numbers. The library
consists of conversion routines that have been extracted from the V8
JavaScript engine.

%package        devel
Summary:        Development files for BCD/DCB routines for IEEE doubles
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{lib_ver} = %{version}

%description    devel
Double-conversion provides binary-decimal and decimal-binary routines
for IEEE double-precision floating point numbers. The library
consists of conversion routines that have been extracted from the V8
JavaScript engine.

This package provides libraries and header files for developing applications
that use double-conversion.

%prep
%setup -q

%build
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON\
    -DBUILD_TESTING:BOOL=ON
%make_jobs

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%post   -n lib%{name}%{lib_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{lib_ver} -p /sbin/ldconfig

%files -n lib%{name}%{lib_ver}
%license COPYING LICENSE
%{_libdir}/libdouble-conversion.so.%{lib_ver}*

%files devel
%doc AUTHORS Changelog README.md
%license COPYING LICENSE
%{_libdir}/libdouble-conversion.so
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/

%changelog
