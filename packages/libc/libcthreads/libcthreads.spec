#
# spec file for package libcthreads
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


Name:           libcthreads
%define lname	libcthreads1
%define timestamp 20200508
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C threads functions 
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libcthreads/wiki
Source:         https://github.com/libyal/libcthreads/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130904
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for cross-platform C threads functions.

libcthreads is part of the libyal library collection

%package -n %lname
Summary:        Library for cross-platform C thread functions
Group:          System/Libraries

%description -n %lname
A library for cross-platform C thread functions.

libcthreads is part of the libyal library collection

%package devel
Summary:        Development files for libcthreads, a cross-platform C thread library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for cross-platform C thread functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcthreads.

%prep
%setup -qn libcthreads-%timestamp

%build
%configure --disable-static --enable-wide-character-type
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%_libdir/libcthreads.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libcthreads*
%_libdir/libcthreads.so
%_libdir/pkgconfig/libcthreads.pc
%_mandir/man3/libcthreads.3*

%changelog
