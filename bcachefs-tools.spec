#
# spec file for package bcachefs-tools
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


Name:           bcachefs-tools
Version:        1.9.1
Release:        0
Summary:        Configuration utilities for bcachefs
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://bcachefs.org/
Source0:        https://evilpiepirate.org/%name/%name-vendored-%version.tar.zst
Source1:        https://evilpiepirate.org/%name/%name-vendored-%version.tar.sign
Source2:        %{name}.keyring
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  libaio-devel >= 0.3.111
BuildRequires:  pkg-config
BuildRequires:  zstd
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
Bcachefs is a filesystem for Linux, with an emphasis on reliability
and robustness.

* Copy on write (COW) like zfs or btrfs
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
# gh/koverstreet/bcachefs-tools#237
# bcachefs-tools uses malloc_usable_size, which is incompatible
# with fortification level 3
export CFLAGS="${RPM_OPT_FLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
export CXXFLAGS="${RPM_OPT_FLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
%make_build PREFIX="%_prefix" ROOT_SBINDIR="%_sbindir"

%install
%make_install PREFIX="%_prefix" ROOT_SBINDIR="%_sbindir"
# this ain't no debian
rm -Rf "%buildroot/etc/initramfs-tools" "%buildroot/%_datadir/initramfs-tools"

%pre
%service_add_pre bcachefsck_all.service bcachefsck_all_fail.service

%post
%service_add_post bcachefsck_all.service bcachefsck_all_fail.service

%preun
%service_del_preun bcachefsck_all.service bcachefsck_all_fail.service

%postun
%service_del_postun bcachefsck_all.service bcachefsck_all_fail.service

%files
%_sbindir/*bcache*
%_unitdir/bcachefsck*
%_unitdir/system-bcachefsck*
%_libexecdir/bcachefsck*
%_udevrulesdir/64-bcachefs.rules
%_mandir/man8/*.8*
%license COPYING
%doc doc/bcachefs-principles-of-operation.tex

%changelog
