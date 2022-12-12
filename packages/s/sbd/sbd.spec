#
# spec file for package sbd
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013 Lars Marowsky-Bree
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%ifarch s390x s390
# minimum timeout on LPAR diag288 watchdog is 15s
%global watchdog_timeout_default 15
%else
%global watchdog_timeout_default 5
%endif

# Be careful with sync_resource_startup_default
# being enabled. This configuration has
# to be in sync with configuration in pacemaker
# where it is called sbd_sync - assure by e.g.
# mutual rpm dependencies.
%bcond_without sync_resource_startup_default
# Syncing enabled per default will lead to
# syncing enabled on upgrade without adaption
# of the config.
# Setting can still be overruled via sysconfig.
# The setting in the config-template packaged
# will follow the default if below is is left
# empty. But it is possible to have the setting
# in the config-template deviate from the default
# by setting below to an explicit 'yes' or 'no'.
%global sync_resource_startup_sysconfig ""

Name:           sbd
Version:        1.5.1+20221128.8ec8e01
Release:        0
Summary:        Storage-based death
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/ClusterLabs/sbd
Source:         %{name}-%{version}.tar.xz
Patch1:         bsc#1140065-Fix-sbd-cluster-exit-if-cmap-is-disconnected.patch
Patch2:         bsc#1180966-0001-Log-sbd-inquisitor-downgrade-the-warning-about-SBD_S.patch
Patch3:         harden_sbd.service.patch
Patch4:         harden_sbd_remote.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  libaio-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(corosync)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libqb)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pacemaker)
BuildRequires:  pkgconfig(pacemaker-cib)
BuildRequires:  pkgconfig(uuid)
Requires(post): %fillup_prereq
Conflicts:      ClusterTools2 < 2.3.2
Conflicts:      libpacemaker3 < 2.1.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
This package contains the storage-based death functionality.

%package devel
Summary:        Storage-based death environment for regression tests
Group:          Productivity/Clustering/HA
Requires:       %{name} = %{version}-%{release}

%description devel
This package provides an environment + testscripts for
regression-testing sbd.

%prep
%autosetup -n %{name}-%{version} -p1

%build
./autogen.sh

%configure --with-watchdog-timeout-default=%{watchdog_timeout_default} \
           --with-sync-resource-startup-default=%{?with_sync_resource_startup_default:yes}%{!?with_sync_resource_startup_default:no}  \
           --with-sync-resource-startup-sysconfig=%{sync_resource_startup_sysconfig} \
           --with-runstatedir=%{_rundir}
make %{?_smp_mflags}

# Avoid "Unknown key name 'XXX' in section 'Service', ignoring." warnings from systemd on older releases
%if 0%{?sle_version} < 150400
    sed -r -i '/^(Protect(Home|Hostname|KernelLogs|KernelModules|System))=/d' \
        src/sbd.service src/sbd_remote.service
%endif

%install
%make_install LIBDIR=%{_libdir}
install -D -m 0755 src/sbd.sh %{buildroot}%{_datadir}/sbd/sbd.sh
install -D -m 0755 tests/regressions.sh %{buildroot}%{_datadir}/sbd/regressions.sh
install -D -m 0644 src/sbd.service %{buildroot}/%{_unitdir}/sbd.service
install -D -m 0644 src/sbd_remote.service %{buildroot}/%{_unitdir}/sbd_remote.service
ln -s service %{buildroot}%{_sbindir}/rcsbd
ln -s service %{buildroot}%{_sbindir}/rcsbd_remote
mkdir -p %{buildroot}%{_fillupdir}
install -m 0644 src/sbd.sysconfig %{buildroot}%{_fillupdir}/sysconfig.sbd

# Don't package static libs
find %{buildroot} -type f -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%post
%service_add_post sbd.service sbd_remote.service

if [ ! -e %{_sysconfdir}/sysconfig/sbd ]; then
    %fillup_only sbd
fi

%pre
%service_add_pre sbd.service sbd_remote.service

%preun
if [ $1 -eq 0 ]; then
    systemctl disable sbd.service sbd_remote.service
fi

%postun
%service_del_postun_without_restart sbd.service sbd_remote.service

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/stonith/
%{_sbindir}/sbd
%{_sbindir}/rcsbd
%{_sbindir}/rcsbd_remote
%{_datadir}/sbd
%{_datadir}/pkgconfig/sbd.pc
%exclude %{_datadir}/sbd/regressions.sh
%{_mandir}/man8/sbd*
%{_unitdir}/sbd.service
%{_unitdir}/sbd_remote.service
%{_fillupdir}/sysconfig.sbd
%license COPYING

%files devel
%defattr(-,root,root)
%dir %{_datadir}/sbd
%{_datadir}/sbd/regressions.sh
%{_libdir}/libsbdtestbed*
%license COPYING

%changelog
