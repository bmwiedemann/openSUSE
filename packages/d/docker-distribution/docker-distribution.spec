#
# spec file for package docker-distribution
#
# Copyright (c) 2020 SUSE LLC
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


%define goipath github.com/docker/distribution
%define registry_user registry
%define registry_group registry

Name:           docker-distribution
Version:        2.7.1
Release:        0
Summary:        The Docker toolset to pack, ship, store, and deliver content
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/docker/distribution
Source0:        distribution-%{version}.tar.xz
Source1:        registry-configuration.yml
Source2:        registry.service
Source4:        README-registry.SUSE
# PATCH-FIX-UPSTREAM https://github.com/docker/distribution/pull/2879
Patch0:         0001-Fix-s3-driver-for-supporting-ceph-radosgw.patch
# PATCH-FIX-UPSTREAM https://github.com/docker/distribution/pull/3204
Patch1:         0002-Relax-filesystem-driver-folder-permissions-to-0777-cont.patch
# PATCH-FIX-UPSTREAM https://github.com/docker/distribution/pull/2886
Patch2:         0003-Support-external-redis-sentinel-cluster.patch
BuildRequires:  go >= 1.13
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
ExclusiveArch:  x86_64 s390x aarch64 %arm ppc64le

%description
The Docker toolset to pack, ship, store, and deliver content.

The main product of this repository is the new registry implementation for
storing and distributing docker images. It supersedes the docker/docker- registry
project with a new API design, focused around security and performance.

The Distribution project has the further long term goal of providing a secure
tool chain for distributing content. The specifications, APIs and tools shoulds
be as useful with docker as they are without.

%package registry
Summary:        Registry server for Docker
Group:          System/Management
%{?systemd_ordering}

%description registry
Registry server for Docker (hosting/delivering of repositories and images).

%prep
%setup -q -n distribution-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %{SOURCE4} .

%build
%goprep %{goipath}
export CGO_ENABLED=0
%define buildtags "include_oss include_gcs"
%define ldflags "-s -w -X %{goipath}/version.Version=v%{version} -X %{goipath}/version.Package=%{goipath}"
%gobuild -ldflags %{ldflags} -tags %{buildtags} cmd/registry

%install
%goinstall
install -D -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/registry/config.yml
install -d  %{buildroot}%{_localstatedir}/lib/docker-registry

#
# systemd service for registry
#
install -Dd -m 0755  %{buildroot}%{_sbindir}
install -D  -m 0644  %{SOURCE2} %{buildroot}%{_unitdir}/registry.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcregistry

%pre registry
getent group %{registry_group} >/dev/null || groupadd -r %{registry_group}
getent passwd %{registry_user} >/dev/null || useradd -r -g %{registry_group} \
  -d %{_localstatedir}/lib/registry \
  -s /sbin/nologin \
  -c "user for docker-registry" \
  %{registry_user}
%service_add_pre registry.service

%post registry
%service_add_post registry.service

%preun registry
%service_del_preun registry.service

%postun registry
%service_del_postun registry.service

%files registry
%defattr(-,root,root)
%{_bindir}/registry
%{_sbindir}/rcregistry
%{_unitdir}/registry.service
%config %{_sysconfdir}/registry
%config(noreplace) %{_sysconfdir}/registry/config.yml
%doc README.md README-registry.SUSE
%license LICENSE
%attr(-,%{registry_user},%{registry_group}) %{_localstatedir}/lib/docker-registry

%changelog
