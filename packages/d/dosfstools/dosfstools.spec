#
# spec file for package dosfstools
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


Name:           dosfstools
Version:        4.2
Release:        0
Summary:        Utilities for Making and Checking MS-DOS FAT File Systems on Linux
License:        GPL-3.0-or-later
Group:          System/Filesystems
URL:            https://github.com/dosfstools/dosfstools
Source:         https://github.com/dosfstools/dosfstools/releases/download/v%{version}/dosfstools-%{version}.tar.gz
# Source2:        https://github.com/dosfstools/dosfstools/releases/download/v%%{version}/dosfstools-%%{version}.tar.gz.sig
# Source3:        %%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)
Supplements:    filesystem(vfat)
Provides:       dosfsck
Provides:       mkdosfs

%description
The dosfstools package includes the mkdosfs and dosfsck utilities, which
respectively make and check MS-DOS FAT file systems on hard drives or on
floppies.

%prep
%setup -q

%build
%configure \
  --docdir=%{_docdir}/dosfstools \
  --enable-compat-symlinks
%make_build CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
%make_install
%if 0%{?suse_version} < 1550
mkdir %{buildroot}/sbin
ln -sf %{_sbindir}/{dosfsck,dosfslabel,mkdosfs,fsck.msdos,mkfs.msdos,fsck.fat,fsck.vfat,mkfs.fat,mkfs.vfat} %{buildroot}/sbin
%endif

%check
%make_build check

%files
%doc %{_docdir}/dosfstools
%if 0%{?suse_version} < 1550
/sbin/*
%endif
%{_sbindir}/dosfsck
%{_sbindir}/dosfslabel
%{_sbindir}/fatlabel
%{_sbindir}/fsck.fat
%{_sbindir}/fsck.msdos
%{_sbindir}/fsck.vfat
%{_sbindir}/mkdosfs
%{_sbindir}/mkfs.fat
%{_sbindir}/mkfs.msdos
%{_sbindir}/mkfs.vfat
%{_mandir}/man8/dosfsck.8%{?ext_man}
%{_mandir}/man8/dosfslabel.8%{?ext_man}
%{_mandir}/man8/fatlabel.8%{?ext_man}
%{_mandir}/man8/fsck.fat.8%{?ext_man}
%{_mandir}/man8/fsck.msdos.8%{?ext_man}
%{_mandir}/man8/fsck.vfat.8%{?ext_man}
%{_mandir}/man8/mkdosfs.8%{?ext_man}
%{_mandir}/man8/mkfs.fat.8%{?ext_man}
%{_mandir}/man8/mkfs.msdos.8%{?ext_man}
%{_mandir}/man8/mkfs.vfat.8%{?ext_man}

%changelog
