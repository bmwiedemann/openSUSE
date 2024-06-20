#
# spec file for package netdata
#
# Copyright (c) 2024 SUSE LLC
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


%define netdata_user    netdata
%define netdata_group   netdata

%define __builder ninja

Name:           netdata
Version:        1.46.0
Release:        0
Summary:        A system for distributed real-time performance and health monitoring
# netdata is GPL-3.0+, other licenses refer to included third-party software (see REDISTRIBUTED.md)
License:        Apache-2.0 AND BSD-2-Clause AND GPL-3.0-or-later AND MIT AND BSD-3-Clause AND LGPL-2.1-or-later AND OFL-1.1 AND CC-BY-4.0 AND WTFPL
Group:          System/Monitoring
URL:            http://my-netdata.io/
Source0:        https://github.com/netdata/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        netdata-rpmlintrc
Patch0:         netdata-logrotate-su.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  judy-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  golang(API) >= 1.22
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libmosquitto)
BuildRequires:  pkgconfig(libnetfilter_acct)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(openssl)
# Broken with current upstream protobuf - uses bundled copy
# BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(yajl)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)
Requires(pre):  shadow permissions
Recommends:     PyYAML
Recommends:     curl
Recommends:     iproute-tc
Recommends:     lm_sensors
Recommends:     nmap-ncat
Recommends:     openssl(cli)
Suggests:       logrotate
Suggests:       nodejs
%if 0%{?suse_version} > 1550
BuildRequires:  python3
%else
BuildRequires:  python311
%endif
%ifarch %ix86 x86_64 aarch64
BuildRequires:  pkgconfig(xenstat)
%endif
BuildRequires:  pkgconfig(libipmimonitoring)
Provides:       group(%{netdata_group})
Provides:       user(%{netdata_user})

%description
Netdata is a system for distributed real-time performance and
health monitoring.
It provides insights, in real-time, of everything happening on the
system it runs on (including applications such as web and database
servers), using interactive web dashboards.

%package plugin-cups
Summary:        The CUPS metrics collection plugin for the Netdata Agent
Enhances:       cups
Requires:       netdata = %{version}
Supplements:    netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/cups.plugin

%description plugin-cups
This plugin allows the Netdata Agent to collect metrics from the
Common UNIX Printing System.

%files plugin-cups
%attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/cups.plugin

%package plugin-freeipmi
Summary:        The FreeIPMI metrics collection plugin for the Netdata Agent
Enhances:       freeipmi
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/freeipmi.plugin

%description plugin-freeipmi
This plugin allows the Netdata Agent to collect metrics from
hardware using FreeIPMI.

%post plugin-freeipmi
%set_permissions

%files plugin-freeipmi
%attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/freeipmi.plugin

%package plugin-nfacct
Summary:        The NFACCT metrics collection plugin for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/nfacct.plugin

%description plugin-nfacct
This plugin allows the Netdata Agent to collect metrics from the
firewall using NFACCT objects.

%post plugin-nfacct
%set_permissions

%files plugin-nfacct
%attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/nfacct.plugin

%package plugin-chartsd
Summary:        The charts.d metrics collection plugin for the Netdata Agent
Requires:       bash
Requires:       netdata = %{version}
Enhances:       nut
Enhances:       apcupsd
Enhances:       iw
Suggests:       sudo
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/charts.d.plugin
BuildArch:      noarch

%description plugin-chartsd
This plugin adds a selection of additional collectors written in
shell script to the Netdata Agent.
It includes collectors for NUT, APCUPSD, LibreSWAN, OpenSIPS, and
Wireless access point statistics.

%files plugin-chartsd
%defattr(0750,root,%{netdata_user},0750)
%{_libexecdir}/%{name}/plugins.d/charts.d.plugin
%{_libexecdir}/%{name}/plugins.d/charts.d.dryrun-helper.sh
%{_libexecdir}/%{name}/charts.d/
%defattr(0644,root,%{netdata_user},0644)
%{_prefix}/lib/%{name}/conf.d/charts.d.conf
%{_prefix}/lib/%{name}/conf.d/charts.d/

