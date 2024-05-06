#
# spec file for package libodraw
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


Name:           libodraw
%define lname	libodraw1
Version:        20240505
Release:        0
Summary:        Library and tools to access to optical disc (split) RAW image files
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libodraw
Source:         https://github.com/libyal/libodraw/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libodraw/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source9:        CUE_sheet_format.pdf
BuildRequires:  bison
BuildRequires:  c_compiler
BuildRequires:  flex
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 2024014
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libhmac) >= 20240414
BuildRequires:  pkgconfig(libuna) >= 20240414
# Various notes: https://en.opensuse.org/libyal

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
cp %_sourcedir/*.pdf .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%ldconfig_scriptlets -n %lname

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
