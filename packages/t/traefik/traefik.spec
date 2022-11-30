#
# spec file for package traefik
#
# Copyright (c) 2022 SUSE LLC
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


%define project github.com/traefik/traefik

Name:           traefik
Version:        2.9.5
Release:        0
Summary:        The Cloud Native Application Proxy
License:        MIT
Group:          Productivity/Networking/Web/Proxy
URL:            https://traefik.io/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        traefik.service
Source3:        traefik.toml
Source4:        %{name}-%{version}.webui.tar.gz
BuildRequires:  go-bindata
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.19
Recommends:     podman
%{?systemd_requires}
%{go_provides}
# Make sure that the binary is not getting stripped.
%{go_nostrip}

%description
Traefik (pronounced traffic) is a modern HTTP reverse proxy and load balancer
that makes deploying microservices easy. Traefik integrates with your existing
infrastructure components (Docker, Swarm mode, Kubernetes, Marathon, Consul,
Etcd, Rancher, Amazon ECS) and configures itself automatically and dynamically.

Pointing Traefik at your orchestrator should be the only configuration step you need.

%prep
%setup -q

%build
build_date=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +"%%Y%%m%%d")
%{goprep} %{project}

# tarball causes "inconsistent vendoring"
tar -xf %{SOURCE1}

# unpack webui
tar -xf %{SOURCE4}

CGO_ENABLED=0

go generate

go build \
  -buildmode=pie \
  -mod=vendor \
  -ldflags "-s -w -X github.com/traefik/traefik/v2/pkg/version.Version=%{version} -X github.com/traefik/traefik/v2/pkg/version.Codename='' -X github.com/traefik/traefik/v2/pkg/version.BuildDate=${build_date}" \
  -o traefik ./cmd/traefik/

%install
install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# configuration
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/%{name}.toml

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -n %{name}}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE.md
%doc README.md SECURITY.md CONTRIBUTING.md
%{_bindir}/%{name}

%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.toml

%changelog
