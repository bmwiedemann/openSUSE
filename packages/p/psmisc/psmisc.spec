#
# spec file for package psmisc
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


Name:           psmisc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dejagnu
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  libselinux-devel
BuildRequires:  linux-glibc-devel >= 4.12
BuildRequires:  ncurses-devel
BuildRequires:  netcat-openbsd
BuildRequires:  pkgconfig(libapparmor)
URL:            https://gitlab.com/psmisc/psmisc/
Version:        23.6
Release:        0
Provides:       ps:/usr/bin/killall
Summary:        Utilities for managing processes on your system
License:        GPL-2.0-or-later
Group:          System/Monitoring
Source:         https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Patch0:         %{name}-v%{version}.dif
Patch2:         %{name}-22.21-pstree.patch
# PATCH-ADD-SUSE boo#908068, boo#1046237, boo#1046237
# https://gitlab.com/bitstreamout/psmisc/tree/mountinfo
Patch3:         0001-Use-mountinfo-to-be-able-to-use-the-mount-identity.patch

%define have_peekfd %ix86 x86_64 ppc ppc64 ppc64le %arm mipsel m68k aarch64

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%lang_package

%prep
%setup -q -n %{name}-v%{version}
%patch2 -p0 -b .pstree
%patch3 -p0 -b .mntinf
%patch0 -p0 -b .p0

%build
grep -h src/ po/*.po|\
 sed -r 's/^#: //'|\
 tr ' ' '\n'|\
 sort -t : -k1,1 -u|\
 sed -r 's/:[0-9]+$//' > po/POTFILES.in
autoreconf -fi
CFLAGS="-D_GNU_SOURCE -D_DEFAULT_SOURCE ${RPM_OPT_FLAGS} -pipe -fPIE"
CXXFLAGS="$CFLAGS"
LDFLAGS=-pie
CC=gcc
export CFLAGS CXXFLAGS LDFLAGS CC
%configure	--disable-rpath \
	--with-gnu-ld		\
	--enable-apparmor       \
	--enable-selinux
make %{?_smp_mflags} CFLAGS="$CFLAGS" "CC=$CC"

%check
make check

%install
make DESTDIR=%{buildroot} install
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/bin/
ln -sf %{_bindir}/fuser %{buildroot}/bin/
%endif
%ifnarch %have_peekfd
rm -f %{buildroot}%{_mandir}/man1/peekfd.1*
%endif
%find_lang psmisc

%files
%defattr (-,root,root,755)
%license COPYING
%if 0%{?suse_version} < 1550
/bin/fuser
%endif
%{_bindir}/fuser
%{_bindir}/killall
%ifarch %have_peekfd
%{_bindir}/peekfd
%endif
%{_bindir}/prtstat
%{_bindir}/pslog
%{_bindir}/pstree
%{_bindir}/pstree.x11
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%ifarch %have_peekfd
%{_mandir}/man1/peekfd.1*
%endif
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pslog.1*
%{_mandir}/man1/pstree.1*

%files lang -f %{name}.lang

%changelog
