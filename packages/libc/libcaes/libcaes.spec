#
# spec file for package libcaes
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


Name:           libcaes
%define lname	libcaes1
%define timestamp 20190102
Version:        0~%timestamp
Release:        0
Summary:        Library for cross-platform AES encryption
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libcaes/wiki
Source:         https://github.com/libyal/libcaes/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libcaes is a library for cross-platform AES encryption.

%package -n %lname
Summary:        Library for cross-platform AES encryption
Group:          System/Libraries

%description -n %lname
libcaes is a library for cross-platform AES encryption.

%package devel
Summary:        Development files for libcaes, a cross-platform AES encryption library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libcaes is a library for cross-platform AES encryption.

This subpackage contains libraries and header files for developing
applications that want to make use of libcaes.

%prep
%setup -qn libcaes-%timestamp

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
%_libdir/libcaes.so.1*

%files devel
%defattr(-,root,root)
%_includedir/libcaes*
%_libdir/libcaes.so
%_libdir/pkgconfig/libcaes.pc
%_mandir/man3/libcaes.3*

%changelog
