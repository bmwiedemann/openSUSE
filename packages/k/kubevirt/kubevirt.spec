#
# spec file for package kubevirt
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


Name:           kubevirt
Version:        0.32.0
Release:        0
Summary:        Container native virtualization
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/kubevirt
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  glibc-devel-static
BuildRequires:  golang(API) = 1.11
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  pkgconfig(libvirt)
ExclusiveArch:  x86_64

%description
Kubevirt is a virtual machine management add-on for Kubernetes

%package        virtctl
Summary:        Client for managing kubevirt

%description    virtctl
The virtctl client is a command-line utility for managing container native virtualization resources

%package        virt-api
Summary:        Kubevirt API server

%description    virt-api
The virt-api package provides the kubernetes API extension for kubevirt

%package        container-disk
Summary:        Container disk for kubevirt

%description    container-disk
The containter-disk package provides a container disk functionality for kubevirt

%package        virt-controller
Summary:        Controller for kubevirt

%description    virt-controller
The virt-controller package provides a controller for kubevirt

%package        virt-handler
Summary:        Handler component for kubevirt

%description    virt-handler
The virt-handler package provides a handler for kubevirt

%package        virt-launcher
Summary:        Launcher component for kubevirt

%description    virt-launcher
The virt-launcher package provides a launcher for kubevirt

%package        virt-operator
Summary:        Operator component for kubevirt

%description    virt-operator
The virt-opertor package provides an operator for kubevirt CRD

%prep
%autosetup -p1

%build
mkdir -p go/src/kubevirt.io go/pkg
ln -s ../../../ go/src/kubevirt.io/kubevirt
export GOPATH=${PWD}/go
cd ${GOPATH}/src/kubevirt.io/kubevirt
env \
KUBEVIRT_GO_BASE_PKGDIR="${GOPATH}/pkg" \
KUBEVIRT_VERSION=%{version} \
KUBEVIRT_SOURCE_DATE_EPOCH="$(date -r LICENSE +%{s})" \
KUBEVIRT_GIT_COMMIT='v%{version}' \
KUBEVIRT_GIT_VERSION='v%{version}' \
KUBEVIRT_GIT_TREE_STATE="clean" \
./hack/build-go.sh install \
	cmd/virtctl \
	cmd/virt-api \
	cmd/virt-controller \
	cmd/virt-chroot \
	cmd/virt-handler \
	cmd/virt-launcher \
	cmd/virt-operator \
	tools/csv-generator \
	%{nil}
./hack/build-copy-artifacts.sh

%install
mkdir -p %{buildroot}%{_bindir}

chmod 0755 _out/cmd/container-disk-v2alpha/container-disk
install -p -m 0755 _out/cmd/container-disk-v2alpha/container-disk %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virtctl/virtctl
install -p -m 0755 _out/cmd/virtctl/virtctl %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virt-api/virt-api
install -p -m 0755 _out/cmd/virt-api/virt-api %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virt-controller/virt-controller
install -p -m 0755 _out/cmd/virt-controller/virt-controller %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virt-chroot/virt-chroot
install -p -m 0755 _out/cmd/virt-chroot/virt-chroot %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virt-handler/virt-handler
install -p -m 0755 _out/cmd/virt-handler/virt-handler %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virt-launcher/virt-launcher
install -p -m 0755 _out/cmd/virt-launcher/virt-launcher %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/virt-operator/virt-operator
install -p -m 0755 _out/cmd/virt-operator/virt-operator %{buildroot}%{_bindir}/
chmod 0755 _out/cmd/csv-generator/csv-generator
install -p -m 0755 _out/cmd/csv-generator/csv-generator %{buildroot}%{_bindir}/


%files virtctl
%license LICENSE
%doc README.md
%{_bindir}/virtctl

%files virt-api
%license LICENSE
%doc README.md
%{_bindir}/virt-api

%files container-disk
%license LICENSE
%doc README.md
%{_bindir}/container-disk

%files virt-controller
%license LICENSE
%doc README.md
%{_bindir}/virt-controller

%files virt-handler
%license LICENSE
%doc README.md
%{_bindir}/virt-handler
%{_bindir}/virt-chroot

%files virt-launcher
%license LICENSE
%doc README.md
%{_bindir}/virt-launcher

%files virt-operator
%license LICENSE
%doc README.md
%{_bindir}/virt-operator
%{_bindir}/csv-generator

%changelog
