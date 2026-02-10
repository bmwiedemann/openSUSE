#
# spec file for package distribution
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define goipath github.com/distribution/distribution/v3
Name:           distribution
Version:        3.0.0
Release:        0
Summary:        The toolset to pack, ship, store, and deliver content
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/distribution/distribution
Source0:        distribution-%{version}.tar.zst
Source1:        registry-configuration.yml
Source2:        registry.service
Source3:        %{name}-registry.tmpfiles
Source4:        README-registry.SUSE
Source10:       system-user-registry.conf
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.24
Provides:       docker-distribution = %{version}
Obsoletes:      docker-distribution < %{version}
ExclusiveArch:  %ix86 x86_64 %arm aarch64 ppc64 ppc64le s390x riscv64

%description
The toolset to pack, ship, store, and deliver content.

This repository's main product is the Open Source Registry implementation for
storing and distributing container images using the OCI Distribution
Specification. The goal of this project is to provide a simple, secure, and
scalable base for building a large scale registry solution or running a simple
private registry. It is a core library for many registry operators including
Docker Hub, GitHub Container Registry, GitLab Container Registry and
DigitalOcean Container Registry, as well as the CNCF Harbor Project, and VMware
Harbor Registry.  The Docker toolset to pack, ship, store, and deliver content.

%package registry
Summary:        Registry server following OCI Distribution Specification
Group:          System/Management
Provides:       docker-distribution-registry = %{version}
Obsoletes:      docker-distribution-registry < %{version}
# shell of the registry user we create on %%pre
Requires(pre):  /usr/sbin/nologin
%sysusers_requires
%{?systemd_ordering}

%description registry
Registry server for Docker (hosting/delivering of repositories and images).

%prep
%setup -q -n distribution-%{version}
cp %{SOURCE4} .

%build
%sysusers_generate_pre %{SOURCE10} registry system-user-registry.conf

%{goprep} %{goipath}
export CGO_ENABLED=1 GO111MODULE=auto
%define buildtags "include_oss include_gcs"
%define ldflags "-s -w -X %{goipath}/version.Version=v%{version} -X %{goipath}/version.Package=%{goipath}"

for cmd in registry digest registry-api-descriptor-template; do
    %{gobuild} -trimpath -ldflags %{ldflags} -tags %{buildtags} cmd/$cmd
done

%install
install -d -m755 %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/

%{goinstall}
install -D -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/registry/config.yml
install -d  %{buildroot}%{_localstatedir}/lib/docker-registry

#
# systemd service for registry
#
install -Dd -m 0755  %{buildroot}%{_sbindir}
install -D  -m 0644  %{SOURCE2} %{buildroot}%{_unitdir}/registry.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcregistry

#
# systemd tmpfiles for transactional-update
#
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}-registry.conf

%pre registry -f registry.pre
%service_add_pre registry.service

%post registry
%service_add_post registry.service
%tmpfiles_create %{name}-registry.conf

%preun registry
%service_del_preun registry.service

%postun registry
%service_del_postun registry.service

%files registry
%license LICENSE
%doc README.md README-registry.SUSE
%{_bindir}/digest
%{_bindir}/registry
%{_bindir}/registry-api-descriptor-template
%{_sbindir}/rcregistry
%{_unitdir}/registry.service
%{_sysusersdir}/system-user-registry.conf
%config %{_sysconfdir}/registry
%config(noreplace) %{_sysconfdir}/registry/config.yml
%ghost %attr(-,registry,registry) %{_localstatedir}/lib/docker-registry
%{_tmpfilesdir}/%{name}-registry.conf

%changelog
