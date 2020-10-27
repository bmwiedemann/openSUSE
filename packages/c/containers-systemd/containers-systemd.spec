#
# spec file for package containers-systemd
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


%define containers bind dhcp-server haproxy mariadb nginx openldap postfix squid
%define container_services container-bind.service container-dhcp-server.service container-dhcp6-server.service container-haproxy.service container-mariadb.service container-nginx.service container-openldap.service container-postfix.service container-squid.service container-image-prune.timer

%if %{undefined service_del_postun_without_restart}
%define service_del_postun_without_restart() \
DISABLE_RESTART_ON_UPDATE=1 \
%service_del_postun %{?*}
%endif

Name:           containers-systemd
Version:        0.0+git20201027.f1d33d8
Release:        0
Summary:        Systemd service files and config files for openSUSE container
License:        MIT
URL:            https://github.com/kubic-project/containers-systemd
Source:         containers-systemd-%{version}.tar.xz
Source1:        containers-systemd.rpmlintrc
BuildArch:      noarch

%description
This package contains the configuration files and systemd units
to run the openSUSE containers via podman managed by systemd.
Currently supported are bind, dhcp-server, mariadb, nginx and squid.
Additional, there is a timer to cleanup dangling container images.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_distconfdir}/default
for i in %{containers}; do
    mkdir -p %{buildroot}/srv/$i
    install -m 644 container-$i.default %{buildroot}%{_distconfdir}/default/container-$i
    install -m 644 container-$i.service %{buildroot}%{_unitdir}/
    # create symlink for rccontainer-*
    ln -s /sbin/service %{buildroot}%{_sbindir}/rccontainer-$i
done
install -m 644 container-dhcp6-server.service %{buildroot}%{_unitdir}/
ln -s /sbin/service %{buildroot}%{_sbindir}/rccontainer-dhcp6-server
install -m 644 container-image-prune.service %{buildroot}%{_unitdir}/
install -m 644 container-image-prune.timer %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/mariadb-secrets
for i in MYSQL_ROOT_PASSWORD MYSQL_ROOT_HOST MYSQL_DATABASE MYSQL_USER MYSQL_PASSWORD; do
  touch %{buildroot}%{_sysconfdir}/mariadb-secrets/$i
done
mkdir -p %{buildroot}%{_sysconfdir}/openldap-secrets
for i in LDAP_ADMIN_PASSWORD LDAP_CONFIG_PASSWORD; do
  touch %{buildroot}%{_sysconfdir}/openldap-secrets/$i
done
mkdir -p %{buildroot}%{_sysconfdir}/postfix-secrets
for i in SMTP_PASSWORD LDAP_MAIL_READER_PASSWORD; do
  touch %{buildroot}%{_sysconfdir}/postfix-secrets/$i
done

%pre
%service_add_pre %{container_services}

%post
%service_add_post %{container_services}

%preun
%service_del_preun %{container_services}

%postun
# Avoid useless container restarts on update of this package
%service_del_postun_without_restart %{container_services}

%files
%license LICENSE
%doc README.md
%{_unitdir}/container-bind.service
%{_distconfdir}/default/container-bind
%{_sbindir}/rccontainer-bind
%ghost %dir /srv/bind
%{_unitdir}/container-dhcp-server.service
%{_unitdir}/container-dhcp6-server.service
%{_distconfdir}/default/container-dhcp-server
%{_sbindir}/rccontainer-dhcp-server
%{_sbindir}/rccontainer-dhcp6-server
%ghost %dir /srv/dhcp-server
%{_unitdir}/container-haproxy.service
%{_distconfdir}/default/container-haproxy
%{_sbindir}/rccontainer-haproxy
%ghost %dir /srv/haproxy
%{_unitdir}/container-mariadb.service
%{_distconfdir}/default/container-mariadb
%{_sbindir}/rccontainer-mariadb
%ghost %dir /srv/mariadb
%dir %attr(0700,root,root) %{_sysconfdir}/mariadb-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_ROOT_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_ROOT_HOST
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_DATABASE
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_USER
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_PASSWORD
%{_unitdir}/container-nginx.service
%{_distconfdir}/default/container-nginx
%{_sbindir}/rccontainer-nginx
%ghost %dir /srv/nginx
%{_unitdir}/container-openldap.service
%{_distconfdir}/default/container-openldap
%{_sbindir}/rccontainer-openldap
%ghost %dir /srv/openldap
%dir %attr(0700,root,root) %{_sysconfdir}/openldap-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/openldap-secrets/LDAP_ADMIN_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/openldap-secrets/LDAP_CONFIG_PASSWORD
%{_unitdir}/container-postfix.service
%{_distconfdir}/default/container-postfix
%{_sbindir}/rccontainer-postfix
%ghost %dir /srv/postfix
%dir %attr(0700,root,root) %{_sysconfdir}/postfix-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/postfix-secrets/SMTP_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/postfix-secrets/LDAP_MAIL_READER_PASSWORD
%{_unitdir}/container-squid.service
%{_distconfdir}/default/container-squid
%{_sbindir}/rccontainer-squid
%ghost %dir /srv/squid
%{_unitdir}/container-image-prune.service
%{_unitdir}/container-image-prune.timer

%changelog
