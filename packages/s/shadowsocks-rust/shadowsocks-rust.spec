#
# spec file for package shadowsocks-rust
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global selinuxtype targeted

Name:           shadowsocks-rust
Version:        1.24.0
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
Source6:        %{name}.apparmor
Source7:        %{name}.fc
Source8:        %{name}.te
# PATCH-FIX-UPSTREAM  https://github.com/AlephAlpha/build-time/pull/5
Patch0:         reproducible.patch
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  libapparmor-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-policy-targeted
BuildRequires:  shadowsocks-common-selinux
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
Requires(pre):  shadowsocks-sysuser
Requires(pre):  shadow
Recommends:     shadowsocks-v2ray-plugin
# ExcludeArch:    ppc ppc64 ppc64le s390 s390x
%{?systemd_ordering}

%description
shadowsocks-rust is a rust port of shadowsocks.

shadowsocks is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

%package apparmor
Summary:        Apparmor profile for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Supplements:    (shadowsocks-rust and apparmor-abstractions)

%description apparmor
This package adds the Apparmor profile to %{name}

%package selinux
Summary:        Selinux support for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-targeted
Requires:       shadowsocks-common-selinux
Supplements:    (shadowsocks-rust and selinux-policy-targeted)

%description selinux
This package adds SELinux enforcement to %{name}.

%prep
%autosetup -p1 -a1 -n %{name}-%{version}
mkdir .cargo
cat >>.cargo/config.toml <<EOF
[source.crates-io]
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = 'vendor'
EOF

%build
cp %{SOURCE7} shadowsocks_rust.fc
cp %{SOURCE8} shadowsocks_rust.te
make -f %{_datadir}/selinux/devel/Makefile shadowsocks_rust.pp

cargo auditable build -j16 --offline --release

%install
%cargo_install

install -d %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/apparmor.d/%{name}

install -d %{buildroot}%{_datadir}/selinux/packages/targeted
install -m 0644 shadowsocks_rust.pp %{buildroot}%{_datadir}/selinux/packages/targeted/shadowsocks_rust.pp

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

%post
%service_add_post %{name}-client.service
%service_add_post %{name}-server.service
%service_add_post %{name}-manager.service

%preun
%service_del_preun %{name}-client.service
%service_del_preun %{name}-server.service
%service_del_preun %{name}-manager.service

%postun
%service_del_postun %{name}-client.service
%service_del_postun %{name}-server.service
%service_del_postun %{name}-manager.service

%post apparmor
if [ -d %{_sysconfdir}/apparmor.d ] && [ -d /sys/kernel/security/apparmor ]; then
    %apparmor_reload %{_sysconfdir}/apparmor.d/%{name}
fi

%preun apparmor
if [ $1 -eq 0 ]; then
    if [ -d %{_sysconfdir}/apparmor.d ] && [ -d /sys/kernel/security/apparmor ]; then
        %apparmor_reload %{_sysconfdir}/apparmor.d/%{name}
    fi
fi

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/shadowsocks_rust.pp
%selinux_relabel_post -s %{selinuxtype}

%preun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} shadowsocks_rust
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files
%doc README.md
%license LICENSE
%{_bindir}/ss*
%{_sbindir}/rc%{name}-*
%{_unitdir}/%{name}-*.service
%attr(640,root,shadowsocks) %config(noreplace) %{_sysconfdir}/shadowsocks/%{name}.json

%files apparmor
%config %{_sysconfdir}/apparmor.d/%{name}

%files selinux
%{_datadir}/selinux/packages/targeted/shadowsocks_rust.pp

%changelog
