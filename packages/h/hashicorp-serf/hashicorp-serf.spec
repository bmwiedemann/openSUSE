#
# spec file for package hashicorp-serf
#
# Copyright (c) 2025 SUSE LLC and contributors
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

# Make sure we work on Leap/SLE 15.x
%{!?_distconfdir: %global _distconfdir %{_sysconfdir}}

Name:           hashicorp-serf
URL:            https://github.com/hashicorp/serf
Summary:        Service orchestration and management tool
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0
Version:        0.10.2
Release:        0
Group:          System/Management
Source:         hashicorp-serf-%{version}.tar.xz
Source1:        vendor.tar.gz
Source2:        serf.service
Source3:        00-default.json
Source4:        system-user-serf.conf
Source5:        LICENSE
BuildRequires:  golang(API) >= 1.23
BuildRequires:  systemd-rpm-macros
Requires(pre):    sysuser-tools
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%sysusers_requires

# Upstream wants 64-bit (e.g., they store 1<<63-1 in integers, etc)
ExcludeArch:    %ix86 %arm

%description
Serf is a service orchestration and management tool.

It offers a decentralized, lightweight, highly available and fault
tolerant solution for service discovery and orchestration that runs
on Linux, Mac OS-X and Windows.

An efficient and lightweight gossip protocol is used to communicate
among the nodes, and node failures are detected and notified to the rest
of the cluster. An event system is built on top of Serf, so that events
such as deploys, configuration changes, et.c, can be propagated around.
Serf is also completely masterless, meaning there's no single point of
failure.

This package provides the agent that should be started on every node.

%prep
%autosetup -p1 -a 1

%build
for cmd in cmd/* ; do
  go build -mod=vendor -v -o bin/$(basename $cmd) ./$cmd
done
  
%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 bin/* %{buildroot}%{_bindir}/

install -d -m 0755 %{buildroot}%{_sysconfdir}/serf/config.d
install -d -m 0755 %{buildroot}%{_distconfdir}/serf/config.d
install -d -m 0755 %{buildroot}%{_sharedstatedir}/serf

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/serf.service
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/system-user-serf.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_distconfdir}/serf/config.d/00-default.json

# Manually copy the documentation in place as there are multiple
# files with the same name (README.md), and that wouldn't be handled
# properly if we do this via the doc macro in the file section
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -d -m 755 %{buildroot}%{_docdir}/%{name}/client
install -d -m 755 %{buildroot}%{_docdir}/%{name}/demo/vagrant-cluster
install -d -m 755 %{buildroot}%{_docdir}/%{name}/demo/web-load-balancer
install -d -m 755 %{buildroot}%{_docdir}/%{name}/ops-misc

install -m 644 README.md %{buildroot}%{_docdir}/%{name}/
install -m 644 CHANGELOG.md %{buildroot}%{_docdir}/%{name}/
cp -r docs %{buildroot}%{_docdir}/%{name}/
install -m 644 client/README.md %{buildroot}%{_docdir}/%{name}/client/
install -m 644 demo/vagrant-cluster/README.md %{buildroot}%{_docdir}/%{name}/demo/vagrant-cluster/
install -m 644 demo/web-load-balancer/README.md %{buildroot}%{_docdir}/%{name}/demo/web-load-balancer/
install -m 644 ops-misc/README.md %{buildroot}%{_docdir}/%{name}/ops-misc/

%check
# We can run some tests, but not the one that check the actual CLI
# tool, as those would require mDNS and other networking features
# that we don't have available here in OBS.
PKGS="./serf/... ./coordinate/..."

# We also bettr skip the ones that have an internal timeout that
# often reveals itself to be to short for OBS workers.
SKIPS="TestMemberEventCoalesce_Basic"

go test -mod=vendor -v -skip "$SKIPS" $PKGS

%pre
%service_add_pre serf.service
%sysusers_create_package %{name} %{SOURCE4}

%post
%systemd_post serf.service

%preun
%systemd_preun serf.service

%postun
%systemd_postun_with_restart serf.service

%files
%{_bindir}/serf
%attr(0750, serf, serf) %dir %{_sharedstatedir}/serf
%dir %{_sysconfdir}/serf
%dir %{_sysconfdir}/serf/config.d
%if "%{_distconfdir}" != "%{_sysconfdir}"
%dir %{_distconfdir}/serf
%dir %{_distconfdir}/serf/config.d
%endif
%{_sysusersdir}/system-user-serf.conf
%{_unitdir}/serf.service
%{_distconfdir}/serf/config.d/00-default.json
%license LICENSE
# See above...
%doc %{_docdir}/%{name}

%changelog
