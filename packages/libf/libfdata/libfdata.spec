#
# spec file for package libfdata
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


Name:           libfdata
%define lname	libfdata1
%define timestamp 20181124
Version:        0~%{timestamp}
Release:        0
Summary:        Library to provide generic file data functions
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfdata/wiki
Source:         https://github.com/libyal/libfdata/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to provide generic file data functions for the libyal family of libraries.

%package -n %{lname}
Summary:        Library to provide generic file data functions
Group:          System/Libraries

%description -n %{lname}
Library to provide generic file data functions for the libyal family of libraries.

%package devel
Summary:        Development files for libfdata
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide generic file data functions for the libyal family of libraries.

This subpackage contains libraries and header files for developing
applications that want to make use of libfdata.

%prep
%setup -q -n libfdata-%{timestamp}

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
%{_libdir}/libfdata.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%{_includedir}/libfdata.h
%{_includedir}/libfdata/
%{_libdir}/libfdata.so
%{_libdir}/pkgconfig/libfdata.pc
%{_mandir}/man3/libfdata.3*

%changelog
