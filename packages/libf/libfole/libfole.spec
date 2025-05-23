#
# spec file for package libfole
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


Name:           libfole
%define lname	libfole1
Version:        20240416
Release:        0
Summary:        Library for Object Linking and Embedding (OLE) data types
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfole
Source:         https://github.com/libyal/libfole/releases/download/%version/libfole-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libfole/releases/download/%version/libfole-alpha-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcerror) >= 20240413
# Various notes: https://en.opensuse.org/libyal

%description
libfole is a library for Object Linking and Embedding (OLE) data types.

Part of the libyal family of libraries.

%package -n %lname
Summary:        Library for Object Linking and Embedding (OLE) data types
Group:          System/Libraries

%description -n %lname
libfole is a library for Object Linking and Embedding (OLE) data types.

Part of the libyal family of libraries.

%package devel
Summary:        Development files for libfole
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfole is a library for Object Linking and Embedding (OLE) data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfole.

%prep
%autosetup -p1

%build
echo "V_%version { global: *; };" >v.sym
%configure --disable-static LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep '  local' config.log && exit 1
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING*
%_libdir/libfole.so.*

%files devel
%_includedir/libfole.h
%_includedir/libfole/
%_libdir/libfole.so
%_libdir/pkgconfig/libfole.pc
%_mandir/man3/libfole.3*

%changelog
