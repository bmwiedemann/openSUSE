#
# spec file for package quagga
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif
%bcond_with    tcp_zebra
%bcond_without irdp
%bcond_with    isis
%bcond_with    isis_topology
%bcond_without pcre
%if %{defined _rundir}
%define         quagga_statedir %{_rundir}/%{name}
%else
%define         quagga_statedir %{_localstatedir}/run/%{name}
%endif
Name:           quagga
Version:        1.2.4
Release:        0
Summary:        Routing Software for BGP, OSPF and RIP
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Routing
Url:            http://www.quagga.net
Source:         http://download.savannah.gnu.org/releases/quagga/%{name}-%{version}.tar.gz
Source1:        %{name}-SUSE.tar.bz2
Source2:        %{name}.pam
Source3:        http://download.savannah.gnu.org/releases/quagga/%{name}-%{version}.tar.gz.asc
# downloaded from: http://download.savannah.gnu.org/releases/quagga/pgp-54CD2E60.asc
# new download from:
# http://www.nongnu.org/quagga/quagga.net.pgp.asc
Source4:        %{name}.keyring
Source5:        %{name}-tmpfs.conf
Source6:        sysconfig.%{name}
Source7:        %{name}.logrotate
Patch1:         %{name}-add-ospf6_main-return-value.patch
Patch2:         %{name}-add-table_test-return-value.patch
Patch3:         0001-systemd-change-the-WantedBy-target.patch
BuildRequires:  autoconf >= 2.6
BuildRequires:  automake >= 1.6
BuildRequires:  c-ares-devel
BuildRequires:  libtool
BuildRequires:  net-snmp-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  xz
Requires(post): %fillup_prereq
Requires(post): %{install_info_prereq}
# shadow for useradd and groupadd
Requires(pre):  shadow
Recommends:     logrotate
Provides:       zebra = %{version}
Obsoletes:      zebra < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with pcre}
BuildRequires:  pcre-devel
%endif
%if 0%{?suse_version} > 1220
BuildRequires:  makeinfo
%endif
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
Requires(post): %insserv_prereq
%endif

%description
Quagga is a routing software suite, providing implementations of
OSPFv2, OSPFv3, RIP v1 and v2, RIPv3 and BGPv4. Quagga is a fork of
GNU Zebra.

%package -n libospf0
Summary:        Quagga's implementation of the OSPF protocol
Group:          System/Libraries

%description -n libospf0
This library contains part of the OSPFv2 implementation of Quagga.

%package -n libospfapiclient0
Summary:        API for Quagga's OSPFv2 implementation
Group:          System/Libraries

%description -n libospfapiclient0
This library contains part of the OSPFv2 implementation of Quagga.

%package -n libzebra1
Summary:        Quagga utility library
Group:          System/Libraries

%description -n libzebra1
This library contains various utility functions to Quagga, such as
data types, buffers and socket handling.

%package -n libfpm_pb0
Summary:        Quagga fpm protobuf library
Group:          System/Libraries

%description -n libfpm_pb0
This library contains forwarding plane manager protobuf definitions
for Quagga.

%package -n libquagga_pb0
Summary:        Quagga quagga protobuf library
Group:          System/Libraries

%description -n libquagga_pb0
This library contains protobuf memory management for Quagga.

%package devel
Summary:        Development files for quagga, a routing software for BGP, OSPF, RIP
Group:          Development/Libraries/C and C++
Requires:       libfpm_pb0 = %{version}
Requires:       libospf0 = %{version}
Requires:       libospfapiclient0 = %{version}
Requires:       libquagga_pb0 = %{version}
Requires:       libzebra1 = %{version}

%description devel
Quagga is a routing software suite, providing implementations of
OSPFv2, OSPFv3, RIP v1 and v2, RIPv3 and BGPv4. Quagga is a fork of
GNU Zebra.

This subpackage contains the headers for the Quagga libraries.

%prep
%setup -q -a 1
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --disable-static --with-pic \
    --enable-vtysh \
    --enable-rtadv \
    --enable-snmp \
    --enable-ipv6 \
    --with-libpam \
    --enable-netlink \
    %if %{with isis}
    --enable-isisd \
    %endif
    %if %{with isis_topology}
    --enable-isis-topology \
    %endif
    %if %{with tcp_zebra}
    --enable-tcp-zebra \
    %endif
    %if %{with irdp}
    --enable-irdp \
    %endif
    %if %{with pcre}
    --enable-pcreposix \
    %endif
    --sysconfdir=%{_sysconfdir}/quagga \
    --localstatedir=%{quagga_statedir} \
    --enable-multipath=0
make %{?_smp_mflags}

%install
rm -r doc/quagga.info
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -d %{buildroot}%{_sysconfdir}/{init.d,quagga,pam.d,logrotate.d}
%if %{with systemd}
install -d %{buildroot}%{_unitdir}
install -p -m 0644 redhat/zebra.service %{buildroot}%{_unitdir}/zebra.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rczebra
install -p -m 0644 redhat/isisd.service %{buildroot}%{_unitdir}/isisd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcisisd
install -p -m 0644 redhat/ripd.service %{buildroot}%{_unitdir}/ripd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcripd
install -p -m 0644 redhat/ospfd.service %{buildroot}%{_unitdir}/ospfd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcospfd
install -p -m 0644 redhat/bgpd.service %{buildroot}%{_unitdir}/bgpd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcbgpd
install -p -m 0644 redhat/ospf6d.service %{buildroot}%{_unitdir}/ospf6d.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcospf6d
install -p -m 0644 redhat/ripngd.service %{buildroot}%{_unitdir}/ripngd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcripngd
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -p -m 0644 %{SOURCE5} %{buildroot}/%{_tmpfilesdir}/quagga.conf
sed -e "s|@quagga_statedir@|%{quagga_statedir}|g" -i \
                             %{buildroot}/%{_tmpfilesdir}/quagga.conf
