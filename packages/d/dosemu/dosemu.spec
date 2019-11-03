#
# spec file for package dosemu
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


Name:           dosemu
BuildRequires:  SDL-devel
BuildRequires:  bin86
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  mkfontdir
BuildRequires:  slang-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xxf86vm)
%if 0%{?suse_version} > 1130
BuildRequires:  gpm-devel
%else
BuildRequires:  gpm
%endif

%if 0%{?suse_version} > 1220
BuildRequires:  bdftopcf
%endif

ExclusiveArch:  %ix86 x86_64
Version:        1.4.0.1.r2065
Release:        0
Summary:        The DOS Emulator
License:        GPL-2.0-or-later
Group:          System/Emulators/PC
Source:         %name-%version.tgz
Source1:        dosemu-freedos-bin.tgz
Patch1:         dosemu-1.4.0-destbufferoverflow.patch
Patch2:         force-vm86-emu.patch
Patch3:         dosemu-flex.patch
Patch4:         dosemu-skip-glibc-test.patch
# PATCH-FIX-UPSTREAM https://github.com/stsp/dosemu2/pull/386 https://github.com/stsp/dosemu2/commit/8d7ab25daf6f2d8ca09e1598fd11de2d8460255e
Patch5:         reproducible.patch
Url:            http://www.dosemu.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package allows MS-DOS programs to be run in Linux. A virtual
machine (the DOS box) provides the necessary BIOS functions and
emulates most of the chip devices (for example: timer, interrupt, and
keyboard controller).

Documentation can be found in /usr/share/doc/packages/dosemu, the man
page, and in the sources.

Starting with version 1.0.2, DOSEMU configuration files are no longer
in /etc but in the user's HOME directory in ~/dosemu. DOSEMU no longer
has the SUID bit set, so if you need access to hardware that requires
root privileges, you must run DOSEMU as root.

If you rely on the old configuration scheme, you can get it back by
using dosemu.bin instead of dosemu (dos and xdos have been renamed to
dosemu and xdosemu).

The parameter $_hogthreshold in ~/dosemu/conf/dosemu.conf defines how
often an idling DOSEMU should return the CPU to Linux and its default
value (1) means "all power to Linux." The higher this value is, the
more CPU power is dedicated to DOSEMU. The value (0) disables this
feature completely, hence: "all power to DOSEMU." If that is not fast
enough, you (running as UID root) can get maximum performance with

nice -19 dos -D-a 2>/dev/null

Do not be surprised if other Linux processes then run very sluggishly.

On sensitive systems, you should never offer an suid-root DOSEMU as
world readable. Even if the '$_secure' option in dosemu.conf is set, it
is still possible that some DPMI clients (most likely Dos4gw based
ones) may succeed in accessing the whole user space (including DOSEMU
code) and thus gain root access. A comfortable solution is to have two
copies of the DOSEMU binary, a non-suid-root one for world access and a
suid-root one (protected by file permissions) only available to trusted
users.

%prep
%setup -q -n %name-1.4.0.1
%patch1
%patch2 -p1
%if 0%{?suse_version} > 1220 && 0%{?suse_version} < 1321
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1
%build
%global _lto_cflags %{_lto_cflags} -flto-partition=one
autoreconf -fiv
export CFLAGS="%optflags -fgnu89-inline"
%configure --sysconfdir=%{_sysconfdir}/%{name} --with-docdir=%{_docdir}/dosemu \
 --with-fdtarball=%{_sourcedir}/dosemu-freedos-bin.tgz
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
%_fixowner %{buildroot}
%_fixgroup %{buildroot}
%_fixperms %{buildroot}
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%defattr(-,root,root)
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
