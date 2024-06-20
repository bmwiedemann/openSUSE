#
# spec file for package kubevirt
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


%if 0%{?sle_version} && !0%{?is_opensuse}
# SLE
%define _exclusive_arch x86_64
%else
%if 0%{?suse_version} == 1600
# ALP
%define _exclusive_arch x86_64
%else
# TW
%define _exclusive_arch x86_64 aarch64
%endif
%endif

Name:           kubevirt
Version:        1.2.2
Release:        0
Summary:        Container native virtualization
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/kubevirt
Source0:        %{name}-%{version}.tar.gz
Source1:        kubevirt_containers_meta
Source2:        kubevirt_containers_meta.service
Source3:        %{url}/releases/download/v%{version}/disks-images-provider.yaml
Source100:      %{name}-rpmlintrc
Patch1:         0001-Collect-component-Role-rules-under-operator-Role-ins.patch
BuildRequires:  glibc-devel-static
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  golang(API) >= 1.21
BuildRequires:  pkgconfig(libvirt)
ExclusiveArch:  %{_exclusive_arch}

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

%package        virt-exportproxy
Summary:        Export proxy for kubevirt
Group:          System/Packages

%description    virt-exportproxy
The virt-exportproxy package provides a proxy for kubevirt to pass
requests to virt-exportserver

%package        virt-exportserver
Summary:        Export server for kubevirt
Group:          System/Packages

%description    virt-exportserver
The virt-exportserver package provides an http server for kubevirt to
serve the data of VirtualMachineExport resource in different formats

%package        virt-handler
Summary:        Handler component for kubevirt
Group:          System/Packages

%description    virt-handler
The virt-handler package provides a handler for kubevirt

%package        virt-launcher
Summary:        Launcher component for kubevirt
Group:          System/Packages
# Starting from v1.1.0, KubeVirt ships /usr/bin/virt-tail which conflicts with
# the respective guestfs tool.
Conflicts:      guestfs-tools

%description    virt-launcher
The virt-launcher package provides a launcher for kubevirt

%package        virt-operator
Summary:        Operator component for kubevirt
Group:          System/Packages

%description    virt-operator
The virt-opertor package provides an operator for kubevirt CRD

%package        pr-helper-conf
Summary:        Configuration files for persistent reservation helper
Group:          System/Packages

%description    pr-helper-conf
The pr-helper-conf package provides configuration files for persistent
reservation helper

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

%package -n     obs-service-kubevirt_containers_meta
Summary:        Kubevirt containers meta information (build service)
Group:          System/Packages

%description -n obs-service-kubevirt_containers_meta
The package provides meta information that is used during the build of
the Kubevirt container images.

%prep
%autosetup -p1

%build
# Hackery to determine which registry path to use in kubevirt-operator.yaml
# when building the manifests
#
# The 'kubevirt_registry_path' macro can be used to define an explicit path in
# the project config, e.g.
#
# Macros:
# %kubevirt_registry_path registry.opensuse.org/Virtualization/container
# :Macros
#
# 'kubevirt_registry_path' can also be defined when building locally, e.g.
#
# osc build --define='kubevirt_registry_path registry.opensuse.org/foo/bar/baz' ...
#
# If 'kubevirt_registry_path' is not specified, the standard publish location
# for SLE and openSUSE-based containers is used.
#
distro='%{?sle_version}:%{?is_opensuse}%{!?is_opensuse:0}'
case "${distro}" in
150500:0)
    tagprefix=suse/sles/15.5
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
    ;;
150600:0)
    tagprefix=suse/sles/15.6
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
    ;;
*:1)
    tagprefix=kubevirt
    labelprefix=org.opensuse.kubevirt
    registry=registry.opensuse.org
    ;;
*)
%if 0%{?suse_version} == 1600
    tagprefix=alp/kubevirt
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
%else
    echo "Unsupported distro: ${distro}" >&2
    exit 1
%endif
    ;;
esac

%if "%{?kubevirt_registry_path}" == ""
    reg_path="${registry}/${tagprefix}"
%else
    reg_path='%{kubevirt_registry_path}'
%endif

sed -i"" \
    -e "s#_TAGPREFIX_#${tagprefix}#g" \
    -e "s#_LABELPREFIX_#${labelprefix}#g" \
    -e "s#_REGISTRY_#${registry}#g" \
    -e "s#_PKG_VERSION_#%{version}#g" \
    -e "s#_PKG_RELEASE_#%{release}#g" \
    -e "s#_DISTRO_#${distro}#g" \
    %{S:1}

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
    cmd/virt-api \
    cmd/virt-chroot \
    cmd/virt-controller \
    cmd/virt-exportproxy \
    cmd/virt-exportserver \
    cmd/virt-freezer \
    cmd/virt-handler \
    cmd/virt-launcher \
    cmd/virt-launcher-monitor \
    cmd/virt-operator \
    cmd/virt-probe \
    cmd/virt-tail \
    cmd/virtctl \
    %{nil}

