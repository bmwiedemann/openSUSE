#
# spec file for package docker-distribution
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           docker-distribution
Version:        2.6.2
Release:        0
Summary:        The Docker toolset to pack, ship, store, and deliver content
License:        Apache-2.0
Group:          System/Management
Url:            http://www.docker.io
Source0:        distribution-%{version}.tar.xz
Source1:        registry-configuration.yml
Source2:        registry.service
Source3:        registry.SuSEfirewall2
Source4:        README-registry.SUSE
BuildRequires:  go >= 1.7.0
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
Requires(pre):  %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 s390x
%{?systemd_requires}

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

%description registry
Registry server for Docker (hosting/delivering of repositories and images).

%prep
%setup -q -n distribution-%{version}
cp %{SOURCE4} .

%build
export GOPATH=$PWD/go
mkdir -p $GOPATH/src/github.com/docker

# Copy the vendor directory into the GOPATH.
cp -r $PWD/vendor/* $GOPATH/src
ln -s $PWD $GOPATH/src/github.com/docker/distribution

make %{?_smp_mflags} binaries

%install
install -D -m755 bin/registry %{buildroot}/%{_bindir}/registry
install -D -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/registry/config.yml
install -d  %{buildroot}%{_localstatedir}/lib/docker-registry

#
# systemd service for registry
#
install -Dd -m 0755  %{buildroot}%{_sbindir}
install -D  -m 0644  %{SOURCE2} %{buildroot}%{_unitdir}/registry.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcregistry

#
# install SuSEfirewall2 rules
#
install -Dpm 0644  %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/registry

%pre registry
%service_add_pre registry.service

%post registry
%service_add_post registry.service
%{fillup_only -n registry}

%preun registry
%service_del_preun registry.service

%postun registry
%service_del_postun registry.service

%files registry
%defattr(-,root,root)
%{_bindir}/registry
%{_sbindir}/rcregistry
%{_unitdir}/registry.service
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/registry
%config %{_sysconfdir}/registry
%config(noreplace) %{_sysconfdir}/registry/config.yml
%doc README.md README-registry.SUSE
%license LICENSE
%{_localstatedir}/lib/docker-registry

%changelog
