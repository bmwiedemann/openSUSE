#
# spec file for package f2fs-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.12
Release:        0
Summary:        Utilities for the Flash-friendly Filesystem (F2FS)
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Filesystems
Url:            https://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git
Source:         %name-%version.tar.xz
Patch1:         f2fs-tools-1.4.0-bigendian.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(uuid)
Supplements:    filesystem(f2fs)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Utilities needed to create and maintain so-called Flash-Friendly (F2)
filesystems.

%package -n libf2fs6
Summary:        Library to manipulate F2 filesystems
Group:          System/Libraries

%description -n libf2fs6
This package contains a shared library used for manipulation of F2
filesystems.

%package -n libf2fs_format5
Summary:        Library to create F2 filesystems
Group:          System/Libraries

%description -n libf2fs_format5
This package contains a shared library to format F2 filesystems.

%package compat
Summary:        f2fs utility compatibility symlinks
Group:          System/Filesystems
BuildArch:      noarch

%description compat
This subpackage contains symbolic links /sbin/fsck.* and /sbin/mkfs.*
needed for programs that assume these locations.

%package devel
Summary:        Development files for f2fs
Group:          Development/Languages/C and C++
Requires:       libf2fs6 = %version
Requires:       libf2fs_format5 = %version

%description devel
This package contains development files for %name.

%prep
%setup -q
%patch -P 1 -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install -p /bin/bash
%make_install
find %buildroot -type f -name "*.la" -delete -print

mkdir -p "%buildroot/sbin" "%buildroot/%_includedir"
ln -sf "%_sbindir"/{defrag.f2fs,dump.f2fs,f2fstat,fibmap.f2fs,fsck.f2fs,mkfs.f2fs,parse.f2fs,resize.f2fs,sload.f2fs} "%buildroot/sbin/"
# for android-tools… this is of course totally untested.
# The shared library for example has a "main" symbol :-/
cp -a include/f2fs_fs.h mkfs/f2fs_format_utils.h \
	"%buildroot/%_includedir/"

%post   -n libf2fs6 -p /sbin/ldconfig
%postun -n libf2fs6 -p /sbin/ldconfig
%post   -n libf2fs_format5 -p /sbin/ldconfig
%postun -n libf2fs_format5 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING
%_sbindir/*
%_mandir/man8/*

%files -n libf2fs6
%defattr(-,root,root)
%_libdir/libf2fs.so.*

%files -n libf2fs_format5
%defattr(-,root,root)
%_libdir/libf2fs_format.so.*

%files compat
%defattr(-,root,root)
/sbin/*

%files devel
%defattr(-,root,root)
%_includedir/*.h
%_libdir/libf2fs*.so

%changelog
