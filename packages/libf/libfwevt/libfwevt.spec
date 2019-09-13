#
# spec file for package libfwevt
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


%define lname	libfwevt1
%define timestamp 20190102
Name:           libfwevt
Version:        0~%{timestamp}
Release:        0
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfwevt/wiki
Source:         https://github.com/libyal/libfwevt/releases/download/%timestamp/%{name}-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcdata)
BuildRequires:  pkgconfig(libcerror)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring)
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libfvalue)
BuildRequires:  pkgconfig(libuna)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwevt
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Windows NT data type support for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwevt.

%prep
%setup -q -n libfwevt-%{timestamp}

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
%{_libdir}/libfwevt.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%{_includedir}/libfwevt.h
%{_includedir}/libfwevt/
%{_libdir}/libfwevt.so
%{_libdir}/pkgconfig/libfwevt.pc
%{_mandir}/man3/libfwevt.3*

%changelog
