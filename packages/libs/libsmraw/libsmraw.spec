#
# spec file for package libsmraw
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


Name:           libsmraw
%define lname	libsmraw1
Version:        20210807
Release:        0
Summary:        Library and tools to access the (split) RAW image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsmraw
Source:         https://github.com/libyal/libsmraw/releases/download/%version/libsmraw-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libsmraw/releases/download/%version/libsmraw-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         system-libs.patch
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse) >= 2.6
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
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20210801
BuildRequires:  pkgconfig(openssl) >= 1.0
%python_subpackages

%description
libsmraw is a library to access the storage media RAW format.
The library supports both RAW and split RAW.

%package -n %lname
Summary:        Library and tools to access the (split) RAW image format
Group:          System/Libraries

%description -n %lname
libsmraw is a library to access the storage media RAW format.
The library supports both RAW and split RAW.

%package devel
Summary:        Development files for libsmraw, a (split) RAW image file library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libsmraw is a library to access the storage media RAW format.

This subpackage contains libraries and header files for developing
applications that want to make use of libsmraw.

%package tools
Summary:        Utilities for reading and writing storage media (split) RAW files
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libsmraw to
acquire, export, query and verify storage media (split) RAW files.

%prep
%autosetup -p1

%build
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}"
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
%license COPYING
%_libdir/libsmraw.so.1*

%files -n %name-devel
%license COPYING
%_includedir/libsmraw*
%_libdir/libsmraw.so
%_libdir/pkgconfig/libsmraw.pc
%_mandir/man3/libsmraw.3*

%files -n %name-tools
%license COPYING
%_bindir/smrawverify
%_bindir/smrawmount
%_mandir/man1/smrawmount.1*

%files %python_files
%license COPYING
%python_sitearch/pysmraw.so

%changelog
