#
# spec file for package iproute2
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


Name:           iproute2
Version:        5.1
Release:        0
%define rversion 5.1.0
Summary:        Linux network configuration utilities
License:        GPL-2.0-only
Group:          Productivity/Networking/Routing
Url:            https://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2
# Using GPL-2.0 instead of GPL-2.0+ because of tc_skbedit.h and tc/q_multiq.c

#DL-URL:	https://kernel.org/pub/linux/utils/net/iproute2/
#Git-Clone:	git://git.kernel.org/pub/scm/linux/kernel/git/shemminger/iproute2
Source:         https://kernel.org/pub/linux/utils/net/iproute2/%name-%rversion.tar.xz
Source2:        https://kernel.org/pub/linux/utils/net/iproute2/%name-%rversion.tar.sign
Source9:        %name.keyring
Patch1:         adjust-installation-directories-for-openSUSE-SLE.patch
Patch2:         use-sysconf-_SC_CLK_TCK-if-HZ-undefined.patch
Patch3:         add-explicit-typecast-to-avoid-gcc-warning.patch
Patch4:         xfrm-support-displaying-transformations-used-for-Mob.patch
Patch6:         split-link-and-compile-steps-for-binaries.patch
Patch7:         examples-fix-bashisms-in-example-script.patch
Patch101:       Revert-tc-ematch-fix-deprecated-yacc-warning.patch
Patch102:       Revert-emp-fix-warning-on-deprecated-bison-directive.patch
Patch201:       bpf-data-section-support-poc.patch
Patch202:       bpf-bss-section-poc.patch
BuildRequires:  bison
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  xz
%define with_xt 1
%if 0%{?with_xt}
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(xtables) >= 1.4.11
%endif
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
Requires:       bash-completion

%description bash-completion
bash command line completion support for iproute.

%prep
%setup -qn %name-%rversion
%patch -P 1 -P 2 -P 3 -P 4 -P 6 -P 7 -P 201 -P 202 -p1
%if 0%{?suse_version} < 1500
%patch -P 101 -p1
%endif
%if 0%{?sles_version} == 11
%patch -P 102 -p1
%endif
find . -name *.orig -delete

%build
# build with -fPIC. For details see
# https://bugzilla.novell.com/show_bug.cgi?id=388021
xt_libdir="$(pkg-config xtables --variable=xtlibdir)"
xt_cflags="$(pkg-config xtables --cflags)"
make %{?_smp_mflags} CCOPTS="-D_GNU_SOURCE %optflags -Wstrict-prototypes -Wno-error -fPIC -DXT_LIB_DIR=\\\"$xt_libdir\\\" $xt_cflags"

%install
b="%buildroot"
install -d "$b"/{etc/,sbin/,usr/{bin,sbin,share/man/man{3,8}}}
install -d "$b"/{/usr/include,%_libdir,/usr/share}
%make_install \
  MODDESTDIR="$b/%_libdir/tc" \
  DOCDIR="%_docdir/%name"

# We have m_xt
rm -f "$b/%_libdir/tc/m_ipt.so"
install -pm0644 "lib/libnetlink.a" "$b/%_libdir/"
chmod -x "$b/%_libdir/libnetlink.a"
install -pm0644 "include/libnetlink.h" "$b/%_includedir/"
chmod -x "$b/%_includedir/libnetlink.h"
#UsrMerge
ln -s "%_sbindir/ip" "$b/sbin"
mkdir -p "$b/bin"
ln -sf "%_sbindir/ip" "$b/bin/ip"
#EndUsrMerge
for BIN in lnstat nstat routef routel ss; do
	ln -sf "%_sbindir/$BIN" "$b/%_bindir/$BIN"
done
rm "$b/%_sbindir/ifcfg"
cp -an README* "$b/%_docdir/%name/"
%fdupes %buildroot/%_prefix

%files
%_bindir/lnstat
%_bindir/nstat
%_bindir/routef
%_bindir/routel
%_bindir/ss
%_sbindir/*
#UsrMerge
/sbin/*
/bin/ip
#EndUsrMerge
%_mandir/man7/*
%_mandir/man8/*
%dir %_sysconfdir/iproute2
%config(noreplace) %_sysconfdir/iproute2/*
%_libdir/tc/
%_datadir/tc/
%_docdir/%name/
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120300
%license COPYING
%else
%doc COPYING
%endif

%files -n libnetlink-devel
%_includedir/*
%_mandir/man3/libnetlink*
%_libdir/lib*

%files bash-completion
%_datadir/bash-completion/

%changelog