%else
install -m 0755 SUSE/* %{buildroot}%{_sysconfdir}/init.d/
ln -sf %{_sysconfdir}/init.d/zebra  %{buildroot}%{_sbindir}/rczebra
ln -sf %{_sysconfdir}/init.d/bgpd   %{buildroot}%{_sbindir}/rcbgpd
ln -sf %{_sysconfdir}/init.d/ospf6d %{buildroot}%{_sbindir}/rcospf6d
ln -sf %{_sysconfdir}/init.d/ospfd  %{buildroot}%{_sbindir}/rcospfd
ln -sf %{_sysconfdir}/init.d/ripngd %{buildroot}%{_sbindir}/rcripngd
ln -sf %{_sysconfdir}/init.d/ripd   %{buildroot}%{_sbindir}/rcripd
%endif
install -d -m 0755 %{buildroot}%{_fillupdir}/
install -m 0644 %{SOURCE6} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/quagga
install -d -m 0750 %{buildroot}%{_localstatedir}/log/quagga
install -d -m 0751 %{buildroot}%{quagga_statedir}
install -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/logrotate.d/quagga
rm -f %{buildroot}%{_sysconfdir}/quagga/*.sample*
cat > %{buildroot}%{_sysconfdir}/quagga/zebra.conf << __EOF__
!hostname quagga

!password quagga
!enable password quagga

log file %{_localstatedir}/log/quagga/zebra.log
__EOF__
cat > %{buildroot}%{_sysconfdir}/quagga/vtysh.conf << __EOF__
! vtysh is using PAM authentication allowing root to use it.
__EOF__

%pre
getent group quagga >/dev/null || %{_sbindir}/groupadd -r quagga || :
getent passwd quagga >/dev/null || \
	%{_sbindir}/useradd -r -g quagga -s %{_bindir}/false \
                  -c "Quagga routing daemon" \
                  -d %{quagga_statedir} quagga || :
%if %{with systemd}
%service_add_pre zebra.service isisd.service ripd.service ospfd.service bgpd.service ospf6d.service ripngd.service
%endif

%post
%if %{with systemd}
# Use %%tmpfiles_create when Leap 43.0 is oldest in support scope
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || :
%service_add_post zebra.service isisd.service ripd.service ospfd.service bgpd.service ospf6d.service ripngd.service
%fillup_only
%else
%fillup_and_insserv
test -d %{quagga_statedir} || mkdir -m 0751 -p %{quagga_statedir}
%endif
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%if %{with systemd}
%service_del_preun zebra.service isisd.service ripd.service ospfd.service bgpd.service ospf6d.service ripngd.service
%else
%stop_on_removal zebra bgpd ospf6d ospfd ripd ripngd
%endif

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%if %{with systemd}
%service_del_postun zebra.service isisd.service ripd.service ospfd.service bgpd.service ospf6d.service ripngd.service
%else
%restart_on_update zebra bgpd ospf6d ospfd ripd ripngd
%insserv_cleanup
%endif

%post   -n libospf0 -p /sbin/ldconfig
%postun -n libospf0 -p /sbin/ldconfig
%post   -n libospfapiclient0 -p /sbin/ldconfig
%postun -n libospfapiclient0 -p /sbin/ldconfig
%post   -n libzebra1 -p /sbin/ldconfig
%postun -n libzebra1 -p /sbin/ldconfig
%post   -n libfpm_pb0 -p /sbin/ldconfig
%postun -n libfpm_pb0 -p /sbin/ldconfig
%post   -n libquagga_pb0 -p /sbin/ldconfig
%postun -n libquagga_pb0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc */*.sample* AUTHORS COPYING* ChangeLog NEWS README REPORTING-BUGS SERVICES TODO
%{_sbindir}/*
%dir %attr(750,quagga,quagga) %{_sysconfdir}/quagga/
%config(noreplace) %attr(640,quagga,quagga) %{_sysconfdir}/%{name}/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%{_fillupdir}/sysconfig.quagga
%if %{with systemd}
%{_unitdir}/*.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/quagga.conf
%else
%config %{_sysconfdir}/init.d/*
%endif
%config (noreplace)%{_sysconfdir}/pam.d/*
%{_bindir}/*
%dir %attr(-,quagga,quagga) %{_localstatedir}/log/quagga
%dir %attr(-,quagga,quagga) %ghost %{quagga_statedir}
%{_infodir}/quagga.info*
%{_mandir}/man?/*

%files -n libospf0
%defattr(-,root,root)
%{_libdir}/libospf.so.*

%files -n libospfapiclient0
%defattr(-,root,root)
%{_libdir}/libospfapiclient.so.*

%files -n libzebra1
%defattr(-,root,root)
%{_libdir}/libzebra.so.*

%files -n libfpm_pb0
%defattr(-,root,root)
%{_libdir}/libfpm_pb.so.*

%files -n libquagga_pb0
%defattr(-,root,root)
%{_libdir}/libquagga_pb.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_includedir}/%{name}/ospfd
%{_includedir}/%{name}/ospfd/*.h
%dir %{_includedir}/%{name}/ospfapi
%{_includedir}/%{name}/ospfapi/*.h

%changelog
