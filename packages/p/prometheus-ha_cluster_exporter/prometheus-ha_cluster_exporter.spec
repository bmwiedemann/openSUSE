#
# spec file for package prometheus-ha_cluster_exporter
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


Name:           prometheus-ha_cluster_exporter
# Version will be processed via set_version source service
Version:        1.3.1+git.1676027782.ad3c0e9
Release:        0
Summary:        Prometheus exporter for Pacemaker HA clusters metrics
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://github.com/ClusterLabs/ha_cluster_exporter
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.14
Requires(post): %fillup_prereq
Provides:       ha_cluster_exporter = %{version}-%{release}
Provides:       prometheus(ha_cluster_exporter) = %{version}-%{release}
ExclusiveArch:  aarch64 x86_64 ppc64le s390x
%{go_nostrip}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%description
Prometheus exporter for Pacemaker HA clusters metrics

%prep
%setup -q            # unpack project sources
%setup -q -T -D -a 1 # unpack go dependencies in vendor.tar.gz, which was prepared by the source services

%define shortname ha_cluster_exporter

%build

export CGO_ENABLED=0
go build -mod=vendor \
         -buildmode=pie \
         -ldflags="-s -w -X github.com/prometheus/common/version.Version=%{version}" \
         -o %{shortname}

%install

# Install the binary.
install -D -m 0755 %{shortname} "%{buildroot}%{_bindir}/%{shortname}"

# Install the systemd unit
install -D -m 0644 %{shortname}.service %{buildroot}%{_unitdir}/%{name}.service

# Install the environment file
install -D -m 0644 %{shortname}.sysconfig %{buildroot}%{_fillupdir}/sysconfig.%{name}

# Install compat wrapper for legacy init systems
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only -n %{name}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc *.md
%doc doc/*
%if 0%{?suse_version} >= 1500
%license LICENSE
%else
%doc LICENSE
%endif
%{_bindir}/%{shortname}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}
%{_sbindir}/rc%{name}

%changelog
