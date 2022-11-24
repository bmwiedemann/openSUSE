#
# spec file for package libfsfat
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


Name:           libfsfat
%define lname	libfsfat1
Version:        20220925
Release:        0
Summary:        Library and tools for accessing the FAT filesystem
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfsfat
Source:         https://github.com/libyal/libfsfat/releases/download/%version/libfsfat-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfsfat/releases/download/%version/libfsfat-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  %python_module devel
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.21
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20220120
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfcrypto) >= 20210415
BuildRequires:  pkgconfig(libfdata) >= 20211023
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libhmac) >= 20220425
BuildRequires:  pkgconfig(libuna) >= 20220611
BuildRequires:  pkgconfig(python3)
%python_subpackages

%description
libfsfat is a library to access the File Allocation Table (FAT) file
system format.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing the FAT file system
Group:          System/Libraries

%description -n %lname
libfsfat is a library to access the File Allocation Table (FAT) file
system format.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfsfat
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfsfat is a library to access the File Allocation Table (FAT) file
system format.

This subpackage contains libraries and header files for developing
applications that want to make use of libfsfat.

%package tools
Summary:        Utilities to inspect FAT file systems
Group:          Productivity/File utilities

%description tools
This subpackage provides the utilities from libfsfat, which allows for
reading FAT File Systems.

%prep
%autosetup -p1

%build
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python \
	PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libfsfat.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/fsfat*
%_mandir/man1/fsfat*

%files %python_files
%python_sitearch/py*.so

%changelog
