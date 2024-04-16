#
# spec file for package libfplist
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


Name:           libfplist
%define lname	libfplist1
Version:        20240415
Release:        0
Summary:        Library for Apple plist formats
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libfplist
Source:         https://github.com/libyal/libfplist/releases/download/%version/libfplist-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfplist/releases/download/%version/libfplist-experimental-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfguid) >= 20240415
BuildRequires:  pkgconfig(libfvalue) >= 20220415
BuildRequires:  pkgconfig(libuna) >= 20240414
# Various notes: https://en.opensuse.org/libyal

%description
libfplist is a library for Apple plist formats. In the macOS, iOS,
NeXTSTEP, and GNUstep programming frameworks, property list files are
files that store serialized objects. Property lists are also used for
localization strings for development.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for plist formats
Group:          System/Libraries

%description -n %lname
libfplist is a library for Apple plist formats. In the macOS, iOS,
NeXTSTEP, and GNUstep programming frameworks, property list files are
files that store serialized objects. Property lists are also used for
localization strings for development.

Part of the libyal family of libraries.

Read-only supported formats:

* XML plist format

Unsupported formats:

* ASCII plist format
* Binary plist format

%package devel
Summary:        Development files for libfplist
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfplist is a library for Apple plist formats.

This subpackage contains libraries and header files for developing
applications that want to make use of libfplist.

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
%_libdir/libfplist.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%changelog
