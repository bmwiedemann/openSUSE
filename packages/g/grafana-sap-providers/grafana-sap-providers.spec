#
# spec file for package grafana-sap-providers
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


Name:           grafana-sap-providers
Version:        1.1
Release:        0
Summary:        Grafana configuration providers for SAP applications
License:        Apache-2.0
Group:          System/Monitoring
Source0:        provider-sles4sap.yaml
Source1:        LICENSE
BuildArch:      noarch
Recommends:     grafana
Requires(pre):  shadow

# TECHNICAL NOTE:
# Originally we used to require grafana but, for product management reasons, we use recommends now
# this impacts how we do pkging here: requiring shadow, creating grafana usr/group
# and modifiying files attributes (this was done automagically when requiring grafana).

%description
Automated configuration provisioners leveraged by other packages to enable a zero-config installation of Grafana dashboards.

%prep
cp %{SOURCE1} %{_builddir}

%pre
echo "Creating grafana user and group if not present"
getent group grafana > /dev/null || groupadd -r grafana
getent passwd grafana > /dev/null || useradd -r -g grafana -d  %{_datadir}/grafana -s /sbin/nologin grafana

%build

%install
install -d -m0755 %{buildroot}%{_localstatedir}/lib/grafana/dashboards/sles4sap
install -Dm644 %{SOURCE0} %{buildroot}%{_sysconfdir}/grafana/provisioning/dashboards/provider-sles4sap.yaml

%files
%defattr(-,root,root)
%license LICENSE
%attr(0755,root,root) %dir %{_sysconfdir}/grafana
%attr(0755,root,root) %dir %{_sysconfdir}/grafana/provisioning
%attr(0755,root,root) %dir %{_sysconfdir}/grafana/provisioning/dashboards
%attr(0644,root,root) %config %{_sysconfdir}/grafana/provisioning/dashboards/provider-sles4sap.yaml
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/dashboards
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/dashboards/sles4sap

%changelog
