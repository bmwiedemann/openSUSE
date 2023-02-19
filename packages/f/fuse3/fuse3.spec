#
# spec file for package fuse3
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


Name:           fuse3
Version:        3.14.0
Release:        0
Summary:        Reference implementation of the "Filesystem in Userspace"
License:        BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Filesystems
URL:            https://github.com/libfuse/libfuse
Source:         https://github.com/libfuse/libfuse/releases/download/fuse-%version/fuse-%version.tar.xz
Source1:        https://github.com/libfuse/libfuse/releases/download/fuse-%version/fuse-%version.tar.xz.asc
Source2:        fuse.keyring
Source1000:     baselibs.conf
Patch1:         conf-rename.patch
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(udev)
Requires:       util-linux >= 2.18
Requires(pre):  group(trusted)
Requires(post): permissions
Supplements:    filesystem(fuse)

%description
FUSE (Filesystem in Userspace) is an interface by the Linux kernel
for userspace programs to export a filesystem to the kernel.

This package contains helper programs for using FUSE mounts.

FUSE file systems are typically implemented as a standalone
applications in their own right and are packaged separately.

%package -n libfuse3-3
Summary:        Library of FUSE, the User space File System for GNU/Linux and BSD
Group:          System/Filesystems

%description -n libfuse3-3
FUSE (Filesystem in Userspace) is an interface by the Linux kernel
for userspace programs to export a filesystem to the kernel.

A FUSE file system is typically implemented as a standalone
application that links with libfuse. libfuse provides a C API over
the raw kernel interface.

%package doc
Summary:        Documentation for the FUSE library version 3
Group:          Documentation/HTML

%description doc
This package contains the documentation for FUSE (userspace filesystem).

%package devel
Summary:        Development package for FUSE (userspace filesystem) modules
Group:          Development/Languages/C and C++
Requires:       fuse3 = %version
Requires:       glibc-devel
Requires:       libfuse3-3 = %version

%description devel
This package contains all include files, libraries and configuration
files needed to develop programs that use the fuse (FUSE) library to
implement file systems in user space.

With fuse-devel, users can compile and install other user space file
systems.

%prep
%autosetup -p1 -n fuse-%version

%build
%define _lto_cflags %nil
%meson -Duseroot=false
%meson_build

%install
%meson_install

find "%buildroot" -type f -name "*.la" -delete -print

# Remove unneeded stuff
rm -rfv %buildroot/%_prefix/lib/udev %buildroot/%_initddir
%fdupes -s doc

%post
%set_permissions %_bindir/fusermount3

%verifyscript
%verify_permissions -e %_bindir/fusermount3

%post -n libfuse3-3 -p /sbin/ldconfig
%postun -n libfuse3-3 -p /sbin/ldconfig

%files
%license LICENSE GPL2.txt LGPL2.txt
%doc AUTHORS ChangeLog.rst
%verify(not mode) %attr(4750,root,trusted) %_bindir/fusermount3
%_sbindir/mount.fuse3
%config %_sysconfdir/fuse3.conf
%_mandir/man1/*
%_mandir/man8/*

%files -n libfuse3-3
%_libdir/libfuse3.so.3*

%files doc
%doc example doc

%files devel
%_libdir/libfuse3.so
%_includedir/fuse3/*.h
%_includedir/fuse3
%_libdir/pkgconfig/*.pc

%changelog
