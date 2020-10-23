#
# spec file for package pacemaker
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


# User-configurable globals and defines to control package behavior
# (these should not test {with X} values, which are declared later)

## User and group to use for nonprivileged services
%global uname hacluster
%global gname haclient

## Where to install Pacemaker documentation
%global pcmk_docdir %{_docdir}/%{name}

# Define conditionals so that "rpmbuild --with <feature>" and
# "rpmbuild --without <feature>" can enable and disable specific features

## Add option to enable support for stonith/external fencing agents
%bcond_without stonithd

## Add option to enable support for storing sensitive information outside CIB
%bcond_without cibsecrets

## Add option to create binaries suitable for use with profiling tools
%bcond_with profiling

## Add option to create binaries with coverage analysis
%bcond_with coverage

## Add option to skip generating documentation
## (the build tools aren't available everywhere)
%bcond_with doc

## Add option to turn off hardening of libraries and daemon executables
%bcond_with hardening

## Add option to disable links for legacy daemon names
%bcond_without legacy_links

# Define globals for convenient use later

%define _rundir /run

%global hacluster_id 90

## Path to Python interpreter (leave commented to auto-detect,
## or uncomment and edit to use a specific version)
%global python_path /usr/bin/python%{python3_version}

# Keep sane profiling data if requested
%if %{with profiling}

## Disable -debuginfo package and stripping binaries/libraries
%define debug_package %{nil}

%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define with_nagios             1
%define enable_lib_cluster_pkg  0
%define enable_fatal_warnings   0
%define with_regression_tests   0

Name:           pacemaker
Version:        2.0.4+20200702.813fdbfdc
Release:        0
Summary:        Scalable High-Availability cluster resource manager
# AGPL-3.0 licensed extra/clustermon.sh is not present in the binary
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
Url:            https://www.clusterlabs.org/
# Hint: use "spectool -s 0 pacemaker.spec" (rpmdevtools) to check the final URL:
# https://github.com/ClusterLabs/pacemaker/archive/e91769e5a39f5cb2f7b097d3c612368f0530535e/pacemaker-e91769e.tar.gz
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
Patch10:        0001-Log-libcrmcommon-lower-message-on-reading-proc-file-.patch
# Required for core functionality
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
# Required for agent_config.h which specifies the correct scratch directory
BuildRequires:  resource-agents
BuildRequires:  sed
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(corosync) >= 2.0.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.16
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libexslt)
# Pacemaker requires a minimum libqb functionality
BuildRequires:  pkgconfig(libqb) > 0.13.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
# Pacemaker requires a minimum Python functionality
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
Requires:       %{name}-cli = %{version}-%{release}
Requires:       corosync >= 2.0.0
Requires:       libpacemaker3 = %{version}-%{release}
Requires:       psmisc
Requires:       python3
Requires:       resource-agents
Recommends:     crmsh
Recommends:     fence-agents
Recommends:     libdlm
Recommends:     sbd
Suggests:       graphviz
Conflicts:      heartbeat < 3.0
Conflicts:      libheartbeat2 < 3.0.0
Provides:       pacemaker-ticket-support = 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
%if %{enable_lib_cluster_pkg}
Requires:       libpacemaker3-cluster = %{version}-%{release}
%endif
# Enables optional functionality
%if 0%{?suse_version} > 1100
BuildRequires:  docbook-xsl-stylesheets
%else
BuildRequires:  docbook-style-xsl
%endif
%if %{with stonithd}
%if 0%{?suse_version}
BuildRequires:  libglue-devel
%else
BuildRequires:  cluster-glue-libs-devel
%endif
%endif
%if %{with doc}
BuildRequires:  asciidoc
BuildRequires:  inkscape
BuildRequires:  publican
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
Requires:       libpacemaker3 = %{version}-%{release}
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

%package -n libpacemaker3
Summary:        Core Pacemaker libraries
Group:          Productivity/Clustering/HA
Requires(pre):  shadow
# sbd 1.4.0+ supports the libpe_status API for pe_working_set_t
Conflicts:      sbd < 1.4.0

