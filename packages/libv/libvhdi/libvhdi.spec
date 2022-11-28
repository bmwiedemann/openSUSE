#
# spec file for package libvhdi
#
# Copyright (c) 2022 SUSE LLC
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
Version:        20221124
Release:        0
Summary:        Library and tools to access the VHD image format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libvhdi/wiki
Source:         https://github.com/libyal/libvhdi/releases/download/%version/libvhdi-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libvhdi/releases/download/%version/libvhdi-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source8:        Virtual_Hard_Disk_VHD_image_format.pdf
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 2022010
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library and tools to access the Virtual Hard Disk (VHD) image format.

Read-supported formats:

* VHD version 1

Supported image types:

* Fixed-size hard disk image
* Dynamic-size (or sparse) hard disk image
* Differential (or differencing) hard disk image
* Note that an undo disk image (.vud) is also a differential image

%package -n %{lname}
Summary:        Library to access the VHD image format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the Virtual Hard Disk (VHD) image format.

Read-supported formats:

* VHD version 1

Supported image types:

* Fixed-size hard disk image
* Dynamic-size (or sparse) hard disk image
* Differential (or differencing) hard disk image
* Note that an undo disk image (.vud) is also a differential image

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
find %{buildroot} -type f -name "*.la" -delete -print
%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libvhdi.so.*

%files -n %name-tools
%license COPYING*
%{_bindir}/vhdi*
%{_mandir}/man1/vhdi*.1*

%files -n %name-devel
%license COPYING*
%doc Virtual_Hard_Disk_*
%{_includedir}/libvhdi.h
%{_includedir}/libvhdi/
%{_libdir}/libvhdi.so
%{_libdir}/pkgconfig/libvhdi.pc
%{_mandir}/man3/libvhdi.3*

%files %python_files
%license COPYING*
%python_sitearch/pyvhdi.so

%changelog
