#
# spec file for package resource-agents
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


Name:           resource-agents
Version:        4.14.0+git15.c784b83c
Release:        0
Summary:        HA Reusable Cluster Resource Scripts
License:        GPL-2.0-only AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Clustering/HA
URL:            http://linux-ha.org/
Source:         resource-agents-%{version}.tar.xz
Source1:        monitoring-plugins-metadata.tar.bz2

Patch1:         drop-deprecated-agents.patch
# PATCH-FIX-OPENSUSE: fix path to sm-notify
Patch2:         0002-nfsserver-fix-path-to-sm-notify.patch
# PATCH-FIX-OPENSUSE: ldirectord: don't create subsys lock
Patch3:         0003-ldirectord-don-t-create-subsys-lock.patch
# PATCH-FIX-OPENSUSE: Revert moving binaries to /usr/libexec
Patch4:         0004-Revert-Low-build-Move-binaries-in-usr-lib-heartbeat-.patch
%if 0%{?suse_version} < 1600
# PATCH-FIX-OPENSUSE: Revert ocf_log: use same log format at pacemaker
Patch6:         0006-Revert-ocf_log-use-same-log-format-as-pacemaker.patch
%endif
# PATCH-FIX-OPENSUSE:
Patch7:         0007-Request-to-add-gcp-vpc-move-route.patch

Patch8:         nfsnotify.patch
Patch9:         portblock.patch

# PATCH-FIX-OPENSUSE: Remove deprecated perl-IO-Socket-INET6 dependency
Patch10:        resource-agents-deprecate-INET6.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cluster-glue-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  libqb-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
Requires:       /usr/bin/logger
Obsoletes:      heartbeat-resources
Provides:       %{name}-devel = %{version}
Provides:       heartbeat-resources
# Merging the aws-vpc-move-ip package as the upstream RA will be adopted.
Provides:       aws-vpc-move-ip = 0.2.20171113
Obsoletes:      aws-vpc-move-ip <= 0.2.20171113
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A set of scripts to interface with several services to operate in a
High Availability environment for both Pacemaker and rgmanager
service managers.

%package zfs
Summary:        resource-agent for ZFS support
License:        GPL-2.0-only AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Clustering/HA
Requires:       %{name}
Provides:       %{name}:%{_mandir}/man7/ocf_heartbeat_ZFS.*
Provides:       %{name}:%{_prefix}/lib/ocf/resource.d/heartbeat/ZFS

%package -n ldirectord
Summary:        A Monitoring Daemon for Maintaining High Availability Resources
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
Requires:       %{name}
Requires:       ipvsadm
Requires:       logrotate
Requires:       perl(IO::Socket::IP)
Requires:       perl(MailTools)
Requires:       perl(Net::SSLeay)
Requires:       perl(Socket6)
Requires:       perl(LWP)
Obsoletes:      heartbeat-ldirectord
Provides:       heartbeat-ldirectord
%{?systemd_requires}

%description zfs
Containing the resource agent and documentation for ZFS support

