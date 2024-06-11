#
# spec file for package frr
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2021, Martin Hauke <mardnh@gmx.de>
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


%bcond_with     cumulus
%bcond_with     datacenter
%bcond_with     mininet
%bcond_with     grpc

%define frr_user frr
%define frr_group frr
%define frrvty_group frrvty
%define frr_home %{_localstatedir}/lib/%{name}
%define frr_statedir %{_rundir}/%{name}
%define frr_daemondir %{_prefix}/lib/frr

Name:           frr
Version:        8.4
Release:        0
Summary:        FRRouting Routing daemon
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/System
URL:            https://www.frrouting.org
#Git-Clone:     https://github.com/FRRouting/frr.git
Source:         https://github.com/FRRouting/frr/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}-tmpfiles.d
Patch1:         0001-disable-zmq-test.patch
Patch2:         harden_frr.service.patch
Patch3:         0003-tools-Run-as-FRR_USER-install-chown-commands-to-avoi.patch
Patch4:         0004-tools-remove-backslash-from-declare-check-regex.patch
Patch5:         0005-root-ok-in-account-frr.pam.patch
Patch6:         0006-bgpd-Check-7-bytes-for-Long-lived-Graceful-Restart-c.patch
Patch7:         0007-bgpd-Ensure-stream-received-has-enough-data.patch
Patch8:         0008-bgpd-Don-t-read-the-first-byte-of-ORF-header-if-we-a.patch
Patch9:         0009-bgpd-Do-not-process-NLRIs-if-the-attribute-length-is.patch
Patch10:        0010-bgpd-Use-treat-as-withdraw-for-tunnel-encapsulation-.patch
Patch11:        0011-babeld-fix-11808-to-avoid-infinite-loops.patch
Patch12:        0012-bgpd-Limit-flowspec-to-no-attribute-means-a-implicit.patch
Patch13:        0013-bgpd-Check-mandatory-attributes-more-carefully-for-U.patch
Patch14:        0014-bgpd-Handle-MP_REACH_NLRI-malformed-packets-with-ses.patch
Patch15:        0015-bgpd-Treat-EOR-as-withdrawn-to-avoid-unwanted-handli.patch
Patch16:        0016-bgpd-Ignore-handling-NLRIs-if-we-received-MP_UNREACH.patch
Patch17:        0017-bgpd-Fix-use-beyond-end-of-stream-of-labeled-unicast.patch
Patch18:        0018-bgpd-Flowspec-overflow-issue.patch
Patch19:        0019-bgpd-fix-error-handling-when-receiving-BGP-Prefix-SID-attribute.patch
Patch20:        0020-ospfd-Solved-crash-in-OSPF-TE-parsing.patch
Patch21:        0021-ospfd-Solved-crash-in-RI-parsing-with-OSPF-TE.patch
Patch22:        0022-ospfd-Correct-Opaque-LSA-Extended-parser.patch
Patch23:        0023-ospfd-protect-call-to-get_edge-in-ospf_te.c.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison >= 2.7
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{with mininet}
BuildRequires:  mininet
%endif
BuildRequires:  net-snmp-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
%if %{with grpc}
BuildRequires:  pkgconfig(grpc)
%endif
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libyang) >= 2.0.0
BuildRequires:  pkgconfig(libzmq) >= 4.0.0
BuildRequires:  pkgconfig(rtrlib) >= 0.5.0
BuildRequires:  pkgconfig(sqlite3)
Requires(post): %{install_info_prereq}
Requires(pre):  %{install_info_prereq}
Requires(pre):  shadow
Requires(preun):%{install_info_prereq}
Recommends:     logrotate
Conflicts:      quagga
Provides:       zebra = %{version}
Obsoletes:      zebra < %{version}
Provides:       group(%{frr_group})
Provides:       group(%{frrvty_group})
Provides:       user(%{frr_user})

%description
FRR is free software which manages TCP/IP based routing protocols.
It supports BGP4, BGP4+, OSPFv2, OSPFv3, IS-IS, RIPv1, RIPv2, RIPng,
PIM and LDP as well as the IPv6 versions of these.

FRR is a fork of Quagga..

%package -n libfrrfpm_pb0
Summary:        FRRouting fpm protobuf library
Group:          System/Libraries

%description -n libfrrfpm_pb0
This library contains forwarding plane manager protobuf definitions
for FRRouting.

