#
# spec file for package pacemaker
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


# User-configurable globals and defines to control package behavior
# (these should not test {with X} values, which are declared later)

## User and group to use for nonprivileged services
%global uname hacluster
%global gname haclient

## Where to install Pacemaker documentation
%global pcmk_docdir %{_docdir}/%{name}

## Where bug reports should be submitted
## Leave bug_url undefined to use ClusterLabs default, others define it here

## What to use as the OCF resource agent root directory
%global ocf_root %{_prefix}/lib/ocf

# Define conditionals so that "rpmbuild --with <feature>" and
# "rpmbuild --without <feature>" can enable and disable specific features

## Add option to enable support for stonith/external fencing agents
%bcond_without stonithd

## Add option to enable support for storing sensitive information outside CIB
%bcond_without cibsecrets

## Add option to enable Native Language Support (experimental)
%bcond_with nls

## Add option to create binaries suitable for use with profiling tools
%bcond_with profiling

## Allow deprecated option to skip or enable documentation
%bcond_with doc

## Add option to default to start-up synchronization with SBD.
##
## If enabled, SBD *MUST* be built to default similarly, otherwise data
## corruption could occur. Building both Pacemaker and SBD to default
## to synchronization improves safety, without requiring higher-level tools
## to be aware of the setting or requiring users to modify configurations
## after upgrading to versions that support synchronization.
%if 0%{?suse_version} >= 1540 || 0%{?sle_version} >= 150400
%bcond_without sbd_sync
%else
%bcond_with sbd_sync
%endif

## Add option to turn off hardening of libraries and daemon executables
%bcond_with hardening

## Add option to disable links for legacy daemon names
%if 0%{?suse_version} < 1600
%bcond_without legacy_links
%else
%bcond_with legacy_links
%endif

# Define globals for convenient use later

%if 0%{?suse_version} >= 1560 || 0%{?sle_version} >= 150600
## Base GnuTLS cipher priorities (presumably only the initial, required keyword)
## overridable with "rpmbuild --define 'pcmk_gnutls_priorities PRIORITY-SPEC'"
%define gnutls_priorities %{?pcmk_gnutls_priorities}%{!?pcmk_gnutls_priorities:@SYSTEM}
%endif

%global hacluster_id 90

## Distro-specific configuration choices

### Use 2.0-style output when other distro packages don't support current output
%if 0%{?suse_version} < 1600
%global compat20 --enable-compat-2.0
%endif

### Default concurrent-fencing to true when distro prefers that
%if 0%{?suse_version} >= 1540 || 0%{?sle_version} >= 150400
%global concurrent_fencing --with-concurrent-fencing-default=true
%endif

### Default resource-stickiness to 1 when distro prefers that
%if 0%{?suse_version} >= 1540 || 0%{?sle_version} >= 150400
%global resource_stickiness --with-resource-stickiness-default=1
%endif

# Python-related definitions

## Prefer Python 3 definitions explicitly, in case 2 is also available
%global python_path %{__python3}

# Keep sane profiling data if requested
%if %{with profiling}

## Disable -debuginfo package and stripping binaries/libraries
%define debug_package %{nil}

%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} < 1600
%define with_nagios             1
%else
%define with_nagios             0
%endif

%define enable_cluster_libs_pkg  0
%define enable_fatal_warnings   0
%define with_regression_tests   0

