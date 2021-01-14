#
# spec file for package prometheus-saptune_exporter
#
# Copyright (c) 2021 SUSE LLC
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


Name:           prometheus-saptune_exporter
# Version will be processed via set_version source service
Version:        0.2
Release:        0
Summary:        Prometheus exporter for saptune metrics
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/SUSE/saptune_exporter
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
ExclusiveArch:  aarch64 x86_64 ppc64le s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
Provides:       saptune_exporter = %{version}-%{release}
Provides:       prometheus(saptune_exporter) = %{version}-%{release}

%{go_nostrip}

%description
Prometheus exporter for Saptune metrics

%prep
%setup -q            # unpack project sources
%setup -q -T -D -a 1 # unpack go dependencies in vendor.tar.gz, which was prepared by the source services

%define shortname saptune_exporter

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
install -D -m 0644 %{shortname}.service %{buildroot}%{_unitdir}/%{name}.service

# Install compat wrapper for legacy init systems
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc *.md
%doc doc/*
%license LICENSE
%{_bindir}/%{shortname}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%changelog
