#
# spec file for package libfmapi
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


Name:           libfmapi
%define lname	libfmapi1
%define timestamp 20180714
Version:        0~%timestamp
Release:        0
Summary:        Library for MAPI data types
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libfmapi/wiki
Source:         https://github.com/libyal/libfmapi/releases/download/%timestamp/%name-experimental-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata)
BuildRequires:  pkgconfig(libcerror) >= 20130904
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libfwnt)
BuildRequires:  pkgconfig(libuna)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for MAPI data types

libfmapi is part of the libyal library collection

%package -n %lname
Summary:        Library for MAPI data types
Group:          System/Libraries

%description -n %lname
A library for MAPI data types.

libfmapi is part of the libyal library collection

%package devel
Summary:        Development files for libfmapi, a library for MAPI data types
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for MAPI data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfmapi.

%prep
%setup -qn libfmapi-%timestamp

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
%_libdir/libfmapi.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libfmapi*
%_libdir/libfmapi.so
%_libdir/pkgconfig/libfmapi.pc
%_mandir/man3/libfmapi.3*

%changelog