Name:           pacemaker
Version:        2.1.7+20240530.09c4d6d2e
Release:        0
Summary:        Scalable High-Availability cluster resource manager
# AGPL-3.0 licensed extra/clustermon.sh is not present in the binary
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
URL:            https://www.clusterlabs.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        crm_report.in
Source100:      pacemaker.rpmlintrc
Patch1:         bug-806256_pacemaker-log-level-notice.patch
Patch2:         bug-728579_pacemaker-stonith-dev-id.patch
Patch3:         pacemaker-nagios-plugin-dir.patch
Patch4:         bug-812269_pacemaker-fencing-device-register-messages.patch
Patch5:         pacemaker-Wno-format-signedness.patch
Patch6:         bug-943295_pacemaker-lrmd-log-notice.patch
Patch7:         bug-977201_pacemaker-controld-self-fencing.patch
Patch8:         bug-995365_pacemaker-cts-restart-systemd-journald.patch
Patch9:         pacemaker-cts-StartCmd.patch
Patch10:        bsc#1180966-0001-Log-pacemakerd-downgrade-the-warning-about-SBD_SYNC_.patch
# Required basic build tools
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-tools >= 0.18
BuildRequires:  grep
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# Required for agent_config.h which specifies the correct scratch directory
BuildRequires:  resource-agents
BuildRequires:  sed
BuildRequires:  pkgconfig(bzip2)
# Required for "make check"
BuildRequires:  pkgconfig(cmocka) >= 1.1.0
BuildRequires:  pkgconfig(corosync) >= 2.0.0
BuildRequires:  pkgconfig(dbus-1)
# Required for core functionality
BuildRequires:  pkgconfig(glib-2.0) >= 2.42
BuildRequires:  pkgconfig(gnutls)
# Pacemaker requires a minimum libqb functionality
BuildRequires:  pkgconfig(libqb) >= 0.17.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(ncurses)
# Pacemaker requires a minimum Python functionality
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
Requires:       %{name}-cli = %{version}-%{release}
%if %{enable_cluster_libs_pkg}
Requires:       %{name}-cluster-libs = %{version}-%{release}
%endif
Requires:       %{name}-libs = %{version}-%{release}
Requires:       corosync >= 2.0.0
Requires:       python3
Requires:       python3-%{name} = %{version}-%{release}
Requires:       resource-agents
Recommends:     crmsh
Recommends:     fence-agents
Recommends:     libdlm
Recommends:     sbd
Suggests:       graphviz
Conflicts:      heartbeat < 3.0
Conflicts:      libheartbeat2 < 3.0.0
# Booth requires this
Provides:       pacemaker-ticket-support = 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
# Enables optional functionality
%if 0%{?suse_version} > 1100
BuildRequires:  docbook-xsl-stylesheets
%else
BuildRequires:  docbook-style-xsl
%endif
%if %{with stonithd}
%if 0%{?suse_version}
BuildRequires:  cluster-glue-devel
%else
BuildRequires:  cluster-glue-libs-devel
%endif
%endif
%if %{with doc}
BuildRequires:  asciidoc
BuildRequires:  inkscape
BuildRequires:  python3-sphinx
%endif
%if %{with_regression_tests}
BuildRequires:  procps
BuildRequires:  python3-curses
BuildRequires:  python3-xml
%endif

%description
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

It supports more than 16 node clusters with significant capabilities
for managing resources and dependencies.

It will run scripts at initialization, when machines go up or down,
when related resources fail and can be configured to periodically check
resource health.

%package cli
Summary:        Command line tools for controlling Pacemaker clusters
Group:          Productivity/Clustering/HA
Requires:       %{name}-libs = %{version}-%{release}
Requires:       logrotate
Requires:       perl-TimeDate
Requires:       procps
Requires:       psmisc
Requires(post): coreutils
# For crm_report
Recommends:     tar
Recommends:     bzip2

%description cli
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-cli package contains command line tools that can be used
to query and control the cluster from machines that may, or may not,
be part of the cluster.

%package libs
Summary:        Core Pacemaker libraries
Group:          System/Libraries
Requires(pre):  shadow
Requires:       %{name}-schemas = %{version}-%{release}
# sbd 1.4.0+ supports the libpe_status API for pe_working_set_t
# sbd 1.4.2+ supports startup/shutdown handshake via pacemakerd-api
#            and handshake defaults to enabled for rhel builds
# sbd 1.5.1+ handshake defaults to enabled with upstream sbd-release
#            implicitly supports handshake defaults to enabled in this spec
Conflicts:      sbd < 1.5.1
Provides:       libpacemaker3 = %version-%release
Obsoletes:      libpacemaker3 < %version-%release

%description libs
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-libs package contains shared libraries needed for cluster
nodes and those just running the CLI tools.

%package cluster-libs
Summary:        Cluster Libraries used by Pacemaker
Group:          System/Libraries
Requires:       %{name}-libs = %{version}-%{release}

