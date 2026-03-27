#
# spec file for package frr
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%if 0%{?suse_version} > 1600
%bcond_without  factorydir
%else
%bcond_with     factorydir
%endif

%define frr_user frr
%define frr_group frr
%define frrvty_group frrvty
%define frr_logs %{_localstatedir}/log/%{name}
# see configure: frr_libstatedir=/var/lib/frr
%define frr_home %{_localstatedir}/lib/%{name}
# see configure: frr_runstatedir=[/var]/run/frr
%define frr_statedir %{_rundir}/%{name}
%define frr_daemondir %{_prefix}/lib/%{name}

Name:           frr
Version:        10.5.1
Release:        0
Summary:        The FRRouting Protocol Suite
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/System
URL:            https://www.frrouting.org
#Git-Clone:     https://github.com/FRRouting/frr.git
Source:         https://github.com/FRRouting/frr/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:         harden_frr.service.patch
Patch1:         0001-disable-zmq-test.patch
Patch2:         0002-frr-logrotate.patch
Patch3:         0003-ospfd-NULL-Pointer-Dereference-fixes.patch
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
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libprotobuf-c)
%if 0%{?sle_version} == 150500
BuildRequires:  libprotoc25_1_0
BuildRequires:  libyang1
%endif
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libyang) >= 2.0.0
BuildRequires:  pkgconfig(libzmq) >= 4.0.0
BuildRequires:  pkgconfig(rtrlib) >= 0.5.0
BuildRequires:  pkgconfig(sqlite3)
%sysusers_requires
Requires(pre):  %{install_info_prereq}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
# /usr/lib/frr/*.sh aka service macros need:
%{?systemd_ordering}
Requires:       grep
Requires:       util-linux
Requires(pre):  grep util-linux
Requires(post): grep util-linux
Requires(preun): grep util-linux
Requires(postun): grep util-linux
# logrotation needs:
Requires:       lsof
Recommends:     logrotate
Conflicts:      quagga
Provides:       zebra = %{version}
Obsoletes:      zebra < %{version}
Provides:       group(%{frr_group})
Provides:       group(%{frrvty_group})
Provides:       user(%{frr_user})

%description
FRR is free software that implements and manages various IPv4 and IPv6 routing protocols.
FRR currently supports the following protocols:
- BGP
- OSPFv2
- OSPFv3
- RIPv1
- RIPv2
- RIPng
- IS-IS
- PIM-SM/MSDP
- LDP
- BFD
- Babel
- PBR
- OpenFabric
- VRRP
- EIGRP (alpha)
- NHRP (alpha)

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

%package -n libmgmt_be_nb0
Summary:        FRRouting utility library
Group:          System/Libraries

%package -n libmlag_pb0
Summary:        FRRouting utility library
Group:          System/Libraries

%description -n libmgmt_be_nb0
This library contains part of the mgmt_be implementation of FRRouting.

%description -n libmlag_pb0
This library contains part of the mlag_pb implementation of FRRouting.

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
Requires:       libmgmt_be_nb0 = %{version}

%description devel
The frr-devel package contains the header and object files necessary for
developing OSPF-API and frr applications.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%build
# GCC LTO objects must be "fat" to avoid assembly errors
# Make sure -Werror=declaration-after-statement is not applied;
# frr sets -std=gnu11 as it requires C11 with atomic support.
export CFLAGS="-ffat-lto-objects -Wno-error=declaration-after-statement"

autoreconf -fiv
%configure \
    --disable-silent-rules \
    --sysconfdir=%{_sysconfdir}\
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
    --enable-pcre2posix \
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
    --enable-grpc
%endif

make %{?_smp_mflags} MAKEINFO="makeinfo --no-split"

# Create frr user/groups
cat > %{name}-user.conf << __EOF__
g %{frr_group}
g %{frrvty_group}
u %{frr_user} - "FRRouting suite" %{frr_home}
m %{frr_user} %{frrvty_group}
__EOF__
%sysusers_generate_pre %{name}-user.conf %{name} %{name}-user.conf