%package -n libfrr_pb0
Summary:        FRRouting protobuf library
Group:          System/Libraries

%description -n libfrr_pb0
This library contains protobuf memory management for FRRouting..

%if %{with grpc}
%package -n libfrrgrpc_pb0
Summary:        FRRouting grpc protobuf library
Group:          System/Libraries

%description -n libfrrgrpc_pb0
This library contains grpc protobuf definitions for FRRouting.
%endif

%package -n libfrrospfapiclient0
Summary:        API for FRRouting's OSPFv2 implementation
Group:          System/Libraries

%description -n libfrrospfapiclient0
This library contains part of the OSPFv2 implementation of FRRouting.

%package -n libfrrsnmp0
Summary:        FRRouting snmp library
Group:          System/Libraries

%description -n libfrrsnmp0
This library contains part of the net-snmp agentx implementation of FRRouting.

%package -n libfrrzmq0
Summary:        FRRouting zeromq library
Group:          System/Libraries

%description -n libfrrzmq0
This library contains part of the zermomq implementation of FRRouting.

%package -n libfrr0
Summary:        FRRouting utility library
Group:          System/Libraries

%description -n libfrr0
This library contains various utility functions to FRRouting, such as
data types, buffers and socket handling.

%package -n libfrrcares0
Summary:        FRRouting utility library
Group:          System/Libraries

%description -n libfrrcares0
This library contains various utility functions to FRRouting, such as
data types, buffers and socket handling.

%package -n libmlag_pb0
Summary:        FRRouting utility library
Group:          System/Libraries

%description -n libmlag_pb0
This library contains part of the mlag implementation of FRRouting.

%package devel
Summary:        Header and object files for frr development
Group:          Development/Libraries/C and C++
Requires:       libfrr0 = %{version}
Requires:       libfrr_pb0 = %{version}
Requires:       libfrrcares0 = %{version}
Requires:       libfrrfpm_pb0 = %{version}
%if %{with grpc}
Requires:       libfrrgrpc_pb0 = %{version}
%endif
Requires:       libfrrospfapiclient0 = %{version}
Requires:       libfrrsnmp0 = %{version}
Requires:       libfrrzmq0 = %{version}
Requires:       libmlag_pb0 = %{version}

%description devel
The frr-devel package contains the header and object files necessary for
developing OSPF-API and frr applications.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%build
# GCC LTO objects must be "fat" to avoid assembly errors
export CFLAGS="-ffat-lto-objects"

autoreconf -fiv
%configure \
    --disable-silent-rules \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --localstatedir=%{frr_statedir} \
    --sbindir=%{frr_daemondir} \
    --with-moduledir=%{_libdir}/frr/modules \
    --disable-static \
    --with-vtysh-pager=%{_bindir}/less \
    --enable-user=%{frr_user} \
    --enable-group=%{frr_group} \
    --enable-vty-group=%{frrvty_group} \
    --enable-configfile-mask=0640 \
    --enable-logfile-mask=0640 \
    --enable-doc \
    --enable-doc-html \
    --enable-babeld \
    --enable-bfdd \
    --enable-bgpd \
    --enable-bgp-vnc \
%if %{with cumulus}
    --enable-cumulus \
%endif
%if %{with datacenter}
    --enable-datacenter \
%endif
    --enable-eigrpd \
    --enable-fpm \
    --enable-irdp \
    --enable-isisd \
    --enable-ldpd \
    --enable-multipath=256 \
    --enable-nhrpd \
    --enable-snmp \
    --enable-zeromq \
    --enable-ospfd \
    --enable-ospf6d \
    --enable-ospfapi \
    --enable-ospfclient \
    --with-libpam \
    --enable-pbrd \
    --enable-pimd \
    --enable-pim6d \
    --enable-protobuf \
    --enable-ripd \
    --enable-ripngd \
    --enable-rpki \
    --enable-rtadv \
    --enable-sharpd \
    --enable-staticd \
    --enable-vtysh \
    --enable-watchfrr \
    --enable-zebra \
    --enable-realms \
    --enable-shell-access \
    --with-crypto=openssl \
    --enable-config-rollbacks \
%if %{with grpc}
    --enable-grpc \
%endif
    --enable-systemd

make %{?_smp_mflags} MAKEINFO="makeinfo --no-split"

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
perl -p -i -e 's|#!/usr/bin/python|#!/usr/bin/python3|g' %{buildroot}/usr/lib/frr/{frr-reload.py,generate_support_bundle.py}

