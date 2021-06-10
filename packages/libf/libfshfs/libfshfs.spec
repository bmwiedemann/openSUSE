#
# spec file for package libfshfs
#
# Copyright (c) 2021 SUSE LLC
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


%define lname	libfshfs1
Name:           libfshfs
Version:        20210510
Release:        0
Summary:        Library and tools to access the Mac OS Hierarchical File System (HFS)
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfshfs
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
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
BuildRequires:  pkgconfig(libfcache) >= 20200708
BuildRequires:  pkgconfig(libfdata) >= 20201129
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libhmac) >= 20200104
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
Read-only supported HFS formats:

* HFS+, Mac OS 10.3 and later (Unicode 3.2 case-insensitive)
* HFSX, Mac OS 10.3 and later (Unicode 3.2 case-sensitive)

Unsupported HFS formats:

* (traditional) HFS
* HFS+, Mac OS 8.1 through 10.2 (Unicode 2.1 case-insensitive)
* HFSX, Mac OS 8.1 through 10.2 (Unicode 2.1 case-sensitive)

Supported HFS format features:

* ZLIB (DEFLATE) compression
* LZVN compression

Unsupported HFS format features:

* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10

Planned:

* Complete resource fork support
* Complete named fork (extended attributes) support

%package -n %{lname}
Summary:        Library and tools to access the Mac OS Hierarchical File System (HFS)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Read-only supported HFS formats:

* HFS+, Mac OS 10.3 and later (Unicode 3.2 case-insensitive)
* HFSX, Mac OS 10.3 and later (Unicode 3.2 case-sensitive)

Unsupported HFS formats:

* (traditional) HFS
* HFS+, Mac OS 8.1 through 10.2 (Unicode 2.1 case-insensitive)
* HFSX, Mac OS 8.1 through 10.2 (Unicode 2.1 case-sensitive)

Supported HFS format features:

* ZLIB (DEFLATE) compression
* LZVN compression

Unsupported HFS format features:

* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10

Planned:

* Complete resource fork support
* Complete named fork (extended attributes) support

%package tools
Summary:        Tools to access the Mac OS Hierarchical File System (HFS)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to access the Mac OS Hierarchical File System (HFS).  See libfshfs for additional details.

%package devel
Summary:        Development files for libfshfs, Mac OS Hierarchical File System (HFS) library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libfshfs is a library to access the Mac OS Hierarchical File System (HFS) format.  see libfshfs for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libfshfs.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfshfs, a Mac OS Hierarchical FIle System (HFS) parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
Provides:       pyfshfs

%description -n python3-%{name}
libfshfs is a library to access Mac OS Hierarchical File System (HFS) format. See libfshfs for details.

This package contains Python 3 bindings for libfshfs.

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfshfs.so.*

%files tools
%license COPYING*
%{_bindir}/fshfs*
%{_mandir}/man1/fshfs*.1*

%files devel
%license COPYING*
%{_includedir}/libfshfs.h
%{_includedir}/libfshfs/
%{_libdir}/libfshfs.so
%{_libdir}/pkgconfig/libfshfs.pc
%{_mandir}/man3/libfshfs.3*

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/pyfshfs.so

%changelog
