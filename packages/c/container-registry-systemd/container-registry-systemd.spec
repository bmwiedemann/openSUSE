#
# spec file for package container-registry-systemd
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


Name:           container-registry-systemd
Version:        0.0+git20200526.1d9ce7b
Release:        0
Summary:        Systemd service files and config files for container-registry
License:        GPL-3.0-or-later
URL:            https://github.com/kubic-project/container-registry-systemd
Source:         container-registry-systemd-%{version}.tar.xz
Requires:       certstrap
Requires(post): %fillup_prereq
BuildArch:      noarch

%description
This package contains the configuration files, systemd units and scripts
to run the openSUSE container registry managed by systemd.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/registry
mkdir -p %{buildroot}%{_distconfdir}/registry
mkdir -p %{buildroot}%{_localstatedir}/lib/container-registry
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}/srv/registry
install -m 644 config.yml* %{buildroot}%{_distconfdir}/registry/
install -m 644 auth_config.yml %{buildroot}%{_distconfdir}/registry
install -m 644 sysconfig.container-registry %{buildroot}%{_fillupdir}/
install -m 755 create-container-registry-certs.sh %{buildroot}%{_sbindir}/create-container-registry-certs
install -m 755 setup-container-registry.sh %{buildroot}%{_sbindir}/setup-container-registry
install -m 644 container-registry.service %{buildroot}%{_unitdir}/
install -m 644 registry-auth_server.service %{buildroot}%{_unitdir}/
# create symlink for rccontainer-registry
ln -s /sbin/service %{buildroot}%{_sbindir}/rccontainer-registry
ln -s /sbin/service %{buildroot}%{_sbindir}/rcregistry-auth_server

%pre
%service_add_pre container-registry.service registry-auth_server.service

%post
%{fillup_only -n container-registry}
%service_add_post container-registry.service registry-auth_server.service

%preun
%service_del_preun container-registry.service registry-auth_server.service

%postun
%service_del_postun container-registry.service registry-auth_server.service

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/registry
%dir %{_distconfdir}/registry
%{_distconfdir}/registry/auth_config.yml
%{_distconfdir}/registry/config.yml
%{_distconfdir}/registry/config.yml.*
%{_unitdir}/container-registry.service
%{_unitdir}/registry-auth_server.service
%{_fillupdir}/sysconfig.container-registry
%{_sbindir}/create-container-registry-certs
%{_sbindir}/setup-container-registry
%{_sbindir}/rccontainer-registry
%{_sbindir}/rcregistry-auth_server
%dir /srv/registry
%dir %{_localstatedir}/lib/container-registry

%changelog
