#
# spec file for package libfsxfs
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


Name:           libfsxfs
%define lname	libfsxfs1
Version:        20220113
Release:        0
Summary:        Library and tools for accessing the SGI X File System (XFS)
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfsxfs
Source:         https://github.com/libyal/libfsxfs/releases/download/%version/libfsxfs-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfsxfs/releases/download/%version/libfsxfs-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  %python_module devel
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libbfio) >= 20220111
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfcrypto) >= 20200104
BuildRequires:  pkgconfig(libfdata) >= 20211023
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libhmac) >= 20210419
BuildRequires:  pkgconfig(libuna) >= 20220102
BuildRequires:  pkgconfig(python3)
%python_subpackages

%description
libfsxfs is a library to access the SGI X File System (XFS).

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing the SGI X File System (XFS)
Group:          System/Libraries

%description -n %lname
libfsxfs is a library to access the SGI X File System (XFS).

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfsxfs
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfsxfs is a library to access the SGI X File System (XFS).

This subpackage contains libraries and header files for developing
applications that want to make use of libfsxfs.

%package tools
Summary:        Utilities to inspect SGI X File Systems (XFS)
Group:          Productivity/File utilities

%description tools
This subpackage provides the utilities from libfsxfs, which allows for
reading SGI X File Systems (XFS).

%prep
%autosetup -p1

%build
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
%configure --disable-static --enable-wide-character-type --enable-python PYTHON_VERSION="%{$python_bin_suffix}"
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
%_libdir/libfsxfs.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/fsxfs*
%_mandir/man1/fsxfs*

%files %python_files
%python_sitearch/py*.so

%changelog
