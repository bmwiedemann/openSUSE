#
# spec file for package dehydrated
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


%define _challengedir %{_localstatedir}/lib/acme-challenge
%define _user         dehydrated
%define _home         %{_sysconfdir}/dehydrated
%define _postrunhooks %{_home}/postrun-hooks.d

%if 0%{?sle_version} >= 120100 || 0%{?suse_version} >= 1210 || 0%{?rhel_version} >= 700 || 0%{?centos_version} >= 700
%define  _lock_dir /run/dehydrated
%bcond_without systemd
%else
%define  _lock_dir %{_localstatedir}/run/dehydrated
%bcond_with    systemd
%endif

%if 0%{?sle_version} >= 150000 || 0%{?suse_version} >= 1500 || %{defined fedora}
%bcond_without nginx
%else
%bcond_with    nginx
%endif

%{!?_tmpfilesdir: %global _tmpfilesdir %{_prefix}/lib/tmpfiles.d }
# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

%if 0%{?suse_version}
%define _apache apache2
%else
%define _apache httpd
%endif

Name:           dehydrated
Version:        0.6.5
Release:        0
Summary:        A client for signing certificates with an ACME server
License:        MIT
URL:            https://github.com/lukas2511/dehydrated
Source0:        %{name}-%{version}.tar.gz
Source1:        acme-challenge.conf.apache.in
Source2:        acme-challenge.conf.nginx.in
Source4:        dehydrated.cron.in
Source5:        dehydrated.tmpfiles.d
Source6:        dehydrated.service.in
Source7:        dehydrated.timer
Source9:        README.maintainer
Source10:       README.Fedora
Source11:       README.hooks
Source12:       %{name}-%{version}.tar.gz.asc
Source13:       %{name}.keyring
Source14:       %{name}-rpmlintrc
BuildRequires:  %{_apache}
Requires:       coreutils
Requires:       curl
Requires:       openssl
Requires:       sudo
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Obsoletes:      dehydrated-lighttpd < %{version}-%{release}
Obsoletes:      letsencrypt.sh < %{version}
Provides:       letsencrypt.sh = %{version}
%if %{with nginx}
BuildRequires:  nginx
%endif
%if %{defined fedora}
BuildRequires:  generic-logos
BuildRequires:  generic-logos-httpd
%endif
# openSUSE >= 12.3 has shadow, pwdutils is provided but obsoleted.
%if 0%{?suse_version} >= 1230
BuildRequires:  shadow
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else #with_systemd
%if 0%{?suse_version}
Requires:       cron
%endif
%endif #with_systemd
%if 0%{?suse_version}
Recommends:     dehydrated-acmeresponder
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a client for signing certificates with an ACME server
(currently only provided by letsencrypt) implemented as a relatively
simple bash-script.

It uses the openssl utility for everything related to actually
handling keys and certificates, so you need to have that installed.

Other dependencies are: curl, sed, grep, mktemp (all found on almost
any system, curl being the only exception).

%package %{_apache}
Summary:        Apache Integration for dehydrated
Requires:       %{_apache}
Requires:       %{name}
Obsoletes:      letsencrypt.sh-%{_apache} < %{version}
Provides:       letsencrypt.sh-%{_apache} = %{version}
%if ! 0%{?suse_version}
Requires:       mod_ssl
%endif

%description %{_apache}
This adds a configuration file for dehydrated's acme-challenge to Apache.

%if %{with nginx}
%package nginx
Summary:        Nginx Integration for dehydrated
Requires:       %{name}
Requires:       nginx
Obsoletes:      letsencrypt.sh-nginx < %{version}
Provides:       letsencrypt.sh-nginx = %{version}

%description nginx
This adds a configuration file for dehydrated's acme-challenge to nginx.
%endif #with nginx

%pre
getent group %{_user} >/dev/null || %{_sbindir}/groupadd -r %{_user}
getent passwd %{_user} >/dev/null || %{_sbindir}/useradd -g %{_user} \
	-s /bin/false -r -c "%{_user}" -d %{_home} %{_user}
if [ -e %{_sysconfdir}/dehydrated/config.sh ]; then mv %{_sysconfdir}/dehydrated/config.sh %{_sysconfdir}/dehydrated/config; fi

%if %{with systemd}
%service_add_pre dehydrated.service dehydrated.timer

%post
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf ||:
%service_add_post dehydrated.service dehydrated.timer

%preun
%service_del_preun dehydrated.service dehydrated.timer

%postun
%service_del_postun dehydrated.service dehydrated.timer
%endif

%prep
%setup -q
cp %{SOURCE9} .
cp %{SOURCE10} .

%build

%install
# sensitive keys
mkdir -p %{buildroot}%{_home}/{accounts,certs,chains}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_home}/config.d
mkdir -p %{buildroot}%{_postrunhooks}

cat docs/man/dehydrated.1 | gzip > %{buildroot}%{_mandir}/man1/dehydrated.1.gz

# Silence E: env-script-interpreter
find \( -name \*.sh -o -name dehydrated \) -exec sed -i "s,#!/usr/bin/env bash,#!$(command -v bash),g" {} \;

