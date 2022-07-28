#
# spec file for package dosemu
#
# Copyright (c) 2022 SUSE LLC
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


Name:           dosemu
Version:        1.4.0.1.r2065
Release:        0
Summary:        The DOS Emulator
License:        GPL-2.0-or-later
Group:          System/Emulators/PC
URL:            http://www.dosemu.org
Source:         %{name}-%{version}.tgz
Source1:        dosemu-freedos-bin.tgz
Patch1:         dosemu-1.4.0-destbufferoverflow.patch
Patch2:         force-vm86-emu.patch
Patch4:         dosemu-skip-glibc-test.patch
# PATCH-FIX-UPSTREAM https://github.com/stsp/dosemu2/pull/386 https://github.com/stsp/dosemu2/commit/8d7ab25daf6f2d8ca09e1598fd11de2d8460255e
Patch5:         reproducible.patch
Patch6:         dosemu-LTO-fix.patch
BuildRequires:  bdftopcf
BuildRequires:  bin86
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gpm-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  mkfontdir
BuildRequires:  pkgconfig
BuildRequires:  slang-devel
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xxf86vm)
ExclusiveArch:  %{ix86} x86_64

%description
This package allows MS-DOS programs to be run in Linux. A virtual
machine (the DOS box) provides the necessary BIOS functions and
emulates most of the chip devices (for example: timer, interrupt, and
keyboard controller).

%prep
%setup -q -n %{name}-1.4.0.1
%patch1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%global _lto_cflags %{_lto_cflags} -flto-partition=one
autoreconf -fiv
export CFLAGS="%{optflags} -fgnu89-inline"
%configure --sysconfdir=%{_sysconfdir}/%{name} --with-docdir=%{_docdir}/dosemu \
 --with-fdtarball=%{_sourcedir}/dosemu-freedos-bin.tgz
%make_build

%install
%make_install
%{_fixowner} %{buildroot}
%{_fixgroup} %{buildroot}
%{_fixperms} %{buildroot}
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/man1/*
%lang(ru) %dir %{_mandir}/ru
%{_libdir}/dosemu
%{_datadir}/dosemu
%doc %{_docdir}/dosemu
%dir %{_sysconfdir}/dosemu
%dir %{_sysconfdir}/dosemu/drives
%config(noreplace) %{_sysconfdir}/dosemu/dosemu.conf
%config(noreplace) %{_sysconfdir}/dosemu/dosemu.users
%config(noreplace) %{_sysconfdir}/dosemu/global.conf
%config(noreplace) %{_sysconfdir}/dosemu/drives/c
%config(noreplace) %{_sysconfdir}/dosemu/drives/d

%changelog
