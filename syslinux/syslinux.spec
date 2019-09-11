#
# spec file for package syslinux
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           syslinux
ExclusiveArch:  %ix86 x86_64
BuildRequires:  libext2fs-devel
BuildRequires:  libpng-devel
BuildRequires:  libuuid-devel
BuildRequires:  nasm
BuildRequires:  netpbm
BuildRequires:  python3
BuildRequires:  xz
# lots of assembler here that would need to be changed :(
#!BuildIgnore:	gcc-PIE
Url:            http://www.syslinux.org/wiki/index.php/The_Syslinux_Project
Suggests:       mtools
Summary:        Boot Loader for Linux
License:        GPL-2.0-or-later
Group:          System/Boot
Version:        4.04
Release:        0
Source:         https://www.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
Source1:        isolinux-config
Source2:        README.gfxboot
Source3:        baselibs.conf
Patch0:         %{name}-%{version}-iso9660.diff
Patch1:         %{name}-%{version}-cwd.diff
Patch2:         %{name}-%{version}-noinitrd.diff
Patch3:         %{name}-%{version}-mboot_bootif.diff
Patch5:         %{name}-%{version}-md5pass.diff
Patch6:         %{name}-%{version}-libext2fs.diff
Patch7:         %{name}-%{version}-gcc47.diff
Patch8:         %{name}-%{version}-isohybrid_efi.diff
Patch9:         %{name}-%{version}-isohybrid_efi_optional.diff
Patch10:        %{name}-%{version}-isohybrid_mbr.diff
Patch11:        %{name}-%{version}-localboot.diff
Patch12:        %{name}-%{version}-geometry.diff
Patch13:        %{name}-%{version}-nostrip.diff
Patch14:        %{name}-%{version}-timeout.diff
Patch15:        %{name}-%{version}-cache_fix.diff
Patch16:        %{name}-%{version}-mtime.diff
Patch17:        %{name}-%{version}-miniacc.diff
Patch18:        %{name}-%{version}-align.diff
# PATCH-FIX-UPSTREAM -- make package build reproducible
Patch19:        syslinux-4.04-reproducible.patch
Patch20:        %{name}-%{version}-python3.diff
Patch21:        sysmacros.patch
Patch22:        remove-note-gnu-section.patch
Patch23:        %{name}-%{version}-lzo.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SYSLINUX is a boot loader for the Linux operating system which operates
off an MS-DOS or Windows FAT file system. It is intended to simplify
first-time installation of Linux and for creation of rescue and other
special purpose boot disks.



Authors:
--------
    H. Peter Anvin <hpa@zytor.com>

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p0
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17
%patch18
%patch19 -p1
%patch20 -p0
%patch21 -p1
%patch22 -p1
%patch23 -p0

%build
cp %{SOURCE2} .
make spotless
make

%install
make install-all \
  INSTALLROOT=%{buildroot} BINDIR=%{_bindir} SBINDIR=%{_bindir} \
  LIBDIR=%{_datadir} INCDIR=%{_includedir} MANDIR=%{_mandir}
install -m 755 mtools/syslinux $RPM_BUILD_ROOT/%{_bindir}/syslinux-mtools
install -m 755 linux/syslinux $RPM_BUILD_ROOT/%{_bindir}/syslinux
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}
rm -rf $RPM_BUILD_ROOT/%{_datadir}/syslinux/com32
rm -rf $RPM_BUILD_ROOT/boot
rm -rf $RPM_BUILD_ROOT/tftpboot

%files
%defattr(-,root,root)
%doc doc/*.txt
%doc README* NEWS
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/syslinux

%changelog
