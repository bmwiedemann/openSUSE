#
# spec file for package iptables
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           iptables
Version:        1.8.9
Release:        0
Summary:        IP packet filter administration utilities
License:        Artistic-2.0 AND GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/iptables/
#Git-Clone:     git://git.netfilter.org/iptables
Source:         https://netfilter.org/projects/iptables/files/%name-%version.tar.xz
Source2:        https://netfilter.org/projects/iptables/files/%name-%version.tar.xz.sig
Source3:        %name.keyring
Source4:        baselibs.conf
Patch1:         iptables-batch.patch
Patch2:         iptables-batch-lock.patch
Patch3:         iptables-1.8.2-dont_read_garbage.patch

BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.33
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.21
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl) >= 1.0
BuildRequires:  pkgconfig(libnetfilter_conntrack) >= 1.0.4
BuildRequires:  pkgconfig(libnfnetlink) >= 1.0.0
BuildRequires:  pkgconfig(libnftnl) >= 1.1.6
Requires:       netcfg >= 11.6
Requires:       xtables-plugins = %version-%release
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
# During the update to iptables 1.8, ip6tables-restore-translate, ip6tables-translate,
# iptables-restore-translate and iptables-translate were moved from iptables-nft subpackage
# (now iptables-backend-nft) to the main package so we need to add a conflict here otherwise
# we hit file conflicts error during the update
Conflicts:      iptables-nft = 1.6.2

%description
iptables is used to set up, maintain, and inspect the rule tables of
the various Netfilter packet filter engines inside the Linux kernel.

%package backend-nft
Summary:        Metapackage to make nft the default backend for iptables/arptables/ebtables
Group:          Productivity/Networking/Security
Requires:       iptables >= 1.8.0
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Provides:       iptables-nft = %version-%release
Obsoletes:      iptables-nft < %version-%release

%description backend-nft
Installation of this package adds higher priority alternatives (cf.
update-alternatives) that makes the iptables, ip6tables, arptables
and ebtables commands point to a program variant that uses the
nftables kernel interface.

%package -n xtables-plugins
Summary:        Match and target extension plugins for iptables
Group:          Productivity/Networking/Security
Conflicts:      iptables < 1.4.18

%description -n xtables-plugins
Match and Target Extension plugins for iptables.

%package -n libipq0
Summary:        Library to interface with the (old) ip_queue kernel mechanism
Group:          System/Libraries

%description -n libipq0
The Netfilter project provides a mechanism (ip_queue) for passing
packets out of the stack for queueing to userspace, then receiving
these packets back into the kernel with a verdict specifying what to
do with the packets (such as ACCEPT or DROP). These packets may also
be modified in userspace prior to reinjection back into the kernel.

ip_queue/libipq is obsoleted by nf_queue/libnetfilter_queue!

%package -n libipq-devel
Summary:        Development files for the ip_queue kernel mechanism
Group:          Development/Libraries/C and C++
Requires:       libipq0 = %version

%description -n libipq-devel
The Netfilter project provides a mechanism (ip_queue) for passing
packets out of the stack for queueing to userspace, then receiving
these packets back into the kernel with a verdict specifying what to
do with the packets (such as ACCEPT or DROP). These packets may also
be modified in userspace prior to reinjection back into the kernel.

ip_queue/libipq is obsoleted by nf_queue/libnetfilter_queue!

%package -n libip4tc2
Summary:        Library for the ip_tables low-level ruleset generation and parsing (IPv4)
Group:          System/Libraries

%description -n libip4tc2
libiptc ("iptables cache") is used to retrieve from the kernel, parse,
construct, and load rulesets into the kernel.
This package contains the iptc IPv4 API.

%package -n libip6tc2
Summary:        Library for the ip_tables low-level ruleset generation and parsing (IPv6)
Group:          System/Libraries

%description -n libip6tc2
libiptc ("iptables cache") is used to retrieve from the kernel, parse,
construct, and load rulesets into the kernel.
This package contains the iptc IPv6 API.

%package -n libiptc-devel
Summary:        Development files for libiptc, a packet filter ruleset library
Group:          Development/Libraries/C and C++
Requires:       libip4tc2 = %version
Requires:       libip6tc2 = %version

%description -n libiptc-devel
libiptc ("iptables cache") is used to retrieve from the kernel, parse,
construct, and load rulesets into the kernel.

%package -n libxtables12
Summary:        The iptables plugin interface
Group:          System/Libraries

