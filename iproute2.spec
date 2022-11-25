#
# spec file for package iproute2
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


%define _buildshell /bin/bash
Name:           iproute2
Version:        6.0
Release:        0
Summary:        Linux network configuration utilities
License:        GPL-2.0-only
Group:          Productivity/Networking/Routing
URL:            https://wiki.linuxfoundation.org/networking/iproute2
# Using GPL-2.0 instead of GPL-2.0+ because of tc_skbedit.h and tc/q_multiq.c

#DL-URL:	https://kernel.org/pub/linux/utils/net/iproute2/
#Git-Clone: https://git.kernel.org/pub/scm/network/iproute2/iproute2.git/
#Git-Mirror:    https://github.com/shemminger/iproute2 ## not regularly updated
Source:         https://kernel.org/pub/linux/utils/net/iproute2/%name-%version.0.tar.xz
Source2:        https://kernel.org/pub/linux/utils/net/iproute2/%name-%version.0.tar.sign
Source3:        %name.tmpfiles
Source9:        %name.keyring
Patch1:         adjust-installation-directories-for-openSUSE-SLE.patch
Patch2:         use-sysconf-_SC_CLK_TCK-if-HZ-undefined.patch
Patch3:         add-explicit-typecast-to-avoid-gcc-warning.patch
Patch4:         xfrm-support-displaying-transformations-used-for-Mob.patch
Patch6:         split-link-and-compile-steps-for-binaries.patch
BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libbpf-devel
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(xtables) >= 1.4.11
Provides:       %name-doc = %version
Provides:       iproute = %version-%release
Provides:       %name(xfrm6_raw) = %version-%release
Obsoletes:      %name-doc < 4.15.0

%description
iproute2 is a collection of user-space utilities to set up networking
under Linux from the command-line. It can inspect and configure,
among other things: interface paramters, IP addresses, routing,
tunnels, bridges, packet transformations (IPsec, etc.), and Quality
of Service.

%package -n libnetlink-devel
Summary:        A Higher Level Interface to the Netlink Service
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Provides:       libnetlink = %version-%release

%description -n libnetlink-devel
libnetlink provides a higher-level interface to rtnetlink(7).
New programs should use libmnl-devel instead.

%package bash-completion
Summary:        Bash completion for iproute
License:        GPL-2.0-or-later
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
bash command line completion support for iproute.

%package arpd
Summary:        Userspace ARP daemon
License:        GPL-2.0-only
Group:          Productivity/Networking/Routing
Provides:       iproute2:/usr/sbin/arpd

%description arpd
The arpd daemon collects gratuitous ARP information, saving it on
local disk and feeding it to the kernel on demand to avoid redundant
broadcasting due to limited standard size (512..1024 entries,
depending on type) of the kernel ARP cache.

%prep
%autosetup -p1 -n %name-%version.0

find . -name *.orig -delete

%build
%global _lto_cflags %_lto_cflags -ffat-lto-objects
# build with -fPIC. For details see
# https://bugzilla.novell.com/show_bug.cgi?id=388021
xt_libdir="$(pkg-config xtables --variable=xtlibdir)"
xt_cflags="$(pkg-config xtables --cflags)"
%if 0%{!?make_build:1}
%define make_build make %{?_smp_mflags}
%endif
%make_build CCOPTS="-D_GNU_SOURCE %optflags -Wstrict-prototypes -Wno-error -fPIC -DXT_LIB_DIR=\\\"$xt_libdir\\\" $xt_cflags"

%install
b="%buildroot"
mkdir -p "$b/usr/bin" "$b/usr/sbin" "$b/sbin"
%make_install MODDESTDIR="$b/%_libdir/tc"

# We have m_xt instead
rm -f "$b/%_libdir/tc/m_ipt.so"

install -pm0644 "lib/libnetlink.a" "$b/%_libdir/"
chmod -x "$b/%_libdir/libnetlink.a"
install -pm0644 "include/libnetlink.h" "$b/%_includedir/"
chmod -x "$b/%_includedir/libnetlink.h"
install -Dm0644 "%SOURCE3" "$b/%_tmpfilesdir/%name.conf"
%if 0%{?usrmerged}
ln -sf "%_sbindir/ip" "$b/%_bindir/ip"
%else
ln -s "%_sbindir/ip" "$b/sbin/"
mkdir -p "$b/bin"
ln -sf "%_sbindir/ip" "$b/bin/ip"
%endif
for BIN in lnstat nstat routel ss; do
	ln -sf "%_sbindir/$BIN" "$b/%_bindir/$BIN"
done
mkdir -p "$b/%_docdir/%name"
cp -an README* examples/bpf "$b/%_docdir/%name/"

# bugzilla.opensuse.org/1205632
# You can't parse routel output anyway so it does not matter what we output
rm -v "$b/%_mandir/man8/routel.8"
cat >"$b/%_sbindir/routel" <<-EOF
	#!/bin/sh
	exec ip r l table all
EOF

%fdupes %buildroot/%_prefix

%post
%tmpfiles_create %_tmpfilesdir/%name.conf

%files
%_bindir/lnstat
%_bindir/nstat
%_bindir/routel
%_bindir/ss
%_sbindir/*
%_tmpfilesdir/%name.conf
%ghost %dir %_rundir/netns
%exclude %_sbindir/arpd
%if 0%{?usrmerged}
%_bindir/ip
%else
/sbin/*
/bin/ip
%endif
%_mandir/man7/*
%_mandir/man8/*
%exclude %_mandir/man8/arpd.8*
%dir %_sysconfdir/iproute2
%config(noreplace) %_sysconfdir/iproute2/*
%_libdir/tc/
%_datadir/tc/
%_docdir/%name/
%license COPYING

%files -n libnetlink-devel
%_includedir/*
%_mandir/man3/libnetlink*
%_libdir/lib*

%files bash-completion
%_datadir/bash-completion/

%files arpd
%_sbindir/arpd
%_mandir/man8/arpd.8*

%changelog
