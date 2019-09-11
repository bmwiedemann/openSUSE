#
# spec file for package libcdatetime
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


%define lname	libcdatetime1
%define timestamp 20181004
Name:           libcdatetime
Version:        0~%{timestamp}
Release:        0
Summary:        Library for cross-platform C date and time functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libcdatetime/wiki
Source:         https://github.com/libyal/libcdatetime/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library for cross-platform C date and time functions.  Part of the libyal library family.

%package -n %{lname}
Summary:        Library for cross-platform C date and time functions
Group:          System/Libraries

%description -n %{lname}
Library for cross-platform C date and time functions.  libcdatetime is a low level member of the libyal library family.

%package devel
Summary:        Development files for libcdatetime, a PFF/OFF file format library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libcdatetime is a library cross-platform C date and time functions.  

This subpackage contains libraries and header files for developing
applications that want to make use of libcdatetime.

%prep
%setup -q -n libcdatetime-%{timestamp}

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
%{_libdir}/libcdatetime.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%{_includedir}/libcdatetime.h
%{_includedir}/libcdatetime/
%{_libdir}/libcdatetime.so
%{_libdir}/pkgconfig/libcdatetime.pc
%{_mandir}/man3/libcdatetime.3*

%changelog