sed -i "s,#WELLKNOWN=.*,WELLKNOWN=%{_challengedir},g" docs/examples/config
install -m 0644 docs/examples/* %{buildroot}%{_home}
install -m 0644 %{SOURCE11} %{buildroot}%{_postrunhooks}
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 dehydrated %{buildroot}%{_bindir}
install -m 0755 -d %{buildroot}%{_challengedir}

install -m 0755 -d %{buildroot}%{_sysconfdir}/%{_apache}/conf.d
sed "s,@CHALLENGEDIR@,%{_challengedir},g" %{SOURCE1} > acme-challenge.conf
install -m 0644 acme-challenge.conf %{buildroot}%{_sysconfdir}/%{_apache}/conf.d

%if %{with nginx}
install -m 0755 -d %{buildroot}%{_sysconfdir}/nginx
sed "s,@CHALLENGEDIR@,%{_challengedir},g" %{SOURCE2} > acme-challenge
install -m 0644 acme-challenge %{buildroot}%{_sysconfdir}/nginx
%endif #with nginx

%if %{with systemd}
install -D    -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
# Use timer
sed "s,@POSTRUNHOOKS_DIR@,%{_postrunhooks},g" %{SOURCE6} > dehydrated.service
install -D -m 644 dehydrated.service  %{buildroot}%{_unitdir}/dehydrated.service
install -D -m 644 %{SOURCE7}          %{buildroot}%{_unitdir}/dehydrated.timer
if [ $(rpm -q --queryformat='%{VERSION}' systemd) -lt 229 ]; then
# No support for this attribute in systemd < v229
sed -i 's/^RandomizedDelaySec/#&/' %{buildroot}%{_unitdir}/dehydrated.timer 
fi
%if 0%{?suse_version}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcdehydrated
%endif
%else #with systemd
install -D -d -m 0750 %{buildroot}%{_lock_dir}
# Use cron
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.d
sed "s,@POSTRUNHOOKS_DIR@,%{_postrunhooks},g" %{SOURCE4} > dehydrated.cron
install -m 0644 dehydrated.cron %{buildroot}%{_sysconfdir}/cron.d/dehydrated
%endif #with systemd

# Adjust config file
perl -p -i -e 's|#LOCKFILE="\$\{BASEDIR\}/lock"|LOCKFILE="%{_lock_dir}/lock"|' %{buildroot}%{_home}/config
perl -p -i -e 's|#CONFIG_D=|CONFIG_D="%{_home}/config.d"|' %{buildroot}%{_home}/config
perl -p -i -e 's|#DEHYDRATED_USER=|DEHYDRATED_USER="%{_user}"|' %{buildroot}%{_home}/config
perl -p -i -e 's|#DEHYDRATED_GROUP=|DEHYDRATED_GROUP="%{_user}"|' %{buildroot}%{_home}/config

diff -urN docs/examples/config %{buildroot}%{_home}/config ||:

# Rename existing config file config files fror nginx
%if %{with nginx}
%pre nginx 
[ -f %{_sysconfdir}/nginx/conf.d/acme-challenge ] && \
  mv %{_sysconfdir}/nginx/conf.d/acme-challenge %{_sysconfdir}/nginx/conf.d/acme-challenge.conf || :
%endif

%files
%defattr(-,root,root)
%attr(750,root,%{_user}) %dir %{_sysconfdir}/dehydrated
%attr(700,%{_user},%{_user}) %dir %{_sysconfdir}/dehydrated/accounts
%attr(700,%{_user},%{_user}) %dir %{_sysconfdir}/dehydrated/certs
%attr(700,%{_user},%{_user}) %dir %{_sysconfdir}/dehydrated/chains
%config(noreplace) %attr(640,root,%{_user}) %{_sysconfdir}/dehydrated/config
%config(noreplace) %attr(750,root,%{_user}) %{_sysconfdir}/dehydrated/config.d
%config(noreplace) %attr(640,root,%{_user}) %{_sysconfdir}/dehydrated/domains.txt
%config(noreplace) %attr(750,root,%{_user}) %{_sysconfdir}/dehydrated/hook.sh
%dir %attr(750,root,%{_user}) %{_postrunhooks}
%config(noreplace) %attr(640,root,%{_user}) %{_postrunhooks}/README.hooks
%{_bindir}/dehydrated
%attr(-,%{_user},root) %dir %{_localstatedir}/lib/acme-challenge
%{_mandir}/man1/*
%doc LICENSE README.md docs/*.md docs/*.jpg
%doc README.maintainer
%if %{defined redhat}
%doc README.Fedora
%endif
%if %{with systemd}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/dehydrated.service
%{_unitdir}/dehydrated.timer
%if 0%{?suse_version}
%{_sbindir}/rcdehydrated
%endif
%ghost %attr(700,%{_user},%{_user}) %dir %{_lock_dir}
%else #with systemd
%config %{_sysconfdir}/cron.d/dehydrated
%attr(700,%{_user},%{_user}) %dir %{_lock_dir}
%endif

%files %{_apache}
%defattr(-,root,root)
%config %{_sysconfdir}/%{_apache}/conf.d/acme-challenge.conf

%if %{with nginx}
%files nginx
%defattr(-,root,root)
%config %attr(640,root,nginx) %{_sysconfdir}/nginx/acme-challenge
%endif #with nginx

%changelog
