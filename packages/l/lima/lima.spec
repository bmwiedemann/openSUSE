#
# spec file for package lima
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


Name:           lima
Version:        2.0.2~0
Release:        0
Summary:        Linux virtual machines, with a focus on running containers
License:        Apache-2.0
URL:            https://github.com/lima-vm/lima
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.gz
Requires:       qemu
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  gcc
BuildRequires:  git

%ifarch aarch64
%global lima_arch aarch64
%else
%global lima_arch %{_target_cpu}
%endif


%description
Linux virtual machines, with a focus on running containers.

%prep
%autosetup -p1 -a1

%build
VERSION=%{version} CC=gcc CGO_ENABLED=1 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w -X github.com/lima-vm/lima/pkg/version.Version="  -o limactl ./cmd/limactl
make native-guestagent
make default_template

%install
install -D -m0755 limactl %{buildroot}%{_bindir}/limactl
install -D -m0755 cmd/docker.lima %{buildroot}%{_bindir}/docker.lima
install -D -m0755 cmd/kubectl.lima %{buildroot}%{_bindir}/kubectl.lima
install -D -m0755 cmd/nerdctl.lima %{buildroot}%{_bindir}/nerdctl.lima
install -D -m0755 cmd/podman.lima %{buildroot}%{_bindir}/podman.lima

install -D -m0755 cmd/lima %{buildroot}%{_bindir}/lima
mkdir -p %{buildroot}/usr/share/%{name}/templates/
install -Dm644 _output/share/lima/lima-guestagent.Linux-%{lima_arch}.gz \
	%{buildroot}/usr/share/lima/%{name}-guestagent.Linux-%{lima_arch}.gz
cp -rv templates/* %{buildroot}/usr/share/%{name}/templates/

%files
%license LICENSE
%doc README.md
%{_bindir}/limactl
%{_bindir}/docker.lima
%{_bindir}/kubectl.lima
%{_bindir}/nerdctl.lima
%{_bindir}/podman.lima
%{_bindir}/lima
%{_usr}/share/%{name}
%{_usr}/share/%{name}/templates/
%{_usr}/share/lima/lima-guestagent.Linux-%{lima_arch}.gz

%changelog
