#
# Copyright 2020-2024 SUSE LLC
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
Name:           prometheus-sap_host_exporter
# Version will be processed via set_version source service
Version:        0.7.0
Release:        0
License:        Apache-2.0
Summary:        Prometheus exporter for SAP hosts
Group:          System/Monitoring
Url:            https://github.com/SUSE/sap_host_exporter
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
ExclusiveArch:  aarch64 x86_64 ppc64le s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang(API) >= 1.23
Provides:       sap_host_exporter = %{version}-%{release}
Provides:       prometheus(sap_host_exporter) = %{version}-%{release}

%description
A Prometheus metrics exporter that connects to the SAPControl web interface
to collect data about SAP systems like NetWeaver and S4/HANA.

%prep
%setup -q            # unpack project sources
%setup -q -T -D -a 1 # unpack go dependencies in vendor.tar.gz, which was prepared by the source services

%define shortname sap_host_exporter

%build
%ifarch s390x
  export CGO_ENABLED=1
%else
  export CGO_ENABLED=0
%endif
go build -mod=vendor \
         -buildmode=pie \
         -ldflags="-s -w -X main.version=%{version}" \
         -o %{shortname}

%install

# Install the binary.
install -D -m 0755 %{shortname} "%{buildroot}%{_bindir}/%{shortname}"

# Install the systemd unit
install -D -m 0644 %{shortname}@.service %{buildroot}%{_unitdir}/%{name}@.service

# Install the default config
install -D -m 0600 doc/%{shortname}.yaml "%{buildroot}/etc/%{shortname}/default.yaml"

# Install compat wrapper for legacy init systems
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

# Install supportconfig plugin
install -D -m 755 supportconfig-sap_host_exporter %{buildroot}%{_prefix}/lib/supportconfig/plugins/%{shortname}


%pre
%service_add_pre %{name}@.service

%post
%service_add_post %{name}@.service

%preun
%service_del_preun %{name}@.service

%postun
%service_del_postun %{name}@.service

%files
%defattr(-,root,root)
%doc *.md
%doc doc/*.md
%if 0%{?suse_version} >= 1500
%license LICENSE
%else
%doc LICENSE
%endif
%{_bindir}/%{shortname}
%{_unitdir}/%{name}@.service
%{_sbindir}/rc%{name}
%dir /etc/%{shortname}/
%config /etc/%{shortname}/default.yaml
%dir %{_prefix}/lib/supportconfig
%dir %{_prefix}/lib/supportconfig/plugins
%{_prefix}/lib/supportconfig/plugins/%{shortname}

%changelog
