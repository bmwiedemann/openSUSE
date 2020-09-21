#
# spec file for package libhomfly
#
# Copyright (c) 2020 SUSE LLC
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


%define lname   libhomfly0
%define unver   1.02r6
Name:           libhomfly
Version:        1.0.2.6
Release:        0
Summary:        Library to compute the homfly polynomial of a link
License:        SUSE-Public-Domain
Group:          Productivity/Scientific/Math
URL:            https://github.com/miguelmarco/libhomfly
Source:         https://github.com/miguelmarco/libhomfly/releases/download/%unver/%name-%unver.tar.gz
BuildRequires:  gc-devel

%description
A library to compute the homfly polynomial of a link.

%package -n %lname
Summary:        Library to compute the homfly polynomial of a link
Group:          System/Libraries

%description -n %lname
A library to compute the homfly polynomial of a link.

%package devel
Summary:        Development files for the homfly library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library to compute the homfly polynomial of a link.

This subpackage provides the development headers for it.

%prep
%autosetup -p1 -n %name-%unver

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libhomfly.so.0*

%files devel
%_includedir/*.h
%_libdir/libhomfly.so

%changelog
