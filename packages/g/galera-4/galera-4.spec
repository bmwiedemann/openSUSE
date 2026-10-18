#
# spec file for package galera-4
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        26.4.28
Release:        0
Summary:        Galera: a synchronous multi-master wsrep provider (replication engine)
License:        GPL-2.0-only
URL:            https://galeracluster.com/
Source:         galera-%{version}.tar.xz
Source2:        garb-user.conf
Patch0:         galera-3-25.3.10_fix_startup_scripts.patch
BuildRequires:  boost-devel >= 1.41
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
# for fileownership of galeradir
BuildRequires:  mariadb >= %{mariadb_version}
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(systemd)
Requires:       %{name}-wsrep-provider
Requires(post): %fillup_prereq
Conflicts:      galera-3
%sysusers_requires
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_filesystem-devel >= 1.41
BuildRequires:  libboost_program_options-devel >= 1.41
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_system-devel
%endif
%endif
# for fileownership of galeradir
%if %{with split_package}
BuildRequires:  mysql-server
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(openssl)
%else
BuildRequires:  openssl-devel
%endif
%if %{defined fedora}
BuildRequires:  python
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
%autosetup -p1 -n galera-%{version}

%build
%sysusers_generate_pre %{SOURCE2} garb garb-user.conf
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%if 0%{?suse_version} > 1320
export CFLAGS="$CFLAGS -Wno-implicit-fallthrough"
export CXXFLAGS="$CXXFLAGS -Wno-implicit-fallthrough"
%endif
%cmake \
  -DINSTALL_LIBDIR=%{_lib} \
  -DINSTALL_GARBD=bin \
  -DINSTALL_GARBD_SYSTEMD=libexec \
  -DINSTALL_GARBD_SERVICE=lib/systemd/system \
  -DINSTALL_GARBD_CONFIGURATION=etc \
  -DINSTALL_MANPAGE=share/man/man8 \
  -DINSTALL_DOCDIR=share/doc/packages/%{name}
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

sed -e 's;%{_prefix}/libexec;%{_libexecdir};' -i %{buildroot}%{_unitdir}/garb.service
# Upstream installs garb-systemd via install(FILES) (MGL-163), losing the
# executable bit the old install(PROGRAMS) gave it; systemd ExecStarts it.
chmod 0755 %{buildroot}%{_libexecdir}/garb-systemd

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
