#
# spec file for package headscale
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


Name:           headscale
Version:        0.22.3
Release:        0
Summary:        An open source, self-hosted implementation of the Tailscale control server
License:        BSD-3-Clause
URL:            https://headscale.net
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        headscale.sysusers
Source3:        headscale.tmpfs.conf
Source4:        headscale.systemd.service
Source5:        config-example.yaml
Source6:        derp-example.yaml
BuildRequires:  golang-packaging
BuildRequires:  zstd
Suggests:       wireguard-tools
Suggests:       postgresql-server

%description
Headscale aims to implement a self-hosted, open source alternative to the Tailscale control server. Headscale's goal is to provide self-hosters and hobbyists with an open-source server they can use for their projects and labs. It implements a narrow scope, a single Tailnet, suitable for a personal use, or a small open-source organisation.

%prep
%autosetup -a1

%build
go build -v -buildmode=pie -mod=vendor -tags "ts2019" -ldflags "-s -w -X github.com/juanfont/headscale/cmd/headscale/cli.Version=%{version}" ./cmd/headscale

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE2} %{buildroot}/usr/lib/sysusers.d/%{name}.conf
install -D -m 644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/%{name}.service
%if 0%{?suse_version} == 1500
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/config-example.yaml
install -D -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/%{name}/config-derp.yaml
%else
install -D -m 644 %{SOURCE5} %{buildroot}/%{_distconfdir}/%{name}/config-example.yaml
install -D -m 644 %{SOURCE6} %{buildroot}/%{_distconfdir}/%{name}/derp-example.yaml
%endif

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sharedstatedir}/%{name}
%if 0%{suse_version} == 1500
%{_sysconfdir}/%{name}
%else
%dir %{_distconfdir}/%{name}
%{_distconfdir}/%{name}/*
%endif
/usr/lib/sysusers.d/%{name}.conf
/usr/lib/tmpfiles.d/%{name}.conf
/usr/lib/systemd/system/%{name}.service

%changelog
