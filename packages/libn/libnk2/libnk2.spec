#
# spec file for package libnk2
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


Name:           libnk2
%define lname	libnk2-1
Version:        20240426
Release:        0
Summary:        Library and tools to access the Outlook Nickfile (NK2) format
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libnk2
Source:         https://github.com/libyal/libnk2/releases/download/%version/%name-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libnk2/releases/download/%version/%name-alpha-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfdatetime) >= 20240415
BuildRequires:  pkgconfig(libfguid) >= 20240415
BuildRequires:  pkgconfig(libfmapi) >= 20240415
BuildRequires:  pkgconfig(libfvalue) >= 20240415
BuildRequires:  pkgconfig(libfwnt) >= 20240415
BuildRequires:  pkgconfig(libuna) >= 20240414
# Various notes: https://en.opensuse.org/libyal

%description
libnk2 is a library to access Outlook's Nickfile (NK2) format.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for accessing the Outlook Nickfile (NK2) format
Group:          System/Libraries

%description -n %lname
libnk2 is a library to access Outlook's Nickfile (NK2) format.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libnk2
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libnk2 is a library to access Outlook's Nickfile (NK2) format.

This subpackage contains libraries and header files for developing
applications that want to make use of libnk2.

%package tools
Summary:        Utilities for reading Outlook Nickfile files
Group:          Productivity/File utilities

%description tools
This subpackage contains the utility programs from libnk2 to
read Outlook Nickfile files.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libnk2.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files tools
%_bindir/nk2*
%_mandir/man1/nk2*

%changelog
