#
# spec file for package libfwevt
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


%define lname	libfwevt1
Name:           libfwevt
Version:        20240504
Release:        0
Summary:        Library for Windows XML Event Log (EVTX) data types
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfwevt
Source:         https://github.com/libyal/%name/releases/download/%version/%name-experimental-%version.tar.gz
Source2:        https://github.com/libyal/%name/releases/download/%version/%name-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfdatetime) >= 2024015
BuildRequires:  pkgconfig(libfguid) >= 20240415
BuildRequires:  pkgconfig(libfvalue) >= 20240415
BuildRequires:  pkgconfig(libfwnt) >= 20240415
BuildRequires:  pkgconfig(libuna) >= 20240414
# Various notes: https://en.opensuse.org/libyal

%description
libfwevt is a library for Windows XML Event Log (EVTX) data types.
libyal is typically used in digital forensic tools.

%package -n %lname
Summary:        Library for Windows XML Event Log data types
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libfwevt is a library for Windows XML Event Log (EVTX) data types.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwevt
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libfwevt is a library for Windows XML Event Log (EVTX) data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwevt.

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
%_libdir/libfwevt.so.*

%files devel
%license COPYING*
%_includedir/libfwevt.h
%_includedir/libfwevt/
%_libdir/libfwevt.so
%_libdir/pkgconfig/libfwevt.pc
%_mandir/man3/libfwevt.3*

%changelog
