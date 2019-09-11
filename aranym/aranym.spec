#
# spec file for package aranym
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


Name:           aranym
Version:        1.1.0
Release:        0
Summary:        Atari Running on Any Machine
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Emulators/Other
URL:            http://aranym.github.io/
Source:         %{name}-%{version}.tar.gz
Source1:        afros812.zip
Patch:          pow10.patch
Patch1:         lto.patch
BuildRequires:  Mesa-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libOSMesa-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  mpfr-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
Requires(post): permissions

%description
ARAnyM is a multiplatform virtual machine (a software layer) for
running Atari ST/TT/Falcon TOS/GEM applications on any hardware with
many host operating systems. The reason for writing ARAnyM is to
provide Atari power users with faster and better machines. The ultimate
goal is to create a new platform where TOS/GEM applications could
continue to live forever.

Features:
* 68040 CPU (including MMU040)
* 68040 and 68881/2 FPU
* 14 MB ST-RAM and up to 3824 MB (configurable) of FastRAM
* VIDEL, Blitter, MFP, ACIA, IKBD for highest possible compatibility
* Sound (compatible with Atari XBIOS Sound subsystem, including
  TimerA DMA IRQ)
* Atari floppy DD/HD for connecting floppy image or real floppy
  drive
* Two IDE channels for connecting disk images, hard drives, or
  CD-ROMs
* Extended keyboard and mouse support (including mouse wheel)
* Direct access to host file system via BetaDOS and MiNT xfs drivers
* Networking using ethernet emulation with a driver for MiNT-Net
* TOS 4.04, EmuTOS, or Linux as the booting operating system
* Runs with FreeMiNT, MagiC, and any other operating system that
  runs also on real Atari computers
* Native CD-ROM access (under Linux, other OS: audio CD only) without
  scsi, ide, or other emulation

%prep
%setup -q -a 1
%patch -p1
%patch1 -p1
# Don't remove -g from CFLAGS
sed -i -e 's,/-g,/-:,' configure.ac configure

%build
%define common_opts --docdir=%{_docdir}/%{name} --enable-addressing=direct --enable-usbhost --enable-nfosmesa
%define _configure ../configure
%ifarch %{ix86} x86_64 %{arm}
mkdir jit
cd jit
%configure %{common_opts} --enable-jit-compiler
make %{?_smp_mflags}
cd ..
%endif
mkdir mmu
cd mmu
%configure %{common_opts} --enable-lilo --enable-fullmmu
make %{?_smp_mflags}
cd ..
%define _configure ./configure
%configure %{common_opts}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%ifarch %{ix86} x86_64 %{arm}
install -m 755 jit/aranym %{buildroot}%{_bindir}/aranym-jit
%endif
install -m 755 mmu/aranym %{buildroot}%{_bindir}/aranym-mmu
for s in 32 48; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/
  install -m 644 contrib/icon-$s.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/aranym.png
done
%ifarch %{ix86} x86_64 %{arm}
%suse_update_desktop_file -i aranym-jit
%endif
%suse_update_desktop_file -i aranym
%suse_update_desktop_file -i aranym-mmu
cp -a afros %{buildroot}%{_datadir}/aranym/afros
find %{buildroot}%{_datadir}/aranym/afros -type d -name CVS -exec rm -rf {} +

%post
%set_permissions %{_bindir}/aratapif

%verifyscript
%verify_permissions -e %{_bindir}/aratapif

%files
%doc %{_docdir}/%{name}
%verify(not mode) %attr(755,root,root) %{_bindir}/aratapif
%{_bindir}/aranym*
%{_mandir}/man1/*.gz
%{_datadir}/aranym
%{_datadir}/applications/*
%{_datadir}/icons/hicolor
%{_datadir}/pixmaps/*

%changelog
