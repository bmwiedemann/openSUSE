#
# spec file for package clair
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define cli_executable_name clairctl
%define services clair.service clair-indexer.service clair-matcher.service clair-watcher.service

Name:           clair
Version:        4.8.0
Release:        0
Summary:        Vulnerability Static Analysis for Containers
License:        Apache-2.0
URL:            https://github.com/quay/clair
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        clair.service
Source3:        clair-indexer.service
Source4:        clair-matcher.service
Source5:        clair-watcher.service
BuildRequires:  go >= 1.23

%description
Clair is an open source project for the static analysis of vulnerabilities in
application containers (currently including OCI and docker).

Clients use the Clair API to index their container images and can then match it
against known vulnerabilities.

Our goal is to enable a more transparent view of the security of
container-based infrastructure. Thus, the project was named Clair after the
French term which translates to clear, bright, transparent.

%package -n %{cli_executable_name}
Summary:        CLI for the Clair Vulnerability scanner

%description -n %{cli_executable_name}
clairctl is a command line tool for working with Clair. This CLI is capable of
generating manifests from most public registries (dockerhub, quay.io, Red Hat
Container Catalog) and submitting them for analysis to a running Clair.

%prep
%autosetup -p 1 -a 1
chmod -x LICENSE

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -buildvcs=false \
   -ldflags="-X github.com/quay/clair/v4/cmd.Version=%{version}" \
   -o bin/ ./cmd/...

%install
# Install the clair binary
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# Install the clairctl binary
install -D -m 0755 bin/%{cli_executable_name} %{buildroot}/%{_bindir}/%{cli_executable_name}

# Systemd unit files
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/clair.service
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/clair-indexer.service
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/clair-matcher.service
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/clair-watcher.service

# configuration directory
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/

%check
%{buildroot}/%{_bindir}/%{cli_executable_name} --version|grep -q %{version}

%pre
%service_add_pre %{services}

%post
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/clair.service
%{_unitdir}/clair-indexer.service
%{_unitdir}/clair-matcher.service
%{_unitdir}/clair-watcher.service
%dir %{_sysconfdir}/%{name}/

%files -n %{cli_executable_name}
%doc README.md
%license LICENSE
%{_bindir}/%{cli_executable_name}

%changelog
