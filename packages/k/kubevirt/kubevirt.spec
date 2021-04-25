#
# spec file for package kubevirt
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


Name:           kubevirt
Version:        0.40.0
Release:        0
Summary:        Container native virtualization
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/kubevirt
Source0:        %{name}-%{version}.tar.gz
Source1:        kubevirt-psp-caasp.yaml
Source100:      %{name}-rpmlintrc
Patch0:         dont-build-virtctl-darwin.patch
Patch1:         dont-use-bazel-in-build-manifests.patch
Patch2:         fix-virsh-domcapabilities-error.patch
Patch3:         fix-double-free-of-VirDomain.patch
BuildRequires:  glibc-devel-static
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  golang(API) = 1.13
BuildRequires:  pkgconfig(libvirt)
ExclusiveArch:  x86_64

%description
Kubevirt is a virtual machine management add-on for Kubernetes

%package        virtctl
Summary:        Client for managing kubevirt
Group:          System/Packages

%description    virtctl
The virtctl client is a command-line utility for managing container native virtualization resources

%package        virt-api
Summary:        Kubevirt API server
Group:          System/Packages

%description    virt-api
The virt-api package provides the kubernetes API extension for kubevirt

%package        container-disk
Summary:        Container disk for kubevirt
Group:          System/Packages

%description    container-disk
The containter-disk package provides a container disk functionality for kubevirt

%package        virt-controller
Summary:        Controller for kubevirt
Group:          System/Packages

%description    virt-controller
The virt-controller package provides a controller for kubevirt

%package        virt-handler
Summary:        Handler component for kubevirt
Group:          System/Packages

%description    virt-handler
The virt-handler package provides a handler for kubevirt

%package        virt-launcher
Summary:        Launcher component for kubevirt
Group:          System/Packages

%description    virt-launcher
The virt-launcher package provides a launcher for kubevirt

%package        virt-operator
Summary:        Operator component for kubevirt
Group:          System/Packages

%description    virt-operator
The virt-opertor package provides an operator for kubevirt CRD

%package        manifests
Summary:        YAML manifests used to install kubevirt
Group:          System/Packages

%description    manifests
This contains the built YAML manifests used to install kubevirt into a
kubernetes installation with kubectl apply.

%package        tests
Summary:        Kubevirt functional tests
Group:          System/Packages

%description    tests
The package provides Kubevirt end-to-end tests.

%prep
%autosetup -p1

%build
# Hackery to determine which registry path to use in kubevirt-operator.yaml
# when building the manifests
#
# The 'registry_path' macro can be used to define an explicit path in the
# project config, e.g.
#
# Macros:
# %registry_path registry.opensuse.org/Virtualization/container
# :Macros
#
# 'registry_path' can also be defined when building locally, e.g.
#
# osc build --define='registry_path registry.opensuse.org/foo/bar/baz' ...
#
# If 'registry_path' is not specified, the standard publish location for SLE and
# openSUSE-based containers is used.
#
# TODO:
# 1. Determine "standard publish location" for SLE and openSUSE variants
# 2. Support Leap when 1 is done
#
%if "%{?registry_path}" == ""
distro='%{?sle_version}:%{is_opensuse}'
case "${distro}" in
    150200:0)
	reg_path='registry.suse.de/suse/containers/sle-server/15/containers/suse/sles/15.2' ;;
    150300:0)
	reg_path='registry.suse.de/suse/containers/sle-server/15/containers/suse/sles/15.3' ;;
    *)
	reg_path='registry.opensuse.org/virtualization/container/kubevirt' ;;
esac
%else
reg_path='%{registry_path}'
%endif

mkdir -p go/src/kubevirt.io go/pkg
ln -s ../../../ go/src/kubevirt.io/kubevirt
export GOPATH=${PWD}/go
export GOFLAGS="-buildmode=pie"
cd ${GOPATH}/src/kubevirt.io/kubevirt
env \
KUBEVIRT_GO_BASE_PKGDIR="${GOPATH}/pkg" \
KUBEVIRT_VERSION=%{version} \
KUBEVIRT_SOURCE_DATE_EPOCH="$(date -r LICENSE +%s)" \
KUBEVIRT_GIT_COMMIT='v%{version}' \
KUBEVIRT_GIT_VERSION='v%{version}' \
KUBEVIRT_GIT_TREE_STATE="clean" \
build_tests="true" \
./hack/build-go.sh install \
	cmd/virtctl \
	cmd/virt-api \
	cmd/virt-controller \
	cmd/virt-chroot \
	cmd/virt-handler \
	cmd/virt-launcher \
	cmd/virt-operator \
	%{nil}

env DOCKER_PREFIX=$reg_path DOCKER_TAG=%{version} ./hack/build-manifests.sh --skipj2

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 0755 _out/cmd/container-disk-v2alpha/container-disk %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virtctl/virtctl %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-api/virt-api %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-controller/virt-controller %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-chroot/virt-chroot %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-handler/virt-handler %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-launcher/virt-launcher %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-operator/virt-operator %{buildroot}%{_bindir}/
install -p -m 0755 _out/tests/tests.test %{buildroot}%{_bindir}/virt-tests

# node-labeller needs to be installed in /bin
mkdir -p %{buildroot}/bin
install -p -m 0755 cmd/virt-launcher/node-labeller/node-labeller.sh %{buildroot}/bin/

mkdir -p %{buildroot}%{_datadir}/kube-virt
cp -r _out/manifests %{buildroot}%{_datadir}/kube-virt/
# TODO:
# Create a proper Pod Security Policy (PSP) for KubeVirt. For now, add one
# that uses the CaaSP privileged PSP. It can be used with CaaSP-based
# Kubernetes clusters.
install -m 644 %{S:1} %{buildroot}/%{_datadir}/kube-virt/manifests/release/
install -m 0644 tests/default-config.json %{buildroot}%{_datadir}/kube-virt

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
/bin/node-labeller.sh

%files virt-operator
%license LICENSE
%doc README.md
%{_bindir}/virt-operator

%files manifests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%{_datadir}/kube-virt/manifests

%files tests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%{_bindir}/virt-tests
%{_datadir}/kube-virt/default-config.json

%changelog
