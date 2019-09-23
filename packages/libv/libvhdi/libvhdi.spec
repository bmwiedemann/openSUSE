#
# spec file for package libvhdi
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


%define lname	libvhdi1
%define timestamp 20181227
Name:           libvhdi
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access the VHD image format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libvhdi/wiki
Source:         https://github.com/libyal/libvhdi/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
Source2:        Virtual_Hard_Disk_VHD_image_format.pdf

BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20170101
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfguid) >= 20130317
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library and tools to access the Virtual Hard Disk (VHD) image format.

Read supported formats:

VHD version 1
Supported image types:

Fixed-size hard disk image
Dynamic-size (or sparse) hard disk image
Differential (or differencing) hard disk image
Note that an undo disk image (.vud) is also a differential image

%package -n %{lname}
Summary:        Library to access the VHD image format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the Virtual Hard Disk (VHD) image format.

Read supported formats:

VHD version 1
Supported image types:

Fixed-size hard disk image
Dynamic-size (or sparse) hard disk image
Differential (or differencing) hard disk image
Note that an undo disk image (.vud) is also a differential image

%package tools
Summary:        Tools to access the VHD image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to access the Virtual Hard Disk (VHD) image format.  See libvhdi for additional details.

%package devel
Summary:        Development files for libvhdi, a VHD image format library
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libvhdi is a library to access the Virtual Hard Disk (VHD) image format.  see libvhdi for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libvhdi.

%package -n python2-%{name}
Summary:        Python 2 bindings for libvhdi, a VHD image format parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python
Obsoletes:      python-%{name}

%description -n python2-%{name}
libvhdi is a library to access Virtual Hard Disk (VHD) image format. See libvhdi for details.

This package contains Python 2 bindings for libvhdi.

%package -n python3-%{name}
Summary:        Python 3 bindings for libvhdi, a VHD image format parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
Provides:       pyvhdi

%description -n python3-%{name}
libvhdi is a library to access Virtual Hard Disk (VHD) image format. See libvhdi for details.

This package contains Python 3 bindings for libvhdi.

%prep
%setup -q -n libvhdi-%{timestamp}
cp "%{SOURCE2}" .

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
%{_libdir}/libvhdi.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/vhdi*
%{_mandir}/man1/vhdi*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%doc Virtual_Hard_Disk_*
%{_includedir}/libvhdi.h
%{_includedir}/libvhdi/
%{_libdir}/libvhdi.so
%{_libdir}/pkgconfig/libvhdi.pc
%{_mandir}/man3/libvhdi.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{python_sitearch}/pyvhdi.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%{python3_sitearch}/pyvhdi.so

%changelog
