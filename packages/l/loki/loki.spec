#
# spec file for package loki
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


%global loki_datadir /var/lib/loki
%global loki_logdir /var/log/loki
%global promtail_datadir /var/lib/promtail

Name:           loki
Version:        2.8.0+git.1680557182.90888a0c
Release:        0
Summary:        Loki: like Prometheus, but for logs
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://grafana.com/loki
Source:         %{name}-%{version}.tar.bz2
Source1:        loki.service
Source2:        promtail.service
Source3:        sysconfig.loki
Source4:        sysconfig.promtail
Source99:       series
Patch0:         harden_promtail.service.patch
Patch1:         proper-data-directories.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang-packaging
BuildRequires:  systemd-devel
BuildRequires:  golang(API) = 1.20
Requires:       logcli = %{version}
Requires:       group(loki)
Requires:       user(loki)
Requires(post): %fillup_prereq
%systemd_ordering

###%%{go_nostrip}

%description
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus.

This package contains the Loki server

%package -n promtail
Summary:        Promtail Client
Group:          System/Monitoring

%description -n promtail
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus.

This package contains the Promtail client.

%package -n logcli
Summary:        LogCLI tool
Group:          System/Monitoring

%description -n logcli
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus.

This package contains the LogCLI command-line tool.

%prep
%autosetup -p1 %{name}-%{version}

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
CGO_ENABLED=1 go build -ldflags="$GOLDFLAGS" ./clients/cmd/promtail

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
install -Dm640 cmd/loki/loki-local-config.yaml \
    %{buildroot}%{_sysconfdir}/loki/loki.yaml
install -Dm640 clients/cmd/promtail/promtail-local-config.yaml \
    %{buildroot}%{_sysconfdir}/loki/promtail.yaml

# Binaries
install -dm755 %{buildroot}%{_bindir}
install -Dm755 loki %{buildroot}%{_bindir}
install -Dm755 promtail %{buildroot}%{_bindir}
install -Dm755 logcli %{buildroot}%{_bindir}

install -D -d -m 0750 %{buildroot}%{promtail_datadir} %{buildroot}%{loki_datadir} %{buildroot}%{loki_logdir}

%pre
%service_add_pre loki.service

%post
%fillup_only
%service_add_post loki.service

%preun
%service_del_preun loki.service

%postun
%service_del_postun loki.service promtail.service

%pre -n promtail
%service_add_pre promtail.service

%post -n promtail
%fillup_only -n promtail
%service_add_post promtail.service

%preun -n promtail
%service_del_preun promtail.service

%postun -n promtail
%service_del_postun promtail.service

%files
%license LICENSE
%doc README.md
%{_unitdir}/loki.service
%{_fillupdir}/sysconfig.loki
%{_bindir}/loki
%dir %{_sysconfdir}/loki
%config(noreplace) %attr(-,root,loki) %{_sysconfdir}/loki/loki.yaml
%{_sbindir}/rcloki
%dir %attr(-,loki,loki) %{loki_datadir}/
%dir %attr(-,loki,loki) %{loki_logdir}/

%files -n promtail
%{_unitdir}/promtail.service
%{_fillupdir}/sysconfig.promtail
%{_bindir}/promtail
%dir %{_sysconfdir}/loki
%config(noreplace) %{_sysconfdir}/loki/promtail.yaml
%{_sbindir}/rcpromtail
%dir %{promtail_datadir}/

%files -n logcli
%{_bindir}/logcli

%changelog