find %{buildroot} -type f -name "*.la" -delete -print

install -d %{buildroot}%{_sysconfdir}/frr
install -d %{buildroot}/%{_docdir}/%{name}
mv %{buildroot}/%{_datadir}/doc/frr/html %{buildroot}/%{_docdir}/%{name}

# remove stray buildinfo files
find %{buildroot}/%{_docdir}/%{name} -type f -name .buildinfo -delete

# systemd init scripts
install -D -m 0644 tools/frr.service %{buildroot}%{_unitdir}/frr.service
install -D -m 0644 tools%{_sysconfdir}/frr/daemons %{buildroot}%{_sysconfdir}/frr/daemons

# add rpki module to daemon
sed -i -e 's/^\(bgpd_options=\)\(.*\)\(".*\)/\1\2 -M rpki\3/' %{buildroot}%{_sysconfdir}/frr/daemons

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
install -D -m 0644 redhat/frr.pam %{buildroot}%{_pam_vendordir}/frr
%else
install -D -m 0644 redhat/frr.pam %{buildroot}%{_sysconfdir}/pam.d/frr
%endif
%if 0%{?suse_version} > 1500
install -D -m 0644 redhat/frr.logrotate %{buildroot}%{_distconfdir}/logrotate.d/frr
%else
install -D -m 0644 redhat/frr.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/frr
%endif

install -d -m 0750 %{buildroot}%{rundir}
install -d -m 0750 %{buildroot}%{_localstatedir}/log/frr
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
sed -e "s|@frr_statedir@|%{frr_statedir}|g" -i %{buildroot}/%{_tmpfilesdir}/%{name}.conf

install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcfrr
rm -f %{buildroot}%{frr_daemondir}/ssd

cat > %{buildroot}%{_sysconfdir}/frr/frr.conf << __EOF__
!hostname frr

!password frr
!enable password frr

log file %{_localstatedir}/log/frr/frr.log
__EOF__
cat > %{buildroot}%{_sysconfdir}/frr/vtysh.conf << __EOF__
! vtysh is using PAM authentication allowing root to use it.
__EOF__

%check
make %{?_smp_mflags} -C tests

%pre
# Create frr user/groups
getent group %{frr_group} >/dev/null || groupadd -r %{frr_group}
getent group %{frrvty_group} >/dev/null || groupadd -r %{frrvty_group}
getent passwd %{frr_user} >/dev/null || useradd -r -g %{frr_group} -G %{frrvty_group} -d %{frr_home} -s /sbin/nologin -c "FRRouting suite" %{frr_user}

%service_add_pre %{name}.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/frr pam.d/frr ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%posttrans
%if 0%{?suse_version} > 1500
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/frr pam.d/frr ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%service_add_post %{name}.service
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf || true

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
%install_info_delete --info-dir=%{_infodir} %{_infodir}/frr.info%{ext_info}

%post   -n libfrr_pb0 -p /sbin/ldconfig
%postun -n libfrr_pb0 -p /sbin/ldconfig
%if %{with grpc}
%post   -n libfrrgrpc_pb0 -p /sbin/ldconfig
%postun -n libfrrgrpc_pb0 -p /sbin/ldconfig
%endif
%post   -n libfrrfpm_pb0 -p /sbin/ldconfig
%postun -n libfrrfpm_pb0 -p /sbin/ldconfig

%post   -n libfrrospfapiclient0 -p /sbin/ldconfig
%postun -n libfrrospfapiclient0 -p /sbin/ldconfig

%post   -n libfrrsnmp0 -p /sbin/ldconfig
%postun -n libfrrsnmp0 -p /sbin/ldconfig

%post   -n libfrrzmq0 -p /sbin/ldconfig
%postun -n libfrrzmq0 -p /sbin/ldconfig

%post   -n libfrr0 -p /sbin/ldconfig
%postun -n libfrr0 -p /sbin/ldconfig

%post   -n libfrrcares0 -p /sbin/ldconfig
%postun -n libfrrcares0 -p /sbin/ldconfig

%post   -n libmlag_pb0 -p /sbin/ldconfig
%postun -n libmlag_pb0 -p /sbin/ldconfig

