#
# spec file for package libaio
#
# Copyright (c) 2021 SUSE LLC
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


%define lname	libaio1
Name:           libaio
Version:        0.3.112+29.696a5e6483ba
Release:        0
Summary:        Linux-Native Asynchronous I/O Access Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://pagure.io/libaio
Source:         libaio-%{version}.tar.xz
Source2:        baselibs.conf

%description
The Linux-native asynchronous I/O facility ("async I/O", or "aio") has
a richer API and capability set than the simple POSIX async I/O
facility. This library provides the Linux-native API for async I/O. The
POSIX async I/O facility requires this library to provide
kernel-accelerated async I/O capabilities, as do applications that
require the Linux-native async I/O API.

%package -n %{lname}
Summary:        Linux-Native Asynchronous I/O Access Library
Group:          System/Libraries
Obsoletes:      libaio < %{version}-%{release}
Provides:       libaio = %{version}-%{release}

%description -n %{lname}
The Linux-native asynchronous I/O facility ("async I/O", or "aio") has
a richer API and capability set than the simple POSIX async I/O
facility. This library provides the Linux-native API for async I/O. The
POSIX async I/O facility requires this library to provide
kernel-accelerated async I/O capabilities, as do applications that
require the Linux-native async I/O API.

%package devel
Summary:        Development Files for Linux-native Asynchronous I/O Access
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
This package provides header files to include, and libraries to link
with, for the Linux-native asynchronous I/O facility ("async I/O", or
"aio").

%prep
%setup -q

%build
make %{?_smp_mflags} OPTFLAGS="%{optflags}"

%install
%make_install libdir=%{_libdir}
rm %{buildroot}%{_libdir}/*.a

%check
make %{?_smp_mflags} partcheck

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libaio.so.*

%files devel
%{_includedir}/libaio.h
%{_libdir}/libaio.so

%changelog