%description -n ldirectord
ldirectord is a stand-alone daemon for monitoring the services on real
servers. Currently, HTTP, HTTPS, and FTP services are supported.
ldirectord works with the heartbeat code (http://www.linux-ha.org/).

See `ldirectord -h` and linux-ha/doc/ldirectord for more information.

%package -n monitoring-plugins-metadata
Summary:        Metadata for Monitoring plugins
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
Requires:       monitoring-plugins-fping
Requires:       monitoring-plugins-http
Requires:       monitoring-plugins-ldap
Requires:       monitoring-plugins-mysql
Requires:       monitoring-plugins-pgsql
Requires:       monitoring-plugins-tcp
Requires:       resource-agents
Provides:       nagios-plugins-metadata
BuildArch:      noarch

%description -n monitoring-plugins-metadata
XML files containing metadata which facilitates using nagios
plugins as resource agents. These files were produced from help
pages of individual nagios plugins.

%prep
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%if 0%{?suse_version} < 1600
%patch -P 6 -p1
%endif
%patch -P 7 -p0
%patch -P 8 -p0
%patch -P 9 -p0
%patch -P 10 -p1

%build
autoreconf -fvi
# because quilt push changed the permissions of  sg_persist.
# chmod 775 heartbeat/sg_persist
%configure \
    --docdir=%{_defaultdocdir}/%{name} \
    --with-ras-set=linux-ha \
    --enable-fatal-warnings=no \
    --enable-libnet=no \
    --with-systemdsystemunitdir=%{_unitdir} \ \
    --with-pkg-name=%{name} \
    --with-rsctmpdir=%{_rundir}/%{name}
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/ha.d/resource.d
ln -s service %{buildroot}/%{_sbindir}/rcldirectord
# Dont package static libs
find %{buildroot} -type f -name "*.la" -delete -print
# Unset execute permissions from things that shouln't have it
find %{buildroot} "(" -name "ocf-*" -o -name "*.dtd" ")" -type f -exec chmod a-x "{}" "+"
chmod 0755 %{buildroot}%{_sbindir}/ocf-tester
chmod 0755 %{buildroot}%{_sbindir}/ocft
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 systemd/resource-agents.conf %{buildroot}%{_prefix}/lib/tmpfiles.d

(
cd %{buildroot}/%{_libdir}/heartbeat
for f in ocf-returncodes ocf-shellfuncs
do
    ln -s %{_prefix}/lib/ocf/lib/heartbeat/$f
done
)

# install nagios plugins XML metadata
tar -xjf %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/nagios/plugins-metadata
for file in $(find plugins-metadata -type f); do
	install -m 644 $file %{buildroot}%{_datadir}/nagios/plugins-metadata
done

# Create a symlink for backward compat of suse:aws-vpc-move-ip
(
mkdir -p %{buildroot}%{_prefix}/lib/ocf/resource.d/suse
cd %{buildroot}%{_prefix}/lib/ocf/resource.d/suse
ln -s %{_prefix}/lib/ocf/resource.d/heartbeat/aws-vpc-move-ip aws-vpc-move-ip
)

%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_prefix}/lib/ocf/resource.d/heartbeat/*
%endif

%post
%service_add_post resource-agents-deps.target
%tmpfiles_create %_tmpfilesdir/resource-agents.conf

%preun
%service_del_preun resource-agents-deps.target

%postun
%service_del_postun resource-agents-deps.target

%pre
%service_add_pre resource-agents-deps.target

%preun -n ldirectord
%service_del_preun ldirectord.service

%postun -n ldirectord
%service_del_postun ldirectord.service

%post -n ldirectord
%service_add_post ldirectord.service

%pre -n ldirectord
%service_add_pre ldirectord.service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/lib
%dir %{_prefix}/lib/tmpfiles.d
%_tmpfilesdir/resource-agents.conf
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.rng
%dir %{_datadir}/%{name}/ocft
%dir %{_datadir}/%{name}/ocft/configs
%config(noreplace) %{_datadir}/%{name}/ocft/configs/*
%{_datadir}/%{name}/ocft/caselib
%{_datadir}/%{name}/ocft/README
%{_datadir}/%{name}/ocft/README.zh_CN
%{_datadir}/%{name}/ocft/helpers.sh
%{_datadir}/%{name}/ocft/runocft
%{_datadir}/%{name}/ocft/runocft.prereq
%{_prefix}/lib/ocf/resource.d/suse
%{_prefix}/lib/ocf/resource.d/heartbeat
%exclude %{_prefix}/lib/ocf/resource.d/heartbeat/ZFS
%{_prefix}/lib/ocf/lib/heartbeat
%{_sbindir}/ocf-tester
%{_sbindir}/ocft
%{_sbindir}/sfex_init
%{_sbindir}/sfex_stat
%{_includedir}/heartbeat
%{_unitdir}/resource-agents-deps.target
%ghost %dir %attr (1755, root, root) %{_rundir}/resource-agents
%doc AUTHORS
%license COPYING
%license COPYING.LGPL
%license COPYING.GPLv3
%doc %{_datadir}/%{name}/ra-api-1.dtd
%{_mandir}/man7/*.7*
%exclude %{_mandir}/man7/ocf_heartbeat_ZFS.*
%{_mandir}/man8/ocf-tester.8*
%{_mandir}/man8/sfex_init.8*
%doc doc/README.webapps
# For compatability with pre-existing agents
%dir %{_sysconfdir}/ha.d
%config %{_sysconfdir}/ha.d/shellfuncs
%dir %{_libdir}/heartbeat
%{_libdir}/heartbeat/*
%{_datadir}/pkgconfig/resource-agents.pc

%files zfs
%{_prefix}/lib/ocf/resource.d/heartbeat/ZFS
%{_mandir}/man7/ocf_heartbeat_ZFS.*

%files -n ldirectord
%defattr(-,root,root)
%doc ldirectord/ldirectord.cf
%{_mandir}/man8/ldirectord.8*
%dir %{_sysconfdir}/ha.d/resource.d
%{_sbindir}/ldirectord
%{_sbindir}/rcldirectord
%{_unitdir}/ldirectord.service
%exclude %{_sysconfdir}/init.d/ldirectord
%{_sysconfdir}/ha.d/resource.d/ldirectord
%config(noreplace) %{_sysconfdir}/logrotate.d/ldirectord

%files -n monitoring-plugins-metadata
%defattr(-,root,root)
%dir %{_datadir}/nagios
%dir %{_datadir}/nagios/plugins-metadata
%attr(0644,root,root) %{_datadir}/nagios/plugins-metadata/*

%changelog
