#
# spec file for package grafana-ha-cluster-dashboards
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


Name:           grafana-ha-cluster-dashboards
# Version will be processed via set_version source service
Version:        1.0.2+git.1596627252.62154d3
Release:        0
Summary:        Grafana Dashboards displaying metrics about a Pacemaker/Corosync High Availability Cluster.
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/ClusterLabs/ha_cluster_exporter
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       grafana
BuildRequires:  grafana

%description
Grafana Dashboards displaying metrics about a Pacemaker/Corosync High Availability Cluster.

%prep
%setup -q

%build

%install
%define dasboards_dir %{_localstatedir}/lib/grafana/dashboards
%define provisioning_dir %{_sysconfdir}/grafana/provisioning/dashboards
install -d -m0755 %{buildroot}%{dasboards_dir}/sleha
install -m644 dashboards/*.json %{buildroot}%{dasboards_dir}/sleha
install -Dm644 dashboards/provider-sleha.yaml %{buildroot}%{provisioning_dir}/provider-sleha.yaml

%files
%defattr(-,root,root)
%doc dashboards/README.md
%license LICENSE
%attr(0755,grafana,grafana) %dir %{dasboards_dir}/sleha
%attr(0644,grafana,grafana) %config %{dasboards_dir}/sleha/*
%attr(0644,root,root) %config %{provisioning_dir}/provider-sleha.yaml

%changelog
