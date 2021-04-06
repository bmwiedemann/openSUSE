#
# spec file for package kanidm
#
# Copyright (c) 2021 SUSE LLC
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


%global rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2

Name:           kanidm
Version:        1.1.0~alpha4~git0.0ac5da8
Release:        0
Summary:        A identity management service and clients.
License:        ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR ISC OR MIT ) AND ( Apache-2.0 OR MIT ) AND ( Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT ) AND ( CC0-1.0 OR Apache-2.0 ) AND ( MIT OR Apache-2.0 OR Zlib ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND MPL-2.0+
URL:            https://github.com/Firstyear/kanidm
Source:         kanidm-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source10:       kanidmd.service
Source11:       kanidm-unixd.service
Source12:       server.toml
Source13:       kanidm-unixd-tasks.service

ExcludeArch:    %ix86 s390x ppc64 ppc64le armhfp armv7hl

BuildRequires:  cargo
BuildRequires:  libudev-devel
BuildRequires:  pam-devel
BuildRequires:  rust >= 1.45.0
BuildRequires:  sqlite-devel
BuildRequires:  pkgconfig(openssl)

%if 0%{?rhel} > 7 || 0%{?fedora}
BuildRequires:  systemd
%{?systemd_requires}
%endif

Requires:       %{name}-clients
# Requires:       %{name}-server
Requires:       %{name}-unixd-clients

#### START BUNDLE METADATA
### See cargo lock2rpmprovides
# currently not needed in suse.
#### END BUNDLE METADATA

%description
An identity management platform written in rust that supports RADIUS, SSH Key management
and more.

%package clients
Summary:        Client tools for interacting with Kanidm
License:        MPL-2.0

%description clients
Client utilities for interactive with kanidm servers

%package server
Summary:        Kanidm server and related tools
License:        MPL-2.0
Requires:       %{name}-clients

%description server
Server for kanidm providing the main authentication and identity service

%package unixd-clients
Summary:        Client nsswitch/pam/ssh integration for consuming kanidm
License:        MPL-2.0
Requires:       %{name}-clients

%description unixd-clients
A localhost resolver and libraries that allow a system to resolve posix
identities to a kanidm instance.

%package docs
Summary:        Documentation for Kanidm Administration
License:        MPL-2.0

%description docs
Documentation for using and configuring Kanidm.


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

# Set our build profile
export KANIDM_BUILD_PROFILE=release_suse_generic
cargo build --offline --release
# Now, move the completions to easier to install locations.
mkdir %{_builddir}/%{name}-%{version}/target/release/_completions
cp %{_builddir}/%{name}-%{version}/target/release/build/*/out/_kanidm* %{_builddir}/%{name}-%{version}/target/release/_completions/
cp %{_builddir}/%{name}-%{version}/target/release/build/*/out/kanidm*.bash %{_builddir}/%{name}-%{version}/target/release/_completions/

%install
install -D -d -m 0755 %{buildroot}%{_sysconfdir}
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/zsh_completion.d
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -D -d -m 0755 %{buildroot}%{configdir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_libdir}
install -D -d -m 0755 %{buildroot}/%_lib/security
install -D -d -m 0755 %{buildroot}%{_datadir}/kanidm
install -D -d -m 0755 %{buildroot}%{_datadir}/kanidm/docs/
install -D -d -m 0755 %{buildroot}%{_datadir}/kanidm/ui/
install -D -d -m 0755 %{buildroot}%{_datadir}/kanidm/ui/pkg
install -D -d -m 0755 %{buildroot}%{_datadir}/kanidm/ui/pkg/external

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidmd %{buildroot}%{_sbindir}/kanidmd
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_badlist_preprocess %{buildroot}%{_bindir}/kanidm_badlist_preprocess
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm %{buildroot}%{_bindir}/kanidm
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_cache_clear %{buildroot}%{_sbindir}/kanidm_cache_clear
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_cache_invalidate %{buildroot}%{_sbindir}/kanidm_cache_invalidate
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_ssh_authorizedkeys %{buildroot}%{_sbindir}/kanidm_ssh_authorizedkeys
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_ssh_authorizedkeys_direct %{buildroot}%{_sbindir}/kanidm_ssh_authorizedkeys_direct
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_unixd %{buildroot}%{_sbindir}/kanidm_unixd
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_unixd_tasks %{buildroot}%{_sbindir}/kanidm_unixd_tasks
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/kanidm_unixd_status %{buildroot}%{_bindir}/kanidm_unixd_status
install -m 0644 %{_builddir}/%{name}-%{version}/target/release/libnss_kanidm.so %{buildroot}%{_libdir}/libnss_kanidm.so.2
install -m 0644 %{_builddir}/%{name}-%{version}/target/release/libpam_kanidm.so %{buildroot}/%_lib/security/pam_kanidm.so

install -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/kanidmd.service

install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/kanidm-unixd.service
install -m 0640 %{SOURCE12} %{buildroot}%{configdir}/server.toml
install -m 0644 %{SOURCE13} %{buildroot}%{_unitdir}/kanidm-unixd-tasks.service

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidmd   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidmd
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm_badlist_preprocess   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm_badlist_preprocess
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm_ssh_authorizedkeys_direct   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm_ssh_authorizedkeys_direct
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm_cache_clear   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm_cache_clear
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm_cache_invalidate   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm_cache_invalidate
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm_ssh_authorizedkeys   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm_ssh_authorizedkeys
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/_kanidm_unixd_status   %{buildroot}%{_sysconfdir}/zsh_completion.d/_kanidm_unixd_status

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidmd.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidmd.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm_badlist_preprocess.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm_badlist_preprocess.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm_ssh_authorizedkeys_direct.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm_ssh_authorizedkeys_direct.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm_cache_clear.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm_cache_clear.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm_cache_invalidate.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm_cache_invalidate.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm_ssh_authorizedkeys.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm_ssh_authorizedkeys.sh
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/_completions/kanidm_unixd_status.bash %{buildroot}%{_sysconfdir}/bash_completion.d/kanidm_unixd_status.sh

install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/SUMMARY.md %{buildroot}%{_datadir}/kanidm/docs/SUMMARY.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/accounts_and_groups.md %{buildroot}%{_datadir}/kanidm/docs/accounts_and_groups.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/administrivia.md %{buildroot}%{_datadir}/kanidm/docs/administrivia.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/client_tools.md %{buildroot}%{_datadir}/kanidm/docs/client_tools.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/installing_the_server.md %{buildroot}%{_datadir}/kanidm/docs/installing_the_server.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/intro.md %{buildroot}%{_datadir}/kanidm/docs/intro.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/ldap.md %{buildroot}%{_datadir}/kanidm/docs/ldap.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/pam_and_nsswitch.md %{buildroot}%{_datadir}/kanidm/docs/pam_and_nsswitch.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/password_quality.md %{buildroot}%{_datadir}/kanidm/docs/password_quality.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/posix_accounts.md %{buildroot}%{_datadir}/kanidm/docs/posix_accounts.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/radius.md %{buildroot}%{_datadir}/kanidm/docs/radius.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/recycle_bin.md %{buildroot}%{_datadir}/kanidm/docs/recycle_bin.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/security_hardening.md %{buildroot}%{_datadir}/kanidm/docs/security_hardening.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/ssh_key_dist.md %{buildroot}%{_datadir}/kanidm/docs/ssh_key_dist.md
install -m 0644 %{_builddir}/%{name}-%{version}/kanidm_book/src/why_tls.md %{buildroot}%{_datadir}/kanidm/docs/why_tls.md

## TODO: Add /usr/share/kanidm/ui/pkg
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/bundle.js %{buildroot}%{_datadir}/kanidm/ui/pkg/bundle.js
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/kanidmd_web_ui.js %{buildroot}%{_datadir}/kanidm/ui/pkg/kanidmd_web_ui.js
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/kanidmd_web_ui_bg.wasm %{buildroot}%{_datadir}/kanidm/ui/pkg/kanidmd_web_ui_bg.wasm
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/package.json %{buildroot}%{_datadir}/kanidm/ui/pkg/package.json

install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/external/bootstrap.min.css %{buildroot}%{_datadir}/kanidm/ui/pkg/external/bootstrap.min.css
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/external/bootstrap.min.js %{buildroot}%{_datadir}/kanidm/ui/pkg/external/bootstrap.min.js
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/external/jquery-3.3.1.slim.min.js %{buildroot}%{_datadir}/kanidm/ui/pkg/external/jquery-3.3.1.slim.min.js
install -m 0644 %{_builddir}/%{name}-%{version}/kanidmd_web_ui/pkg/external/popper.min.js %{buildroot}%{_datadir}/kanidm/ui/pkg/external/popper.min.js

## End install

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%pre server
%service_add_pre kanidmd.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%post server
%service_add_post kanidmd.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%preun server
%service_del_preun kanidmd.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%postun server
%service_del_postun kanidmd.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%pre unixd-clients
%service_add_pre kanidm-unixd.service
%service_add_pre kanidm-unixd-tasks.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%post unixd-clients
%service_add_post kanidm-unixd.service
%service_add_post kanidm-unixd-tasks.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%preun unixd-clients
%service_del_preun kanidm-unixd.service
%service_del_preun kanidm-unixd-tasks.service
%endif

%if 0%{?rhel} > 7 || 0%{?fedora}
%else

%postun unixd-clients
%service_del_postun kanidm-unixd.service
%service_del_postun kanidm-unixd-tasks.service
%endif

%files
%defattr(-,root,root)
# percent exclude /usr/.crates.toml

%files clients
%defattr(-,root,root)
%dir %{configdir}
%{_bindir}/kanidm
%dir %{_sysconfdir}/zsh_completion.d
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/zsh_completion.d/_kanidm
%{_sysconfdir}/bash_completion.d/kanidm.sh

%files server
%{_bindir}/kanidm_badlist_preprocess
%{_sbindir}/kanidmd
%{_unitdir}/kanidmd.service
%dir %{_datadir}/kanidm
%dir %{_datadir}/kanidm/ui
%dir %{_datadir}/kanidm/ui/pkg
%dir %{_datadir}/kanidm/ui/pkg/external
%{_datadir}/kanidm/ui/pkg/*
%{_datadir}/kanidm/ui/pkg/external/*
%dir %{configdir}
%config(noreplace) %{configdir}/server.toml
%dir %{_sysconfdir}/zsh_completion.d
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/zsh_completion.d/_kanidmd
%{_sysconfdir}/zsh_completion.d/_kanidm_badlist_preprocess
%{_sysconfdir}/bash_completion.d/kanidmd.sh
%{_sysconfdir}/bash_completion.d/kanidm_badlist_preprocess.sh

%files unixd-clients
%{_libdir}/libnss_kanidm.so.2
/%_lib/security/pam_kanidm.so
%{_sbindir}/kanidm_cache_clear
%{_sbindir}/kanidm_cache_invalidate
%{_sbindir}/kanidm_ssh_authorizedkeys
%{_sbindir}/kanidm_ssh_authorizedkeys_direct
%{_sbindir}/kanidm_unixd
%{_sbindir}/kanidm_unixd_tasks
%{_bindir}/kanidm_unixd_status
%{_unitdir}/kanidm-unixd.service
%{_unitdir}/kanidm-unixd-tasks.service
%dir %{_sysconfdir}/zsh_completion.d
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/zsh_completion.d/_kanidm_ssh_authorizedkeys_direct
%{_sysconfdir}/zsh_completion.d/_kanidm_cache_clear
%{_sysconfdir}/zsh_completion.d/_kanidm_cache_invalidate
%{_sysconfdir}/zsh_completion.d/_kanidm_ssh_authorizedkeys
%{_sysconfdir}/zsh_completion.d/_kanidm_unixd_status
%{_sysconfdir}/bash_completion.d/kanidm_ssh_authorizedkeys_direct.sh
%{_sysconfdir}/bash_completion.d/kanidm_cache_clear.sh
%{_sysconfdir}/bash_completion.d/kanidm_cache_invalidate.sh
%{_sysconfdir}/bash_completion.d/kanidm_ssh_authorizedkeys.sh
%{_sysconfdir}/bash_completion.d/kanidm_unixd_status.sh

%files docs
%dir %{_datadir}/kanidm
%dir %{_datadir}/kanidm/docs
%doc %{_datadir}/kanidm/docs/*

%changelog
