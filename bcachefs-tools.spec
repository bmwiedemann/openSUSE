#
# spec file for package bcachefs-tools
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


Name:           bcachefs-tools
Version:        24
Release:        0
Summary:        Configuration utilities for bcachefs
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://bcachefs.org/

Source:         %name-%version.tar.xz
BuildRequires:  libaio-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
Bcachefs is a filesystem for Linux, with an emphasis on reliability
and robustness.

* Copy on write (COW) - like zfs or btrfs
* Full data and metadata checksumming
* Multiple devices
* Replication
* Erasure coding
* Caching
* Compression
* Encryption
* Snapshots

This package contains utilities for creating and mounting bcachefs.

%prep
%autosetup -p1

%build
%make_build NO_RUST=1 EXTRA_CFLAGS="%optflags"

%install
b="%buildroot"
%make_install PREFIX="%_prefix" ROOT_SBINDIR="%_sbindir" NO_RUST=1
if [ "%_lib" != lib ]; then
	mkdir -p "$b/%_libdir"
	mv "$b/usr/lib/"*.so "$b/%_libdir/"
fi
# this ain't no debian
rm -Rf "$b/etc/initramfs-tools" "$b/%_datadir/initramfs-tools"

%files
%_sbindir/*bcache*
%_mandir/man8/*.8*
%_libdir/libbcachefs.so
%license COPYING

%changelog
