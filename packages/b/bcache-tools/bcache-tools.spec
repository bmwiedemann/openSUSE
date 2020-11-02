#
# spec file for package bcache-tools
#
# Copyright (c) 2020 SUSE LLC
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


Name:           bcache-tools
Version:        1.1
Release:        0
Summary:        Configuration utilities for bcache
License:        GPL-2.0-only
Group:          System/Base
URL:            http://bcache.evilpiepirate.org/

Source:         %name-%version.tar.xz
Patch1:         0001-bcache-tools-set-zoned-size-aligned-data_offset-on-b.patch
Patch2:         0002-bcache-tools-add-is_zoned_device.patch
Patch3:         0003-bcache-tools-convert-writeback-to-writethrough-mode-.patch
Patch4:         0004-bcache-tools-add-struct-cache_sb_disk-into-bcache.h.patch
Patch5:         0005-bcache-tools-bitwise.h-more-swap-bitwise-for-differe.patch
Patch6:         0006-bcache-tools-list.h-only-define-offsetof-when-it-is-.patch
Patch7:         0007-bcache-tools-add-to_cache_sb-and-to_cache_sb_disk.patch
Patch8:         0008-bcache-tools-define-separated-super-block-for-in-mem.patch
Patch9:         0009-bcache-tools-upgrade-super-block-versions-for-featur.patch
Patch10:        0010-bcache-tools-add-large_bucket-incompat-feature.patch
Patch11:        0011-bcache-tools-add-print_cache_set_supported_feature_s.patch
Patch12:        0012-bcache-tools-Fix-potential-coredump-issues.patch
Patch13:        0013-bcache-tools-Export-CACHED_UUID-and-CACHED_LABEL.patch
Patch14:        0014-bcache-tools-Remove-the-dependency-on-libsmartcols.patch
Patch15:        0015-bcache-tools-make-permit-only-one-cache-device-to-be.patch
Patch16:        0016-bcache-tools-add-bcache-status.patch
Patch17:        0017-bcache-tools-add-man-page-bcache-status.8.patch
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)

%description
This package contains utilities for configuring the bcache Module.

%prep
%autosetup -p1

%build
export SUSE_ASNEEDED=0
%make_build all \
	CFLAGS="%optflags $(pkg-config blkid uuid --cflags) -std=gnu99" \
	LDFLAGS="$(pkg-config blkid uuid --libs)"

%install
b="%buildroot"
# Without these existing, make install would fail
mkdir -p "$b"/{sbin,%_sbindir,%_mandir/man8,/lib/udev/rules.d}
mkdir -p "$b/%_sysconfdir/initramfs-tools/scripts/init-premount"
mkdir -p "$b/%_sysconfdir/initramfs-tools/hooks"
%make_install DRACUTLIBDIR="%_prefix/lib/dracut"
# Not used in openSUSE
rm -Rf "$b/%_sysconfdir/initramfs-tools" "$b/%_prefix/lib/initcpio" \
	"$b/%_datadir/initramfs-tools"
mkdir -p "$b/%_prefix/lib"
mv "$b/lib/udev" "$b/%_prefix/lib/"

%files
%_sbindir/bcache-super-show
%_sbindir/make-bcache
%_sbindir/bcache
%_prefix/lib/dracut/
%_prefix/lib/udev
%_mandir/man8/*.8*
%license COPYING

%changelog
