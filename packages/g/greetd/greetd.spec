#
# spec file for package greetd
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


%if 0%{?suse_version} >= 1550
  %define _pam_confdir %{_pam_vendordir}
  %define _config_norepl %nil
%else
  %define _pam_confdir %{_sysconfdir}/pam.d
  %define _config_norepl %config(noreplace)
%endif

Name:           greetd
Version:        0.10.3
Release:        0
Summary:        Minimal and flexible login manager daemon
License:        GPL-3.0-only
Group:          System/Management
URL:            https://git.sr.ht/~kennylevinsen/greetd
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source3:        greetd.pam
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
Requires:       pam

%description
greetd is a login manager daemon. greetd on its own does not have any user interface,
but instead offloads that to greeters, which are arbitrary applications that implement the greetd IPC protocol.

%prep
%autosetup -a1

%build
%{cargo_build}

%install

install -D -p -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 target/release/agreety %{buildroot}%{_bindir}/agreety

# https://github.com/openSUSE/openSUSEway/issues/37
sed -i -e "s|\$SHELL|bash|" config.toml
install -D -p -m 0644 config.toml %{buildroot}/%{_sysconfdir}/%{name}/config.toml

install -D -m 0644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_pam_confdir}/greetd

install -d %{buildroot}%{_localstatedir}/cache/greetd
install -d %{buildroot}%{_sharedstatedir}/greetd
install -d %{buildroot}/run/greetd

%check
%{cargo_test}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun_without_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/agreety
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/%{name}/config.toml
%_config_norepl %{_pam_confdir}/greetd
%ghost %attr(711,root,greeter) %dir /run/greetd/
%attr(750,greeter,greeter) %dir %{_sharedstatedir}/greetd
%ghost %dir %{_localstatedir}/cache/greetd/

%changelog
