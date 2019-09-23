#
# spec file for package libcdata
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libcdata
%define lname	libcdata1
%define timestamp 20190112
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C generic data functions
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcdata/wiki
Source:         https://github.com/libyal/libcdata/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130904
BuildRequires:  pkgconfig(libcthreads) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for cross-platform C generic data functions.

This package is part of the libyal library collection and is used by other libraries in the collection

%package -n %lname
Summary:        Library for cross-platform C generic data functions
Group:          System/Libraries

%description -n %lname
A library for cross-platform C generic data functions.

This subpackage contains the actual shared object library

%package devel
Summary:        Development files for libcdata, a cross-platform C generic data library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for cross-platform C generic data functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcdata.

%prep
%setup -qn libcdata-%timestamp

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
%_libdir/libcdata.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libcdata*
%_libdir/libcdata.so
%_libdir/pkgconfig/libcdata.pc
%_mandir/man3/libcdata.3*

%changelog
