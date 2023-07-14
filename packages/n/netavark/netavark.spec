#
# spec file for package netavark
#
# Copyright (c) 2023 SUSE LLC
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


Name:           netavark
Version:        1.7.0
Release:        0
Summary:        Container network stack
License:        Apache-2.0
URL:            https://github.com/containers/%{name}
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  go-md2man
BuildRequires:  protobuf-devel
BuildRequires:  rust+cargo >= 1.66
BuildRequires:  systemd-rpm-macros
# aardvark-dns and %%{name} are usually released in sync
Requires:       aardvark-dns >= %{version}
# Provides: container-network-stack = 2

%description
Netavark is a rust based network stack for containers. It is being
designed to work with Podman but is also applicable for other OCI
container management applications.
Netavark is a tool for configuring networking for Linux containers.
Its features include:
* Configuration of container networks via JSON configuration file
* Creation and management of required network interfaces,
    including MACVLAN networks
* All required firewall configuration to perform NAT and port
    forwarding as required for containers
* Support for iptables and firewalld at present, with support
    for nftables planned in a future release
* Support for rootless containers
* Support for IPv4 and IPv6
* Support for container DNS resolution via aardvark-dns.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
cargo build --release
mkdir -p bin
cp target/release/%{name} bin/

cd docs
go-md2man -in %{name}.1.md -out %{name}.1

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir}

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_unitdir}/%{name}-dhcp-proxy.service
%{_unitdir}/%{name}-dhcp-proxy.socket

%pre
%service_add_pre %{name}-dhcp-proxy.service %{name}-dhcp-proxy.socket

%post
%service_add_post %{name}-dhcp-proxy.service %{name}-dhcp-proxy.socket

%preun
%service_del_preun %{name}-dhcp-proxy.service %{name}-dhcp-proxy.socket

%postun
%service_del_postun %{name}-dhcp-proxy.service %{name}-dhcp-proxy.socket

%changelog