%description cluster-libs
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-cluster-libs package contains cluster-aware shared
libraries needed for nodes that will form part of the cluster nodes.

%package -n python3-%{name}
Summary:        Python libraries for Pacemaker
Requires:       %{name}-libs = %{version}-%{release}
Requires:       python3
BuildArch:      noarch

%description -n python3-%{name}
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The python3-%{name} package contains a Python library that can be used
to interface with Pacemaker.

%package remote
Summary:        Pacemaker remote executor daemon for non-cluster nodes
Group:          Productivity/Clustering/HA
Requires:       %{name}-cli = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       resource-agents
%{?systemd_requires}

%description remote
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-remote package contains the Pacemaker Remote daemon
which is capable of extending pacemaker functionality to remote
nodes not running the full corosync/cluster stack.

%package devel
Summary:        Pacemaker development package
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libtool-ltdl-devel
Requires:       pkgconfig
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(corosync) >= 2.0.0
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libqb)
Requires:       pkgconfig(libxml-2.0) >= 2.6.0
Requires:       pkgconfig(libxslt)
Requires:       pkgconfig(uuid)
%if %{enable_cluster_libs_pkg}
Requires:       %{name}-cluster-libs = %{version}-%{release}
%endif
%if %{with_regression_tests}
# For the regression tests, we can run them only if all pacemaker
# packages are installed, so we pull that in here for the regression
# builds; this is supposed to be disabled for shipping code.
Requires:       pacemaker
%endif
Provides:       libpacemaker-devel = %version-%release
Obsoletes:      libpacemaker-devel < %version-%release

%description devel
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-devel package contains headers and shared libraries
for developing tools for Pacemaker.

%package cts
Summary:        Test framework for cluster-related technologies
Group:          Productivity/Clustering/HA
Requires:       %{name} = %{version}-%{release}
Requires:       procps
Requires:       psmisc
Requires:       python3
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-psutil
BuildArch:      noarch
#Requires:       python3-systemd
Recommends:     python3-systemd

%description cts
Test framework for cluster-related technologies like Pacemaker

%package doc
Summary:        Documentation for Pacemaker
Group:          Productivity/Clustering/HA
BuildArch:      noarch

%description doc
Documentation for Pacemaker.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

%package schemas
Summary:        Schemas and upgrade stylesheets for Pacemaker
Group:          Productivity/Clustering/HA
BuildArch:      noarch

%description schemas
Schemas and upgrade stylesheets for Pacemaker

Pacemaker is an advanced, scalable High-Availability cluster resource
manager

%prep
%autosetup -p1

%build

export systemdsystemunitdir=%{?_unitdir}%{!?_unitdir:no}

%if %{with hardening}
# prefer distro-provided hardening flags in case they are defined
# through _hardening_{c,ld}flags macros, configure script will
# use its own defaults otherwise; if such hardenings are completely
# undesired, rpmbuild using "--without hardening"
# (or "--define '_without_hardening 1'")
export CFLAGS_HARDENED_EXE="%{?_hardening_cflags}"
export CFLAGS_HARDENED_LIB="%{?_hardening_cflags}"
export LDFLAGS_HARDENED_EXE="%{?_hardening_ldflags}"
export LDFLAGS_HARDENED_LIB="%{?_hardening_ldflags}"
%endif

mkdir -p libltdl/config
autoreconf -fvi

%configure \
        --docdir=%{_docdir}/%{name}                \
        --disable-silent-rules                     \
%if %{with_nagios}
        --with-nagios=true                         \
%else
        --with-nagios=false                        \
%endif
%if !%{enable_fatal_warnings}
        --enable-fatal-warnings=no                 \
