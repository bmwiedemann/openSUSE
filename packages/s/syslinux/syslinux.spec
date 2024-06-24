#
# spec file for package syslinux
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
URL:            http://www.syslinux.org/wiki/index.php/The_Syslinux_Project
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
Patch0:         %{name}-%{version}-iso9660.patch
Patch1:         %{name}-%{version}-cwd.patch
Patch2:         %{name}-%{version}-noinitrd.patch
Patch3:         %{name}-%{version}-mboot_bootif.patch
Patch5:         %{name}-%{version}-md5pass.patch
Patch6:         %{name}-%{version}-libext2fs.patch
Patch7:         %{name}-%{version}-gcc47.patch
Patch8:         %{name}-%{version}-isohybrid_efi.patch
Patch9:         %{name}-%{version}-isohybrid_efi_optional.patch
Patch10:        %{name}-%{version}-isohybrid_mbr.patch
Patch11:        %{name}-%{version}-localboot.patch
Patch12:        %{name}-%{version}-geometry.patch
Patch13:        %{name}-%{version}-nostrip.patch
Patch14:        %{name}-%{version}-timeout.patch
Patch15:        %{name}-%{version}-cache_fix.patch
Patch16:        %{name}-%{version}-mtime.patch
Patch17:        %{name}-%{version}-miniacc.patch
Patch18:        %{name}-%{version}-align.patch
# PATCH-FIX-UPSTREAM -- make package build reproducible
Patch19:        syslinux-4.04-reproducible.patch
Patch20:        %{name}-%{version}-python3.patch
Patch21:        sysmacros.patch
Patch22:        remove-note-gnu-section.patch
Patch23:        %{name}-%{version}-lzo.patch
Patch24:        %{name}-%{version}-gcc10.patch
Patch25:        syslinux-4.04-reproducible-isohybrid.patch
Patch26:        %{name}-%{version}-pie.patch

%description
SYSLINUX is a boot loader for the Linux operating system which operates
off an MS-DOS or Windows FAT file system. It is intended to simplify
first-time installation of Linux and for creation of rescue and other
special purpose boot disks.



Authors:
--------
    H. Peter Anvin <hpa@zytor.com>

%prep
%autosetup -p1

%build
cp %{SOURCE2} .
make spotless
make
# rebuild the on-system binaries with distribution optflags for stack protector etc.
for dir in extlinux utils linux mtools
do
	cd $dir
	make clean
	make OPTFLAGS="%optflags"
	cd ..
done

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
