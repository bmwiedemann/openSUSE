#
# spec file for package libvsmbr
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


Name:           libvsmbr
%define lname	libvsmbr1
Version:        20240505
Release:        0
Summary:        Library and tools to access the MS-DOS volume system format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libvsmbr
Source:         https://github.com/libyal/libvsmbr/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libvsmbr/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
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
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libvsmbr is a library to access the MS-DOS volume system.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing the MS-DOS partition table format
Group:          System/Libraries

%description -n %lname
libvsmbr is a library to access the MS-DOS volume system.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libvsmbr
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libvsmbr is a library to access the MS-DOS volume systems.

This subpackage contains libraries and header files for developing
applications that want to make use of libvsmbr.

%package tools
Summary:        Utilities for inspecting MS-DOS partition tables
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libvsmbr to
inspect MS-DOS partition tables.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
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
%_libdir/libvsmbr.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/vsmbr*
%_mandir/man1/vsmbr*

%files %python_files
%python_sitearch/*.so

%changelog
