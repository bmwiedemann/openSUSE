#
# spec file for package libcnotify
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


Name:           libcnotify
%define lname	libcnotify1
%define timestamp 20180102
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform C notify functions
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcnotify/wiki
Source:         https://github.com/libyal/libcnotify/releases/download/%timestamp/%name-beta-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for cross-platform C notify functions.  Part of the libyal library collection.

%package -n %lname
Summary:        Library for cross-platform C notify functions
Group:          System/Libraries

%description -n %lname
A library for cross-platform C notify functions.

%package devel
Summary:        Development files for libcnotify, a cross-platform C notify library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A library for cross-platform C notify functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcnotify.

%prep
%setup -qn libcnotify-%timestamp

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
%_libdir/libcnotify.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libcnotify*
%_libdir/libcnotify.so
%_libdir/pkgconfig/libcnotify.pc
%_mandir/man3/libcnotify.3*

%changelog
