#
# spec file for package fastlzlib
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define sover 1
%define libname libfastlz%{sover}
Name:           fastlzlib
Version:        0.0+git.20150524
Release:        0
Summary:        Zlib-like encapsulation interface to LZ4/FastLZ
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/bareos/fastlzlib
Source:         %{name}-%{version}.tar.xz
BuildRequires:  zlib-devel

%description
A library that bundles and wraps LZ4 and FastLZ in a zlib-like interface.

%package -n %{libname}
Summary:        Zlib-like encapsulation interface to LZ4/FastLZ
Group:          Development/Libraries/C and C++

%description -n %{libname}
A library that bundles and wraps LZ4 and FastLZ in a zlib-like interface.

%package devel
Summary:        Development files for the "fastlzlib" compression library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Conflicts:      liblz4-devel

%description devel
Header files for the fastlzlib library, a library that bundles and
wraps LZ4 and FastLZ in a zlib-like interface.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/doc/libfastlz

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/fastlzcat

%files -n %{libname}
%license COPYING
%doc README
%{_libdir}/libfastlz.so.%{sover}*

%files devel
%license COPYING
%{_includedir}/*
%{_libdir}/libfastlz.so

%changelog
