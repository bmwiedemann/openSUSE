#
# spec file for package greetd
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

Name:           greetd
Version:        0.6.1
Release:        0
Summary:        Minimal and flexible login manager daemon
License:        GPL-3.0
Group:          System/Management
URL:            https://git.sr.ht/~kennylevinsen/greetd
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
Source3:        greetd.pam
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
Requires(post): diffutils
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires:       pam

%description
greetd is a login manager daemon. greetd on its own does not have any user interface,
but instead offloads that to greeters, which are arbitrary applications that implement the greetd IPC protocol.

%prep
%setup -qa1
%cargo_prep
cp %{SOURCE2} .cargo/config

%build
%cargo_build

%install

install -D -p -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 target/release/agreety %{buildroot}%{_bindir}/agreety

install -D -p -m 0644 config.toml %{buildroot}/%{_sysconfdir}/%{name}/config.toml

install -D -m 0644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_distconfdir}/pam.d/greetd

install -d %{buildroot}%{_localstatedir}/cache/greetd
install -d %{buildroot}%{_localstatedir}/lib/greetd
install -d %{buildroot}/run/greetd

%pre
%service_add_pre %{name}.service
getent group greeter >/dev/null || %{_sbindir}/groupadd -r greeter
getent passwd greeter >/dev/null || %{_sbindir}/useradd -r -g greeter -G video -s /bin/false \
	-c "%{name} daemon" -d %{_localstatedir}/lib/greeter greeter
%{_sbindir}/usermod -g greeter -G video -s /bin/false greeter 2> /dev/null

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/agreety
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/%{name}/config.toml
%{_distconfdir}/pam.d/greetd
%ghost %attr(711,root,greeter) %dir /run/greetd/
%ghost %attr(750,greeter,greeter) %dir %{_localstatedir}/lib/greetd/
%ghost %dir %{_localstatedir}/cache/greetd/

%changelog
