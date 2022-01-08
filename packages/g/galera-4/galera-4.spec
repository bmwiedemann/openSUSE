#
# spec file for package galera-4
#
# Copyright (c) 2021 SUSE LLC
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


%define copyright Copyright 2007-2015 Codership Oy. All rights reserved. Use is subject to license terms under GPLv2 license.
%define libs %{_libdir}/%{name}
%define docs %{_docdir}/%{name}
%define homedir   %{_localstatedir}/lib/garb
%define galeradir %{_localstatedir}/lib/galera
%define mariadb_version 10.5.10
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_with cmake
Name:           galera-4
Version:        26.4.10
Release:        0
Summary:        Galera: a synchronous multi-master wsrep provider (replication engine)
License:        GPL-2.0-only
Group:          Productivity/Databases/Tools
URL:            https://galeracluster.com/
Source:         http://releases.galeracluster.com/galera-4/source/%{name}-%{version}.tar.gz
Source1:        http://releases.galeracluster.com/galera-4/source/%{name}-%{version}.tar.gz.asc
Source2:        garb-user.conf
Patch0:         galera-3-25.3.10_fix_startup_scripts.patch
BuildRequires:  boost-devel
BuildRequires:  check-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
# for fileownership of galeradir
BuildRequires:  mariadb >= %{mariadb_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  sysuser-tools
Requires:       %{name}-wsrep-provider
Conflicts:      galera-3
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%endif
%if %{with cmake}
BuildRequires:  cmake
%endif
# for fileownership of galeradir
%if %{with split_package}
BuildRequires:  mysql-server
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  libopenssl-devel
%else
BuildRequires:  openssl-devel
%endif
%if %{defined fedora}
BuildRequires:  python
%endif
%if %{without cmake}
BuildRequires:  scons
%endif

%description
Galera is a fast synchronous multimaster wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see http://launchpad.net/wsrep. For a description of Galera
replication engine see http://www.codership.com.

%{copyright}

This software comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to modify and redistribute it under the GPLv2 license.

%package wsrep-provider
Summary:        Galera support library
Group:          Productivity/Databases/Tools
URL:            https://galeracluster.com/
Requires:       mariadb-galera >= 10.4
# already required in mariadb-galera
Recommends:     socat
# for old setups. newer setups will need mariadbbackup
Recommends:     xtrabackup
Conflicts:      galera-3-wsrep-provider
Conflicts:      mariadb < 10.4

%description wsrep-provider
Galera is a fast synchronous multimaster wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see http://launchpad.net/wsrep. For a description of Galera
replication engine see http://www.codership.com.

This package provides the libgalera_smm library.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%if 0%{?suse_version} > 1320
export CFLAGS="$CFLAGS -Wno-implicit-fallthrough"
export CXXFLAGS="$CXXFLAGS -Wno-implicit-fallthrough"
%endif
%if %{with cmake}
%cmake
%cmake_build
%else
scons %{?_smp_mflags} deterministic_tests=1 version=%{version} ssl=1 system_asio=1 boost_pool=1
%endif
%sysusers_generate_pre %{SOURCE2} garb garb-user.conf

%install
install -D -m 644 garb/files/garb.service %{buildroot}%{_unitdir}/garb.service
install -D -m 755 garb/files/garb-systemd %{buildroot}%{_bindir}/garb-systemd
mkdir -p %{buildroot}%{_sysusersdir}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/

install -D -m 644 garb/files/garb.cnf        %{buildroot}%{_fillupdir}/sysconfig.garb

install -D -m 755 garb/garbd                 %{buildroot}%{_bindir}/garbd
install -D -m 755 libgalera_smm.so           %{buildroot}%{libs}/libgalera_smm.so

install -d %{buildroot}%{docs}
install -m 644 COPYING                       %{buildroot}%{docs}/COPYING
install -m 644 asio/LICENSE_1_0.txt          %{buildroot}%{docs}/LICENSE.asio
install -m 644 scripts/packages/README       %{buildroot}%{docs}/README
install -m 644 scripts/packages/README-MySQL %{buildroot}%{docs}/README-MySQL

install -D -m 644 man/garbd.8                %{buildroot}%{_mandir}/man8/garbd.8
install -D -d -m 0750 %{buildroot}%{homedir} %{buildroot}%{galeradir}
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/my.cnf.d/
cat > %{buildroot}%{_sysconfdir}/my.cnf.d/51-%{name}-wsrep-provider.cnf <<EOF
# All changes to this file will be overwritten with the next package update.
# For configuring galera please use 50-galera.cnf or another file
# This file is only here to set the proper path to the wsrep_provider library
[mysqld]
wsrep_provider=%{libs}/libgalera_smm.so
EOF

%files
# common
%doc %{docs}
# /common
# garb
%{_unitdir}/garb.service
%{_bindir}/garb-systemd
%config(noreplace,missingok) %{_fillupdir}/sysconfig.garb
%{_bindir}/garbd
#
%{_mandir}/man8/garbd.8%{?ext_man}
#
%dir %attr(0750,garb,garb) %{homedir}
%{_sysusersdir}/garb-user.conf
# /garb
# plugin
%if %{with split_package}
%dir %attr(0750,mysql,mysql) %{galeradir}
%endif
# plugin

%files wsrep-provider
%dir %{libs}
%{libs}/libgalera_smm.so
%config %{_sysconfdir}/my.cnf.d/51-%{name}-wsrep-provider.cnf

%pre -f garb.pre

%service_add_pre garb.service

%preun
%service_del_preun garb.service

%post
%service_add_post garb.service

%postun
%service_del_postun garb.service

%changelog
