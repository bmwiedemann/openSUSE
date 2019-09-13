#
# spec file for package libfcache
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


Name:           libfcache
%define lname	libfcache1
%define timestamp 20181011
Version:        0~%{timestamp}
Release:        0
Summary:        Library to provide generic file data cache functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfcache/wiki
Source:         https://github.com/libyal/libfcache/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to provide generic file data cache functions for the libyal family of libraries.

%package -n %{lname}
Summary:        Library to provide generic file data cache functions
Group:          System/Libraries

%description -n %{lname}
Library to provide generic file data cache functions for the libyal family of libraries.

%package devel
Summary:        Development files for libfcache
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide generic file data cache functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfcache.

%prep
%setup -q -n libfcache-%{timestamp}

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
%doc AUTHORS ChangeLog
%license COPYING 
%{_libdir}/libfcache.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%{_includedir}/libfcache.h
%{_includedir}/libfcache/
%{_libdir}/libfcache.so
%{_libdir}/pkgconfig/libfcache.pc
%{_mandir}/man3/libfcache.3*

%changelog
