#
# spec file for package traefik2
#
# Copyright (c) 2025 SUSE LLC
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
Version:        2.11.18
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
Source4:        traefik-user.conf
BuildRequires:  go-bindata
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  (golang(API) >= 1.23)
Recommends:     podman
Provides:       traefik = %{version}
Provides:       group(traefik)
Provides:       user(traefik)
%sysusers_requires
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
%sysusers_generate_pre %{SOURCE4} %{name} traefik-user.conf
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
# system user
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/traefik-user.conf

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

%pre -f %{name}.pre
%service_add_pre traefik.service

%post
%service_add_post traefik.service
%{fillup_only -n traefik}
# fix ownership for config and logging directory
chown -R traefik: %{_sysconfdir}/traefik %{_localstatedir}/log/traefik

%preun
%service_del_preun traefik.service

%postun
%service_del_postun traefik.service

%files
%{_sysusersdir}/traefik-user.conf

%license LICENSE.md
%doc README.md SECURITY.md CONTRIBUTING.md
%{_bindir}/traefik

%{_unitdir}/traefik.service
%{_sbindir}/rctraefik

%defattr(0660, traefik, traefik, 0750)
%dir %{_sysconfdir}/traefik
%dir %{_sysconfdir}/traefik/conf.d

%config(noreplace) %{_sysconfdir}/traefik/traefik.toml
%dir %{_localstatedir}/log/traefik

%changelog
