#
# spec file for package kanidm
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


# Solid source of inspiration.
# https://build.opensuse.org/package/view_file/home:luke_nukem:rust_apps/nushell/nushell.spec?expand=1

%global rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2

Name:           kanidm
Version:        v1.1.0alpha.2~git0.ca71b12
Release:        0
Summary:        Kanidm identity project
License:        MPL-2.0 AND Apache-2.0 AND MIT AND ISC AND OpenSSL AND APSL-2.0
URL:            https://github.com/kanidm/kanidm
Source:         kanidm-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source10:       kanidmd.service
Source11:       kanidm-unixd.service
Source12:       server.toml

ExcludeArch:    %ix86

BuildRequires:  cargo
BuildRequires:  lld
BuildRequires:  rust >= 1.45.0
BuildRequires:  rust-std-static
# BuildRequires:  pkgconfig(openssl)
# BuildRequires:  sqlite-devel
BuildRequires:  pam-devel

Requires:       %{name}-clients
Requires:       %{name}-server
Requires:       %{name}-unixd-clients

# Are openssl and sqlite implied as requires from this?

%description
An identity management platform written in rust that supports RADIUS, SSH Key management
and more.

%package clients
Summary:        Client tools for interacting with Kanidm
License:        MPL-2.0

%description clients
Client utilities for interactive with kanidm

%package server
Summary:        Kanidm server and related tools
License:        MPL-2.0
Requires:       %{name}-clients
# Requires:	libsqlite3-0

%description server
Server for kanidm

%package unixd-clients
Summary:        Client nsswitch/pam/ssh integration for consuming kanidm
License:        MPL-2.0
Requires:       %{name}-clients
Requires:       pam
# Requires:	libsqlite3-0

%description unixd-clients
A localhost resolver and libraries that allow a system to resolve posix
identities to a kanidm instance.


%define configdir %{_sysconfdir}/%{name}

%prep
%setup -q
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking
find vendor -type f -name \*.rs -exec chmod -x '{}' \;

%build
export RUSTFLAGS="%{rustflags}"
# Allow building on older compliers with deps that have newer features.
# export RUSTC_BOOTSTRAP=1
cargo build --offline --release

%install
install -D -d -m 0755 %{buildroot}%{configdir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_libdir}
install -D -d -m 0755 %{buildroot}/%_lib/security

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm %{buildroot}%{_bindir}/kanidm
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_badlist_preprocess %{buildroot}%{_bindir}/kanidm_badlist_preprocess
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_cache_clear %{buildroot}%{_sbindir}/kanidm_cache_clear
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_cache_invalidate %{buildroot}%{_sbindir}/kanidm_cache_invalidate
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_ssh_authorizedkeys %{buildroot}%{_sbindir}/kanidm_ssh_authorizedkeys
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_ssh_authorizedkeys_direct %{buildroot}%{_sbindir}/kanidm_ssh_authorizedkeys_direct
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_unixd %{buildroot}%{_sbindir}/kanidm_unixd
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_unixd_status %{buildroot}%{_bindir}/kanidm_unixd_status
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidmd %{buildroot}%{_sbindir}/kanidmd
install -m 0644 %{_builddir}/%{name}-%{version}/target/release/libnss_kanidm.so %{buildroot}%{_libdir}/libnss_kanidm.so.2
install -m 0644 %{_builddir}/%{name}-%{version}/target/release/libpam_kanidm.so %{buildroot}/%_lib/security/pam_kanidm.so

install -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/kanidmd.service
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/kanidm-unixd.service
install -m 0640 %{SOURCE12} %{buildroot}%{configdir}/server.toml

# Example of how to install examples later.
# install -D -m 0755 examples %{buildroot}%{_datadir}/kandim/examples

%pre server
%service_add_pre kanidmd.service

%post server
%service_add_post kanidmd.service

%preun server
%service_del_preun kanidmd.service

%postun server
%service_del_postun kanidmd.service

%pre unixd-clients
%service_add_pre kanidm-unixd.service

%post unixd-clients
%service_add_post kanidm-unixd.service

%preun unixd-clients
%service_del_preun kanidm-unixd.service

%postun unixd-clients
%service_del_postun kanidm-unixd.service

%files
%defattr(-,root,root)
# %{_datadir}/kandim/examples
%exclude /usr/.crates.toml

%files clients
%defattr(-,root,root)
%dir %{configdir}
%{_bindir}/kanidm

%files server
%{_bindir}/kanidm_badlist_preprocess
%{_sbindir}/kanidmd
%{_unitdir}/kanidmd.service
%dir %{configdir}
%config(noreplace) %{configdir}/server.toml

%files unixd-clients
%{_libdir}/libnss_kanidm.so.2
/%_lib/security/pam_kanidm.so
%{_sbindir}/kanidm_cache_clear
%{_sbindir}/kanidm_cache_invalidate
%{_sbindir}/kanidm_ssh_authorizedkeys
%{_sbindir}/kanidm_ssh_authorizedkeys_direct
%{_sbindir}/kanidm_unixd
%{_bindir}/kanidm_unixd_status
%{_unitdir}/kanidm-unixd.service

%changelog
