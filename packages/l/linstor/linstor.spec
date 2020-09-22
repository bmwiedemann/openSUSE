#
# spec file for package linstor
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define NAME_VERS %{name}-server-%{version}
%define GRADLE_TASKS installdist
%define GRADLE_FLAGS --offline --gradle-user-home /tmp --no-daemon --exclude-task generateJava
%define LS_PREFIX %{_datadir}/linstor-server
%define FIREWALLD_SERVICES %{_libexecdir}/firewalld/services
Name:           linstor
Version:        1.8.0
Release:        0
Summary:        DRBD replicated volume manager
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/LINBIT/linstor-server
Source:         http://www.linbit.com/downloads/linstor/%{name}-server-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  gradle
BuildRequires:  java-1_8_0-openjdk-devel
BuildRequires:  java-1_8_0-openjdk-headless
#Still in python2 actually...
BuildRequires:  python3
BuildArch:      noarch

%description
Linstor is a software that manages DRBD replicated LVM/ZFS volumes
across a group of machines. It maintains DRBD configuration on the
participating machines. It creates/deletes the backing LVM/ZFS
volumes. It automatically places the backing volumes among the
participating machines.

%prep
%setup -q -n %{NAME_VERS}

%build
rm -rf ./build/install
gradle %{GRADLE_TASKS} %{GRADLE_FLAGS}

sed -i "s#%{_bindir}/env sh#/bin/sh#" %{_builddir}/%{NAME_VERS}/build/install/linstor-server/bin/Controller \
                                    %{_builddir}/%{NAME_VERS}/build/install/linstor-server/bin/Satellite \
                                    %{_builddir}/%{NAME_VERS}/build/install/linstor-server/bin/linstor-config

%install
mkdir -p %{buildroot}/%{LS_PREFIX}
cp -r %{_builddir}/%{NAME_VERS}/build/install/linstor-server/lib %{buildroot}/%{LS_PREFIX}
rm %{buildroot}/%{LS_PREFIX}/lib/%{NAME_VERS}.jar
cp -r %{_builddir}/%{NAME_VERS}/server/build/install/server/lib/conf %{buildroot}/%{LS_PREFIX}/lib
mkdir -p %{buildroot}/%{LS_PREFIX}/bin
cp -r %{_builddir}/%{NAME_VERS}/build/install/linstor-server/bin/Controller %{buildroot}/%{LS_PREFIX}/bin
cp -r %{_builddir}/%{NAME_VERS}/build/install/linstor-server/bin/Satellite %{buildroot}/%{LS_PREFIX}/bin
cp -r %{_builddir}/%{NAME_VERS}/build/install/linstor-server/bin/linstor-config %{buildroot}/%{LS_PREFIX}/bin
cp -r %{_builddir}/%{NAME_VERS}/scripts/postinstall.sh %{buildroot}/%{LS_PREFIX}/bin/controller.postinst.sh
mkdir -p %{buildroot}/%{_unitdir}
cp -r %{_builddir}/%{NAME_VERS}/scripts/linstor-controller.service %{buildroot}/%{_unitdir}
cp -r %{_builddir}/%{NAME_VERS}/scripts/linstor-satellite.service %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{FIREWALLD_SERVICES}
mkdir -p %{buildroot}/%{_prefix}/lib/firewalld
%if 0
#drbd.xml is included in yast2-drbd
cp %{_builddir}/%{NAME_VERS}/scripts/firewalld/drbd.xml %{buildroot}/%{FIREWALLD_SERVICES}
%endif
cp %{_builddir}/%{NAME_VERS}/scripts/firewalld/linstor-controller.xml %{buildroot}/%{FIREWALLD_SERVICES}
cp %{_builddir}/%{NAME_VERS}/scripts/firewalld/linstor-satellite.xml %{buildroot}/%{FIREWALLD_SERVICES}

mkdir -p %{buildroot}/%{_sysconfdir}/linstor
cp %{_builddir}/%{NAME_VERS}/docs/linstor.toml-example %{buildroot}/%{_sysconfdir}/linstor/
mkdir -p %{buildroot}/%{_sbindir}
ln -fs %{_sbindir}/service %{buildroot}/%{_sbindir}/rclinstor-satellite
ln -fs %{_sbindir}/service %{buildroot}/%{_sbindir}/rclinstor-controller
ls -l %{buildroot}/%{_sbindir}

%fdupes -s %{buildroot}

### common

%package common
Summary:        Common files shared between controller and satellite
Group:          Productivity/Clustering/HA
Requires:       jre-headless

%description common
Linstor shared components between linstor-controller and linstor-satellite

%files common -f %{_builddir}/%{NAME_VERS}/server/jar.deps
%dir %{LS_PREFIX}
%dir %{LS_PREFIX}/lib
%{LS_PREFIX}/lib/server-%{version}.jar
%dir %{LS_PREFIX}/lib/conf
%{LS_PREFIX}/lib/conf/logback.xml
%dir %attr(755,root,root) %{_prefix}/lib/firewalld
%dir %attr(755,root,root) %{FIREWALLD_SERVICES}
%dir %attr(755,root,root) %{_libexecdir}/firewalld

### controller

%package controller
Summary:        Linstor controller specific files
Group:          Productivity/Clustering/HA
Requires:       linstor-common = %{version}
Recommends:     %{python_module linstor}
Recommends:     %{python_module linstor-client}

%description controller
Linstor controller manages linstor satellites and persistent data storage.

%files controller -f %{_builddir}/%{NAME_VERS}/controller/jar.deps
%dir %{LS_PREFIX}
%dir %{LS_PREFIX}/lib
%{LS_PREFIX}/lib/controller-%{version}.jar
%dir %{LS_PREFIX}/bin
%{LS_PREFIX}/bin/Controller
%{LS_PREFIX}/bin/linstor-config
%{LS_PREFIX}/bin/controller.postinst.sh
%{_unitdir}/linstor-controller.service
%{FIREWALLD_SERVICES}/linstor-controller.xml
%dir %{_sysconfdir}/linstor
%{_sysconfdir}/linstor/linstor.toml-example
%{_sbindir}/rclinstor-controller

%pre controller
%service_add_pre linstor-controller.service

%post controller
%{LS_PREFIX}/bin/controller.postinst.sh
%service_add_post linstor-controller.service
%firewalld_reload

%preun controller
%service_del_preun linstor-controller.service

%postun controller
%service_del_postun linstor-controller.service

### satellite

%package satellite
Summary:        Linstor satellite specific files
Group:          Productivity/Clustering/HA
Requires:       drbd-utils
Requires:       linstor-common = %{version}
Requires:       lvm2
Recommends:     %{python_module linstor}
Recommends:     %{python_module linstor-client}

%description satellite
Linstor satellite, communicates with linstor-controller
and creates drbd resource files.

%files satellite -f %{_builddir}/%{NAME_VERS}/satellite/jar.deps
%dir %{LS_PREFIX}
%dir %{LS_PREFIX}/lib
%{LS_PREFIX}/lib/satellite-%{version}.jar
%dir %{LS_PREFIX}/bin
%{LS_PREFIX}/bin/Satellite
%{_unitdir}/linstor-satellite.service
%{FIREWALLD_SERVICES}/linstor-satellite.xml
%if 0
%{FIREWALLD_SERVICES}/drbd.xml
%endif
%{_sbindir}/rclinstor-satellite

%pre satellite
%service_add_pre linstor-satellite.service

%post satellite
%service_add_post linstor-satellite.service
%firewalld_reload

%preun satellite
%service_del_preun linstor-satellite.service

%postun satellite
%service_del_postun linstor-satellite.service

%changelog
