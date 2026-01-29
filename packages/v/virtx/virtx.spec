#
# spec file for package VirtX
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           virtx
Version:        0.1+ga780082
Release:        0
Summary:        VirtX is a simple federation of KVM hosts based on libvirt and serf
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/OpenSUSE/virtx
Source:         virtx-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        virtx.service
BuildRequires:  golang-packaging
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  golang(API) >= 1.23
BuildRequires:  bash-completion
BuildRequires:  systemd-rpm-macros
Requires:       qemu-pr-helper
Requires:       qemu-hw-display-virtio-gpu-pci
Requires:       libvirt-daemon-qemu
Requires:       libvirt-daemon-proxy
Requires:       libvirt-daemon-config-network
Requires:       numa-preplace
Requires:       hashicorp-serf
%{?systemd_ordering}

%description
A tool for managing a simple federation of KVM hosts based on libvirt and
serf leveraging shared storage, and offering a REST API, to make it easier
to implement custom KVM platforms.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}, generated during the build.

%prep
%autosetup -a 1 -p 1

%build
make VERSION=%{version}
./virtx completion bash > virtx-completion.sh

%install
# Install the binaries
install -D -m 0755 virtx "%{buildroot}/%{_bindir}/virtx"
install -D -m 0755 virtxd "%{buildroot}/%{_sbindir}/virtxd"
install -D -m 0755 virtx-completion.sh "%{buildroot}/%{_datadir}/bash-completion/completions/virtx"
install -D -m 0644 %{SOURCE2} "%{buildroot}/%{_unitdir}/virtx.service"

%check
# execute the command line client as a basic check
./virtx --help

%pre
%service_add_pre virtx.service

%post
%service_add_post virtx.service

%preun
%service_del_preun virtx.service

%postun
%service_del_postun virtx.service

%files
%doc README.md
%license LICENSE google-uuid-license.txt serf-client-license.txt cobra-license.txt
%{_bindir}/virtx
%{_sbindir}/virtxd
%{_unitdir}/virtx.service

%files bash-completion
%{_datadir}/bash-completion/completions/virtx
%changelog
