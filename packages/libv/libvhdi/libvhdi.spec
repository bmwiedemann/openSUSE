#
# spec file for package libvhdi
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


%define lname	libvhdi1
Name:           libvhdi
Version:        20210425
Release:        0
Summary:        Library and tools to access the VHD image format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libvhdi/wiki
Source:         %{name}-%{version}.tar.xz
Source2:        Virtual_Hard_Disk_VHD_image_format.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)

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

%description tools
Tools to access the Virtual Hard Disk (VHD) image format.  See libvhdi for additional details.

%package devel
Summary:        Development files for libvhdi, a VHD image format library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libvhdi is a library to access the Virtual Hard Disk (VHD) image format.  see libvhdi for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libvhdi.

%package -n python3-%{name}
Summary:        Python 3 bindings for libvhdi, a VHD image format parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Provides:       pyvhdi

%description -n python3-%{name}
libvhdi is a library to access Virtual Hard Disk (VHD) image format. See libvhdi for details.

This package contains Python 3 bindings for libvhdi.

%prep
%autosetup -p1
cp "%{SOURCE2}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libvhdi.so.*

%files tools
%license COPYING*
%{_bindir}/vhdi*
%{_mandir}/man1/vhdi*.1*

%files devel
%license COPYING*
%doc Virtual_Hard_Disk_*
%{_includedir}/libvhdi.h
%{_includedir}/libvhdi/
%{_libdir}/libvhdi.so
%{_libdir}/pkgconfig/libvhdi.pc
%{_mandir}/man3/libvhdi.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyvhdi.so

%changelog