# Create tmpfiles.d config
cat >  %{name}-tmpfiles.conf << __EOF__
d %{frr_logs}                   0750 %{frr_user} %{frr_group}
d %{frr_home}                   0750 %{frr_user} %{frr_group}
d %{frr_statedir}               0751 %{frr_user} %{frrvty_group}
__EOF__
%if %{with factorydir}
# The vtysh.conf is never written by vtysh, symlink it.
# The daemon file is edited by the user, the frr.conf is
# written by user or by vtysh `write`, thus copy them
# from the factory directory.
cat >> %{name}-tmpfiles.conf << __EOF__
d %{_sysconfdir}/frr            0751 %{frr_user} %{frr_group}
C %{_sysconfdir}/frr/daemons    0640 %{frr_user} %{frr_group}
C %{_sysconfdir}/frr/frr.conf   0640 %{frr_user} %{frr_group}
L %{_sysconfdir}/frr/vtysh.conf -    -           -
__EOF__
%endif

# Create initial frr config
cat > frr.conf << __EOF__
#
# FRR's configuration shell, vtysh, dynamically edits the live, in-memory
# configuration while FRR is running. When instructed, vtysh will persist the
# live configuration to this file, overwriting its contents. If you want to
# avoid this, you can edit this file manually before starting FRR, or instruct
# vtysh to write configuration to a different file.
#

# Log to syslog (journal) by default
log syslog notifications

# Log rotation configuration expects optional log files in the %{frr_logs}
# directory, written by a syslog daemon or by the frr daemons directly, e.g.:
#log file %{frr_logs}/frr.log informational
#log daemon bgpd %{frr_logs}/frr/bgpd.log debugging
__EOF__

# Create default vtysh config
cat > vtysh.conf << __EOF__
! vtysh is using PAM authentication allowing root and frrvty group members to use it.
__EOF__


%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install

