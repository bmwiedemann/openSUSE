#
# spec file for package containers-systemd
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


%define containers bind cups dhcp-server dovecot fetchmail haproxy mariadb minidlna nfs-server nginx openldap postfix roundcube samba spamassassin squid wsdd
%define container_services container-bind.service container-cups.service container-dhcp-server.service container-dhcp6-server.service container-dovecot.service container-fetchmail.service container-haproxy.service container-mariadb.service container-minidlna.service container-nfs-server.service container-nginx.service container-openldap.service container-postfix.service container-roundcube.service container-samba.service container-spamassassin.service container-squid.service container-wsdd.service container-image-prune.service container-image-prune.timer container-certbot-renew.service container-certbot-renew.timer

%if %{undefined service_del_postun_without_restart}
%define service_del_postun_without_restart() \
DISABLE_RESTART_ON_UPDATE=1 \
%service_del_postun %{?*}
%endif

Name:           containers-systemd
Version:        0.0+git20231208.299201e
Release:        0
Summary:        Systemd service files and config files for openSUSE container
License:        MIT
URL:            https://github.com/openSUSE/containers-systemd
Source:         containers-systemd-%{version}.tar.xz
Source1:        containers-systemd.rpmlintrc
BuildArch:      noarch

%description
This package contains the configuration files and systemd units
to run the openSUSE containers via podman managed by systemd.
Currently supported are bind, cups, dhcp-server, dovecot, fetchmail, haproxy,
mariadb, minidlna, nginx, openldap, postfix, roundcube, samba,
spamassassin, squid and wsdd. Additional, there is a timer to cleanup
dangling container images.

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
done
install -m 644 container-certbot.default %{buildroot}%{_distconfdir}/default/container-certbot
install -m 644 container-certbot-renew.service %{buildroot}%{_unitdir}/
install -m 644 container-certbot-renew.timer %{buildroot}%{_unitdir}/
install -m 644 container-dhcp6-server.service %{buildroot}%{_unitdir}/
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
for i in SMTP_PASSWORD LDAP_BIND_PASSWORD; do
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
%ghost %dir /srv/bind
%{_unitdir}/container-cups.service
%{_distconfdir}/default/container-cups
%ghost %dir /srv/cups
%{_unitdir}/container-certbot-renew.service
%{_unitdir}/container-certbot-renew.timer
%{_distconfdir}/default/container-certbot
%{_unitdir}/container-dhcp-server.service
%{_unitdir}/container-dhcp6-server.service
%{_distconfdir}/default/container-dhcp-server
%ghost %dir /srv/dhcp-server
%{_unitdir}/container-dovecot.service
%{_distconfdir}/default/container-dovecot
%ghost %dir /srv/dovecot
%{_unitdir}/container-fetchmail.service
%{_distconfdir}/default/container-fetchmail
%{_unitdir}/container-haproxy.service
%{_distconfdir}/default/container-haproxy
%ghost %dir /srv/haproxy
%{_unitdir}/container-mariadb.service
%{_distconfdir}/default/container-mariadb
%ghost %dir /srv/mariadb
%dir %attr(0700,root,root) %{_sysconfdir}/mariadb-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_ROOT_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_ROOT_HOST
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_DATABASE
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_USER
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/mariadb-secrets/MYSQL_PASSWORD
%{_unitdir}/container-minidlna.service
%{_distconfdir}/default/container-minidlna
%{_unitdir}/container-nfs-server.service
%{_distconfdir}/default/container-nfs-server
%{_unitdir}/container-nginx.service
%{_distconfdir}/default/container-nginx
%ghost %dir /srv/nginx
%{_unitdir}/container-openldap.service
%{_distconfdir}/default/container-openldap
%ghost %dir /srv/openldap
%dir %attr(0700,root,root) %{_sysconfdir}/openldap-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/openldap-secrets/LDAP_ADMIN_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/openldap-secrets/LDAP_CONFIG_PASSWORD
%{_unitdir}/container-postfix.service
%{_distconfdir}/default/container-postfix
%ghost %dir /srv/postfix
%dir %attr(0700,root,root) %{_sysconfdir}/postfix-secrets
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/postfix-secrets/SMTP_PASSWORD
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/postfix-secrets/LDAP_BIND_PASSWORD
%{_unitdir}/container-roundcube.service
%{_distconfdir}/default/container-roundcube
%{_unitdir}/container-samba.service
%{_distconfdir}/default/container-samba
%{_unitdir}/container-spamassassin.service
%{_distconfdir}/default/container-spamassassin
%{_unitdir}/container-squid.service
%{_distconfdir}/default/container-squid
%ghost %dir /srv/squid
%{_unitdir}/container-wsdd.service
%{_distconfdir}/default/container-wsdd
%{_unitdir}/container-image-prune.service
%{_unitdir}/container-image-prune.timer

%changelog
