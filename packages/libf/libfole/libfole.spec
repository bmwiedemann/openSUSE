#
# spec file for package libfole
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libfole
%define lname	libfole1
%define timestamp 20170502
Version:        0~%{timestamp}
Release:        0
Summary:        Library for Object Linking and Embedding (OLE) data types
License:        LGPL-3.0+
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfole/wiki
Source:         https://github.com/libyal/libfole/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcerror) >= 20150101
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libfole is a library for Object Linking and Embedding (OLE) data types.

Part of the libyal family of libraries.

%package -n %{lname}
Summary:        Library for Object Linking and Embedding (OLE) data types
Group:          System/Libraries

%description -n %{lname}
libfole is a library for Object Linking and Embedding (OLE) data types.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfole
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libfole is a library for Object Linking and Embedding (OLE) data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfole.

%prep
%setup -q -n libfole-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libfole.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog
%{_includedir}/libfole.h
%{_includedir}/libfole/
%{_libdir}/libfole.so
%{_libdir}/pkgconfig/libfole.pc
%{_mandir}/man3/libfole.3*

%changelog
