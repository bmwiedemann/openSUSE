#
# spec file for package bcachefs-tools
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        1.31.1
Release:        0
Summary:        Configuration utilities for bcachefs
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://bcachefs.org/
#Git-Clone:     https://evilpiepirate.org/git/bcachefs-tools.git
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
%if 0%{?suse_version} >= 1690
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-devel
BuildRequires:  kernel-syms
%kernel_module_package -n bcachefs -x xen -p %_sourcedir/bcachefs-preamble
%endif

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
# The combination of -Og/-O1/-O2 + LTO produces a broken mkfs.bcachefs which
# crashes (disabling one of the two fixes it). Given this -O+LTO scenario, if
# -g2 is also used, the lto1-wpa process runs into memory exhaustion (>80GB)
# and the build fails altogether.
%define _lto_cflags %nil
# gh/koverstreet/bcachefs-tools#237
# bcachefs-tools uses malloc_usable_size, which is incompatible
# with fortification level 3
export CFLAGS="${RPM_OPT_FLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
export CXXFLAGS="$CFLAGS"
# Workaround antisocial Makefile that forces its own -O level
export EXTRA_CFLAGS="$CFLAGS"
%make_build PREFIX="%_prefix" ROOT_SBINDIR="%_sbindir"

%if 0%{?suse_version} >= 1690
%make_build install_dkms DKMSDIR="/tmp/kb"
cd /tmp/kb
for kmp_flavor in %{?flavors_to_build}; do
        rm -Rf "../obj-$kmp_flavor"
        cp -a . "../obj-$kmp_flavor"
        cd "../obj-$kmp_flavor/"
        %make_build KDIR="/usr/src/linux-obj/%_target_cpu/$kmp_flavor"
        cd -
done
%endif

%install
%make_install PREFIX="%_prefix" ROOT_SBINDIR="%_sbindir" DKMSDIR=/tmpdel
rm -Rf "%buildroot/tmpdel"
# this ain't no debian
rm -Rf "%buildroot/etc/initramfs-tools" "%buildroot/%_datadir/initramfs-tools"

%if 0%{?suse_version} >= 1690
cd /tmp/kb
for kmp_flavor in %flavors_to_build; do
	cd "../obj-$kmp_flavor/"
        %make_build -C "/usr/src/linux-obj/%_target_cpu/$kmp_flavor" \
		M="$PWD" INSTALL_MOD_PATH="%buildroot" modules_install
	cd -
done
%endif

%files
%_sbindir/*bcache*
%_udevrulesdir/64-bcachefs.rules
%_mandir/man8/*.8*
%license COPYING
%doc doc/bcachefs-principles-of-operation.tex

%changelog
