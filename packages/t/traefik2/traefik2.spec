#
# spec file for package traefik2
#
# Copyright (c) 2024 SUSE LLC
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
%ifarch ppc64 s390x
%define buildmode default
%else
%define buildmode pie
%endif
Name:           traefik2
Version:        2.11.6
Release:        0
Summary:        The Cloud Native Application Proxy
License:        MIT
Group:          Productivity/Networking/Web/Proxy
URL:            https://traefik.io/
# set the desired version in the spec-file
# download the source files and create the vendor tarball with "osc service mr"
Source0:        https://github.com/traefik/traefik/releases/download/v%{version}/traefik-v%{version}.src.tar.gz
Source1:        vendor.tar.gz
Source2:        traefik.service
Source3:        traefik.toml
Provides:       traefik = %{version}
BuildRequires:  go-bindata
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  (golang(API) >= 1.22)
Recommends:     podman
%{?systemd_requires}
%{go_provides}

%description
Traefik (pronounced traffic) is a modern HTTP reverse proxy and load balancer
that makes deploying microservices easy. Traefik integrates with your existing
infrastructure components (Docker, Swarm mode, Kubernetes, Marathon, Consul,
Etcd, Rancher, Amazon ECS) and configures itself automatically and dynamically.

Pointing Traefik at your orchestrator should be the only configuration step you need.

%prep
%setup -q -c %{name}-%{version} -b0 -a1

%build
%{goprep} %{project}

# see script/generate
go generate

build_date=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +"%%Y%%m%%d")
# see script/binary
CGO_ENABLED=1 GOGC=off go build \
  -buildmode=%{buildmode} \
  -mod=vendor \
  -ldflags "-X github.com/traefik/traefik/v2/pkg/version.Version=%{version} \
            -X github.com/traefik/traefik/v2/pkg/version.Codename='' \
            -X github.com/traefik/traefik/v2/pkg/version.BuildDate=${build_date}" \
  -installsuffix nocgo \
  -o traefik \
  ./cmd/traefik

%install
install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 traefik %{buildroot}%{_bindir}/traefik

# service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/traefik.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rctraefik

# configuration
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/traefik/traefik.toml
mkdir -p %{buildroot}%{_sysconfdir}/traefik/conf.d

# logging
mkdir -p %{buildroot}%{_localstatedir}/log/traefik

%pre
%service_add_pre traefik.service

%post
%service_add_post traefik.service
%{fillup_only -n traefik}

%preun
%service_del_preun traefik.service

%postun
%service_del_postun traefik.service

%files
%license LICENSE.md
%doc README.md SECURITY.md CONTRIBUTING.md
%{_bindir}/traefik

%{_unitdir}/traefik.service
%{_sbindir}/rctraefik

%dir %{_sysconfdir}/traefik
%dir %{_sysconfdir}/traefik/conf.d

%config(noreplace) %{_sysconfdir}/traefik/traefik.toml
%attr(750,root,root) %dir %{_localstatedir}/log/traefik

%changelog
