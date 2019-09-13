#
# spec file for package mtd-utils
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


Name:           mtd-utils
Version:        2.1.0
Release:        0
Summary:        Tools for maintaining Memory Technology Devices
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            http://www.linux-mtd.infradead.org/
Source0:        ftp://ftp.infradead.org/pub/mtd-utils/mtd-utils-%{version}.tar.bz2
Source1:        ftp://ftp.infradead.org/pub/mtd-utils/mtd-utils-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  libacl-devel
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
Supplements:    filesystem(jffs2)
Supplements:    filesystem(ubifs)

%description
This package contains tools for erasing and formatting flash devices,
including JFFS2, M-Systems DiskOnChip devices, etc.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%license COPYING
%doc ubifs-utils/mkfs.ubifs/README
%{_sbindir}/doc_loadbios
%{_sbindir}/docfdisk
%{_sbindir}/flash_erase
%{_sbindir}/flash_eraseall
%{_sbindir}/flash_lock
%{_sbindir}/flash_otp_dump
%{_sbindir}/flash_otp_info
%{_sbindir}/flash_otp_lock
%{_sbindir}/flash_otp_write
%{_sbindir}/flash_unlock
%{_sbindir}/flashcp
%{_sbindir}/ftl_check
%{_sbindir}/ftl_format
%{_sbindir}/jffs2dump
%{_sbindir}/jffs2reader
%{_sbindir}/lsmtd
%{_sbindir}/mkfs.jffs2
%{_sbindir}/mkfs.ubifs
%{_sbindir}/mtd_debug
%{_sbindir}/mtdinfo
%{_sbindir}/mtdpart
%{_sbindir}/nanddump
%{_sbindir}/nandtest
%{_sbindir}/nandwrite
%{_sbindir}/nftl_format
%{_sbindir}/nftldump
%{_sbindir}/recv_image
%{_sbindir}/rfddump
%{_sbindir}/rfdformat
%{_sbindir}/serve_image
%{_sbindir}/sumtool
%{_sbindir}/ubiattach
%{_sbindir}/ubiblock
%{_sbindir}/ubicrc32
%{_sbindir}/ubidetach
%{_sbindir}/ubiformat
%{_sbindir}/ubimkvol
%{_sbindir}/ubinfo
%{_sbindir}/ubinize
%{_sbindir}/ubirename
%{_sbindir}/ubirmvol
%{_sbindir}/ubirsvol
%{_sbindir}/ubiupdatevol
%{_mandir}/man1/mkfs.jffs2.1%{?ext_man}
%{_mandir}/man8/lsmtd.8%{?ext_man}
%{_mandir}/man8/ubinize.8%{?ext_man}

%changelog