%description -n libpacemaker3
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The libpacemaker3 package contains shared libraries needed for cluster
nodes and those just running the CLI tools.

%package -n libpacemaker3-cluster
Summary:        Cluster Libraries used by Pacemaker
Group:          Productivity/Clustering/HA
Requires:       libpacemaker3 = %{version}-%{release}

%description -n libpacemaker3-cluster
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The libpacemaker3-cluster package contains cluster-aware shared
libraries needed for nodes that will form part of the cluster nodes.

%package remote
Summary:        Pacemaker remote daemon for non-cluster nodes
Group:          Productivity/Clustering/HA
Requires:       %{name}-cli = %{version}-%{release}
Requires:       libpacemaker3 = %{version}-%{release}
Requires:       procps
Requires:       resource-agents
%{?systemd_requires}

%description remote
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The %{name}-remote package contains the Pacemaker Remote daemon
which is capable of extending pacemaker functionality to remote
nodes not running the full corosync/cluster stack.

%package -n libpacemaker-devel
Summary:        Pacemaker development package
Group:          Development/Libraries/C and C++
Requires:       libpacemaker3 = %{version}-%{release}
Requires:       libtool-ltdl-devel
Requires:       pkgconfig
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(corosync) >= 2.0.0
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libqb)
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(libxslt)
Requires:       pkgconfig(uuid)
%if %{enable_lib_cluster_pkg}
Requires:       libpacemaker3-cluster = %{version}-%{release}
%endif
%if %{with_regression_tests}
# For the regression tests, we can run them only if all pacemaker
# packages are installed, so we pull that in here for the regression
# builds; this is supposed to be disabled for shipping code.
Requires:       pacemaker
%endif

%description -n libpacemaker-devel
Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

The libpacemaker-devel package contains headers and shared libraries
for developing tools for Pacemaker.

%package       cts
Summary:        Test framework for cluster-related technologies
Group:          Productivity/Clustering/HA
Requires:       %{name} = %{version}-%{release}
Requires:       procps
Requires:       psmisc
Requires:       python3
BuildArch:      noarch
#Requires:       python3-systemd
Recommends:     python3-systemd

%description   cts
Test framework for cluster-related technologies like Pacemaker

%package       doc
Summary:        Documentation for Pacemaker
Group:          Productivity/Clustering/HA
BuildArch:      noarch

%description   doc
Documentation for Pacemaker.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

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

autoreconf -fvi

%configure \
        --docdir=%{_docdir}/%{name}                \
        --disable-static                           \
        --disable-silent-rules                     \
        --with-acl=true                            \
%if %{with_nagios}
        --with-nagios=true                         \
%endif
%if !%{enable_fatal_warnings}
        --enable-fatal-warnings=no                 \
%endif
        PYTHON=%{python_path}                          \
        %{!?with_hardening:    --disable-hardening}    \
        %{!?with_legacy_links: --disable-legacy-links} \
        %{?with_profiling:     --with-profiling}       \
        %{?with_coverage:      --with-coverage}        \
        %{?with_cibsecrets:    --with-cibsecrets}      \
        %{!?with_doc:          --with-brand=}          \
        --with-initdir=%{_initddir}                    \
        --with-runstatedir=%{_rundir}                  \
        --localstatedir=%{_var}                        \
        --with-version=%{version}-%{release}

make %{?_smp_mflags}

%install
%make_install

install -d -m755 %{buildroot}%{_fillupdir}
install -m 644 daemons/pacemakerd/pacemaker.sysconfig %{buildroot}%{_fillupdir}/sysconfig.pacemaker
install -m 644 tools/crm_mon.sysconfig %{buildroot}%{_fillupdir}/sysconfig.crm_mon

# Don't package static libs
find %{buildroot} -type f -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

