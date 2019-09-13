#
# spec file for package libvslvm
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


%define lname	libvslvm1
%define timestamp 20160110
Name:           libvslvm
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access the Linux Logical Volume Manager (LVM) volume system
License:        LGPL-3.0+ and GFDL-1.3+
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libvslvm/
Source:         https://github.com/libyal/libvslvm/releases/download/%{timestamp}/libvslvm-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20150101
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfvalue) >= 20150101
BuildRequires:  pkgconfig(libuna) >= 20150101

#Build fails with factory version of these - tested 7/14/2016
#BuildRequires:  pkgconfig(libcerror) >= 20140105
#BuildRequires:  pkgconfig(libcstring) >= 20120425

BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libvslvm is a library to access the Linux Logical Volume Manager (LVM) volume system.

%package -n %{lname}
Summary:        Library to access Linux Logical Volume Manager (LVM) volume containers
License:        LGPL-3.0+
Group:          System/Libraries

%description -n %{lname}
The libvslvm library is a library to access Linux Logical Volume Manager (LVM) volume containers

%package tools
Summary:        Several tools for reading Linux Logical Volume Manager (LVM) volume systems
License:        LGPL-3.0+
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Several tools for reading Linux Logical Volume Manager (LVM) volume systems

See libvslvm for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libvslvm
License:        LGPL-3.0+ and GFDL-1.3+
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Header files and libraries for developing applications for libvslvm

See libvslvm for additional details.

This package contains libraries and header files for developing
applications that want to make use of libvslvm.

%package -n python2-%{name}
Summary:        Python 2 bindings for libvslvm
License:        LGPL-3.0+
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python
BuildRequires:  pkgconfig(python2)
Obsoletes:		python-%{name}

%description -n python2-%{name}
This packinge provides Python 2 bindings for libvslvm

%package -n python3-%{name}
Summary:        Python 3 bindings for libvslvm
License:        LGPL-3.0+
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name}
This packinge provides Python 3 bindings for libvslvm

%prep
%setup -q -n libvslvm-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/libvslvm.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_bindir}/vslvm*
%{_mandir}/man1/vslvm*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_includedir}/libvslvm.h
%{_includedir}/libvslvm/
%{_libdir}/libvslvm.so
%{_libdir}/pkgconfig/libvslvm.pc
%{_mandir}/man3/libvslvm.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{python_sitearch}/pyvslvm.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS COPYING
%{python3_sitearch}/pyvslvm.so

%changelog
