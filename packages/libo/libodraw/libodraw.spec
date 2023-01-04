#
# spec file for package libodraw
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libodraw
%define lname	libodraw1
Version:        20210503
Release:        0
Summary:        Library and tools to access to optical disc (split) RAW image files
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libodraw
Source:         %name-%version.tar.xz
Source2:        CUE_sheet_format.pdf
Patch1:         system-libs.patch
BuildRequires:  bison
BuildRequires:  c_compiler
BuildRequires:  flex
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20201204

%description
libodraw is a library to access optical disc (split) RAW images such
as BIN/ISO/CUE.

%package -n %lname
Summary:        Library to access to optical disc (split) RAW image files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libodraw is a library to access optical disc (split) RAW images such
as BIN/ISO/CUE.

%package devel
Summary:        Development files for libodraw, a disc image file library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libodraw is a library to access optical disc (split) RAW images such
as BIN/ISO/CUE.

This subpackage contains libraries and header files for developing
applications that want to make use of libodraw.

%package tools
Summary:        Utilities for reading BIN/ISO/CUE image files through libodraw
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
This subpackage contains the utility programs from libodraw, which
can read optical disc (split) RAW image files such as BIN/ISO/CUE.

%prep
%autosetup -p1
cp "%{S:2}" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libodraw.so.1*

%files devel
%license COPYING*
%doc CUE_*.pdf
%_includedir/libodraw*
%_libdir/libodraw.so
%_libdir/pkgconfig/libodraw.pc
%_mandir/man3/libodraw.3*

%files tools
%license COPYING*
%_bindir/odrawverify
%_bindir/odrawinfo
%_mandir/man1/odrawinfo.1*

%changelog
