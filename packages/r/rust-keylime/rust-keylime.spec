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
Name:           rust-keylime
Version:        0.1.0+git.1655384301.b834667
Release:        0
Summary:        Rust implementation of the keylime agent
License:        Apache-2.0 AND MIT
URL:            https://github.com/keylime/rust-keylime
Source:         rust-keylime-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        keylime_agent.service
Source4:        keylime.xml
Source5:        logrotate.keylime
# PATCH-FIX-OPENSUSE keylime.conf.diff
Patch1:         keylime.conf.diff
BuildRequires:  cargo
BuildRequires:  firewall-macros
BuildRequires:  libarchive-devel
BuildRequires:  rust
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  zeromq-devel
Requires:       libtss2-tcti-device0
Requires:       logrotate
ExcludeArch:    %{ix86} s390x ppc64 ppc64le armhfp armv7hl

%description
Rust implementation of keylime agent. Keylime is system integrity
monitoring system.

%prep
%autosetup -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
RUSTFLAGS=%{rustflags} cargo build --release --no-default-features --features "with-zmq"

%install
RUSTFLAGS=%{rustflags} cargo install --frozen --no-default-features --features "with-zmq" --root=%{buildroot}%{_prefix} --path .

install -Dpm 644 keylime.conf %{buildroot}%{_sysconfdir}/keylime.conf
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/keylime_agent.service
install -Dpm 644 %{SOURCE4} %{buildroot}%{_prefix}/lib/firewalld/services/keylime.xml
install -Dpm 644 %{SOURCE5} %{buildroot}%{_distconfdir}/logrotate.d/keylime
install -d %{buildroot}%{_localstatedir}/log/keylime

# Create work directory
mkdir -p %{buildroot}%{_localstatedir}/keylime

rm %{buildroot}%{_prefix}/.crates.toml
rm %{buildroot}%{_prefix}/.crates2.json

%pre
%service_add_pre keylime_agent.service

%post
%firewalld_reload
%service_add_post keylime_agent.service

%preun
%service_del_preun keylime_agent.service

%postun
%service_del_postun keylime_agent.service

%files
%doc README.md
%license LICENSE
%{_bindir}/keylime_agent
%{_bindir}/keylime_ima_emulator
%config(noreplace) %{_sysconfdir}/keylime.conf
%dir %attr(0700,root,root) %{_localstatedir}/keylime
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/keylime.xml
%{_unitdir}/keylime_agent.service
%{_distconfdir}/logrotate.d/keylime
%dir %attr(750,keylime,tss) %{_localstatedir}/log/keylime

%changelog
