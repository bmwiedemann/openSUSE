#
# spec file for package traefik
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
Name:           traefik
Version:        3.0.4
Release:        0
Summary:        The Cloud Native Application Proxy
License:        MIT
Group:          Productivity/Networking/Web/Proxy
URL:            https://traefik.io/
# set the desired version in the spec-file
# download the source files and create the vendor tarball with "osc service mr"
Source0:        https://github.com/traefik/traefik/releases/download/v%{version}/%{name}-v%{version}.src.tar.gz
Source1:        vendor.tar.gz
Source2:        traefik.service
Source3:        traefik.yml
BuildRequires:  go-bindata
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  (golang(API) >= 1.22)
Recommends:     podman
Conflicts:      traefik2
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
%autopatch -p1

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
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# configuration
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/%{name}.yml
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d

# logging
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

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
%dir %{_sysconfdir}/%{name}/conf.d

%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yml
%attr(750,root,root) %dir %{_localstatedir}/log/%{name}

%changelog
