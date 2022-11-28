#
# spec file for package libphdi
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


Name:           libphdi
%define lname	libphdi1
Version:        20221025
Release:        0
Summary:        Library and tools to access the Parallels Hard Disk images
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libphdi
Source:         https://github.com/libyal/libphdi/releases/download/%version/libphdi-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libphdi/releases/download/%version/libphdi-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcdirectory) >= 20220105
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfvalue) >= 20220120
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libphdi is a library to access the Parallels Hard Disk image format.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing Parallels Hard Disk images
Group:          System/Libraries

%description -n %lname
libphdi is a library to access the Parallels Hard Disk image format.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libphdi
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libphdi is a library to access the Parallels Hard Disk image format.

This subpackage contains libraries and header files for developing
applications that want to make use of libphdi.

%package tools
Summary:        Utilities for reading Parallels Hard Disk images
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libphdi to
read Parallels Hard Disk images.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python \
	PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv %_builddir/rt/* %buildroot/
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libphdi.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/phdi*
%_mandir/man1/phdi*

%files %python_files
%python_sitearch/*.so

%changelog
