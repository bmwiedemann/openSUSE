#
# spec file for package libcerror
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


Name:           libcerror
%define lname	libcerror1
%define timestamp 20181117
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C error functions
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcerror/wiki
Source:         https://github.com/libyal/%name/releases/download/%timestamp/%name-beta-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description 
A library for cross-platform C error functions.

This package is part of the libyal library collection and is used by other libraries in the collection

%package -n %lname
Summary:        Library for cross-platform C error functions
Group:          System/Libraries

%description -n %lname
A library for cross-platform C error functions.

This subpackage contains the actual shared object library

%package devel
Summary:        Development files for libcerror, a cross-platform C error library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for cross-platform C error functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcerror.

%prep
%setup -qn libcerror-%timestamp

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
%_libdir/libcerror.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libcerror*
%_libdir/libcerror.so
%_libdir/pkgconfig/libcerror.pc
%_mandir/man3/libcerror.3*

%changelog
