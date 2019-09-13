#
# spec file for package libmapidb
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


Name:           libmapidb
%define lname	libmapidb1
%define timestamp 20170304
Version:        0~%timestamp
Release:        0
Summary:        Library for accessing the Exchange MAPI database format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libmapidb/wiki
Source:         https://github.com/libyal/libmapidb/releases/download/%timestamp/%name-experimental-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130904
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for accessing the Exchange MAPI database format

libmapidb is part of the libyal library collection

%package -n %lname
Summary:        Library for MAPI data types
Group:          System/Libraries

%description -n %lname
A library for accessing the Exchange MAPI database format

libmapidb is part of the libyal library collection

%package devel
Summary:        Development files for libmapidb, a library for accessing the Exchange MAPI database format
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for accessing the Exchange MAPI database format

This subpackage contains libraries and header files for developing
applications that want to make use of libmapidb.

%prep
%setup -qn libmapidb-%timestamp

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
%doc AUTHORS ChangeLog
%license COPYING 
%_libdir/libmapidb.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libmapidb*
%_libdir/libmapidb.so
%_libdir/pkgconfig/libmapidb.pc
%_mandir/man3/libmapidb.3*

%changelog