%package plugin-pythond
Summary:        The python.d metrics collection plugin for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
%if 0%{?suse_version} > 1550
Requires:       python3
%else
Requires:       python311
%endif
Suggests:       sudo
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/python.d.plugin
BuildArch:      noarch

%description plugin-pythond
This plugin adds a selection of additional collectors written in
Python to the Netdata Agent.
Many of the collectors provided by this package are also available
in netdata-plugin-go. In msot cases, you probably want to use those
versions instead of the Python versions.

%files plugin-pythond
%defattr(0750,root,%{netdata_user},0750)
%{_libexecdir}/%{name}/plugins.d/python.d.plugin
%{_libexecdir}/%{name}/python.d
%defattr(0640,root,%{netdata_user},0640)
%{_prefix}/lib/%{name}/conf.d/python.d.conf
%{_prefix}/lib/%{name}/conf.d/python.d

%package plugin-go
Summary:        The go.d metrics collection plugin for the Netdata Agent
Requires:       netdata = %{version}
Suggests:       nvme-cli
Suggests:       sudo
Supplements:    netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/go.d.plugin

%description plugin-go
This plugin adds a selection of additional collectors written in Go
to the Netdata Agent.
A significant percentage of the application specific collectors
provided by Netdata are part of this plugin, so most users will
want it installed.

%post plugin-go
%set_permissions

%files plugin-go
%defattr(0750,root,%{netdata_user},0750)
# CAP_NET_ADMIN needed for WireGuard collector
# CAP_NET_RAW needed for ping collector
%caps(cap_net_admin,cap_net_raw=eip) %{_libexecdir}/%{name}/plugins.d/go.d.plugin
%defattr(0644,root,%{netdata_user},0644)
%{_prefix}/lib/%{name}/conf.d/go.d.conf
%{_prefix}/lib/%{name}/conf.d/go.d

%package plugin-apps
Summary:        The per-application metrics collection plugin for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/apps.plugin

%description plugin-apps
This plugin allows the Netdata Agent to collect per-application and
per-user metrics without using cgroups.

%post plugin-apps
%set_permissions

%files plugin-apps
%defattr(0750,root,%{netdata_user},0750)
# CAP_DAC_READ_SEARCH and CAP_SYS_PTRACE needed for data collection by the plugin.
%caps(cap_dac_read_search,cap_sys_ptrace=ep) %{_libexecdir}/%{name}/plugins.d/apps.plugin
%defattr(0644,root,%{netdata_user},0644)
%{_prefix}/lib/%{name}/conf.d/apps_groups.conf

%package plugin-slabinfo
Summary:        The slabinfo metrics collector for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/slabinfo.plugin

%description plugin-slabinfo
This plugin allows the Netdata Agent to collect perfromance and
utilization metrics for the Linux kernel’s SLAB allocator.

%post plugin-slabinfo
%set_permissions

%files plugin-slabinfo
%defattr(0750,root,%{netdata_user},0750)
# CAP_DAC_READ_SEARCH needed to access the files the plugin reads to collect data.
%caps(cap_dac_read_search=ep) %{_libexecdir}/%{name}/plugins.d/slabinfo.plugin

%package plugin-perf
Summary:        The perf metrics collector for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/perf.plugin

%description plugin-perf
This plugin allows the Netdata to collect metrics from the Linux
perf subsystem.

%post plugin-perf
%set_permissions

%files plugin-perf
%defattr(0750,root,%{netdata_user},0750)
# Either CAP_SYS_ADMIN or CAP_PERFMON needed for data collection
%caps(cap_perfmon=ep) %{_libexecdir}/%{name}/plugins.d/perf.plugin

%package plugin-debugfs
Summary:        The debugfs metrics collector for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/debugfs.plugin

%description plugin-debugfs
This plugin allows the Netdata Agent to collect Linux kernel
metrics exposed through debugfs.

%post plugin-debugfs
%set_permissions

%files plugin-debugfs
# CAP_DAC_READ_SEARCH required for data collection.
%caps(cap_dac_read_search=ep) %attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/debugfs.plugin

%package plugin-logs-management
Summary:        The logs-management plugin for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/logs-management.plugin

