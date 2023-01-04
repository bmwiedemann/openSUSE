#
# spec file for package libfshfs
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


%define lname	libfshfs1
Name:           libfshfs
Version:        20220831
Release:        0
Summary:        Library and tools to access the Mac OS Hierarchical File System (HFS)
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libfshfs
Source:         https://github.com/libyal/libfshfs/releases/download/%version/libfshfs-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfshfs/releases/download/%version/libfshfs-experimental-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20220120
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20220110
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfmos) >= 20220811
BuildRequires:  pkgconfig(libhmac) >= 20220425
BuildRequires:  pkgconfig(libuna) >= 20220601
BuildRequires:  pkgconfig(zlib)
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

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
* extended attributes

Unsupported HFS format features:

* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10

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
* extended attributes

Unsupported HFS format features:

* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10

%package tools
Summary:        Tools to access the Mac OS Hierarchical File System (HFS)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Tools to access the Mac OS Hierarchical File System (HFS). See
libfshfs for additional details.

%package devel
Summary:        Development files for libfshfs, Mac OS Hierarchical File System (HFS) library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libfshfs is a library to access the Mac OS Hierarchical File System
(HFS) format. see libfshfs for details.

This subpackage contains libraries and header files for developing
applications that want to make use of libfshfs.

%prep
%autosetup -p1

%build
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type --enable-python \
	PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* %buildroot/
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/libfshfs.so.*

%files -n %name-tools
%license COPYING*
%{_bindir}/fshfs*
%{_mandir}/man1/fshfs*.1*

%files -n %name-devel
%license COPYING*
%{_includedir}/libfshfs.h
%{_includedir}/libfshfs/
%{_libdir}/libfshfs.so
%{_libdir}/pkgconfig/libfshfs.pc
%{_mandir}/man3/libfshfs.3*

%files %python_files
%license COPYING*
%{python_sitearch}/pyfshfs.so

%changelog
