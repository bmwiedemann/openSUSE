#
# spec file for package galera-4
#
# Copyright (c) 2022 SUSE LLC
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
%define docs %{_docdir}/%{name}
%define homedir   %{_localstatedir}/lib/garb
%define galeradir %{_localstatedir}/lib/galera
%define mariadb_version 10.5.10
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           galera-4
Version:        26.4.13
Release:        0
Summary:        Galera: a synchronous multi-master wsrep provider (replication engine)
License:        GPL-2.0-only
Group:          Productivity/Databases/Tools
URL:            https://galeracluster.com/
Source:         https://releases.galeracluster.com/galera-4.12/source/%{name}-%{version}.tar.gz
Source1:        https://releases.galeracluster.com/galera-4.12/source/%{name}-%{version}.tar.gz.asc
Source2:        garb-user.conf
Patch0:         galera-3-25.3.10_fix_startup_scripts.patch
Patch2:         fix-cmake-install.patch
BuildRequires:  boost-devel
BuildRequires:  check-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
# for fileownership of galeradir
BuildRequires:  mariadb >= %{mariadb_version}
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
%sysusers_requires
BuildRequires:  pkgconfig(systemd)
Requires:       %{name}-wsrep-provider
Conflicts:      galera-3
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  cmake
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
Requires(post): %fillup_prereq

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
%sysusers_generate_pre %{SOURCE2} garb garb-user.conf
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%if 0%{?suse_version} > 1320
export CFLAGS="$CFLAGS -Wno-implicit-fallthrough"
export CXXFLAGS="$CXXFLAGS -Wno-implicit-fallthrough"
%endif
%cmake -DGALERA_SYSTEMD_UNITDIR:PATH=%{_unitdir} \
       -DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_libexecdir} \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_datarootdir}/doc/packages/%{name}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sysusersdir}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/

mkdir -p %{buildroot}%{_fillupdir}
mv %{buildroot}%{_prefix}/etc/garb.cnf %{buildroot}%{_fillupdir}/sysconfig.garb

install -D -d -m 0750 %{buildroot}%{homedir} %{buildroot}%{galeradir}
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/my.cnf.d/
cat > %{buildroot}%{_sysconfdir}/my.cnf.d/51-%{name}-wsrep-provider.cnf <<EOF
# All changes to this file will be overwritten with the next package update.
# For configuring galera please use 50-galera.cnf or another file
# This file is only here to set the proper path to the wsrep_provider library
[mysqld]
wsrep_provider=%{_libdir}/libgalera_smm.so
EOF

sed -e 's;/usr/libexec;%{_libexecdir};' -i %{buildroot}%{_unitdir}/garb.service

%files
# common
%doc %{docs}
# /common
# garb
%{_unitdir}/garb.service
%{_libexecdir}/garb-systemd
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
%{_libdir}/libgalera_smm.so
%config %{_sysconfdir}/my.cnf.d/51-%{name}-wsrep-provider.cnf

%pre -f garb.pre
%service_add_pre garb.service

%preun
%service_del_preun garb.service

%post
%service_add_post garb.service
%fillup_only -n garb

%postun
%service_del_postun garb.service

%changelog
