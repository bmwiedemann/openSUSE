#
# spec file for package pnglite
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define abi_major 0
%define abi_minor 1
%define libname libpnglite%{abi_major}
Name:           pnglite
Version:        0.1.17
Release:        0
Summary:        A light-weight C library for loading PNG images
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://www.danielkarling.se/stuff/pnglite/
Source:         http://downloads.sourceforge.net/pnglite/%{name}-%{version}.zip
# PATCH-FIX-FEDORA use system zlib
Patch0:         pnglite-0.1.17-zlib.patch
BuildRequires:  zlib-devel
BuildRequires:  unzip

%description
pnglite is a C library for loading PNG images. It was created as a
substitute for libpng in situations when libpng is more than enough. It
currently requires zlib for inflate and CRC checking and it can read the
most common types of PNG images. The library has a small and simple to use
interface.

%package -n %{libname}
Summary:        A light-weight C library for loading PNG images
Group:          System/Libraries

%description -n %{libname}
pnglite is a C library for loading PNG images. It was created as a
substitute for libpng in situations when libpng is more than enough. It
currently requires zlib for inflate and CRC checking and it can read the
most common types of PNG images. The library has a small and simple to use
interface.

%package devel
Summary:        Files needed to build and link programs with pnglite
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This contains a header file and a link to library for the linker
to link against pnglite.

%prep
%setup -q -c
%patch0 -p1 -b .zlib
sed 's/\r//' -i pnglite.h

%build
gcc %{optflags} -shared -fPIC -Wl,--soname,libpnglite.so.%{abi_major} \
       -o libpnglite.so.%{abi_major}.%{abi_minor} pnglite.c

%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}

install -pm 0644 pnglite.h %{buildroot}%{_includedir}
install libpnglite.so.%{abi_major}.%{abi_minor} %{buildroot}%{_libdir}
ln -s libpnglite.so.%{abi_major}.%{abi_minor} %{buildroot}%{_libdir}/libpnglite.so.%{abi_major}
ln -s libpnglite.so.%{abi_major}.%{abi_minor} %{buildroot}%{_libdir}/libpnglite.so

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