%description plugin-logs-management
This plugin allows the Netdata Agent to collect logs from the system
and parse them to extract metrics.

%files plugin-logs-management
%defattr(0644,root,%{netdata_user},0755)
%{_prefix}/lib/%{name}/conf.d/logsmanagement.d.conf
%{_prefix}/lib/%{name}/conf.d/logsmanagement.d
%defattr(0750,root,%{netdata_user},0750)
# CAP_DAC_READ_SEARCH and CAP_SYSLOG needed for data collection.
%caps(cap_dac_read_search,cap_syslog=ep) %attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/logs-management.plugin

%package plugin-network-viewer
Summary:        The network viewer plugin for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/network-viewer.plugin

%description plugin-network-viewer
This plugin allows the Netdata Agent to provide network connection
mapping functionality for use in netdata Cloud.

%files plugin-network-viewer
%defattr(0750,root,%{netdata_user},0750)
# CAP_SYS_ADMIN, CAP_SYS_PTRACE and CAP_DAC_READ_SEARCH needed for data collection.
%caps(cap_sys_admin,cap_sys_ptrace,cap_dac_read_search=ep) %attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/network-viewer.plugin

%package plugin-systemd-journal
Summary:        The systemd-journal plugin for the Netdata Agent
Requires:       netdata = %{version}
Enhances:       netdata
Provides:       netdata:%{_libexecdir}/%{name}/plugins.d/systemd-journal.plugin

%description plugin-systemd-journal
This plugin allows the Netdata Agent to present entries from the systemd
journal on Netdata Cloud or the local Agent Dashboard.

%files plugin-systemd-journal
%defattr(0750,root,%{netdata_user},0750)
# CAP_DAC_READ_SEARCH required for data collection.
%caps(cap_dac_read_search=ep) %attr(0750,root,%{netdata_user}) %{_libexecdir}/%{name}/plugins.d/systemd-journal.plugin

%prep
%autosetup -n %{name}-v%{version} -p1
sed -i 's,%{_bindir}/env bash,/bin/bash,' src/claim/%{name}-claim.sh.in

%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
%if 0%{?suse_version} > 1550
sed -i 's,^pybinary=.*,pybinary=%{_bindir}/python3,' src/collectors/python.d.plugin/python.d.plugin.in
%else
sed -i 's,^pybinary=.*,pybinary=%{_bindir}/python3.11,' src/collectors/python.d.plugin/python.d.plugin.in
%endif

tar -xf %{SOURCE1} -C src/go/collectors/go.d.plugin
%endif

%build
export GOFLAGS=-mod=vendor
%ifnarch ppc64
    export GOFLAGS="$GOFLAGS -buildmode=pie"
%endif

# Agent-Cloud Link and the Prometheus exporter require protobuf,
# which is broken with openSUSE’s version (too new).
# Bundled protobuf requires Abseil, which this build system
# will fetch from a Git repo.
# They explicitly disable disconnected mode.
%cmake \
    -DENABLE_PLUGIN_EBPF=False \
    -DENABLE_ACLK=False -DENABLE_EXPORTER_PROMETHEUS_REMOTE_WRITE=False \
    -DNETDATA_USER=%{netdata_user} \
    -DCMAKE_INSTALL_PREFIX=/
%cmake_build

%install
%cmake_install
install -D -m 0644 %{buildroot}%{_prefix}/lib/%{name}/system/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{buildroot}%{_prefix}/lib/%{name}/system/logrotate/%{name} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -m 0644 system/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

