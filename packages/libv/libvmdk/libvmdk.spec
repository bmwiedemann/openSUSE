#
# spec file for package libvmdk
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


%define lname	libvmdk1
Name:           libvmdk
Version:        20210418
Release:        0
Summary:        Library to access the VMware Virtual Disk (VMDK) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libvmdk/
Source:         %{name}-%{version}.tar.xz
Source2:        VMWare_Virtual_Disk_Format_VMDK.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
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
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

%description
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

Read supported extent file formats:
- RAW (flat)
- COWD version 1 (sparse)
- VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:
- delta links
- grain compression (as of version 20131209)
- data markers (as of version 20140416)

VMDK format features not supported at the moment:
- images that use a physical device
- changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking filek

%package -n %{lname}
Summary:        Library to access the VMDK image format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

Read supported extent file formats:
- RAW (flat)
- COWD version 1 (sparse)
- VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:
- delta links
- grain compression (as of version 20131209)
- data markers (as of version 20140416)

VMDK format features not supported at the moment:
- images that use a physical device
- changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking filek

%package tools
Summary:        Tools to access the VMDK image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for accessing VMware Virtual Disk (VMDK) files.

See libvmdk for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libvmdk
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

See libvmdk for additional details.

This package contains libraries and header files for developing
applications that want to make use of libvmdk.

%package -n python3-%{name}
Summary:        Python 3 bindings for libvmdk, a VMDK image format parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description -n python3-%{name}
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

This package contains the Python 3 bindings for libvmdk.

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

%check
#make check

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libvmdk.so.*

%files tools
%license COPYING*
%{_bindir}/vmdk*
%{_mandir}/man1/vmdk*.1*

%files devel
%license COPYING*
%doc VMWare_Virtual_Disk_Format*
%{_includedir}/libvmdk.h
%{_includedir}/libvmdk/
%{_libdir}/libvmdk.so
%{_libdir}/pkgconfig/libvmdk.pc
%{_mandir}/man3/libvmdk.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyvmdk.so

%changelog