# For now, don't package the servicelog-related binaries built only for
# ppc64le when certain dependencies are installed. If they get more exercise by
# advanced users, we can reconsider.
rm -f %{buildroot}/%{_sbindir}/notifyServicelogEvent
rm -f %{buildroot}/%{_sbindir}/ipmiservicelogd

# Don't ship init scripts for systemd based platforms
rm -f %{buildroot}/%{_initddir}/pacemaker
rm -f %{buildroot}/%{_initddir}/pacemaker_remote

%if %{with coverage}
GCOV_BASE=%{buildroot}/%{_var}/lib/pacemaker/gcov
mkdir -p $GCOV_BASE
find . -name '*.gcno' -type f | while read F ; do
        D=`dirname $F`
        mkdir -p ${GCOV_BASE}/$D
        cp $F ${GCOV_BASE}/$D
done
%endif

ln -s service %{buildroot}%{_sbindir}/rcpacemaker
ln -s service %{buildroot}%{_sbindir}/rcpacemaker_remote
ln -s service %{buildroot}%{_sbindir}/rccrm_mon

mv %{buildroot}%{_sbindir}/crm_report %{buildroot}%{_sbindir}/crm_report.pacemaker
install -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/crm_report

ln -s ../heartbeat/NodeUtilization %{buildroot}%{_prefix}/lib/ocf/resource.d/pacemaker/

%fdupes -s %{buildroot}

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

%pre -n libpacemaker3
getent group %{gname} >/dev/null || groupadd -r %{gname} -g %{hacluster_id}
getent passwd %{uname} >/dev/null || useradd -r -g %{gname} -u %{hacluster_id} -s /sbin/nologin -c "cluster user" %{uname}
exit 0

%post -n libpacemaker3 -p /sbin/ldconfig
%postun -n libpacemaker3 -p /sbin/ldconfig

%if %{enable_lib_cluster_pkg}
%post -n libpacemaker3-cluster -p /sbin/ldconfig
%postun -n libpacemaker3-cluster -p /sbin/ldconfig
%endif

%if %{with_regression_tests}
%post -n libpacemaker-devel
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
%defattr(-,root,root)
%{_defaultdocdir}/%{name}/
%{_sbindir}/pacemakerd

%{_unitdir}/pacemaker.service
%{_sbindir}/rcpacemaker

