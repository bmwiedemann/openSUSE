#
# spec file for package containers-systemd
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

%define containers bind dhcp-server mariadb
%define container_services container-bind.service container-dhcp-server.service container-dhcp6-server.service container-mariadb.service

Name:           containers-systemd
Version:        0.0+git20191030.b2f919f
Release:        0
Summary:        Systemd service files and config files for openSUSE container
License:        MIT
URL:            https://github.com/thkukuk/containers-systemd
Source:         containers-systemd-%{version}.tar.xz
Source1:        containers-systemd.rpmlintrc
Requires(post): %fillup_prereq
BuildArch:      noarch

%description
This package contains the configuration files and systemd units
to run the openSUSE containers via podman managed by systemd.
Currently supported are bind, dhcp-server and mariadb.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_fillupdir}
for i in %{containers}; do
    mkdir -p %{buildroot}/srv/$i
    install -m 644 sysconfig.container-$i %{buildroot}%{_fillupdir}/
    install -m 644 container-$i.service %{buildroot}%{_unitdir}/
    # create symlink for rccontainer-*
    ln -s /sbin/service %{buildroot}%{_sbindir}/rccontainer-$i
done
install -m 644 container-dhcp6-server.service %{buildroot}%{_unitdir}/
ln -s /sbin/service %{buildroot}%{_sbindir}/rccontainer-dhcp6-server
mkdir -p %{buildroot}%{_sysconfdir}/mariadb-secrets
for i in MYSQL_ROOT_PASSWORD MYSQL_ROOT_HOST MYSQL_DATABASE MYSQL_USER MYSQL_PASSWORD; do
  touch %{buildroot}%{_sysconfdir}/mariadb-secrets/$i
done

%pre
%service_add_pre %{container_services}

%post
for i in %{containers}; do
    %{fillup_only -n container-$i}
done
%service_add_post %{container_services}

%preun
%service_del_preun %{container_services}

%postun
# Avoid useless container restarts on update of this package
DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun %{container_services}

%files
%license LICENSE
%doc README.md
%{_unitdir}/container-bind.service
%{_fillupdir}/sysconfig.container-bind
%{_sbindir}/rccontainer-bind
%ghost %dir /srv/bind
%{_unitdir}/container-dhcp-server.service
%{_unitdir}/container-dhcp6-server.service
%{_fillupdir}/sysconfig.container-dhcp-server
%{_sbindir}/rccontainer-dhcp-server
%{_sbindir}/rccontainer-dhcp6-server
%ghost %dir /srv/dhcp-server
%{_unitdir}/container-mariadb.service
%{_fillupdir}/sysconfig.container-mariadb
%{_sbindir}/rccontainer-mariadb
%ghost %dir /srv/mariadb
%dir %attr(0700,root,root) %{_sysconfdir}/mariadb-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_ROOT_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_ROOT_HOST
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_DATABASE
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_USER
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_PASSWORD

%changelog
