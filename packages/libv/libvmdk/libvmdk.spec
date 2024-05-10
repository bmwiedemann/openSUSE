#
# spec file for package libvmdk
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}

%define lname	libvmdk1
Name:           libvmdk
Version:        20240510
Release:        0
Summary:        Library to access the VMware Virtual Disk (VMDK) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libvmdk/
Source:         https://github.com/libyal/libvmdk/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libvmdk/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source11:       VMWare_Virtual_Disk_Format_VMDK.pdf
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfcache) >= 20240414
BuildRequires:  pkgconfig(libfdata) >= 20240415
BuildRequires:  pkgconfig(libfvalue) >= 20240415
BuildRequires:  pkgconfig(libuna) >= 20240414
BuildRequires:  pkgconfig(zlib)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

%package -n %lname
Summary:        Library to access the VMDK image format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

Read supported extent file formats:

* RAW (flat)
* COWD version 1 (sparse)
* VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:

* delta links
* grain compression
* data markers

VMDK format features not supported at the moment:

* images that use a physical device
* changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking files

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
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.

See libvmdk for additional details.

This package contains libraries and header files for developing
applications that want to make use of libvmdk.

%prep
%autosetup -p1
cp %_sourcedir/*.pdf .

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libvmdk.so.*

%files -n %name-tools
%license COPYING*
%_bindir/vmdk*
%_mandir/man1/vmdk*.1*

%files -n %name-devel
%license COPYING*
%doc VMWare_Virtual_Disk_Format*
%_includedir/libvmdk.h
%_includedir/libvmdk/
%_libdir/libvmdk.so
%_libdir/pkgconfig/libvmdk.pc
%_mandir/man3/libvmdk.3*

%files %python_files
%license COPYING*
%python_sitearch/pyvmdk.so

%changelog
