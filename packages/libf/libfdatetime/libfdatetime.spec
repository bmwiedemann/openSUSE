#
# spec file for package libfdatetime
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


Name:           libfdatetime
%define lname	libfdatetime1
%define timestamp 20180910
Version:        0~%timestamp
Release:        0
Summary:        A library for date and time data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libfdatetime/wiki
Source:         https://github.com/libyal/libfdatetime/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for date and time data types. Part of the libyal family of libraries.

%package -n %lname
Summary:        A library for date and time data types
Group:          System/Libraries

%description -n %lname
A library for date and time data types. Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfdatetime, a date and time data type library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for date and time data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfdatetime.

%prep
%setup -qn libfdatetime-%timestamp

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
%_libdir/libfdatetime.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libfdatetime*
%_libdir/libfdatetime.so
%_libdir/pkgconfig/libfdatetime.pc
%_mandir/man3/libfdatetime.3*

%changelog
