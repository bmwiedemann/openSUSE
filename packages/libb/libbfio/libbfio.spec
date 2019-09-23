#
# spec file for package libbfio
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


Name:           libbfio
%define lname	libbfio1
%define timestamp 20190112
Version:        0~%timestamp
Release:        0
Summary:        Library to provide basic file input/output abstraction
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libbfio/wiki
Source:         https://github.com/libyal/libbfio/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20190112
BuildRequires:  pkgconfig(libcerror) >= 20150101
BuildRequires:  pkgconfig(libcfile) >= 20120425
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcpath) >= 20120425
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

%package -n %lname
Summary:        Library to provide basic file input/output abstraction
Group:          System/Libraries

%description -n %lname
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

%package devel
Summary:        Development files for libbfio, a basic file input/output abstraction library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

This subpackage contains libraries and header files for developing
applications that want to make use of libbfio.

%prep
%setup -qn libbfio-%timestamp

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
%_libdir/libbfio.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libbfio*
%_libdir/libbfio.so
%_libdir/pkgconfig/libbfio.pc
%_mandir/man3/libbfio.3*

%changelog
