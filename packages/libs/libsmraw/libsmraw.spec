#
# spec file for package libsmraw
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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

Name:           libsmraw
%define lname	libsmraw1
Version:        20260902
Release:        0
Summary:        Library and tools to access the (split) RAW image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libsmraw
Source:         https://github.com/libyal/libsmraw/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libsmraw/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse3) >= 3.0
BuildRequires:  pkgconfig(libbfio) >= 20260623
BuildRequires:  pkgconfig(libcdata) >= 20260703
BuildRequires:  pkgconfig(libcerror) >= 20260703
BuildRequires:  pkgconfig(libcfile) >= 20260704
BuildRequires:  pkgconfig(libclocale) >= 20260703
BuildRequires:  pkgconfig(libcnotify) >= 20260703
BuildRequires:  pkgconfig(libcpath) >= 20260703
BuildRequires:  pkgconfig(libcsplit) >= 20260703
BuildRequires:  pkgconfig(libcthreads) >= 20260703
BuildRequires:  pkgconfig(libfcache) >= 20260520
BuildRequires:  pkgconfig(libfdata) >= 20260521
BuildRequires:  pkgconfig(libfvalue) >= 20260531
BuildRequires:  pkgconfig(libhmac) >= 20260522
BuildRequires:  pkgconfig(libuna) >= 20260602
BuildRequires:  pkgconfig(openssl) >= 1.0
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

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
Requires:       libbfio-devel

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
%_bindir/smraw*
%_mandir/man1/smraw*.1*

%files %python_files
%license COPYING
%python_sitearch/pysmraw*

%changelog
