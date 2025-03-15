#
# spec file for package vault-sync
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


Name:           vault-sync
Version:        0.10.0
Release:        0
Summary:        Synchronize secrets between HashiCorp Vault instances
License:        Apache-2.0
URL:            https://github.com/pbchekin/vault-sync
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        vault-sync.service
Source3:        vault-sync.yaml.dummy
BuildRequires:  cargo >= 1.69.0
BuildRequires:  cargo-packaging
BuildRequires:  openssl-devel
BuildRequires:  zstd
BuildRequires:  user(vault-sync)
Requires:       user(vault-sync)

%description
A poor man's tool to replicate secrets from one Vault instance to another.

How it works

When vault-sync starts, it does a full copy of the secrets from the source
Vault instance to the destination Vault instance. Periodically, vault-sync does
a full reconciliation to make sure all the destination secrets are up to date.

At the same time, you can manually enable the Socket Audit Device for the
source Vault, so Vault will be sending audit logs to vault-sync. Using these
audit logs, vault-sync keeps the secrets in the destination Vault up to date.
Note that vault-sync does not create or delete the audit devices by itself.

It is possible to use the same Vault instance as the source and the
destination. You can use this feature to replicate a "folder" of secrets to
another "folder" on the same server. You need to specify different prefixes
(src.prefix and dst.prefix) in the configuration file to make sure the source
and the destination do not overlap.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}/
install -D -m 0640 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/vault-sync.yaml

%check
%{cargo_test}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md vault-sync.example.yaml
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(640,root,vault-sync) %{_sysconfdir}/%{name}/vault-sync.yaml

%changelog
