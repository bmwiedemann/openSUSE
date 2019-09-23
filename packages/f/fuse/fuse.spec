#
# spec file for package fuse
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fuse
Version:        2.9.8
Release:        0
Summary:        User space File System
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Filesystems
URL:            https://github.com/libfuse/libfuse
Source:         https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
Source2:        fuse.rpmlintrc
Source3:        baselibs.conf
Source4:        fuse.conf
Source5:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz.asc
Source6:        fuse.keyring
Patch0:         fuse-install-fix.diff
Patch3:         fusermount-compile-as-pie.patch
Patch4:         aarch64-build-fix.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         permissions
%if 0%{?suse_version} > 1320
Requires(pre):  group(trusted)
%endif
%if 0%{?suse_version} > 1130
Requires:       util-linux >= 2.18
%else
Requires:       util-linux(fake+no-canonicalize)
%endif
%if 0%{?suse_version} >= 1000
Supplements:    filesystem(fuse)
%endif

%description
With FUSE, a user space program can export a file system through the
kernel-default (Linux kernel).

User space file systems which are implemented using FUSE are provided
by the following packages:

- curlftpfs (mount FTP servers),

- encfs (layered file encryption),

- fuseiso (mount iso, img, bin, mdf and nrg CD-ROM images),

- fusepod (mount iPods),

- fusesmb (mount a fully browseable network neighborhood),

- gphotofs (mount gphoto-supported cameras),

- ntfs-3g (mount NTFS volumes read-write),

- obexfs (mount of bluetooth devices),

- sshfs (mount over ssh),

- wdfs (mount of WebDAV shares)

This package contains the mount binaries for fuse (might not be needed
by some FUSE filesystems like ntfs-3g) and the documentation for FUSE.

After installing fuse-devel, administrators can compile and install
other user space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%package -n libulockmgr1
Summary:        Library of FUSE, the User space File System for GNU/Linux and BSD
Group:          System/Filesystems

%description -n libulockmgr1
With FUSE, a user space program can export a file system through the
kernel-default (Linux kernel).

%package -n libfuse2
Summary:        Library of FUSE, the User space File System for GNU/Linux and BSD
Group:          System/Filesystems

%description -n libfuse2
With FUSE, a user space program can export a file system through the
kernel-default (Linux kernel).

A FUSE file system which only needs libfuse2 is ntfs-3g, other FUSE
file systems might need the fuse package in addition to have fusermount
and /sbin/mount.fuse.

After installing fuse-devel, administrators can compile and install
other user space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%package doc
Summary:        Document package for FUSE (userspace filesystem)
Group:          Development/Languages/C and C++

%description doc
This package contains the documentation for FUSE (userspace filesystem).

%package devel
Summary:        Development package for FUSE (userspace filesystem) modules
Group:          Development/Languages/C and C++
Requires:       fuse = %{version}
Requires:       fuse-doc = %{version}
Requires:       glibc-devel
Requires:       libfuse2 = %{version}
Requires:       libulockmgr1 = %{version}

%description devel
This package contains all include files, libraries and configuration
files needed to develop programs that use the fuse (FUSE) library to
implement kernel-default (Linux) file systems in user space.

With fuse-devel, administrators can compile and install other user
space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%package devel-static
Summary:        Development package for FUSE (userspace filesystem) modules
Group:          Development/Languages/C and C++
Requires:       fuse-devel = %{version}
Provides:       fuse-devel:%{_libdir}/libfuse.a

%description devel-static
This package contains all include files, libraries and configuration
files needed to develop programs that use the fuse (FUSE) library to
implement kernel-default (Linux) file systems in user space.

With fuse-devel, administrators can compile and install other user
space file systems which can be found at
https://github.com/libfuse/libfuse/wiki/

%prep
%setup -q
%patch0 -p1
%patch3 -p1
%patch4

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -g -fno-strict-aliasing"
export MOUNT_FUSE_PATH=%{_sbindir}
autoreconf -fi
%configure --with-pic \
    --with-pkgconfigdir=%{_libdir}/pkgconfig \
    --enable-lib \
    --enable-util \
    --enable-example
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_sysconfdir}/init.d
install -m644 -D %{SOURCE4} %{buildroot}/%{_sysconfdir}/fuse.conf
# Needed for OpenSUSE buildservice
%if 0%{?suse_version} <= 1020
install -m644 -D util/udev.rules %{buildroot}/%{_sysconfdir}/udev/rules.d/99-fuse.rules
%endif
find %{buildroot} -type f -name "*.la" -delete -print
# not needed for fuse, might reappar in separate package:
rm -f %{buildroot}/%{_libdir}/libulockmgr.a
#UsrMerge
mkdir %{buildroot}/sbin
mkdir %{buildroot}/%{_lib}
ln -s -v %{_sbindir}/mount.fuse %{buildroot}/sbin
pushd %{buildroot}/%{_libdir}
for libname in $(ls *.so.*);do
ln -s -v /%{_libdir}/$libname %{buildroot}/%{_lib}
done
popd
#EndUsrMerge

(cd example && make clean)
rm -rf example/.deps example/Makefile.am example/Makefile.in
rm -rf doc/Makefile.am doc/Makefile.in doc/Makefile

%post
%if 0%{?suse_version} >= 1140
%set_permissions %{_bindir}/fusermount
%else
%run_permissions
%endif

%verifyscript
%verify_permissions -e %{_bindir}/fusermount

%post -n libfuse2 -p /sbin/ldconfig
%postun -n libfuse2 -p /sbin/ldconfig
%post -n libulockmgr1 -p /sbin/ldconfig
%postun -n libulockmgr1 -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README*
%if 0%{?suse_version} <= 1020
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%{_sysconfdir}/udev/rules.d/99-fuse.rules
%endif
%verify(not mode) %attr(4750,root,trusted) %{_bindir}/fusermount
#UsrMerge
/sbin/mount.fuse
#EndUsrMerge
%{_sbindir}/mount.fuse
%config %{_sysconfdir}/fuse.conf
%{_bindir}/ulockmgr_server
%{_mandir}/man1/fusermount.1%{?ext_man}
%{_mandir}/man1/ulockmgr_server.1%{?ext_man}
%{_mandir}/man8/mount.fuse.8%{?ext_man}

%files -n libfuse2
#UsrMerge
/%{_lib}/libfuse.so.2*
#EndUsrMerge
%{_libdir}/libfuse.so.2*

%files -n libulockmgr1
#UsrMerge
/%{_lib}/libulockmgr.so.*
#EndUsrMerge
%{_libdir}/libulockmgr.so.*

%files doc
%doc example doc

%files devel
%{_libdir}/libfuse.so
%{_libdir}/libulockmgr.so
%{_includedir}/fuse.h
%{_includedir}/fuse
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ulockmgr.h

%files devel-static
%{_libdir}/libfuse.a

%changelog