%exclude %{_libexecdir}/pacemaker/cts-log-watcher
%exclude %{_libexecdir}/pacemaker/cts-support
%exclude %{_sbindir}/pacemaker-remoted
%if %{with legacy_links}
%exclude %{_sbindir}/pacemaker_remoted
%endif
%dir %{_libexecdir}/pacemaker
%{_libexecdir}/pacemaker/*

%{_sbindir}/fence_legacy

%{_mandir}/man7/pacemaker-controld.7%{ext_man}
%{_mandir}/man7/pacemaker-schedulerd.7%{ext_man}
%{_mandir}/man7/pacemaker-fenced.7%{ext_man}
%{_mandir}/man7/ocf_pacemaker_controld.7%{ext_man}
%{_mandir}/man7/ocf_pacemaker_o2cb.7%{ext_man}
%{_mandir}/man7/ocf_pacemaker_remote.7%{ext_man}
%{_mandir}/man8/fence_legacy.8%{ext_man}
%{_mandir}/man8/pacemakerd.8%{ext_man}

%doc %{_datadir}/pacemaker/alerts

#%license licenses/GPLv2
%doc COPYING ChangeLog

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/cib
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/pengine
%{_prefix}/lib/ocf/resource.d/pacemaker/controld
%{_prefix}/lib/ocf/resource.d/pacemaker/o2cb
%{_prefix}/lib/ocf/resource.d/pacemaker/remote

%files cli
%defattr(-,root,root)
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
%{_sbindir}/crm_standby
%{_sbindir}/crm_verify
%{_sbindir}/crmadmin
%{_sbindir}/iso8601
%{_sbindir}/crm_shadow
%{_sbindir}/crm_simulate
%{_sbindir}/crm_report
%{_sbindir}/crm_report.pacemaker
%{_sbindir}/crm_rule
%{_sbindir}/crm_ticket
%{_sbindir}/stonith_admin
%exclude %{_datadir}/pacemaker/alerts
%exclude %{_datadir}/pacemaker/tests
%{_datadir}/pacemaker
%{_datadir}/pkgconfig/pacemaker-schemas.pc
%{_datadir}/snmp/mibs/PCMK-MIB.txt

%exclude %{_prefix}/lib/ocf/resource.d/pacemaker/controld
%exclude %{_prefix}/lib/ocf/resource.d/pacemaker/o2cb
%exclude %{_prefix}/lib/ocf/resource.d/pacemaker/remote

%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%{_prefix}/lib/ocf/resource.d/pacemaker

%config(noreplace) %{_fillupdir}/sysconfig.pacemaker
%config(noreplace) %{_fillupdir}/sysconfig.crm_mon
%{_mandir}/man7/*
%exclude %{_mandir}/man7/pacemaker-controld.*
%exclude %{_mandir}/man7/pacemaker-schedulerd.*
%exclude %{_mandir}/man7/pacemaker-fenced.*
%exclude %{_mandir}/man7/ocf_pacemaker_controld.*
%exclude %{_mandir}/man7/ocf_pacemaker_o2cb.*
%exclude %{_mandir}/man7/ocf_pacemaker_remote.*
%{_mandir}/man8/*
%exclude %{_mandir}/man8/fence_legacy.*
%exclude %{_mandir}/man8/pacemakerd.*
%exclude %{_mandir}/man8/pacemaker-remoted.*

#%license licenses/GPLv2
%doc COPYING ChangeLog

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/blackbox
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/cores
%dir %attr (770, %{uname}, %{gname}) %{_var}/log/pacemaker
%dir %attr (770, %{uname}, %{gname}) %{_var}/log/pacemaker/bundles

%files -n libpacemaker3
%defattr(-,root,root)

%{_libdir}/libcib.so.*
%{_libdir}/liblrmd.so.*
%{_libdir}/libcrmservice.so.*
%{_libdir}/libcrmcommon.so.*
%{_libdir}/libpe_status.so.*
%{_libdir}/libpe_rules.so.*
%{_libdir}/libpacemaker.so.*
%{_libdir}/libstonithd.so.*
#%license licenses/LGPLv2.1
%doc COPYING ChangeLog
%{_libdir}/libcrmcluster.so.*

%if %{enable_lib_cluster_pkg}
%files -n libpacemaker3-cluster
%defattr(-,root,root)
%{_libdir}/libcrmcluster.so.*
#%license licenses/LGPLv2.1
%doc COPYING ChangeLog
%endif

%files remote
%defattr(-,root,root)
%{_unitdir}/pacemaker_remote.service
%{_sbindir}/rcpacemaker_remote

%{_sbindir}/pacemaker-remoted
%if %{with legacy_links}
%{_sbindir}/pacemaker_remoted
%endif
%{_mandir}/man8/pacemaker-remoted.8%{ext_man}
#%license licenses/GPLv2
%doc COPYING ChangeLog

%if %{with doc}
%files doc
%defattr(-,root,root)
%doc %{pcmk_docdir}
#%license licenses/CC-BY-SA-4.0
%endif

%files cts
%defattr(-,root,root)
%{python3_sitelib}/cts
%{_datadir}/pacemaker/tests

%{_libexecdir}/pacemaker/cts-log-watcher
%{_libexecdir}/pacemaker/cts-support

#%license licenses/GPLv2
%doc COPYING ChangeLog

%files -n libpacemaker-devel
%defattr(-,root,root)
%{_includedir}/pacemaker
%{_libdir}/*.so
%if %{with coverage}
%{_var}/lib/pacemaker/gcov
%endif
%{_libdir}/pkgconfig/*.pc
#%license licenses/LGPLv2.1
%doc COPYING ChangeLog

%changelog
