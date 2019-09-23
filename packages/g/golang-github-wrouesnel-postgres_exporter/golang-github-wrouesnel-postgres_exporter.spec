#
# spec file for package golang-github-wrouesnel-postgres_exporter
#
# Copyright (c) 2017 Silvio Moioli <moio@suse.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%{go_nostrip}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define project github.com/wrouesnel/postgres_exporter
Name:           golang-github-wrouesnel-postgres_exporter
Version:        0.4.7
Release:        0
License:        Apache-2.0
Summary:        Prometheus exporter for PostgreSQL
Url:            https://prometheus.io/
Group:          System/Management
Source:         postgres_exporter-%{version}.tar.xz
Source1:        prometheus-postgres_exporter.service
Source2:        prometheus-postgres_exporter.sysconfig
Patch0:         architectures.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API)
BuildRequires:  xz
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow
%{go_provides}

%description
Prometheus exporter for PostgreSQL server metrics. Supported PostgreSQL versions: 9.1 and up.

%prep
%setup -q -n postgres_exporter-%{version}
%patch0 -p1

%build
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

go run mage.go binary

%install
cd $HOME/go/src/%{project}
install -D -m 0755 bin/postgres_exporter_v0.0.0_linux-*/postgres_exporter %{buildroot}/%{_bindir}/prometheus-postgres_exporter

install -m755 -d %buildroot%{_fillupdir}
install -m644 %{S:2} %buildroot%{_fillupdir}/sysconfig.prometheus-postgres_exporter

install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/prometheus-postgres_exporter.service
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcprometheus-postgres_exporter

%pre
%service_add_pre prometheus-postgres_exporter.service
getent group prometheus >/dev/null || %{_sbindir}/groupadd -r prometheus
getent passwd prometheus >/dev/null || %{_sbindir}/useradd -r -g prometheus -d %{_localstatedir}/lib/prometheus -M -s /sbin/nologin prometheus

%post
%fillup_only -n prometheus-postgres_exporter
%service_add_post prometheus-postgres_exporter.service

%preun
%service_del_preun prometheus-postgres_exporter.service

%postun
%service_del_postun prometheus-postgres_exporter.service

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/prometheus-postgres_exporter
%{_fillupdir}/sysconfig.prometheus-postgres_exporter
%{_sbindir}/rcprometheus-postgres_exporter
%{_unitdir}/prometheus-postgres_exporter.service

%changelog
