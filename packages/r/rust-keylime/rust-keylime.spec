#
# spec file for package rust-keylime
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
# Consolidate _distconfdir and _sysconfdir
%if 0%{?_distconfdir:1}
  %define _config_norepl %{nil}
%else
  %define _distconfdir   %{_sysconfdir}
  %define _config_norepl %config(noreplace)
%endif
Name:           rust-keylime
Version:        0.1.0+git.1664480840.0ea0492
Release:        0
Summary:        Rust implementation of the keylime agent
License:        Apache-2.0 AND MIT
URL:            https://github.com/keylime/rust-keylime
Source:         rust-keylime-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        keylime.xml
Source4:        keylime-user.conf
Source5:        tmpfiles.keylime
# PATCH-FIX-OPENSUSE keylime-agent.conf.diff
Patch1:         keylime-agent.conf.diff
BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  firewall-macros
BuildRequires:  libarchive-devel
BuildRequires:  rust
BuildRequires:  sysuser-tools
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  zeromq-devel
Requires:       libtss2-tcti-device0
Requires:       logrotate
Requires:       tpm2.0-abrmd
Provides:       user(keylime)
%sysusers_requires

%description
Rust implementation of keylime agent. Keylime is system integrity
monitoring system.

%prep
%autosetup -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release --no-default-features --features "with-zmq"
%sysusers_generate_pre %{SOURCE4} keylime keylime-user.conf

%install
RUSTFLAGS=%{rustflags} cargo install --frozen --no-default-features --features "with-zmq" --root=%{buildroot}%{_prefix} --path .

install -Dpm 0600 keylime-agent.conf %{buildroot}%{_distconfdir}/keylime/agent.conf
install -Dpm 0644 ./dist/systemd/system/keylime_agent.service %{buildroot}%{_unitdir}/keylime_agent.service
install -Dpm 0644 ./dist/systemd/system/var-lib-keylime-secure.mount %{buildroot}%{_unitdir}/var-lib-keylime-secure.mount

install -Dpm 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/keylime.xml
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/keylime-user.conf
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/keylime.conf
install -d %{buildroot}%{_localstatedir}/log/keylime
install -d %{buildroot}%{_libexecdir}/keylime

# Create work directory
mkdir -p %{buildroot}%{_sharedstatedir}/keylime

rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

%pre -f keylime.pre
%service_add_pre keylime_agent.service
%service_add_pre var-lib-keylime-secure.mount

%post
%firewalld_reload
%tmpfiles_create keylime.conf
%service_add_post keylime_agent.service
%service_add_post var-lib-keylime-secure.mount

%preun
%service_del_preun keylime_agent.service
%service_del_preun var-lib-keylime-secure.mount

%postun
%service_del_postun keylime_agent.service
%service_del_postun var-lib-keylime-secure.mount

%files
%doc README.md
%license LICENSE
%{_bindir}/keylime_agent
%{_bindir}/keylime_ima_emulator
%dir %attr(0700,keylime,tss) %{_distconfdir}/keylime
%_config_norepl %attr (0600,keylime,tss) %{_distconfdir}/keylime/agent.conf
%{_unitdir}/keylime_agent.service
%{_unitdir}/var-lib-keylime-secure.mount
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/keylime.xml
%{_sysusersdir}/keylime-user.conf
%{_tmpfilesdir}/keylime.conf
%dir %attr(0750,keylime,tss) %{_localstatedir}/log/keylime
%dir %attr(0750,keylime,tss) %{_libexecdir}/keylime
%dir %attr(0700,keylime,tss) %{_sharedstatedir}/keylime

%changelog
