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
Version:        1.0.3+git.1600360477.8b8f9ce
Release:        0
Summary:        Grafana Dashboards displaying metrics about a Pacemaker/Corosync High Availability Cluster.
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/ClusterLabs/ha_cluster_exporter
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires(pre):  shadow
Recommends:     grafana

# TECHNICAL NOTE:
# Originally we used to require grafana but, for product management reasons, we use recommends now.
# This impacts how we do pkging here: requiring shadow, creating grafana usr/group
# and modifiying files attributes (this was done automagically when requiring grafana).

%description
Grafana Dashboards displaying metrics about a Pacemaker/Corosync High Availability Cluster.

%prep
%setup -q

%pre
echo "Creating grafana user and group if not present"
getent group grafana > /dev/null || groupadd -r grafana
getent passwd grafana > /dev/null || useradd -r -g grafana -d  %{_datadir}/grafana -s /sbin/nologin grafana

%build

%install
install -d -m0755 %{buildroot}%{_localstatedir}/lib/grafana/dashboards/sleha
install -m644 dashboards/*.json %{buildroot}%{_localstatedir}/lib/grafana/dashboards/sleha
install -Dm644 dashboards/provider-sleha.yaml %{buildroot}%{_sysconfdir}/grafana/provisioning/dashboards/provider-sleha.yaml

%files
%defattr(-,root,root)
%doc dashboards/README.md
%license LICENSE
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/dashboards
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/dashboards/sleha
%attr(0644,grafana,grafana) %config %{_localstatedir}/lib/grafana/dashboards/sleha/*
%attr(0755,root,root) %dir %{_sysconfdir}/grafana
%attr(0755,root,root) %dir %{_sysconfdir}/grafana/provisioning
%attr(0755,root,root) %dir %{_sysconfdir}/grafana/provisioning/dashboards
%attr(0644,root,root) %config %{_sysconfdir}/grafana/provisioning/dashboards/provider-sleha.yaml

%changelog
