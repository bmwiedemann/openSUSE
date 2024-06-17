#
# spec file for package shadowsocks-rust
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


Name:           shadowsocks-rust
Version:        1.20.0
Release:        0
Summary:        Rust port of Shadowsocks
License:        MIT
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/shadowsocks/shadowsocks-rust
Source0:        https://github.com/shadowsocks/shadowsocks-rust/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.json
Source3:        %{name}-client.service
Source4:        %{name}-server.service
Source5:        %{name}-manager.service
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
Requires(pre):  shadow
Recommends:     shadowsocks-v2ray-plugin
# ExcludeArch:    ppc ppc64 ppc64le s390 s390x
%{?systemd_ordering}

%description
shadowsocks-rust is a rust port of shadowsocks.

shadowsocks is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}
mkdir .cargo
cat >>.cargo/config.toml <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF

%build
%cargo_build

%install
%cargo_install
install -d %{buildroot}%{_sysconfdir}/shadowsocks/
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/shadowsocks/

install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}

install -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-client
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-server
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-manager

%pre
%service_add_pre %{name}-client.service
%service_add_pre %{name}-server.service
%service_add_pre %{name}-manager.service
getent group shadowsocks >/dev/null || %{_sbindir}/groupadd --system shadowsocks
getent passwd shadowsocks >/dev/null || %{_sbindir}/useradd --system -c "shadowsocks User" \
         -d %{_localstatedir}/shadowsocks -m -g shadowsocks -s %{_sbindir}/nologin \
         shadowsocks

%post
%service_add_post %{name}-client.service
%service_add_post %{name}-server.service
%service_add_post %{name}-manager.service
chown root:shadowsocks %{_sysconfdir}/shadowsocks -R
chmod 640 %{_sysconfdir}/shadowsocks -R

%preun
%service_del_preun %{name}-client.service
%service_del_preun %{name}-server.service
%service_del_preun %{name}-manager.service

%postun
%service_del_postun %{name}-client.service
%service_del_postun %{name}-server.service
%service_del_postun %{name}-manager.service

%files
%doc README.md
%license LICENSE
%{_bindir}/ss*
%{_sbindir}/rc%{name}-*
%{_unitdir}/%{name}-*.service
%dir %{_sysconfdir}/shadowsocks
# %config(noreplace) %attr(660,%{name},root) %{_sysconfdir}/shadowsocks
%config %{_sysconfdir}/shadowsocks/%{name}.json

%changelog
