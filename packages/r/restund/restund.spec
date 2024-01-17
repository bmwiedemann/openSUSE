#
# spec file for package restund
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%define restund_user restund
%define restund_group restund
%define restund_home %{_localstatedir}/lib/restund
Name:           restund
Version:        0.4.12
Release:        0
Summary:        Modular STUN/TURN server
License:        BSD-3-Clause
Group:          Productivity/Telephony/Servers
URL:            http://www.creytiv.com/restund.html
Source:         http://www.creytiv.com/pub/restund-%{version}.tar.gz
Source1:        %{name}.service
Source2:        re.mk
BuildRequires:  mysql-devel
BuildRequires:  re-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  shadow

%description
Restund is a modular and flexible STUN and TURN Server with IPv4 and
IPv6 support.
The server is designed around the principle of a lightweight core
using server modules to extend its functionality.

Some of the modules supported:
 * Authentication module
 * Binding module
 * MySQL module
 * Statistics module
 * Status module
 * Syslog module
 * TURN module

%prep
%setup -q
sed -e 's|@$(CC)|$(CC)|g' \
    -e 's|@$(LD)|$(LD)|g' \
    -e 's|@$(AR)|$(AR)|g' \
    -e 's|@rm -rf|rm -rf|g' \
     -i Makefile
sed -e 's|/usr/local/lib|%{_libdir}|g' \
    -e 's|%{_sysconfdir}/restund.auth|%{_sysconfdir}/restund/restund.auth|g' \
    -i etc/restund.conf
mkdir -p ../re/mk
cp %{SOURCE2} ../re/mk

%build
export CFLAGS="%optflags -fPIE"
export EXTRA_LFLAGS="-pie"
%make_build BUILD=$(pwd)

%install
make DESTDIR=%{buildroot} LIBDIR=%{_libdir}  install
install -d %{buildroot}%{_sysconfdir}/restund
install -pm 0640 etc/restund.conf %{buildroot}%{_sysconfdir}/restund/restund.conf
install -pm 0640 etc/restund.auth %{buildroot}%{_sysconfdir}/restund/restund.auth
install -d %{buildroot}/%{_localstatedir}/lib/restund
install -D -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -d %{buildroot}%{_bindir}
install -pm755 util/genha1.sh %{buildroot}%{_bindir}/restund-genha1
install -pm755 util/genrest.sh %{buildroot}%{_bindir}/restund-genrest
# Don't package munin plugins
rm -rf %{buildroot}%{_datadir}/munin/

%pre
%service_add_pre %{name}.service
# Create restund user/group
getent group %{restund_group} >/dev/null || groupadd -r %{restund_group}
getent passwd %{restund_user} >/dev/null || useradd -r -g %{restund_group} -d %{restund_home} -s /sbin/nologin -c "restund -  Modular STUN/TURN Server" %{restund_user}

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license docs/COPYING
%doc docs/ChangeLog docs/README docs/restund.txt docs/tuning.txt
%dir %{_sysconfdir}/restund
%config(noreplace) %attr(0640,root,%{restund_group}) %{_sysconfdir}/restund/restund.conf
%config(noreplace) %attr(0640,root,%{restund_group}) %{_sysconfdir}/restund/restund.auth
%{_sbindir}/restund
%{_sbindir}/rc%{name}
%{_bindir}/restund-genha1
%{_bindir}/restund-genrest
%dir %{_libdir}/restund
%dir %{_libdir}/restund/modules
%{_libdir}/restund/modules/auth.so
%{_libdir}/restund/modules/binding.so
%{_libdir}/restund/modules/filedb.so
%{_libdir}/restund/modules/mysql_ser.so
%{_libdir}/restund/modules/restauth.so
%{_libdir}/restund/modules/stat.so
%{_libdir}/restund/modules/status.so
%{_libdir}/restund/modules/syslog.so
%{_libdir}/restund/modules/turn.so
%{_localstatedir}/lib/restund
%{_unitdir}/%{name}.service

%changelog
