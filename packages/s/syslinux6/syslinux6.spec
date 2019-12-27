#
# spec file for package syslinux6
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


Name:           syslinux6
ExclusiveArch:  %ix86 x86_64
BuildRequires:  glibc-devel-32bit
BuildRequires:  libext2fs-devel
BuildRequires:  libpng-devel
BuildRequires:  libuuid-devel
BuildRequires:  nasm
BuildRequires:  netpbm
BuildRequires:  python3
BuildRequires:  xz
BuildRequires:  asciidoc
# lots of assembler here that would need to be changed :(
#!BuildIgnore:	gcc-PIE
Url:            http://www.syslinux.org/wiki/index.php/The_Syslinux_Project
Suggests:       mtools
Summary:        Boot Loader for Linux
License:        GPL-2.0-or-later
Group:          System/Boot
Version:        6.03.99+20171123
Release:        0
Source0:        syslinux-%{version}.tar.xz
Source1:        isolinux-config
Source2:        README.gfxboot
Source3:        baselibs.conf
Source4:        syslinux6-rpmlintrc
Patch10:        10_isolinux_config.diff
Patch11:        11_md5pass.diff
Patch12:        12_mboot_bootif.diff
Patch13:        13_mtime.diff
Patch14:        14_miniacc.diff
Patch15:        15_fix_keywords_path.diff
Patch16:        16_add_install_all_target.diff
Patch17:        17_remove_gnu_note.diff
Patch18:        18_lzo.diff
Conflicts:      syslinux < %{version}

%description
SYSLINUX is a boot loader for the Linux operating system which operates
off an MS-DOS or Windows FAT file system. It is intended to simplify
first-time installation of Linux and for creation of rescue and other
special purpose boot disks.



Authors:
--------
    H. Peter Anvin <hpa@zytor.com>

%prep
%setup -q -n syslinux-%{version}
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
cp %{SOURCE2} .
make spotless
make PYTHON=python3 bios all
%ifarch x86_64
make PYTHON=python3 efi64 all
make PYTHON=python3 efi32 all
%endif
make -C txt

%install
make bios install \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_bindir} \
	LIBDIR=%{_datadir} INCDIR=%{_includedir} MANDIR=%{_mandir} \
	TFTPBOOT=/tftpboot EXTLINUXDIR=/boot/extlinux
%ifarch x86_64
make efi64 install \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_bindir} \
	LIBDIR=%{_datadir} INCDIR=%{_includedir} MANDIR=%{_mandir} \
	TFTPBOOT=/tftpboot EXTLINUXDIR=/boot/extlinux

make efi32 install \
	INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_bindir} \
	LIBDIR=%{_datadir} INCDIR=%{_includedir} MANDIR=%{_mandir} \
	TFTPBOOT=/tftpboot EXTLINUXDIR=/boot/extlinux
%endif

install -m 755 bios/mtools/syslinux %{buildroot}%{_bindir}/syslinux-mtools
install -m 755 bios/linux/syslinux %{buildroot}%{_bindir}/syslinux
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_datadir}/syslinux/com32
for i in isolinux.1 pxelinux.1 syslinux-cli.1 syslinux.1 syslinux.cfg.5 ; do
  install -D -m 644 txt/man/$i %{buildroot}%{_mandir}/man${i: -1}/$i
done

%files
%defattr(-,root,root)
%doc doc/*.txt
%doc README* NEWS
%{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/syslinux
%license COPYING

%changelog
