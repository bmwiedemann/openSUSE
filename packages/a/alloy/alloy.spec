#
# spec file for package alloy
#
# Copyright (c) 2025 SUSE LLC
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


Name:           alloy
Version:        1.6.1
Release:        0
Summary:        OpenTelemetry Collector distribution with programmable pipelines
License:        Apache-2.0
URL:            https://github.com/grafana/alloy
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        ui-%{version}.tar.gz
Source3:        PACKAGING_README.md
Source4:        Makefile
BuildRequires:  go >= 1.23.5
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  user(alloy)
# Require the system user and group
Requires(pre):  user(alloy)
Requires(pre):  group(alloy)
# for the sysconfig file
Requires(post): %fillup_prereq

# /usr/lib/go/1.23/pkg/tool/linux_386/link: mapping output file failed: cannot allocate memory
ExcludeArch:    %{ix86}

%description
Grafana Alloy is an open source OpenTelemetry Collector distribution with
built-in Prometheus pipelines and support for metrics, logs, traces, and
profiles.

What can Alloy do?
* Programmable pipelines: Use a rich expression-based syntax for configuring
  powerful observability pipelines.
* OpenTelemetry Collector Distribution: Alloy is a distribution of
  OpenTelemetry Collector and supports dozens of its components, alongside new
  components that make use of Alloy's programmable pipelines.
* Big tent: Alloy embraces Grafana's "big tent" philosophy, where Alloy can be
  used with other vendors or open source databases. It has components to
  perfectly integrate with multiple telemetry ecosystems:
  - OpenTelemetry Collector
  - Prometheus
  - Grafana Loki
  - Grafana Pyroscope
* Kubernetes-native: Use components to interact with native and custom
  Kubernetes resources; no need to learn how to use a separate Kubernetes
  operator.
* Shareable pipelines: Use modules to share your pipelines with the world.
* Automatic workload distribution: Configure Alloy instances to form a cluster
  for automatic workload distribution.
* Centralized configuration support: Alloy supports retrieving its
  configuration from a server for centralized configuration management.
* Debugging utilities: Use the built-in UI for visualizing and debugging
  pipelines.

%prep
%autosetup -p 1 -a 1
pwd
cd internal/web/
tar xzf %{SOURCE2}
cd ../../

%build
# hash will be shortended by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/alloy.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/grafana/alloy/internal/build.Revision=${COMMIT_HASH:0:8} \
   -X github.com/grafana/alloy/internal/build.Branch=HEAD \
   -X github.com/grafana/alloy/internal/build.Version=v%{version} \
   -X github.com/grafana/alloy/internal/build.BuildUser=geeko@obs \
   -X github.com/grafana/alloy/internal/build.BuildDate=${BUILD_DATE}" \
   -tags "builtinassets promtail_journal_enabled" \
   -o bin/%{name} .

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# systemd unit
install -D -m 0644 packaging/rpm/%{name}.service %{buildroot}/%{_unitdir}/%{name}.service

# configuration directory
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}

# sysconfig file
install -D -m 0644 packaging/environment-file %{buildroot}%{_fillupdir}/sysconfig.alloy

# working directory
install -d -m 0770 %{buildroot}/%{_sharedstatedir}/%{name}
install -d -m 0770 %{buildroot}/%{_sharedstatedir}/%{name}/data/

%pre
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md packaging/config.alloy
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %attr(770,root,alloy) %config %{_sysconfdir}/%{name}
%dir %attr(770,alloy,alloy) %{_sharedstatedir}/%{name}
%{_fillupdir}/sysconfig.alloy

%changelog
