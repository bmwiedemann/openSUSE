#
# spec file for package teleport
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           teleport
Version:        8.3.1
Release:        0
Summary:        Identity-aware, multi-protocol access proxy
License:        Apache-2.0
URL:            https://github.com/gravitational/teleport
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        teleport.service
Source3:        teleport.yaml
BuildRequires:  go >= 1.17
BuildRequires:  systemd-rpm-macros
Requires:       teleport-tctl

%description
Teleport is the easiest, most secure way to access all your infrastructure. Teleport is an identity-aware, multi-protocol access proxy which understands SSH, HTTPS, RDP, Kubernetes API, MySQL, MongoDB and PostgreSQL wire protocols.

On the server-side, Teleport is a single binary which enables convenient secure access to behind-NAT resources such as:
* SSH nodes - SSH works in browsers too!
* Kubernetes clusters
* PostgreSQL, MongoDB, CockroachDB and MySQL databases
* Internal Web apps
* Windows Hosts
* Networked servers

%package -n teleport-tctl
Summary:        CLI tool for managing a teleport server
License:        Apache-2.0

%description -n teleport-tctl
An administrative tool that can configure Teleport Auth Service.

%package -n teleport-tsh
Summary:        CLI tool for logging into nodes via Teleport SSH
License:        Apache-2.0

%description -n teleport-tsh
A tool that lets end users interact with Teleport nodes. This replaces ssh.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.VERSION=%{version}" \
   -o bin/tsh ./tool/tsh
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.VERSION=%{version}" \
   -o bin/tctl ./tool/tctl
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.VERSION=%{version}" \
   -o bin/teleport ./tool/teleport

%install
# Install the binary.
install -D -m 0755 bin/tsh "%{buildroot}/%{_bindir}/tsh"
install -D -m 0755 bin/tctl "%{buildroot}/%{_bindir}/tctl"
install -D -m 0755 bin/teleport "%{buildroot}/%{_sbindir}/teleport"
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/teleport.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/teleport.yaml

%pre -n teleport
%service_add_pre teleport.service

%post -n teleport
%service_add_post teleport.service

%preun -n teleport
%service_del_preun teleport.service

%postun -n teleport
%service_del_postun teleport.service

%files -n teleport
%doc README.md
%license LICENSE
%{_sbindir}/teleport
%{_unitdir}/teleport.service
%config(noreplace) %{_sysconfdir}/teleport.yaml

%files -n teleport-tsh
%doc README.md
%license LICENSE
%{_bindir}/tsh

%files -n teleport-tctl
%doc README.md
%license LICENSE
%{_bindir}/tctl

%changelog
