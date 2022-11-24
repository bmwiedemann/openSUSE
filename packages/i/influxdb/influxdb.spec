#
# spec file for package influxdb
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


%if 0%{?suse_version} > 1230 || 0%{?rhel_version} > 6 || 0%{?centos_version} > 6 || 0%{?fedora_version} >= 20 || 0%{?el7}%{?fc20}%{?fc21}%{?fc22}
%bcond_without systemd
%else
%bcond_with    systemd
%endif

Name:           influxdb
Summary:        Scalable datastore for metrics, events, and real-time analytics
License:        MIT
Group:          Productivity/Databases/Servers
Version:        1.10.0
Release:        0
URL:            https://github.com/influxdata/influxdb
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        influxdb.service
Source3:        influxdb.tmpfiles
Source4:        influxdb.init
Source5:        Compability_note.txt
Patch0:         harden_influxdb.service.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  go >= 1.18
BuildRequires:  golang-packaging >= 15.0.8
BuildRequires:  xmlto
BuildRequires:  pkgconfig(flux) >= 0.170.1
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}
%endif
Requires(pre):  pwdutils
%if %{with systemd}
%{systemd_requires}
Requires(post): systemd
%else
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
%endif
# conflicts with new package influxdb2
Conflicts:      influxdb2
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
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 1 -n %{name}-%{version}
%patch0 -p1

%build
# Disable phone-home to usage.influxdata.com
sed -i 's/.*reporting-disabled = false/reporting-disabled = true/' etc/config.sample.toml
%goprep github.com/influxdata/influxdb
%gobuild -mod=vendor -ldflags="-X main.version=%{version}" cmd/...

make -C ./man build

%install
%gosrc
%fdupes -s %{buildroot}/%{go_contribsrcdir}/github.com/influxdata/influxdb

mkdir -p %{buildroot}%{_sysconfdir}/influxdb
install -D -m 644 etc/config.sample.toml %{buildroot}%{_sysconfdir}/influxdb/config.toml
mkdir -p %{buildroot}%{_localstatedir}/log/influxdb
mkdir -p %{buildroot}%{_localstatedir}/lib/influxdb
mkdir -p %{buildroot}%{_localstatedir}/lib/influxdb/{data,meta,hh,wal}
mkdir -p %{buildroot}%{_sbindir}
%if %{with systemd}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/influxdb.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcinfluxdb
install -D -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/influxdb.conf
%else
install -D -m 0755 %{S:4} %{buildroot}%{_sysconfdir}/init.d/influxdb
ln -s -f %{_sysconfdir}/init.d/influxdb %{buildroot}%{_sbindir}/rcinfluxdb
mkdir -p %{buildroot}%{_localstatedir}/run/influxdb
%endif
install -D -m 0755 -t %{buildroot}%{_bindir} %{_builddir}/go/bin/*

# Warn about compatibility problems with previous version
mkdir -p %{buildroot}%{_localstatedir}/adm/update-messages/
cp -v %{SOURCE5} %{buildroot}%{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

make -C ./man install DESTDIR=%{buildroot}%{_prefix}

%check
#%%gotest github.com/influxdata/influxdb

%pre
getent group influxdb >/dev/null || groupadd -r influxdb
getent passwd influxdb >/dev/null || useradd -r -g influxdb \
	-d %{_localstatedir}/lib/influxdb \
	-s /sbin/nologin \
	-c "user for InfluxDB database server" influxdb
%if %{with systemd}
%service_add_pre influxdb.service
%endif

%preun
%if %{with systemd}
%service_del_preun influxdb.service
%else
%stop_on_removal influxdb
%endif

%if %{with systemd}
%post
%tmpfiles_create %_tmpfilesdir/influxdb.conf
%service_add_post influxdb.service
%endif

%postun
%if %{with systemd}
%service_del_postun influxdb.service
%else
%restart_on_update influxdb
%insserv_cleanup
%endif

%files
%license LICENSE
%doc QUERIES.md README.md CHANGELOG.md
%dir %{_sysconfdir}/influxdb
%config(noreplace) %attr(0640 root,influxdb) %{_sysconfdir}/influxdb/config.toml
%{_bindir}/influx
%{_bindir}/influx_inspect
%{_bindir}/influxd
%{_bindir}/influx_tools
%{_sbindir}/rcinfluxdb
%if %{with systemd}
%{_unitdir}/influxdb.service
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/influxdb.conf
%else
/etc/init.d/influxdb
%attr(0755, influxdb, influxdb) %dir %{_rundir}/influxdb
%endif
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/log/influxdb
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/lib/influxdb
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/lib/influxdb/meta
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/lib/influxdb/data
%attr(0755, influxdb, influxdb) %dir %{_localstatedir}/lib/influxdb/hh
%attr(0700, influxdb, influxdb) %dir %{_localstatedir}/lib/influxdb/wal
%{_mandir}/man1/influx.1.gz
%{_mandir}/man1/influx_inspect.1.gz
%{_mandir}/man1/influxd-backup.1.gz
%{_mandir}/man1/influxd-config.1.gz
%{_mandir}/man1/influxd-restore.1.gz
%{_mandir}/man1/influxd-run.1.gz
%{_mandir}/man1/influxd-version.1.gz
%{_mandir}/man1/influxd.1.gz
%{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

%files devel
%license LICENSE
%dir %{go_contribsrcdir}/github.com
%dir %{go_contribsrcdir}/github.com/influxdata
%{go_contribsrcdir}/github.com/influxdata/influxdb

%changelog
