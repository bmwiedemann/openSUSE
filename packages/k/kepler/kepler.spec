#
# spec file for package kepler
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


Name:           kepler
Version:        0.7.11
Release:        0
Summary:        Kubernetes-based Efficient Power Level Exporter
License:        Apache-2.0 AND (BSD-2-Clause OR GPL-2.0-only) AND GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/sustainable-computing-io/kepler/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch1:         0001-use-local-bpf2go.patch
Patch2:         0002-change-data-path.patch
Patch3:         0003-Bump-x-net.patch

BuildRequires:  bpf2go
BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  zlib-devel
BuildRequires:  golang(API) >= 1.21
Recommends:     cpuid
%{?systemd_ordering}

%description
Kubernetes-based Efficient Power Level Exporter

%prep
%autosetup -a1 -p1 -n kepler-%{version}

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go generate ./pkg/bpf
go build -o %{name} ./cmd/exporter/exporter.go
echo -n "true" > ./ENABLE_PROCESS_METRICS

%install
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/data
install -d %{buildroot}%{_sysconfdir}/%{name}/%{name}.config

install -D -m755 ./%{name}  %{buildroot}%{_bindir}/%{name}
install -D -m644 ./packaging/rpm/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m644 ./ENABLE_PROCESS_METRICS %{buildroot}%{_sysconfdir}/%{name}/%{name}.config/ENABLE_PROCESS_METRICS
install -D -m644 ./data/cpus.yaml %{buildroot}%{_datadir}/%{name}/data/cpus.yaml
install -D -m644 ./data/model_weight/acpi_AbsPowerModel.json %{buildroot}%{_datadir}/%{name}/data/model_weight/acpi_AbsPowerModel.json
install -D -m644 ./data/model_weight/acpi_DynPowerModel.json %{buildroot}%{_datadir}/%{name}/data/model_weight/acpi_DynPowerModel.json
install -D -m644 ./data/model_weight/intel_rapl_AbsPowerModel.json %{buildroot}%{_datadir}/%{name}/data/model_weight/intel_rapl_AbsPowerModel.json
install -D -m644 ./data/model_weight/intel_rapl_DynPowerModel.json %{buildroot}%{_datadir}/%{name}/data/model_weight/intel_rapl_DynPowerModel.json

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE-APACHE
%license LICENSE-BSD2
%license LICENSE-GPL2
%dir /%{_sysconfdir}/%{name}
%dir /%{_sysconfdir}/%{name}/%{name}.config
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%dir %{_datadir}/%{name}/data/model_weight
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config /%{_sysconfdir}/%{name}/%{name}.config/ENABLE_PROCESS_METRICS
%{_datadir}/kepler/data/cpus.yaml
%{_datadir}/kepler/data/model_weight/acpi_AbsPowerModel.json
%{_datadir}/kepler/data/model_weight/acpi_DynPowerModel.json
%{_datadir}/kepler/data/model_weight/intel_rapl_AbsPowerModel.json
%{_datadir}/kepler/data/model_weight/intel_rapl_DynPowerModel.json

%changelog
