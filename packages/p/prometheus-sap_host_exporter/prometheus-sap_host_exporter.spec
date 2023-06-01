#
# spec file for package prometheus-sap_host_exporter
#
# Copyright (c) 2023 SUSE LLC
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


Name:           prometheus-sap_host_exporter
# Version will be processed via set_version source service
Version:        0.6.0+git.1685628435.48c4099
Release:        0
License:        Apache-2.0
Summary:        Prometheus exporter for SAP hosts
Group:          System/Monitoring
URL:            https://github.com/SUSE/sap_host_exporter
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
ExclusiveArch:  aarch64 x86_64 ppc64le s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang(API) >= 1.20
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

export CGO_ENABLED=0
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

%changelog