%python3_fix_shebang_path %{buildroot}%{frr_daemondir}/*.py

install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/frr/html %{buildroot}%{_docdir}/%{name}

# remove stray buildinfo files
find %{buildroot}/%{_docdir}/%{name} -type f -name .buildinfo -delete

# remove stray libtool .la files
find %{buildroot}%{_libdir}/ -type f -name "*.la" -delete -print

# remove system-v init helper scripts & man page
rm -f %{buildroot}%{frr_daemondir}/{frr,ssd}
rm -f %{buildroot}%{_mandir}/man1/frr.1*

# add rpki module to daemons file
sed -e 's/^\(bgpd_options=\)\(.*\)\(".*\)/\1\2 -M rpki\3/' -i tools/etc/frr/daemons

%if %{with factorydir}
install -d -m 0755 %{buildroot}%{_datadir}/factory%{_sysconfdir}
install -d -m 0751 %{buildroot}%{_datadir}/factory%{_sysconfdir}/%{name}
install -D -m 0640 tools/etc/frr/daemons %{buildroot}%{_datadir}/factory%{_sysconfdir}/%{name}/
install -D -m 0640 frr.conf              %{buildroot}%{_datadir}/factory%{_sysconfdir}/%{name}/
install -D -m 0640 vtysh.conf            %{buildroot}%{_datadir}/factory%{_sysconfdir}/%{name}/
%else
install -d -m 0751 %{buildroot}%{_sysconfdir}/frr
install -D -m 0640 tools/etc/frr/daemons %{buildroot}%{_sysconfdir}/%{name}/
install -D -m 0640 frr.conf              %{buildroot}%{_sysconfdir}/%{name}/
install -D -m 0640 vtysh.conf            %{buildroot}%{_sysconfdir}/%{name}/
%endif

# systemd service + daemons file
install -D -m 0644 tools/frr.service %{buildroot}%{_unitdir}/frr.service
sed -e "s|/var/run/frr|%{frr_statedir}|g" -i %{buildroot}%{_unitdir}/frr.service

# pam and logrotation config
%if 0%{?suse_version} > 1500
install -D -m 0644 redhat/frr.pam %{buildroot}%{_pam_vendordir}/frr
install -D -m 0644 tools/etc/logrotate.d/frr %{buildroot}%{_distconfdir}/logrotate.d/frr
sed -e "s|/var/log/frr|%{frr_logs}|g" -e "s|/var/run/frr|%{frr_statedir}|g" \
    -i %{buildroot}%{_distconfdir}/logrotate.d/frr
%else
install -D -m 0644 redhat/frr.pam %{buildroot}%{_sysconfdir}/pam.d/frr
install -D -m 0644 tools/etc/logrotate.d/frr %{buildroot}%{_sysconfdir}/logrotate.d/frr
sed -e "s|/var/log/frr|%{frr_logs}|g" -e "s|/var/run/frr|%{frr_statedir}|g" \
    -i %{buildroot}%{_sysconfdir}/logrotate.d/frr
%endif

install -D -m 0644 %{name}-tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{name}-user.conf %{buildroot}%{_sysusersdir}/%{name}-user.conf

%check
make %{?_smp_mflags} -C tests

%pre -f %{name}.pre
%service_add_pre %{name}.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/frr pam.d/frr ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif
%if %{with factorydir}
# Prepare for migration to /usr/share/factory/etc/frr, save any old .rpmsave
for i in %{name}/frr.conf %{name}/vtysh.conf %{name}/daemons ; do
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
%if %{with factorydir}
# Migration to /usr/share/factory/etc/frr, restore just created .rpmsave
for i in %{name}/frr.conf %{name}/vtysh.conf %{name}/daemons ; do
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

%post   -n libmgmt_be_nb0 -p /sbin/ldconfig
%postun -n libmgmt_be_nb0 -p /sbin/ldconfig

%post   -n libmlag_pb0 -p /sbin/ldconfig
%postun -n libmlag_pb0 -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%doc doc/mpls
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/frr
%{_distconfdir}/logrotate.d/frr
%else
%config(noreplace) %{_sysconfdir}/pam.d/frr
%config(noreplace) %{_sysconfdir}/logrotate.d/frr
%endif
%if %{with factorydir}
%dir %{_datadir}/factory
%dir %{_datadir}/factory%{_sysconfdir}
%dir %attr(0751,%{frr_user},%{frr_group}) %{_datadir}/factory%{_sysconfdir}/%{name}
%attr(0640,%{frr_user},%{frr_group})      %{_datadir}/factory%{_sysconfdir}/%{name}/daemons
%attr(0640,%{frr_user},%{frr_group})      %{_datadir}/factory%{_sysconfdir}/%{name}/frr.conf
%attr(0640,%{frr_user},%{frrvty_group})   %{_datadir}/factory%{_sysconfdir}/%{name}/vtysh.conf
%dir %attr(0751,%{frr_user},%{frr_group})                  %ghost %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,%{frr_user},%{frr_group})    %ghost %{_sysconfdir}/%{name}/daemons
%config(noreplace) %attr(0640,%{frr_user},%{frr_group})    %ghost %{_sysconfdir}/%{name}/frr.conf
%config(noreplace) %attr(0640,%{frr_user},%{frrvty_group}) %ghost %{_sysconfdir}/%{name}/vtysh.conf
%else
%dir %attr(0751,%{frr_user},%{frr_group}) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,%{frr_user},%{frr_group})           %{_sysconfdir}/%{name}/daemons
%config(noreplace) %attr(0640,%{frr_user},%{frr_group})           %{_sysconfdir}/%{name}/frr.conf
%config(noreplace) %attr(0640,%{frr_user},%{frrvty_group})        %{_sysconfdir}/%{name}/vtysh.conf
%endif
%{_infodir}/frr.info%{?ext_info}
%{_mandir}/man?/*
%{_docdir}/%{name}/html
%{_unitdir}/%{name}.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0750,%{frr_user},%{frr_group})    %ghost %{frr_logs}
%dir %attr(0750,%{frr_user},%{frr_group})    %ghost %{frr_home}
%dir %attr(0751,%{frr_user},%{frrvty_group}) %ghost %{frr_statedir}
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
%{frr_daemondir}/frr-reload
%{frr_daemondir}/frr-reload.py
%{frr_daemondir}/frr_babeltrace.py
%{frr_daemondir}/frrcommon.sh
%{frr_daemondir}/frrinit.sh
%{frr_daemondir}/generate_support_bundle.py
%{frr_daemondir}/isisd
%{frr_daemondir}/ldpd
%{frr_daemondir}/mgmtd
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
%{frr_daemondir}/fpm_listener
%dir %{_libdir}/frr
%dir %{_libdir}/frr/modules
%{_libdir}/frr/modules/zebra_cumulus_mlag.so
%{_libdir}/frr/modules/zebra_fpm.so
%{_libdir}/frr/modules/pathd_pcep.so
%{_libdir}/frr/modules/bgpd_rpki.so
%if %{with grpc}
%{_libdir}/frr/modules/grpc.so
%endif
%{_libdir}/frr/modules/dplane_fpm_nl.so
%{_libdir}/frr/modules/bgpd_bmp.so
%{_sysusersdir}/%{name}-user.conf

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

%files -n libmgmt_be_nb0
%{_libdir}/libmgmt_be_nb.so.0*

%files -n libmlag_pb0
%{_libdir}/libmlag_pb.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*pc

%changelog
