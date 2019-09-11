#
# spec file for package libcsystem
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


Name:           libcsystem
%define lname	libcsystem1
%define timestamp 20150629
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C system functions 
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcsystem/wiki
Source:         https://github.com/libyal/%{name}/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror)
BuildRequires:  pkgconfig(libclocale)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring)
# libuna requires libcsystem, so this creates a build loop
#BuildRequires:  pkgconfig(libuna)

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for cross-platform C system functions.

libcsystem is part of the libyal library collection

%package -n %lname
Summary:        Library for cross-platform C system functions
Group:          System/Libraries

%description -n %lname
A library for cross-platform C system functions.

libcsystem is part of the libyal library collection

%package devel
Summary:        Development files for libcsystem, a cross-platform C system library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for cross-platform C system functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcsystem.

%prep
%setup -qn libcsystem-%timestamp

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
%_libdir/libcsystem.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libcsystem*
%_libdir/libcsystem.so
%_libdir/pkgconfig/libcsystem.pc
%_mandir/man3/libcsystem.3*

%changelog
