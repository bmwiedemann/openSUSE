#
# spec file for package libbfoverlay
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


Name:           libbfoverlay
%define lname	libbfoverlay1
Version:        20240505
Release:        0
Summary:        Library for file overlay support in bfio
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libbfoverlay
Source:         https://github.com/libyal/libbfoverlay/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libbfoverlay/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfvalue) >= 20240414
BuildRequires:  pkgconfig(libuna) >= 20240414
# Various notes: https://en.opensuse.org/libyal

%description
libbfoverlay is a library to provide basic file overlay support.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for Update Sequence Number (USN) Journal data types
Group:          System/Libraries

%description -n %lname
libbfoverlay is a library to provide basic file overlay support.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libbfoverlay
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libbfoverlay is a library to provide basic file overlay support.

This subpackage contains libraries and header files for developing
applications that want to make use of libbfoverlay.

%package tools
Summary:        Utilities to assist with bfio file overlays
Group:          Productivity/File utilities

%description tools
This subpackage provides the utilities from libbfoverlay.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libbfoverlay.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files tools
%_bindir/bfoverlay*

%changelog
