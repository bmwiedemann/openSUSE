#
# spec file for package libsmdev
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


%define lname	libsmdev1
%define timestamp 20190315
Name:           libsmdev
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access storage media devices
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libsmdev/wiki
Source:         https://github.com/libyal/libsmdev/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20120425
BuildRequires:  pkgconfig(libcerror) >= 20170101
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libsmdev is a library to access and read storage media devices.

%package -n %{lname}
Summary:        Library to access storage media devices
Group:          System/Libraries

%description -n %{lname}
libsmdev is a library to access and read storage media devices.

%package devel
Summary:        Development files for libsmdev, a storage media access library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libsmdev is a library to access and read storage media devices.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmdev.

%package tools
Summary:        Utilities for reading storage media devices through libsmdev
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libsmdev, which
can access and read storage media devices and will determine
information about such.

%package -n python2-%{name}
Summary:        Python bindings for libsmdev
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
BuildRequires:  pkgconfig(python2)
Provides:       pysmdev = %{version}

%description -n python2-%{name}
Python 2 bindings for libsmdev, which is a library to access and read storage media devices.

%package -n python3-%{name}
Summary:        Python bindings for libsmdev
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
BuildRequires:  pkgconfig(python3)
Provides:       pysmdev = %{version}

%description -n python3-%{name}
Python 3 bindings for libsmdev, which is a library to access and read storage media devices.

%prep
%setup -q -n libsmdev-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
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
%{_libdir}/libsmdev.so.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_includedir}/libsmdev*
%{_libdir}/libsmdev.so
%{_libdir}/pkgconfig/libsmdev.pc
%{_mandir}/man3/libsmdev.3*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/smdevinfo
%{_mandir}/man1/smdevinfo.1*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{python_sitearch}/pysmdev.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{python3_sitearch}/pysmdev.so

%changelog
