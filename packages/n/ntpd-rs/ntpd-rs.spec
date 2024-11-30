#
# spec file for package ntpd-rs
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


%define services ntpd-rs.service ntpd-rs-metrics.service
Name:           ntpd-rs
Version:        1.3.1
Release:        0
Summary:        Full-featured implementation of NTP with NTS support
License:        Apache-2.0 OR MIT
Group:          Productivity/Networking/Other
#Git-Clone:     https://github.com/pendulum-project/ntpd-rs
URL:            https://tweedegolf.nl/en/pendulum
Source:         https://github.com/pendulum-project/ntpd-rs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}.tmpfiles
Source3:        %{name}.sysusers
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires(pre):  %{name}-common = %{version}
Conflicts:      ntp-daemon
Provides:       ntp-daemon

%description
A full-featured implementation of the Network Time Protocol,
including support for NTS (Network Time Security).

It includes both client and server support.

%package common
Summary:        System user 'ntpd-rs' and 'ntpd-rs-observe'
BuildArch:      noarch
%sysusers_requires

%description common
A full-featured implementation of the Network Time Protocol,
including support for NTS (Network Time Security).

This subpackage sets up the system user/group for the rest of ntpd-rs.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}
%sysusers_generate_pre %{SOURCE3} %{name} %{name}.conf

%install
install -Dpm0755 target/release/ntp-ctl -t %{buildroot}/%{_bindir}
install -Dpm0755 target/release/ntp-daemon -t %{buildroot}/%{_bindir}
install -Dpm0755 target/release/ntp-metrics-exporter -t %{buildroot}/%{_bindir}

install -Dpm0644 docs/precompiled/man/*.5 -t %{buildroot}/%{_mandir}/man5
install -Dpm0644 docs/precompiled/man/*.8 -t %{buildroot}/%{_mandir}/man8

install -Dpm0644 docs/examples/conf/ntp.toml.default %{buildroot}/%{_sysconfdir}/ntpd-rs/ntp.toml

install -Dpm0644 docs/examples/conf/ntpd-rs.service -t %{buildroot}/%{_unitdir}
install -Dpm0644 docs/examples/conf/ntpd-rs-metrics.service -t %{buildroot}/%{_unitdir}

install -Dpm0644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

install -d %{buildroot}/%{_sharedstatedir}/ntpd-rs
install -d %{buildroot}/%{_sharedstatedir}/ntpd-rs-observe
install -d %{buildroot}/%{_rundir}/ntpd-rs

%pre
%service_add_pre %{services}

%pre common -f %{name}.pre

%post
%service_add_post %{services}
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || true

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%check
### skip tests that are not working in OBS build environment
#[  147s] running 2 tests
#[  147s] test hwtimestamp::tests::get_hwtimestamp ... FAILED
#[  147s] test socket::tests::test_send_timestamp ... FAILED
#%%{cargo_test} -- -- --skip hwtimestamp::tests::get_hwtimestamp --skip socket::tests::test_send_timestamp

%files
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md SECURITY.md
%doc docs/examples/conf/ntp.toml.default
%dir %{_sysconfdir}/ntpd-rs
%config(noreplace) %{_sysconfdir}/ntpd-rs/ntp.toml
%{_bindir}/ntp-ctl
%{_bindir}/ntp-daemon
%{_bindir}/ntp-metrics-exporter
%{_mandir}/man5/ntp.toml.5%{?ext_man}
%{_mandir}/man8/ntp-ctl.8%{?ext_man}
%{_mandir}/man8/ntp-daemon.8%{?ext_man}
%{_mandir}/man8/ntp-metrics-exporter.8%{?ext_man}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/ntpd-rs.service
%{_unitdir}/ntpd-rs-metrics.service
%ghost %dir %attr(0700, ntpd-rs, ntpd-rs) %{_sharedstatedir}/ntpd-rs
%ghost %dir %attr(0700, ntpd-rs-observe, ntpd-rs-observe) %{_sharedstatedir}/ntpd-rs-observe
%ghost %dir %attr(0700, ntpd-rs-observe, ntpd-rs-observe) %{_rundir}/ntpd-rs

%files common
%{_sysusersdir}/%{name}.conf

%changelog
