#
# spec file for package f2fs-tools
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


Name:           f2fs-tools
Version:        1.15.0
Release:        0
Summary:        Utilities for the Flash-friendly Filesystem (F2FS)
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Filesystems
URL:            https://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git
Source:         https://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/f2fs-tools-%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(uuid)
Supplements:    filesystem(f2fs)

%description
Utilities needed to create and maintain so-called Flash-Friendly (F2)
filesystems.

%package -n libf2fs9
Summary:        Library to manipulate F2 filesystems
Group:          System/Libraries

%description -n libf2fs9
This package contains a shared library used for manipulation of F2
filesystems.

%package -n libf2fs_format8
Summary:        Library to create F2 filesystems
Group:          System/Libraries

%description -n libf2fs_format8
This package contains a shared library to format F2 filesystems.

%if 0%{?suse_version} < 1550
%package compat
Summary:        f2fs utility compatibility symlinks
Group:          System/Filesystems
BuildArch:      noarch

%description compat
This subpackage contains symbolic links /sbin/fsck.* and /sbin/mkfs.*
needed for programs that assume these locations.
%endif

%package devel
Summary:        Development files for f2fs
Group:          Development/Languages/C and C++
Requires:       libf2fs9 = %version-%release
Requires:       libf2fs_format8 = %version-%release

%description devel
This package contains development files for %name.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install -p /bin/bash
%make_install
find %buildroot -type f -name "*.la" -delete -print
# sg3_utils already ships this
rm -f "%buildroot/%_sbindir/sg_write_buffer"

mkdir -p "%buildroot/sbin" "%buildroot/%_includedir"
%if 0%{?suse_version} < 1550
ln -sf "%_sbindir"/{defrag.f2fs,dump.f2fs,f2fstat,fibmap.f2fs,fsck.f2fs,mkfs.f2fs,parse.f2fs,resize.f2fs,sload.f2fs} "%buildroot/sbin/"
%endif
# for android-tools… this is of course totally untested.
# The shared library for example has a "main" symbol :-/
cp -a include/f2fs_fs.h mkfs/f2fs_format_utils.h \
	"%buildroot/%_includedir/"

%post   -n libf2fs9 -p /sbin/ldconfig
%postun -n libf2fs9 -p /sbin/ldconfig
%post   -n libf2fs_format8 -p /sbin/ldconfig
%postun -n libf2fs_format8 -p /sbin/ldconfig

%files
%license COPYING
%_sbindir/*
%_mandir/man8/*

%files -n libf2fs9
%_libdir/libf2fs.so.*

%files -n libf2fs_format8
%_libdir/libf2fs_format.so.*

%if 0%{?suse_version} < 1550
%files compat
/sbin/*
%endif

%files devel
%_includedir/*.h
%_libdir/libf2fs*.so

%changelog
