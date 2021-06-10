#
# spec file for package libfsapfs
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


Name:           libfsapfs
Version:        20210513
Release:        0
Summary:        Library and tools to access the Apple File System (APFS)
License:        LGPL-3.0-only
Group:          System/Filesystems
URL:            https://github.com/libyal/libfsapfs
Source:         %name-%version.tar.xz
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcaes) >= 20201012
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
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib) >= 1.2.5

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
Requires:       %{name} = %{version}

%description devel
Development files for %{name}.

%package -n libfsapfs1
Summary:        Library for access the Apple File System (APFS)
Group:          System/Libraries

%description -n libfsapfs1
libfsapfs1 is a library for access the Apple File System (APFS).

%package -n python3-libfsapfs
Summary:        Python bindings for %{name}
Group:          System/Filesystems
Requires:       libfsapfs1

%description -n python3-libfsapfs
Python bindings for %{name}, a library for access the Apple File System
(APFS).

%prep
%autosetup -p1

%build
if [ ! -e configure ]; then ./autogen.sh; fi
%define _lto_cflags -ffat-lto-objects
export LDFLAGS="-Wl,-z,relro,-z,now"
export CFLAGS="%{optflags}"
%configure --disable-static \
  --enable-wide-character-type \
  --enable-verbose-output \
  --enable-debug-output \
  --enable-python3

%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%check
make check || /bin/true

%post -n libfsapfs1 -p /sbin/ldconfig
%postun -n libfsapfs1 -p /sbin/ldconfig

%files
%license COPYING*
%{_bindir}/fsapfsinfo
%{_bindir}/fsapfsmount
%{_mandir}/man*/*

%files devel
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/*

%files -n libfsapfs1
%{_libdir}/%{name}*so.*

%files -n python3-libfsapfs
%{python3_sitearch}/pyfsapfs*

%changelog
