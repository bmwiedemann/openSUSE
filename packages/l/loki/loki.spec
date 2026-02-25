#
# spec file for package loki
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%global loki_services     loki.target     loki.service     loki@.service
%global promtail_services promtail.target promtail.service promtail@.service

%global loki_public_binaries   logcli logql-analyzer loki loki-canary lokitool
%global promtail_binaries promtail

Name:           loki
Version:        3.6.7
Release:        0
Summary:        Loki: like Prometheus, but for logs
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://grafana.com/loki
Source:         %{name}-%{version}.tar.xz
Source1:        loki.service
Source2:        promtail.service
Source3:        sysconfig.loki
Source4:        sysconfig.promtail
Source5:        loki@.service
Source6:        promtail@.service
Source7:        loki.target
Source8:        promtail.target
Source99:       series
Patch0:         proper-data-directories.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang-packaging
BuildRequires:  systemd-devel
BuildRequires:  golang(API) = 1.24
Requires:       logcli = %{version}
Requires(pre):  group(loki)
Requires(pre):  user(loki)
Requires:       group(loki)
Requires:       user(loki)
Requires(post): %fillup_prereq
%systemd_ordering

%description
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation
system inspired by Prometheus.

This package contains the Loki server.

%package -n promtail
Summary:        Promtail Client
Group:          System/Monitoring

%description -n promtail
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation
system inspired by Prometheus.

This package contains the Promtail client.

%package -n logcli
Summary:        LogCLI tool
Group:          System/Monitoring

%description -n logcli
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation
system inspired by Prometheus.

This package contains the LogCLI command-line tool.

%package -n lokitool
Summary:        A command-line tool to manage Loki
Group:          System/Monitoring

%description -n lokitool
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation
system inspired by Prometheus.

This package contains the lokitool command-line tool.

%prep
%autosetup -p1 %{name}-%{version}

%build
%define buildpkg github.com/grafana/loki/v3/pkg/util/build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

%ifarch %{ix86} s390 s390x %{arm} riscv64
    export CGO_ENABLED=1
%else
    export CGO_ENABLED=0
%endif

export GOFLAGS="-mod=vendor -buildmode=pie -tags=netgo"
export GOLDFLAGS="-X %{buildpkg}.Version=%{version} \
                  -X %{buildpkg}.Revision=v%{version} \
                  -X %{buildpkg}.Branch=main \
                  -X %{buildpkg}.BuildUser=openSUSE \
                  -X %{buildpkg}.BuildDate=${BUILD_DATE}"

for i in %{loki_public_binaries} %{?loki_internal_binaries}  ; do
  go build -ldflags="$GOLDFLAGS" ./cmd/${i}
done
CGO_ENABLED=1 go build -ldflags="$GOLDFLAGS" --tags=promtail_journal_enabled,netgo ./clients/cmd/promtail

#check
./lokitool version
for i in %{loki_public_binaries} %{?loki_internal_binaries} %{promtail_binaries} ; do
  if [ "x${i}" != "xlokitool" -a "x${i}" != "xlogql-analyzer" ] ; then
./${i} --version
  fi
done

%install

# Service files for Loki and promtail
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/loki.service
install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/promtail.service
install -Dm644 %{SOURCE5} %{buildroot}%{_unitdir}/loki@.service
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}/promtail@.service
install -Dm644 %{SOURCE7} %{buildroot}%{_unitdir}/loki.target
install -Dm644 %{SOURCE8} %{buildroot}%{_unitdir}/promtail.target

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
install -D -m 0755 -t %{buildroot}%{_bindir} %{loki_public_binaries} %{?loki_internal_binaries} %{promtail_binaries}

install -D -m 0750 -d %{buildroot}%{promtail_datadir} %{buildroot}%{loki_datadir} %{buildroot}%{loki_logdir}

%pre
%service_add_pre %{loki_services}

%post
%fillup_only -n loki
%service_add_post %{loki_services}

%preun
%service_del_preun %{loki_services}

%postun
%service_del_postun %{loki_services} %{promtail_services}

%pre -n promtail
%service_add_pre %{promtail_services}

%post -n promtail
%fillup_only -n promtail
%service_add_post %{promtail_services}

%preun -n promtail
%service_del_preun %{promtail_services}

%postun -n promtail
%service_del_postun %{promtail_services}

%files
%license LICENSE
%doc README.md
%{_unitdir}/loki.target
%{_unitdir}/loki.service
%{_unitdir}/loki@.service
%{_fillupdir}/sysconfig.loki
%{_bindir}/loki
%{_bindir}/loki-canary
%{_bindir}/logql-analyzer
%dir %{_sysconfdir}/loki
%config(noreplace) %attr(-,root,loki) %{_sysconfdir}/loki/loki.yaml
%{_sbindir}/rcloki
%dir %attr(-,loki,loki) %{loki_datadir}/
%dir %attr(-,loki,loki) %{loki_logdir}/

%files -n promtail
%{_unitdir}/promtail.target
%{_unitdir}/promtail.service
%{_unitdir}/promtail@.service
%{_fillupdir}/sysconfig.promtail
%{_bindir}/promtail
%dir %{_sysconfdir}/loki
%config(noreplace) %{_sysconfdir}/loki/promtail.yaml
%{_sbindir}/rcpromtail
%dir %{promtail_datadir}/

%files -n logcli
%license LICENSE
%{_bindir}/logcli

%files -n lokitool
%license LICENSE
%{_bindir}/lokitool

%changelog
