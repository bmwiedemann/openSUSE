#
# spec file for package influxdb2
#
# Copyright (c) 2023 SUSE LLC
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


Name:           influxdb2
Summary:        Scalable datastore for metrics, events, and real-time analytics
License:        MIT
Group:          Productivity/Databases/Servers
Version:        2.7.1
Release:        0
URL:            https://github.com/influxdata/influxdb
Source:         %{name}-%{version}.tar.xz
Source1:        influxdb.service
Source2:        influxdb.tmpfiles
Source3:        influxdb-user.conf
Source4:        config.yaml
# Prebuild UI assets as specified in ./scripts/fetch_ui_assets.sh
# https://github.com/influxdata/ui/releases/download/OSS-v2.6.1/build.tar.gz
Source98:       ui-assets-%{version}.tar.xz
Source99:       vendor.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  sysuser-tools
%{sysusers_requires}
BuildRequires:  fdupes
BuildRequires:  go >= 1.19
BuildRequires:  golang-packaging >= 15.0.8
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(flux) >= 0.191.0
%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}
%{systemd_requires}
Requires(post): systemd
ExcludeArch:    %ix86 %arm ppc

%description
InfluxDB is an distributed time series database with no external dependencies.
It's useful for recording metrics, events, and performing analytics.

%package devel
Summary:        InfluxDB development files
Group:          Development/Languages/Golang
Requires:       go

%description devel
Go sources and other development files for InfluxDB

%prep
%setup -q
%setup -q -T -D -a 99
%setup -q -T -D -a 98
mv build ui
echo 'UI assets predownloaded!' > ui/fetch_ui_assets.sh

%build
export GO111MODULE=on

# TODO:
# Disable phone-home to usage.influxdata.com

# Build influxdb
%goprep github.com/influxdata/influxdb/v2
%gobuild -mod=vendor -ldflags="-X main.version=%{version}" cmd/...

%sysusers_generate_pre %{SOURCE3} %{name}

%install
%gosrc
%fdupes -s %{buildroot}/%{go_contribsrcdir}/github.com/influxdata/influxdb

mkdir -p %{buildroot}%{_localstatedir}/log/influxdb
mkdir -p %{buildroot}%{_localstatedir}/lib/influxdb
mkdir -p %{buildroot}%{_datadir}/influxdb2/ui
cp ui/build/* %{buildroot}%{_datadir}/influxdb2/ui
mkdir -p %{buildroot}%{_sbindir}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/influxdb.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcinfluxdb
install -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/influxdb.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/influxdb-user.conf
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/influxdb2/config.yaml
install -D -m 0755 -t %{buildroot}%{_bindir} %{_builddir}/go/bin/*

%fdupes %{buildroot}/%{_prefix}

%check
#%%gotest github.com/influxdata/influxdb

%pre -f %{name}.pre
%service_add_pre influxdb.service

%preun
%service_del_preun influxdb.service

%post
%tmpfiles_create %_tmpfilesdir/influxdb.conf
%service_add_post influxdb.service

%postun
%service_del_postun influxdb.service

%files
%license LICENSE
%doc README.md CHANGELOG.md
%dir %{_sysconfdir}/influxdb2
%config(noreplace) %{_sysconfdir}/influxdb2/config.yaml
%{_bindir}/influxd
%{_bindir}/telemetryd
%{_sbindir}/rcinfluxdb
%{_unitdir}/influxdb.service
%{_datadir}/influxdb2
%{_sysusersdir}/influxdb-user.conf
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/influxdb.conf
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/log/influxdb
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/lib/influxdb
%ghost %attr(0755, influxdb, influxdb) %dir %{_rundir}/influxdb

%files devel
%license LICENSE
%dir %{go_contribsrcdir}/github.com
%dir %{go_contribsrcdir}/github.com/influxdata
%{go_contribsrcdir}/github.com/influxdata/influxdb

%changelog
