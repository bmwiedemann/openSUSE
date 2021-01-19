#
# spec file for package dnscrypt-proxy
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


%define _buildshell /bin/bash
%define user_group  dnscrypt
%define config_dir  %{_sysconfdir}/%{name}
%define home_dir    %{_localstatedir}/lib/%{name}
%define log_dir     %{_localstatedir}/log/%{name}
%define services    %{name}.socket %{name}.service %{name}-resolvconf.service
%define vlic_dir  vendored

Name:           dnscrypt-proxy
Version:        2.0.45
Release:        0
Summary:        A tool for securing communications between a client and a DNS resolver
License:        ISC
Group:          Productivity/Networking/DNS/Utilities
URL:            https://dnscrypt.info/
Source0:        https://codeload.github.com/DNSCrypt/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.socket
Source3:        %{name}-resolvconf.service
# File to use with sed to modify default configuration.
Source4:        example-dnscrypt-proxy.toml.sed
# Find licenses of vendored packages.
Source5:        find_licenses.sh
# Install licenses of vendored packages.
Source6:        install_licenses.sh
# Some words
Source7:        README.openSUSE
# Example how to override socket unit
Source8:        %{name}.socket.conf
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.15
BuildRequires:  pkgconfig(libsystemd)
# For systemd pidfile solution.
Requires:       bash
# for daemon group/user
Requires(pre):  shadow
%{?systemd_requires}
Recommends:     ca-certificates
# needed for resolvconf support
Suggests:       openresolv
Provides:       dnscrypt = %{version}-%{release}
Obsoletes:      dnscrypt < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A flexible DNS proxy, with support for modern encrypted DNS protocols
such as DNSCrypt v2, DNS-over-HTTPS and Anonymized DNSCrypt.

%prep
%setup -q -n %{name}-%{version}

# Find licenses of vendored packages and prepare for installation
bash %{SOURCE5} %{vlic_dir}

# duplicate original config file
cp ./%{name}/example-%{name}.toml ./%{name}.toml.default

# Edit default port and file locations
sed -i -f %{SOURCE4} ./%{name}.toml.default

# duplicate edited config file
cp ./%{name}.toml.default ./%{name}.toml

# Delete "example" to prevent fdupes from deleting the backup config file if run for buildroot
sed -i "s/## This is an example configuration file./## This is a configuration file./" ./dnscrypt-proxy.toml

# python path instead of env
sed -i "1s/#! \/usr\/bin\/env python3/#! \/usr\/bin\/python3/" utils/generate-domains-blocklist/generate-domains-blocklist.py

%build
cd %{name}
go build -mod=vendor -buildmode=pie

%install
# Directories
install -D -d -m 0750               \
  %{buildroot}%{log_dir}            \
  %{buildroot}%{home_dir}           \
  %{buildroot}%{config_dir}

install -D -d -m 0755 %{buildroot}%{_datadir}/%{name}/

# Binary
install -D -m 0755 %{name}/%{name} %{buildroot}%{_sbindir}/%{name}

# blocklist generator
cp -a utils/generate-domains-blocklist/ %{buildroot}%{_datadir}/%{name}/

# Config files
install -D -m 0640 ./%{name}.toml %{buildroot}/%{config_dir}/%{name}.toml
install -D -m 0640 ./%{name}.toml.default %{buildroot}/%{config_dir}/%{name}.toml.default
install -D -m 0640 ./%{name}/example-allowed-ips.txt %{buildroot}/%{config_dir}/allowed-ips.txt
install -D -m 0640 ./%{name}/example-allowed-names.txt %{buildroot}/%{config_dir}/allowed-names.txt
install -D -m 0640 ./%{name}/example-blocked-ips.txt %{buildroot}/%{config_dir}/blocked-ips.txt
install -D -m 0640 ./%{name}/example-blocked-names.txt %{buildroot}/%{config_dir}/blocked-names.txt
install -D -m 0640 ./%{name}/example-captive-portals.txt %{buildroot}/%{config_dir}/captive-portals.txt
install -D -m 0640 ./%{name}/example-cloaking-rules.txt %{buildroot}/%{config_dir}/cloaking-rules.txt
install -D -m 0640 ./%{name}/example-forwarding-rules.txt %{buildroot}/%{config_dir}/forwarding-rules.txt

# Systemd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.socket
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-resolvconf.service

# service link
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-resolvconf

# Vendor Licenses
install -d -m 0755 %{buildroot}%{_licensedir}/%{name}/%{vlic_dir}
bash %{SOURCE6} %{vlic_dir} %{buildroot}/%{_licensedir}/%{name}/%{vlic_dir}

# Some hints. Improvements and feedback welcome!
cp %{SOURCE7} README.openSUSE

# Example drop-in.
cp %{SOURCE8} %{name}.socket.conf

%pre
# group and user
getent group %{user_group} >/dev/null || %{_sbindir}/groupadd -r %{user_group}
getent passwd %{user_group} >/dev/null || %{_sbindir}/useradd -r -g %{user_group} \
  -d %{home_dir} -s /bin/false -c "DNScrypt Proxy" %{user_group}

%service_add_pre %{services}

%post
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%doc ChangeLog README.md README.openSUSE %{name}.socket.conf %{name}.toml.default
%doc %{name}/example-*
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/%{name}.toml
%config %attr(-,root,%{user_group}) %{config_dir}/%{name}.toml.default
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/allowed-ips.txt
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/allowed-names.txt
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/blocked-ips.txt
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/blocked-names.txt
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/captive-portals.txt
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/cloaking-rules.txt
%config(noreplace) %attr(-,root,%{user_group}) %{config_dir}/forwarding-rules.txt
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_sbindir}/rc%{name}-resolvconf
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_unitdir}/%{name}-resolvconf.service
%{_datadir}/%{name}/
%dir %attr(0750,root,%{user_group}) %{config_dir}
%dir %attr(0750,%{user_group},%{user_group}) %{home_dir}
%dir %attr(0750,%{user_group},%{user_group}) %{log_dir}
%license LICENSE
%{_licensedir}/%{name}/%{vlic_dir}/

%changelog
