#
# spec file for package lldap
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


Name:           lldap
Version:        0.6.1
Release:        0
Summary:        Light LDAP implementation
License:        MIT
URL:            https://github.com/lldap/lldap
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source11:       %{name}.service
Source21:       system-user-%{name}.conf
BuildRequires:  cargo1.82
BuildRequires:  cargo-packaging
BuildRequires:  zstd
BuildRequires:  wasm-pack
BuildRequires:  wasm-bindgen
BuildRequires:  gzip
BuildRequires:  sysuser-tools
ExclusiveArch:  %{rust_tier1_arches}

# nothing provides libldap-data = 2.4.46-150600.23.21 needed by libldap-2_4-2, (got version 2.6.8-lp156.3.3)
#!BuildIgnore: libldap-data

%description
This project is a lightweight authentication server that provides an
opinionated, simplified LDAP interface for authentication. It integrates with
many backends, from KeyCloak to Authelia to Nextcloud and more!

It comes with a frontend that makes user management easy, and allows users to
edit their own details or reset their password by email.

The goal is not to provide a full LDAP server; if you're interested in that,
check out OpenLDAP. This server is a user management system that is:

- simple to setup (no messing around with slapd),
- simple to manage (friendly web UI),
- low resources,
- opinionated with basic defaults so you don't have to understand the
  subtleties of LDAP.

It mostly targets self-hosting servers, with open-source components like
Nextcloud, Airsonic and so on that only support LDAP as a source of external
authentication.

For more features (OAuth/OpenID support, reverse proxy, ...) you can install
other components (KeyCloak, Authelia, ...) using this server as the source of
truth for users, via LDAP.

By default, the data is stored in SQLite, but you can swap the backend with
MySQL/MariaDB or PostgreSQL.

%package -n %{name}-migration-tool
Summary:        This package contains the %{name}_migration_tool binary
Provides:       %{name}_migration_tool = %{version}

%description -n %{name}-migration-tool
This package contains the %{name}_migration_tool binary.

%package -n %{name}-set-password
Summary:        This package contains the %{name}_set_password binary
Provides:       %{name}_set_password = %{version}

%description -n %{name}-set-password
This package contains the %{name}_set_password binary.

%prep
%autosetup -a 1 -p 1

%build
%{cargo_build} -p lldap -p lldap_migration_tool -p lldap_set_password

echo "Start building frontend files"
cd ./app
wasm-pack build --target web --release --mode no-install -- --offline --locked
gzip -9 -k -f pkg/lldap_app_bg.wasm
cd ..

# system-user
%sysusers_generate_pre %{SOURCE21} user

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/lldap_migration_tool %{buildroot}%{_bindir}/lldap_migration_tool
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/lldap_set_password %{buildroot}%{_bindir}/lldap_set_password

install -d -m 0750 %{buildroot}%{_sysconfdir}/%{name}/

install -d -m 0750 %{buildroot}%{_sharedstatedir}/%{name}/

install -d -m 0755 %{buildroot}%{_unitdir}/
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}.service

# system user
install -Dm644 %{SOURCE21} %{buildroot}%{_sysusersdir}/system-user-%{name}.conf

# fix paths in lldap_config.toml.example
cp -v lldap_config.docker_template.toml lldap_config.toml.example
sed -i '/^database_url/ s#/data/#/var/lib/lldap/#' lldap_config.toml.example
sed -i '/^key_file/ s#data#var/lib/lldap#' lldap_config.toml.example

%pre -f user.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md lldap_config.toml.example
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%dir %attr(750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(640,root,%{name}) %ghost %{_sysconfdir}/%{name}/lldap_config.toml
%dir %attr(770,root,%{name}) %{_sharedstatedir}/%{name}/

%{_sysusersdir}/system-user-%{name}.conf

%files -n %{name}-migration-tool
%{_bindir}/lldap_migration_tool

%files -n %{name}-set-password
%{_bindir}/lldap_set_password

%changelog