%files
%license COPYING COPYING-LGPLv2.1
%doc README.md
%doc doc/mpls
%dir %attr(750,%{frr_user},%{frr_user}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(640,%{frr_user},%{frr_group}) %{_sysconfdir}/%{name}/[!v]*.conf*
%config(noreplace) %attr(640,%{frr_user},%{frrvty_group}) %{_sysconfdir}/%{name}/vtysh.conf
%config(noreplace) %%attr(640,%{frr_user},%{frr_group}) %{_sysconfdir}/%{name}/daemons
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/frr
%else
%config(noreplace) %{_sysconfdir}/pam.d/frr
%endif
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/frr
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/frr
%endif
%{_infodir}/frr.info%{?ext_info}
%{_mandir}/man?/*
%{_docdir}/%{name}/html
%{_unitdir}/%{name}.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%dir %attr(-,%{frr_user},%{frr_group}) %{_localstatedir}/log/frr
%dir %attr(-,%{frr_user},%{frr_group}) %ghost %{frr_statedir}
%{_sbindir}/rc%{name}
%dir %{_prefix}/lib/frr
%{_prefix}/lib/frr/fabricd
%{_prefix}/lib/frr/vrrpd
%{_datadir}/yang
%{_bindir}/mtracebis
%{_bindir}/vtysh
%{frr_daemondir}/babeld
%{frr_daemondir}/bfdd
%{frr_daemondir}/bgpd
%{frr_daemondir}/eigrpd
%{frr_daemondir}/frr
%{frr_daemondir}/frr-reload
%{frr_daemondir}/frr-reload.py
%{frr_daemondir}/frr_babeltrace.py
%{frr_daemondir}/frrcommon.sh
%{frr_daemondir}/frrinit.sh
%{frr_daemondir}/isisd
%{frr_daemondir}/ldpd
%{frr_daemondir}/nhrpd
%{frr_daemondir}/ospfclient.py
%{frr_daemondir}/ospf6d
%{frr_daemondir}/ospfd
%{frr_daemondir}/pathd
%{frr_daemondir}/pbrd
%{frr_daemondir}/pimd
%{frr_daemondir}/pim6d
%{frr_daemondir}/ripd
%{frr_daemondir}/ripngd
%{frr_daemondir}/sharpd
%{frr_daemondir}/staticd
%{frr_daemondir}/watchfrr
%{frr_daemondir}/watchfrr.sh
%{frr_daemondir}/zebra
%dir %{_libdir}/frr
%dir %{_libdir}/frr/modules
%{_libdir}/frr/modules/zebra_cumulus_mlag.so
%{_libdir}/frr/modules/zebra_fpm.so
%{_libdir}/frr/modules/zebra_irdp.so
%{_libdir}/frr/modules/pathd_pcep.so
%{_libdir}/frr/modules/bgpd_rpki.so
%if %{with grpc}
%{_libdir}/frr/modules/grpc.so
%endif
%{_libdir}/frr/modules/dplane_fpm_nl.so
%{_libdir}/frr/modules/bgpd_bmp.so
%{_prefix}/lib/frr/generate_support_bundle.py

%files -n libfrr_pb0
%{_libdir}/libfrr_pb.so.0*

%files -n libfrrfpm_pb0
%{_libdir}/libfrrfpm_pb.so.0*

%if %{with grpc}
%files -n libfrrgrpc_pb0
%{_libdir}/libfrrgrpc_pb.so.0*
%endif

%files -n libfrrospfapiclient0
%{_libdir}/libfrrospfapiclient.so.0*

%files -n libfrrsnmp0
%{_libdir}/libfrrsnmp.so.0*
%{_libdir}/frr/modules/*_snmp.so

%files -n libfrrzmq0
%{_libdir}/libfrrzmq.so.0*

%files -n libfrr0
%{_libdir}/libfrr.so.0*

%files -n libfrrcares0
%{_libdir}/libfrrcares.so.0*

%files -n libmlag_pb0
%{_libdir}/libmlag_pb.so.0*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_includedir}/%{name}/ospfd
%{_includedir}/%{name}/ospfd/*.h
%dir %{_includedir}/%{name}/ospfapi
%{_includedir}/%{name}/ospfapi/*.h
%dir %{_includedir}/%{name}/eigrpd
%{_includedir}/%{name}/eigrpd/*.h
%dir %{_includedir}/%{name}/bfdd
%{_includedir}/%{name}/bfdd/*.h
%{_libdir}/lib*.so

%changelog
