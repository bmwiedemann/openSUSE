#
# spec file for package partclone
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Mariusz Fik <fisiu@opensuse.org>
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


Name:           partclone
Version:        0.3.23
Release:        0
Summary:        File System Clone Utilities
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://partclone.org/
Source:         https://github.com/Thomas-Tsai/partclone/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  libbtrfs-devel
BuildRequires:  nilfs-utils-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libntfs-3g)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)

%description
A set of file system clone utilities, including
ext2/3, reiserfs, reiser4, xfs, hfs+ file systems

%lang_package

%prep
%autosetup

%build
export CFLAGS="%{optflags} -fcommon"
autoreconf -fiv
%configure \
  --enable-ncursesw \
  --enable-fuse \
  --enable-fs-test \
  --enable-btrfs \
  --enable-extfs \
  --enable-fat \
  --enable-hfsp \
  --enable-apfs \
  --enable-ntfs \
  --enable-xfs \
  --enable-f2fs \
  --enable-nilfs2 \
  --enable-minix \
  --enable-exfat
# During build following occurs, but it seems harmless
# files fail-mbr.bin and fail-mbr.bin.orig differ significantly:
%make_build LIBS="-lncursesw -lpthread -lfuse" ||:

%install
%make_install INSTLIBDIR=%{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}
%find_lang %{name}

%files
%license COPYING
%doc ChangeLog README.md
%{_sbindir}/partclone.apfs
%{_sbindir}/partclone.btrfs
%{_sbindir}/partclone.chkimg
%{_sbindir}/partclone.dd
%{_sbindir}/partclone.ext2
%{_sbindir}/partclone.ext3
%{_sbindir}/partclone.ext4
%{_sbindir}/partclone.ext4dev
%{_sbindir}/partclone.extfs
%{_sbindir}/partclone.exfat
%{_sbindir}/partclone.f2fs
%{_sbindir}/partclone.fat
%{_sbindir}/partclone.fat12
%{_sbindir}/partclone.fat16
%{_sbindir}/partclone.fat32
%{_sbindir}/partclone.imgfuse
%{_sbindir}/partclone.hfs+
%{_sbindir}/partclone.hfsp
%{_sbindir}/partclone.hfsplus
%{_sbindir}/partclone.imager
%{_sbindir}/partclone.info
%{_sbindir}/partclone.minix
%{_sbindir}/partclone.nilfs2
%{_sbindir}/partclone.ntfs
%{_sbindir}/partclone.ntfsfixboot
%{_sbindir}/partclone.ntfsreloc
%{_sbindir}/partclone.restore
%{_sbindir}/partclone.vfat
%{_sbindir}/partclone.xfs
%{_mandir}/man8/partclone.8%{?ext_man}
%{_mandir}/man8/partclone.btrfs.8%{?ext_man}
%{_mandir}/man8/partclone.chkimg.8%{?ext_man}
%{_mandir}/man8/partclone.dd.8%{?ext_man}
%{_mandir}/man8/partclone.ext2.8%{?ext_man}
%{_mandir}/man8/partclone.ext3.8%{?ext_man}
%{_mandir}/man8/partclone.ext4.8%{?ext_man}
%{_mandir}/man8/partclone.ext4dev.8%{?ext_man}
%{_mandir}/man8/partclone.extfs.8%{?ext_man}
%{_mandir}/man8/partclone.exfat.8%{?ext_man}
%{_mandir}/man8/partclone.f2fs.8%{?ext_man}
%{_mandir}/man8/partclone.fat.8%{?ext_man}
%{_mandir}/man8/partclone.fat12.8%{?ext_man}
%{_mandir}/man8/partclone.fat16.8%{?ext_man}
%{_mandir}/man8/partclone.fat32.8%{?ext_man}
%{_mandir}/man8/partclone.hfs+.8%{?ext_man}
%{_mandir}/man8/partclone.hfsp.8%{?ext_man}
%{_mandir}/man8/partclone.hfsplus.8%{?ext_man}
%{_mandir}/man8/partclone.imager.8%{?ext_man}
%{_mandir}/man8/partclone.info.8%{?ext_man}
%{_mandir}/man8/partclone.minix.8%{?ext_man}
%{_mandir}/man8/partclone.nilfs2.8%{?ext_man}
%{_mandir}/man8/partclone.ntfs.8%{?ext_man}
%{_mandir}/man8/partclone.ntfsfixboot.8%{?ext_man}
%{_mandir}/man8/partclone.ntfsreloc.8%{?ext_man}
%{_mandir}/man8/partclone.restore.8%{?ext_man}
%{_mandir}/man8/partclone.vfat.8%{?ext_man}
%{_mandir}/man8/partclone.xfs.8%{?ext_man}
%{_datadir}/partclone

%files lang -f %{name}.lang

%changelog
