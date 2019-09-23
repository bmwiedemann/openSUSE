#
# spec file for package libfvalue
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


Name:           libfvalue
%define lname	libfvalue1
%define timestamp 20180817
Version:        0~%{timestamp}
Release:        0
Summary:        Library to provide generic file value functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfvalue/wiki
Source:         https://github.com/libyal/libfvalue/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcerror)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libfwnt) >= 20170115
BuildRequires:  pkgconfig(libuna)
#version from factory causes a sigfault in plaso/run_tests.py  (as of Jan 2017)
#BuildRequires:  pkgconfig(libcdata) > 20170102
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to provide generic file value functions for the libyal family of libraries.

%package -n %{lname}
Summary:        Library to provide generic file value functions
Group:          System/Libraries

%description -n %{lname}
Library to provide generic file value functions for the libyal family of libraries.

%package devel
Summary:        Development files for libfvalue
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide generic file value functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfvalue.

%prep
%setup -q -n libfvalue-%{timestamp}

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
%{_libdir}/libfvalue.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{_includedir}/libfvalue.h
%{_includedir}/libfvalue/
%{_libdir}/libfvalue.so
%{_libdir}/pkgconfig/libfvalue.pc
%{_mandir}/man3/libfvalue.3*

%changelog