%description -n libxtables12
This library contains all the iptables code shared between iptables,
ip6tables, their extensions, and for external integration for e.g.
iproute2's m_xt.

%package -n libxtables-devel
Summary:        Headers and manpages for iptables
Group:          Development/Libraries/C and C++
Requires:       libxtables12 = %version

%description -n libxtables-devel
This library contains all the iptables code shared between iptables,
ip6tables, their extensions, and for external integration for e.g.

Link your extension (iptables plugins) with $(pkg-config xtables
--libs) and place the plugin in the directory given by $(pkg-config
xtables --variable=xtlibdir).

%prep
%autosetup -p1

%build
# We have the iptables-batch patch, so always regenerate.
./autogen.sh
# bnc#561793 - do not include unclean module in iptables manpage
rm -f extensions/libipt_unclean.man
# includedir is overriden on purpose to detect projects that
# fail to include libxtables_CFLAGS
%configure --includedir="%_includedir/%name" --enable-libipq
%make_build V=1

%install
%make_install
b="%buildroot"
# no contents and is unused; proposed for removal upstream
rm -f "$b/%_libdir/"libiptc.so*
# iptables-apply is not installed by upstream Makefile
install -m0755 iptables/iptables-apply "$b/%_sbindir/"
rm -f "$b/%_libdir"/*.la
rm -f "$b/%_sysconfdir/ethertypes" # provided by netcfg
rm -f "$b/%_sysconfdir/xtables.conf" # packaging bug

for i in iptables iptables-restore iptables-save ip6tables ip6tables-restore \
    ip6tables-save arptables arptables-restore arptables-save ebtables \
    ebtables-restore ebtables-save; do
%if ! %{with libalternatives}
	ln -fsv "%_sysconfdir/alternatives/$i" "$b/%_sbindir/$i"
%else
	ln -fsv %_bindir/alts "$b/%_sbindir/$i"
%endif
done

%if 0%{?suse_version}
%fdupes %buildroot/%_prefix
%endif

%if %{with libalternatives}
mkdir -pv "$b/%_datadir/libalternatives/iptables"
cat >"$b/%_datadir/libalternatives/iptables/1.conf" <<-EOF
	binary=%_sbindir/xtables-legacy-multi
	group=iptables, ip6tables, ip6tables-restore, ip6tables-save, iptables-restore, iptables-save
	options=KeepArgv0
EOF
cat >"$b/%_datadir/libalternatives/iptables/2.conf" <<-EOF
	binary=%_sbindir/xtables-nft-multi
	group=iptables, ip6tables, ip6tables-restore, ip6tables-save, iptables-restore, iptables-save
	options=KeepArgv0
EOF
for i in ip6tables ip6tables-restore ip6tables-save iptables-restore iptables-save; do
	mkdir -pv "$b/%_datadir/libalternatives/$i"
	cp -av "$b/%_datadir/libalternatives/iptables/"*.conf "$b/%_datadir/libalternatives/$i/"
done

mkdir -pv $b/%_datadir/libalternatives/arptables
cat >"$b/%_datadir/libalternatives/arptables/2.conf" <<-EOF
	binary=%_sbindir/xtables-nft-multi
	group=arptables, arptables-restore, arptables-save
	options=KeepArgv0
EOF
for i in arptables-restore arptables-save; do
	mkdir -pv "$b/%_datadir/libalternatives/$i"
	cp -av "$b/%_datadir/libalternatives/arptables/2.conf" "$b/%_datadir/libalternatives/$i/"
done

mkdir -p "$b/%_datadir/libalternatives/ebtables"
cat >"$b/%_datadir/libalternatives/ebtables/2.conf" <<-EOF
	binary=%_sbindir/xtables-nft-multi
	group=ebtables, ebtables-restore, ebtables-save
	options=KeepArgv0
EOF
for i in ebtables-restore ebtables-save; do
	mkdir -pv "$b/%_datadir/libalternatives/$i"
	cp -av "$b/%_datadir/libalternatives/ebtables/2.conf" "$b/%_datadir/libalternatives/$i/"
done

%endif

%if %{with libalternatives}
%pre
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f "%_sbindir/update-alternatives" ]; then
         update-alternatives --remove iptables "%_sbindir/xtables-legacy-multi"
fi
%else

%post
update-alternatives \
	--install "%_sbindir/iptables" iptables "%_sbindir/xtables-legacy-multi" 1 \
	--slave "%_sbindir/iptables-restore" iptables-restore "%_sbindir/xtables-legacy-multi" \
	--slave "%_sbindir/iptables-save" iptables-save "%_sbindir/xtables-legacy-multi" \
	--slave "%_sbindir/ip6tables" ip6tables "%_sbindir/xtables-legacy-multi" \
	--slave "%_sbindir/ip6tables-restore" ip6tables-restore "%_sbindir/xtables-legacy-multi" \
	--slave "%_sbindir/ip6tables-save" ip6tables-save "%_sbindir/xtables-legacy-multi"

%postun
if test "$1" = 0; then
	update-alternatives --remove iptables "%_sbindir/xtables-legacy-multi"
fi
%endif

%if %{with libalternatives}
%pre backend-nft
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f "%_sbindir/update-alternatives" ]; then
	update-alternatives --remove iptables "%_sbindir/xtables-nft-multi"
	update-alternatives --remove arptables "%_sbindir/xtables-nft-multi"
	update-alternatives --remove ebtables "%_sbindir/xtables-nft-multi"
fi
%else

%post backend-nft
update-alternatives \
	--install "%_sbindir/iptables" iptables "%_sbindir/xtables-nft-multi" 2 \
	--slave "%_sbindir/iptables-restore" iptables-restore "%_sbindir/xtables-nft-multi" \
	--slave "%_sbindir/iptables-save" iptables-save "%_sbindir/xtables-nft-multi" \
	--slave "%_sbindir/ip6tables" ip6tables "%_sbindir/xtables-nft-multi" \
	--slave "%_sbindir/ip6tables-restore" ip6tables-restore "%_sbindir/xtables-nft-multi" \
	--slave "%_sbindir/ip6tables-save" ip6tables-save "%_sbindir/xtables-nft-multi"
update-alternatives --install "%_sbindir/arptables" arptables "%_sbindir/xtables-nft-multi" 2 \
	--slave "%_sbindir/arptables-restore" arptables-restore "%_sbindir/xtables-nft-multi" \
	--slave "%_sbindir/arptables-save" arptables-save "%_sbindir/xtables-nft-multi"
update-alternatives --install "%_sbindir/ebtables" ebtables "%_sbindir/xtables-nft-multi" 2 \
	--slave "%_sbindir/ebtables-restore" ebtables-restore "%_sbindir/xtables-nft-multi" \
	--slave "%_sbindir/ebtables-save" ebtables-save "%_sbindir/xtables-nft-multi"

%postun backend-nft
if test "$1" = 0; then
	update-alternatives --remove iptables "%_sbindir/xtables-nft-multi"
	update-alternatives --remove arptables "%_sbindir/xtables-nft-multi"
	update-alternatives --remove ebtables "%_sbindir/xtables-nft-multi"
fi
%endif

%post   -n libipq0 -p /sbin/ldconfig
%postun -n libipq0 -p /sbin/ldconfig
%post   -n libip4tc2 -p /sbin/ldconfig
%postun -n libip4tc2 -p /sbin/ldconfig
%post   -n libip6tc2 -p /sbin/ldconfig
%postun -n libip6tc2 -p /sbin/ldconfig
%post   -n libxtables12 -p /sbin/ldconfig
%postun -n libxtables12 -p /sbin/ldconfig

%files
%license COPYING
%_bindir/iptables-xml
%_sbindir/iptables-apply
%_sbindir/iptables-legacy*
%_sbindir/iptables-nft*
%_sbindir/iptables-*translate*
%_sbindir/ip6tables-apply
%_sbindir/ip6tables-legacy*
%_sbindir/ip6tables-nft*
%_sbindir/ip6tables-*translate*
%_sbindir/arptables-nft*
%_sbindir/ebtables-nft*
%_sbindir/ebtables-*translate*
%_sbindir/xtables*
%_mandir/man1/*tables*
%_mandir/man8/*tables*
# backend-legacy (implicit)
%if ! %{with libalternatives}
%ghost %_sysconfdir/alternatives/iptables
%ghost %_sysconfdir/alternatives/iptables-restore
%ghost %_sysconfdir/alternatives/iptables-save
%ghost %_sysconfdir/alternatives/ip6tables
%ghost %_sysconfdir/alternatives/ip6tables-restore
%ghost %_sysconfdir/alternatives/ip6tables-save
%else
%_datadir/libalternatives/ip6tables/1.conf
%dir %_datadir/libalternatives/ip6tables
%_datadir/libalternatives/ip6tables-restore/1.conf
%dir %_datadir/libalternatives/ip6tables-restore
%_datadir/libalternatives/ip6tables-save/1.conf
%dir %_datadir/libalternatives/ip6tables-save
%_datadir/libalternatives/iptables/1.conf
%dir %_datadir/libalternatives/iptables
%_datadir/libalternatives/iptables-restore/1.conf
%dir %_datadir/libalternatives/iptables-restore
%_datadir/libalternatives/iptables-save/1.conf
%dir %_datadir/libalternatives/iptables-save
%endif
%_sbindir/iptables
%_sbindir/iptables-restore
%_sbindir/iptables-save
%_sbindir/ip6tables
%_sbindir/ip6tables-restore
%_sbindir/ip6tables-save

%files backend-nft
%if ! %{with libalternatives}
%ghost %_sysconfdir/alternatives/iptables
%ghost %_sysconfdir/alternatives/iptables-restore
%ghost %_sysconfdir/alternatives/iptables-save
%ghost %_sysconfdir/alternatives/ip6tables
%ghost %_sysconfdir/alternatives/ip6tables-restore
%ghost %_sysconfdir/alternatives/ip6tables-save
%ghost %_sysconfdir/alternatives/arptables
%ghost %_sysconfdir/alternatives/arptables-restore
%ghost %_sysconfdir/alternatives/arptables-save
%ghost %_sysconfdir/alternatives/ebtables
%ghost %_sysconfdir/alternatives/ebtables-restore
%ghost %_sysconfdir/alternatives/ebtables-save
%_sbindir/iptables
%_sbindir/iptables-restore
%_sbindir/iptables-save
%_sbindir/ip6tables
%_sbindir/ip6tables-restore
%_sbindir/ip6tables-save
%else
%_datadir/libalternatives/arptables/2.conf
%dir %_datadir/libalternatives/arptables
%_datadir/libalternatives/arptables-restore/2.conf
%dir %_datadir/libalternatives/arptables-restore
%_datadir/libalternatives/arptables-save/2.conf
%dir %_datadir/libalternatives/arptables-save
%_datadir/libalternatives/ebtables/2.conf
%dir %_datadir/libalternatives/ebtables
%_datadir/libalternatives/ebtables-restore/2.conf
%dir %_datadir/libalternatives/ebtables-restore
%_datadir/libalternatives/ebtables-save/2.conf
%dir %_datadir/libalternatives/ebtables-save
%_datadir/libalternatives/ip6tables/2.conf
%dir %_datadir/libalternatives/ip6tables
%_datadir/libalternatives/ip6tables-restore/2.conf
%dir %_datadir/libalternatives/ip6tables-restore
%_datadir/libalternatives/ip6tables-save/2.conf
%dir %_datadir/libalternatives/ip6tables-save
%_datadir/libalternatives/iptables/2.conf
%dir %_datadir/libalternatives/iptables
%_datadir/libalternatives/iptables-restore/2.conf
%dir %_datadir/libalternatives/iptables-restore
%_datadir/libalternatives/iptables-save/2.conf
%dir %_datadir/libalternatives/iptables-save
%_datadir/libalternatives/iptables-save/2.conf
%endif
%_sbindir/arptables
%_sbindir/arptables-restore
%_sbindir/arptables-save
%_sbindir/ebtables
%_sbindir/ebtables-restore
%_sbindir/ebtables-save

%files -n xtables-plugins
%_libdir/xtables/
%_sbindir/nfnl_osf
%_mandir/man8/nfnl_osf.8*
%_datadir/xtables/

%files -n libipq0
%_libdir/libipq.so.0*

%files -n libipq-devel
%doc %_mandir/man3/libipq*
%doc %_mandir/man3/ipq*
%dir %_includedir/%name/
%_includedir/%name/libipq*
%_libdir/libipq.so
%_libdir/pkgconfig/libipq.pc

%files -n libip4tc2
%_libdir/libip4tc.so.2*

%files -n libip6tc2
%_libdir/libip6tc.so.2*

%files -n libiptc-devel
%dir %_includedir/%name/
%_includedir/%name/libiptc*
%_libdir/libip*tc.so
%_libdir/pkgconfig/libip*tc.pc

%files -n libxtables12
%_libdir/libxtables.so.12*

%files -n libxtables-devel
%dir %_includedir/%name/
%_includedir/%name/xtables.h
%_includedir/%name/xtables-version.h
%_libdir/libxtables.so
%_libdir/pkgconfig/xtables.pc

%changelog
