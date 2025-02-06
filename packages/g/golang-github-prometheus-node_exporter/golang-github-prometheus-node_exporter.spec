#
# spec file for package golang-github-prometheus-node_exporter
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           golang-github-prometheus-node_exporter
Version:        1.8.2
Release:        0
Summary:        Prometheus exporter for machine metrics
License:        Apache-2.0
Group:          System/Management
URL:            https://prometheus.io/
Source:         node_exporter-%{version}.tar.gz
# Generated after applying fix_arp_collector.patch
Source1:        vendor.tar.gz
Source2:        prometheus-node_exporter.service
Source4:        prometheus-node_exporter.sysconfig
BuildRequires:  fdupes
BuildRequires:  golang-github-prometheus-promu >= 0.12.0
BuildRequires:  golang(API) >= 1.22
%{?systemd_ordering}
Requires(post): %fillup_prereq
Requires(pre):  user(prometheus)
Requires(pre):  group(prometheus)
Provides:       node_exporter
Provides:       prometheus(node_exporter)
ExcludeArch:    s390
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%description
Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors.

%prep
%autosetup -a1 -p1 -n node_exporter-%{version}

%build
%ifarch i586 s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl
export BUILD_CGO_FLAG="--cgo"
%endif
export GOFLAGS="-buildmode=pie"
promu build -v $BUILD_CGO_FLAG

%install
install -D -m 0755 %{_builddir}/node_exporter-%{version}/node_exporter %{buildroot}/%{_bindir}/node_exporter
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/prometheus-node_exporter.service
install -D -m 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.prometheus-node_exporter
%fdupes %{buildroot}

%check
go test -x .
./node_exporter --version

%pre
%service_add_pre prometheus-node_exporter.service

%post
%service_add_post prometheus-node_exporter.service
%fillup_only -n prometheus-node_exporter

%preun
%service_del_preun prometheus-node_exporter.service

%postun
%service_del_postun prometheus-node_exporter.service

%files
%doc README.md
%license LICENSE
%{_bindir}/node_exporter
%{_unitdir}/prometheus-node_exporter.service
%{_fillupdir}/sysconfig.prometheus-node_exporter

%changelog
