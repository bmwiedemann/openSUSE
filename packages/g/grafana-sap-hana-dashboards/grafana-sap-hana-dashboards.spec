#
# spec file for package grafana-sap-hana-dashboards
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


Name:           grafana-sap-hana-dashboards
# Version will be processed via set_version source service
Version:        1.0.1+git.1596627316.015380b
Release:        0
Summary:        Grafana Dashboards displaying metrics about SAP HANA databases.
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/SUSE/hanadb_exporter
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       grafana-sap-providers
BuildRequires:  grafana-sap-providers

%description
Grafana Dashboards displaying metrics about SAP HANA databases.

%prep
%setup -q

%build

%install
%define dasboards_dir %{_localstatedir}/lib/grafana/dashboards
install -d -m0755 %{buildroot}%{dasboards_dir}/sles4sap
install -m644 dashboards/*.json %{buildroot}%{dasboards_dir}/sles4sap

%files
%defattr(-,root,root)
%doc dashboards/README.md
%license LICENSE
%attr(0755,grafana,grafana) %dir %{dasboards_dir}/sles4sap
%attr(0644,grafana,grafana) %config %{dasboards_dir}/sles4sap/*

%changelog
