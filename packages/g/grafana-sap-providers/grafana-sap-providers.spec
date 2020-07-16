#
# Copyright 2020 SUSE LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
Name:           grafana-sap-providers
Version:        1.0
Release:        0
License:        Apache-2.0
Summary:        Grafana configuration providers for SAP applications
Group:          System/Monitoring
Source0:        provider-sles4sap.yaml
Source1:        LICENSE
BuildArch:      noarch
Requires:       grafana
BuildRequires:  grafana

%description
Automated configuration provisioners leveraged by other packages to enable a zero-config installation of Grafana dashboards.

%prep
cp %{SOURCE1} %{_builddir}

%build

%install
%define dasboards_dir %{_localstatedir}/lib/grafana/dashboards
%define provisioning_dir %{_sysconfdir}/grafana/provisioning/dashboards
install -d -m0755 %{buildroot}%{dasboards_dir}/sles4sap
install -Dm644 %{SOURCE0} %{buildroot}%{provisioning_dir}/provider-sles4sap.yaml

%files
%defattr(-,root,root)
%license LICENSE
%attr(0755,grafana,grafana) %dir %{dasboards_dir}/sles4sap
%attr(0644,root,root) %config %{provisioning_dir}/provider-sles4sap.yaml

%changelog
