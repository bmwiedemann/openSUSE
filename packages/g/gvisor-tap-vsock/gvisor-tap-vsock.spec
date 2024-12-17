#
# spec file for package gvisor-tap-vsock
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


Name:           gvisor-tap-vsock
Version:        0.8.1
Release:        0
Summary:        Go replacement for libslirp and VPNKit
License:        Apache-2.0
Group:          Systems/Networking
URL:            https://github.com/containers/%{name}
Source0:        gvisor-tap-vsock-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  golang >= 1.16.6
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
Provides:       gvproxy = %{version}-%{release}

%description
%{summary}

%{name} is based on the network stack of gVisor. Compared to libslirp,
%{name} brings a configurable DNS server and
dynamic port forwarding.

%prep
%autosetup -a0

%build
go build \
    -buildmode pie \
    -ldflags "-linkmode=external -s -w" \
    -o bin/gvproxy ./cmd/gvproxy

go build \
    -buildmode pie \
    -ldflags "-linkmode=external -s -w" \
    -o bin/gvforwarder ./cmd/vm

%install
install -D -m 0755 bin/gvproxy %{buildroot}%{_libexecdir}/podman/gvproxy
install -D -m 0755 bin/gvforwarder %{buildroot}%{_libexecdir}/podman/gvforwarder
install -D -m0644 contrib/systemd/gv-user-network@.service -t %{buildroot}%{_unitdir}

%pre
%service_add_pre gv-user-network@.service

%post
%service_add_post gv-user-network@.service

%preun
%service_del_preun gv-user-network@.service

%postun
%service_del_postun gv-user-network@.service

%files
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/gvproxy
%{_libexecdir}/podman/gvforwarder
%{_unitdir}/gv-user-network@.service

%changelog