env DOCKER_PREFIX=$reg_path DOCKER_TAG=%{version}-%{release} KUBEVIRT_NO_BAZEL=true ./hack/build-manifests.sh

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 0755 _out/cmd/container-disk-v2alpha/container-disk %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virtctl/virtctl %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-api/virt-api %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-controller/virt-controller %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-chroot/virt-chroot %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-exportproxy/virt-exportproxy %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-exportserver/virt-exportserver %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-handler/virt-handler %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-launcher/virt-launcher %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-launcher-monitor/virt-launcher-monitor %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-freezer/virt-freezer %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-probe/virt-probe %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-tail/virt-tail %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-operator/virt-operator %{buildroot}%{_bindir}/
install -p -m 0755 _out/tests/tests.test %{buildroot}%{_bindir}/virt-tests
install -p -m 0755 cmd/virt-launcher/node-labeller/node-labeller.sh %{buildroot}%{_bindir}/

# Install network stuff
mkdir -p %{buildroot}%{_datadir}/kube-virt/virt-handler
install -p -m 0644 cmd/virt-handler/nsswitch.conf %{buildroot}%{_datadir}/kube-virt/virt-handler/

# virt-launcher SELinux policy needs to land in virt-handler container
install -p -m 0644 cmd/virt-handler/virt_launcher.cil %{buildroot}%{_datadir}/kube-virt/virt-handler/

# Persistent reservation helper configuration files
mkdir -p %{buildroot}%{_datadir}/kube-virt/pr-helper
install -p -m 0644 cmd/pr-helper/multipath.conf %{buildroot}%{_datadir}/kube-virt/pr-helper/

# Configuration files for libvirt
mkdir -p %{buildroot}%{_datadir}/kube-virt/virt-launcher
install -p -m 0644 cmd/virt-launcher/virtqemud.conf %{buildroot}%{_datadir}/kube-virt/virt-launcher
install -p -m 0644 cmd/virt-launcher/qemu.conf %{buildroot}%{_datadir}/kube-virt/virt-launcher

# Install release manifests
mkdir -p %{buildroot}%{_datadir}/kube-virt/manifests/release
install -m 0644 _out/manifests/release/kubevirt-operator.yaml %{buildroot}%{_datadir}/kube-virt/manifests/release/
install -m 0644 _out/manifests/release/kubevirt-cr.yaml %{buildroot}%{_datadir}/kube-virt/manifests/release/

# Install manifests for testing
mkdir -p %{buildroot}%{_datadir}/kube-virt/manifests/testing
install -m 0644 _out/manifests/testing/* %{buildroot}%{_datadir}/kube-virt/manifests/testing/
# The generated disks-images-provider.yaml refers to nonexistent container
# images. Overwrite it with the upstream version for testing.
install -m 0644 %{S:3} %{buildroot}/%{_datadir}/kube-virt/manifests/testing/
install -m 0644 tests/default-config.json %{buildroot}%{_datadir}/kube-virt/manifests/testing/

# Install kubevirt_containers_meta build service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{S:1} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{S:2} %{buildroot}%{_prefix}/lib/obs/service

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

%files virt-exportproxy
%license LICENSE
%doc README.md
%{_bindir}/virt-exportproxy

%files virt-exportserver
%license LICENSE
%doc README.md
%{_bindir}/virt-exportserver

%files virt-handler
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%dir %{_datadir}/kube-virt/virt-handler
%{_bindir}/virt-handler
%{_bindir}/virt-chroot
%{_datadir}/kube-virt/virt-handler

%files virt-launcher
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%dir %{_datadir}/kube-virt/virt-launcher
%{_bindir}/virt-launcher
%{_bindir}/virt-launcher-monitor
%{_bindir}/virt-freezer
%{_bindir}/virt-probe
%{_bindir}/virt-tail
%{_bindir}/node-labeller.sh
%{_datadir}/kube-virt/virt-launcher

%files virt-operator
%license LICENSE
%doc README.md
%{_bindir}/virt-operator

%files pr-helper-conf
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%dir %{_datadir}/kube-virt/pr-helper
%{_datadir}/kube-virt/pr-helper

%files manifests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%dir %{_datadir}/kube-virt/manifests
%{_datadir}/kube-virt/manifests/release

%files tests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt
%dir %{_datadir}/kube-virt/manifests
%{_bindir}/virt-tests
%{_datadir}/kube-virt/manifests/testing

%files -n obs-service-kubevirt_containers_meta
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