%endif
        PYTHON=%{python_path}                          \
        %{!?with_hardening:    --disable-hardening}    \
        %{?with_legacy_links:  --enable-legacy-links}  \
        %{?with_profiling:     --with-profiling}       \
        %{?with_cibsecrets:    --with-cibsecrets}      \
        %{?with_nls:           --enable-nls}           \
        %{?with_sbd_sync:      --with-sbd-sync-default="true"} \
        %{?gnutls_priorities:  --with-gnutls-priorities="%{gnutls_priorities}"} \
        %{?bug_url:            --with-bug-url=%{bug_url}} \
        %{?ocf_root:           --with-ocfdir=%{ocf_root}} \
        %{?concurrent_fencing}                         \
        %{?resource_stickiness}                        \
        %{?compat20}                                   \
        --disable-static                               \
        --with-initdir=%{_initddir}                    \
        --with-runstatedir=%{_rundir}                  \
        --localstatedir=%{_var}                        \
        --with-version=%{version}-%{release}

make %{?_smp_mflags}

pushd python
%py3_build
popd

%install
%make_install

pushd python
%py3_install
popd

rm -fr %{buildroot}/etc/sysconfig
install -d -m755 %{buildroot}%{_fillupdir}
install -m 644 etc/sysconfig/pacemaker %{buildroot}%{_fillupdir}/sysconfig.pacemaker
install -m 644 etc/sysconfig/crm_mon %{buildroot}%{_fillupdir}/sysconfig.crm_mon

%if %{with nls}
%find_lang %{name}
%endif

# Don't package static libs
find %{buildroot} -type f -name "*.a" -delete -print
# Don't package libtool archives
find %{buildroot} -type f -name "*.la" -delete -print

ln -s service %{buildroot}%{_sbindir}/rcpacemaker
ln -s service %{buildroot}%{_sbindir}/rcpacemaker_remote
ln -s service %{buildroot}%{_sbindir}/rccrm_mon

mv %{buildroot}%{_sbindir}/crm_report %{buildroot}%{_sbindir}/crm_report.pacemaker
install -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/crm_report

%if 0%{?suse_version} < 1600
ln -s ../heartbeat/NodeUtilization %{buildroot}%{ocf_root}/resource.d/pacemaker/
%endif

