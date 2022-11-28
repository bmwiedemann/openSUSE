#
# spec file for package libfsapfs
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libfsapfs
Version:        20221102
Release:        0
Summary:        Library and tools to access the Apple File System (APFS)
License:        LGPL-3.0-only
Group:          System/Filesystems
URL:            https://github.com/libyal/libfsapfs
Source:         https://github.com/libyal/libfsapfs/releases/download/%version/libfsapfs-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libfsapfs/releases/download/%version/libfsapfs-experimental-%version.tar.gz.asc
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcaes) >= 20220529
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
BuildRequires:  pkgconfig(libuna) >= 20220611
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib) >= 1.2.5
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
libfsapfs is a library to access the Apple File System (APFS).

Read-only supported APFS formats:

* version 2

Supported APFS format features:

* ZLIB (DEFLATE) compression
* LZVN compression
* encryption

Unsupported APFS format features:

* APFS version 1
* Fusion drive (NX_INCOMPAT_FUSION)
* snapshots
* LZFSE compression, compression methods 11 and 12
* "uncompressed", compression methods 1, 9 and 10
* T2 encryption

%package devel
Summary:        Development files for libfsapfs
Group:          Development/Languages/C and C++
Requires:       libfsapfs1 = %version

%description devel
Development files for %{name}.

%package -n libfsapfs1
Summary:        Library for access the Apple File System (APFS)
Group:          System/Libraries

%description -n libfsapfs1
libfsapfs1 is a library for access the Apple File System (APFS).

%prep
%autosetup -p1

%build
%define _lto_cflags -ffat-lto-objects
export LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS="%{optflags}"
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static \
  --enable-wide-character-type \
  --enable-verbose-output \
  --enable-debug-output \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* "%buildroot/"
rm -fv "%buildroot/%_libdir"/*.la

%check
make check || /bin/true

%post -n libfsapfs1 -p /sbin/ldconfig
%postun -n libfsapfs1 -p /sbin/ldconfig

%files -n %name
%license COPYING*
%{_bindir}/fsapfsinfo
%{_bindir}/fsapfsmount
%{_mandir}/man*/*

%files -n %name-devel
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/*

%files -n libfsapfs1
%{_libdir}/%{name}*so.*

%files %python_files
%{python_sitearch}/pyfsapfs*

%changelog
