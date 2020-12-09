#
# spec file for package loki
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


Name:           loki
Version:        2.0.0+git.1603727260.6978ee5d
Release:        0
Summary:        Loki: like Prometheus, but for logs.
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://grafana.com/loki
Source:         %{name}-%{version}.tar.bz2
Source1:        loki.service
Source2:        promtail.service
Source3:        sysconfig.loki
Source4:        sysconfig.promtail
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang-packaging
BuildRequires:  systemd-devel
BuildRequires:  golang(API) >= 1.13
Requires:       group(loki)
Requires:       user(loki)
Requires(post): %fillup_prereq
%systemd_ordering

%{go_nostrip}

%description
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus.

%prep
%setup -q %{name}-%{version}

%build
%define buildpkg github.com/grafana/loki/pkg/build
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor -buildmode=pie -tags=netgo"
export GOLDFLAGS="-s -w -X %{buildpkg}.Version=%{version} \
                        -X %{buildpkg}.Revision=%{release} \
                        -X %{buildpkg}.Branch=NA \
                        -X %{buildpkg}.BuildUser=NA \
                        -X %{buildpkg}.BuildDate=NA"

go build -ldflags="$GOLDFLAGS" ./cmd/loki
go build -ldflags="$GOLDFLAGS" ./cmd/logcli
CGO_ENABLED=1 go build -ldflags="$GOLDFLAGS" ./cmd/promtail

%install

# Service files for Loki and promtail
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/loki.service
install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/promtail.service
install -Dm644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.loki
install -Dm644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.promtail
install -dm755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcloki
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcpromtail

# Config files
install -Dm644 cmd/loki/loki-local-config.yaml \
    %{buildroot}%{_sysconfdir}/loki/loki.yaml
install -Dm644 cmd/promtail/promtail-local-config.yaml \
    %{buildroot}%{_sysconfdir}/loki/promtail.yaml

# Binaries
install -dm755 %{buildroot}%{_bindir}
install -Dm755 loki %{buildroot}%{_bindir}
install -Dm755 promtail %{buildroot}%{_bindir}
install -Dm755 logcli %{buildroot}%{_bindir}

%pre
%service_add_pre loki.service promtail.service

%post
%fillup_only -n loki
%fillup_only -n promtail
%service_add_post loki.service promtail.service

%preun
%service_del_preun loki.service promtail.service

%postun
%service_del_postun loki.service promtail.service

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_unitdir}/loki.service
%{_unitdir}/promtail.service
%{_fillupdir}/sysconfig.loki
%{_fillupdir}/sysconfig.promtail
%{_bindir}/loki
%{_bindir}/promtail
%{_bindir}/logcli
%dir %{_sysconfdir}/loki
%config(noreplace) %{_sysconfdir}/loki/loki.yaml
%config(noreplace) %{_sysconfdir}/loki/promtail.yaml
%{_sbindir}/rcloki
%{_sbindir}/rcpromtail

%changelog