sed -i 's,^#!%{_bindir}/env bash,#!/bin/bash,;s,^#!%{_bindir}/env sh,#!/bin/sh,' \
    %{buildroot}%{_libexecdir}/%{name}/plugins.d/* \
    %{buildroot}%{_sysconfdir}/%{name}/edit-config

# Respect FHS
mv %{buildroot}%{_sysconfdir}/%{name}/edit-config %{buildroot}%{_libexecdir}/%{name}
sed -i 's|%{_prefix}/lib|%{_libdir}|' %{buildroot}%{_libexecdir}/%{name}/edit-config

# This should be opt-in, not opt-out.
# Disable statistics by default.
touch %{buildroot}%{_sysconfdir}/%{name}/.opt-out-from-anonymous-statistics

install -m 755 -d %{buildroot}%{_localstatedir}/cache/%{name}
install -m 755 -d %{buildroot}%{_localstatedir}/log/%{name}
install -m 755 -d %{buildroot}%{_localstatedir}/lib/%{name}/registry

rm %{buildroot}%{_prefix}/lib/%{name}/conf.d/netdata-updater.conf
rm -r %{buildroot}%{_prefix}/lib/%{name}/system
rm %{buildroot}%{_libexecdir}/%{name}/install-service.sh
rm %{buildroot}%{_libexecdir}/%{name}/netdata-updater.sh

# This is a suid binary that is supposed to allow Netdata to run
# some privileged commands. Not packaged due to security concerns.
rm %{buildroot}%{_libexecdir}/%{name}/plugins.d/ndsudo

%fdupes %{buildroot}/lib %{buildroot}%{_libexecdir} %{buildroot}%{_datadir}

%check

%pre
getent group %{netdata_group} >/dev/null || \
    %{_sbindir}/groupadd -r %{netdata_group}
getent passwd %{netdata_user} >/dev/null || \
    %{_sbindir}/useradd -r -g %{netdata_group} -s /bin/false \
    -c "netdata daemon user" -d %{_localstatedir}/lib/empty %{netdata_user}
%{_sbindir}/usermod -g %{netdata_group} %{netdata_user} >/dev/null
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md CHANGELOG.md
%license LICENSE REDISTRIBUTED.md

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/plugins.d
%{_libexecdir}/%{name}/plugins.d/*.sh
%exclude %{_libexecdir}/%{name}/plugins.d/charts.d.dryrun-helper.sh
%{_libexecdir}/%{name}/plugins.d/cgroup-network
%{_libexecdir}/%{name}/plugins.d/ioping.plugin
%{_libexecdir}/%{name}/plugins.d/local-listeners
%{_libexecdir}/%{name}/plugins.d/loopsleepms.sh.inc
%ifarch %ix86 x86_64 aarch64
%{_libexecdir}/%{name}/plugins.d/xenstat.plugin
%endif

%dir %{_prefix}/lib/%{name}
%dir %{_prefix}/lib/%{name}/conf.d
%dir %{_prefix}/lib/%{name}/conf.d/schema.d
%{_prefix}/lib/%{name}/conf.d/health.d
%{_prefix}/lib/%{name}/conf.d/statsd.d
%{_prefix}/lib/%{name}/conf.d/vnodes
%{_prefix}/lib/%{name}/conf.d/exporting.conf
%{_prefix}/lib/%{name}/conf.d/health_alarm_notify.conf
%{_prefix}/lib/%{name}/conf.d/health_email_recipients.conf
%{_prefix}/lib/%{name}/conf.d/ioping.conf
%{_prefix}/lib/%{name}/conf.d/netdata.conf
%{_prefix}/lib/%{name}/conf.d/stream.conf
%{_prefix}/lib/%{name}/conf.d/schema.d/*.json

%{_sbindir}/%{name}
%{_sbindir}/%{name}-claim.sh
%{_sbindir}/%{name}cli
%{_sbindir}/rc%{name}
%{_sbindir}/systemd-cat-native

%{_unitdir}/%{name}.service

%attr(-,root,%{netdata_group}) %dir %{_datadir}/%{name}
%attr(-,root,%{netdata_group}) %{_datadir}/%{name}/web

%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/cache/%{name}
%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/log/%{name}
%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/lib/%{name}

# Do not allow users to read netdata config dir and files as they can
# contain passwords!
%defattr(0640,root,%{netdata_group},0750)

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/health.d
%dir %{_sysconfdir}/%{name}/python.d
%dir %{_sysconfdir}/%{name}/statsd.d

%config(noreplace) %{_sysconfdir}/%{name}/.opt-out-from-anonymous-statistics
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
# used for statistics
%config %{_sysconfdir}/%{name}/.install-type

%attr(0750,root,%{netdata_group}) %{_libexecdir}/%{name}/edit-config

%changelog