%fdupes -s %{buildroot}
%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_libexecdir}/pacemaker/*
%python3_fix_shebang_path %{buildroot}%{_datadir}/pacemaker/tests/*
%python3_fix_shebang_path %{buildroot}%{_datadir}/pacemaker/tests/cts/*
%endif

%check
make %{_smp_mflags} check
# Prevent false positives in rpmlint
./cts/cts-regression -V scheduler cli 2>&1

%pre
%service_add_pre pacemaker.service

%post
%service_add_post pacemaker.service

%preun
%service_del_preun pacemaker.service

%postun
%service_del_postun pacemaker.service

%pre remote
%service_add_pre pacemaker_remote.service

%post remote
%service_add_post pacemaker_remote.service

%preun remote
%service_del_preun pacemaker_remote.service

%postun remote
%service_del_postun pacemaker_remote.service

%pre cli
%service_add_pre crm_mon.service

%post cli
if [ ! -e %{_sysconfdir}/sysconfig/pacemaker ]; then
    %fillup_only -n pacemaker
fi

%service_add_post crm_mon.service

if [ ! -e %{_sysconfdir}/sysconfig/crm_mon ]; then
    %fillup_only -n crm_mon
fi

if [ "$1" -eq "2" ]; then
    # Package upgrade, not initial install:
    # Move any pre-2.0 logs to new location to ensure they get rotated
    { mv -fbS.rpmsave %{_var}/log/pacemaker.log* %{_var}/log/pacemaker \
      || mv -f %{_var}/log/pacemaker.log* %{_var}/log/pacemaker
    } >/dev/null 2>/dev/null || :
fi

%preun cli
%service_del_preun crm_mon.service

%postun cli
%service_del_postun crm_mon.service

%pre libs
getent group %{gname} >/dev/null || groupadd -r %{gname} -g %{hacluster_id}
getent passwd %{uname} >/dev/null || useradd -r -g %{gname} -u %{hacluster_id} -s /sbin/nologin -c "cluster user" %{uname}
exit 0

%if %{defined ldconfig_scriptlets}
%ldconfig_scriptlets libs
%ldconfig_scriptlets cluster-libs
%else
%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%if %{enable_cluster_libs_pkg}
%post cluster-libs -p /sbin/ldconfig
%postun cluster-libs -p /sbin/ldconfig
%endif
%endif

%if %{with_regression_tests}
%post devel
if [ ! -e /tmp/.pcmk_regression_tests_ran ]; then
	touch /tmp/.pcmk_regression_tests_ran
	# Needed so that the shell doesn't get stuck on escape
	# sequences
	export TERM=dumb
	%{_datadir}/pacemaker/tests/cts-cli || true
	%{_datadir}/pacemaker/tests/cts-scheduler -V || true
fi
%endif

%files
%{_defaultdocdir}/%{name}/
%{_sbindir}/pacemakerd

%{_unitdir}/pacemaker.service
%{_sbindir}/rcpacemaker

%exclude %{_libexecdir}/pacemaker/cts-log-watcher
%exclude %{_libexecdir}/pacemaker/cts-support
%exclude %{_sbindir}/pacemaker-remoted
%exclude %{_sbindir}/pacemaker_remoted
%dir %{_libexecdir}/pacemaker
%{_libexecdir}/pacemaker/*

%if %{with stonithd}
%{_sbindir}/fence_legacy
%endif
%{_sbindir}/fence_watchdog

%{_mandir}/man7/pacemaker-based.7%{ext_man}
%{_mandir}/man7/pacemaker-controld.7%{ext_man}
%{_mandir}/man7/pacemaker-schedulerd.7%{ext_man}
%{_mandir}/man7/pacemaker-fenced.7%{ext_man}
%{_mandir}/man7/ocf_pacemaker_controld.7%{ext_man}
%{_mandir}/man7/ocf_pacemaker_o2cb.7%{ext_man}
%{_mandir}/man7/ocf_pacemaker_remote.7%{ext_man}
%if %{with stonithd}
%{_mandir}/man8/fence_legacy.8%{ext_man}
%endif
%{_mandir}/man8/fence_watchdog.8%{ext_man}
%{_mandir}/man8/pacemakerd.8%{ext_man}

%doc %{_datadir}/pacemaker/alerts

#%license licenses/GPLv2
%license COPYING
%doc ChangeLog

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/cib
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/pengine
%{ocf_root}/resource.d/pacemaker/controld
%{ocf_root}/resource.d/pacemaker/o2cb
%{ocf_root}/resource.d/pacemaker/remote

%files cli
%dir %attr (750, root, %{gname}) %{_sysconfdir}/pacemaker
%config(noreplace) %{_sysconfdir}/logrotate.d/pacemaker
%{_unitdir}/crm_mon.service
%{_sbindir}/rccrm_mon
%{_sbindir}/attrd_updater
%{_sbindir}/cibadmin
%if %{with cibsecrets}
%{_sbindir}/cibsecret
%endif
%{_sbindir}/crm_attribute
%{_sbindir}/crm_diff
%{_sbindir}/crm_error
%{_sbindir}/crm_failcount
%{_sbindir}/crm_master
%{_sbindir}/crm_mon
%{_sbindir}/crm_node
%{_sbindir}/crm_resource
%{_sbindir}/crm_rule
%{_sbindir}/crm_standby
%{_sbindir}/crm_verify
%{_sbindir}/crmadmin
%{_sbindir}/iso8601
%{_sbindir}/crm_shadow
%{_sbindir}/crm_simulate
%{_sbindir}/crm_report
%{_sbindir}/crm_report.pacemaker
%{_sbindir}/crm_ticket
%{_sbindir}/stonith_admin
# "dirname" is owned by -schemas, which is a prerequisite
%{_datadir}/pacemaker/report.collector
%{_datadir}/pacemaker/report.common
# XXX "dirname" is not owned by any prerequisite
%{_datadir}/snmp/mibs/PCMK-MIB.txt

%exclude %{ocf_root}/resource.d/pacemaker/controld
%exclude %{ocf_root}/resource.d/pacemaker/o2cb
%exclude %{ocf_root}/resource.d/pacemaker/remote

%dir %{ocf_root}
%dir %{ocf_root}/resource.d
%{ocf_root}/resource.d/pacemaker

%config(noreplace) %{_fillupdir}/sysconfig.pacemaker
%config(noreplace) %{_fillupdir}/sysconfig.crm_mon
%{_mandir}/man7/*pacemaker*
%exclude %{_mandir}/man7/pacemaker-based.*
%exclude %{_mandir}/man7/pacemaker-controld.*
%exclude %{_mandir}/man7/pacemaker-schedulerd.*
%exclude %{_mandir}/man7/pacemaker-fenced.*
%exclude %{_mandir}/man7/ocf_pacemaker_controld.*
%exclude %{_mandir}/man7/ocf_pacemaker_o2cb.*
%exclude %{_mandir}/man7/ocf_pacemaker_remote.*
%{_mandir}/man8/crm*.8%{ext_man}
%{_mandir}/man8/attrd_updater.*
%{_mandir}/man8/cibadmin.*
%if %{with cibsecrets}
%{_mandir}/man8/cibsecret.*
%endif
%{_mandir}/man8/iso8601.*
%{_mandir}/man8/stonith_admin.*

#%license licenses/GPLv2
%license COPYING
%doc ChangeLog

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/blackbox
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/cores
%dir %attr (770, %{uname}, %{gname}) %{_var}/log/pacemaker
%dir %attr (770, %{uname}, %{gname}) %{_var}/log/pacemaker/bundles

%files libs %{?with_nls:-f %{name}.lang}
%{_libdir}/libcib.so.*
%{_libdir}/liblrmd.so.*
%{_libdir}/libcrmservice.so.*
%{_libdir}/libcrmcommon.so.*
%{_libdir}/libpe_status.so.*
%{_libdir}/libpe_rules.so.*
%{_libdir}/libpacemaker.so.*
%{_libdir}/libstonithd.so.*
#%license licenses/LGPLv2.1
%license COPYING
%doc ChangeLog
%if !%{enable_cluster_libs_pkg}
%{_libdir}/libcrmcluster.so.*
%endif

%if %{enable_cluster_libs_pkg}
%files cluster-libs
%{_libdir}/libcrmcluster.so.*
#%license licenses/LGPLv2.1
%license COPYING
%doc ChangeLog
%endif

%files -n python3-%{name}
%{python3_sitelib}/pacemaker/
%{python3_sitelib}/pacemaker-*.egg-info
%exclude %{python3_sitelib}/pacemaker/_cts/
#%license licenses/LGPLv2.1
%license COPYING
%doc ChangeLog

%files remote
%{_unitdir}/pacemaker_remote.service
%{_sbindir}/rcpacemaker_remote

%{_sbindir}/pacemaker-remoted
%{_sbindir}/pacemaker_remoted
%{_mandir}/man8/pacemaker-remoted.8%{ext_man}
#%license licenses/GPLv2
%license COPYING
%doc ChangeLog

%if %{with doc}
%files doc
%doc %{pcmk_docdir}
#%license licenses/CC-BY-SA-4.0
%endif

%files cts
%{python3_sitelib}/pacemaker/_cts/
%{_datadir}/pacemaker/tests

%{_libexecdir}/pacemaker/cts-log-watcher
%{_libexecdir}/pacemaker/cts-support

#%license licenses/GPLv2
%license COPYING
%doc ChangeLog

%files devel
%{_includedir}/pacemaker
%{_libdir}/libcib.so
%{_libdir}/liblrmd.so
%{_libdir}/libcrmservice.so
%{_libdir}/libcrmcommon.so
%{_libdir}/libpe_status.so
%{_libdir}/libpe_rules.so
%{_libdir}/libpacemaker.so
%{_libdir}/libstonithd.so
%{_libdir}/libcrmcluster.so
%{_libdir}/pkgconfig/*pacemaker*.pc
#%license licenses/LGPLv2.1
%license COPYING
%doc ChangeLog

%files schemas
#%license licenses/GPLv2
%dir %{_datadir}/pacemaker
%{_datadir}/pacemaker/*.rng
%{_datadir}/pacemaker/*.xsl
%{_datadir}/pacemaker/api
%{_datadir}/pacemaker/base
%{_datadir}/pkgconfig/pacemaker-schemas.pc

%changelog
