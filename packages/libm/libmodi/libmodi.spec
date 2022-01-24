#
# spec file for package libmodi
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


Name:           libmodi
%define lname	libmodi1
Version:        20210807
Release:        0
Summary:        Library and tools to access the Mac OS disk image formats
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libmodi
Source:         https://github.com/libyal/libmodi/releases/download/%version/libmodi-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libmodi/releases/download/%version/libmodi-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcaes) >= 20201012
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcdirectory) >= 20200702
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
BuildRequires:  pkgconfig(libfplist) >= 20210404
BuildRequires:  pkgconfig(libfvalue) >= 20210510
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libuna) >= 20210801
%python_subpackages

%description
libmodi is a library to access the Mac OS disk image formats.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing Mac OS disk image formats
Group:          System/Libraries

%description -n %lname
libmodi is a library to access the Mac OS disk image formats.

Supported formats include:

* Sparse bundle disk image
* Sparse disk image
* Universal Disk Image Format (UDIF) image
  * uncompressed
  * ADC compressed
  * bzip2 compressed
  * LZMA compressed
  * zlib/DEFLATE compressed

%package devel
Summary:        Development files for libmodi
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libmodi is a library to access the Mac OS disk image formats.

This subpackage contains libraries and header files for developing
applications that want to make use of libmodi.

%package tools
Summary:        Utilities for reading Mac OS disk image formats
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libmodi to
read MacOS disk image formats.

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
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libmodi.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n %name-tools
%_bindir/modi*
%_mandir/man1/modi*

%files %python_files
%python_sitearch/pymodi.so

%changelog
