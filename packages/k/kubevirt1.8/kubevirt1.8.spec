#
# spec file for package kubevirt
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _exclusive_arch x86_64 aarch64

%define upstream_name kubevirt
Name:           kubevirt1.8
Version:        1.8.4
Release:        0
Summary:        Container native virtualization
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/kubevirt
Source0:        %{upstream_name}-%{version}.tar.gz
Source1:        kubevirt1.8_containers_meta
Source2:        kubevirt1.8_containers_meta.service
Source3:        %{url}/releases/download/v%{version}/disks-images-provider.yaml
Source100:      %{name}-rpmlintrc
BuildRequires:  glibc-devel-static
BuildRequires:  golang-packaging
BuildRequires:  libnbd-devel
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  golang(API) >= 1.25
BuildRequires:  pkgconfig(libvirt)
ExclusiveArch:  %{_exclusive_arch}

%description
Kubevirt is a virtual machine management add-on for Kubernetes

%package        virtctl
Provides:       kubevirt-virtctl = %{version}-%{release}
Obsoletes:      kubevirt-virtctl < %{version}-%{release}
# Heritage: also Provides/Obsoletes the dashed kubevirt-1.8-* names that
# briefly shipped to Factory (2026-06) before the rename to kubevirt1.8-*.
Provides:       kubevirt-1.8-virtctl = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virtctl < %{version}-%{release}
Summary:        Client for managing kubevirt
Group:          System/Packages

%description    virtctl
The virtctl client is a command-line utility for managing container native virtualization resources

%package        virt-api
Provides:       kubevirt-virt-api = %{version}-%{release}
Obsoletes:      kubevirt-virt-api < %{version}-%{release}
Provides:       kubevirt-1.8-virt-api = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-api < %{version}-%{release}
Summary:        Kubevirt API server
Group:          System/Packages

%description    virt-api
The virt-api package provides the kubernetes API extension for kubevirt

%package        container-disk
Provides:       kubevirt-container-disk = %{version}-%{release}
Obsoletes:      kubevirt-container-disk < %{version}-%{release}
Provides:       kubevirt-1.8-container-disk = %{version}-%{release}
Obsoletes:      kubevirt-1.8-container-disk < %{version}-%{release}
Summary:        Container disk for kubevirt
Group:          System/Packages

%description    container-disk
The containter-disk package provides a container disk functionality for kubevirt

%package        virt-controller
Provides:       kubevirt-virt-controller = %{version}-%{release}
Obsoletes:      kubevirt-virt-controller < %{version}-%{release}
Provides:       kubevirt-1.8-virt-controller = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-controller < %{version}-%{release}
Summary:        Controller for kubevirt
Group:          System/Packages

%description    virt-controller
The virt-controller package provides a controller for kubevirt

%package        virt-exportproxy
Provides:       kubevirt-virt-exportproxy = %{version}-%{release}
Obsoletes:      kubevirt-virt-exportproxy < %{version}-%{release}
Provides:       kubevirt-1.8-virt-exportproxy = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-exportproxy < %{version}-%{release}
Summary:        Export proxy for kubevirt
Group:          System/Packages

%description    virt-exportproxy
The virt-exportproxy package provides a proxy for kubevirt to pass
requests to virt-exportserver

%package        virt-exportserver
Provides:       kubevirt-virt-exportserver = %{version}-%{release}
Obsoletes:      kubevirt-virt-exportserver < %{version}-%{release}
Provides:       kubevirt-1.8-virt-exportserver = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-exportserver < %{version}-%{release}
Summary:        Export server for kubevirt
Group:          System/Packages

%description    virt-exportserver
The virt-exportserver package provides an http server for kubevirt to
serve the data of VirtualMachineExport resource in different formats

%package        virt-handler
Provides:       kubevirt-virt-handler = %{version}-%{release}
Obsoletes:      kubevirt-virt-handler < %{version}-%{release}
Provides:       kubevirt-1.8-virt-handler = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-handler < %{version}-%{release}
Summary:        Handler component for kubevirt
Group:          System/Packages

%description    virt-handler
The virt-handler package provides a handler for kubevirt

%package        virt-launcher
Provides:       kubevirt-virt-launcher = %{version}-%{release}
Obsoletes:      kubevirt-virt-launcher < %{version}-%{release}
Provides:       kubevirt-1.8-virt-launcher = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-launcher < %{version}-%{release}
Summary:        Launcher component for kubevirt
Group:          System/Packages
# Starting from v1.1.0, KubeVirt ships /usr/bin/virt-tail which conflicts with
# the respective guestfs tool.
Conflicts:      guestfs-tools

%description    virt-launcher
The virt-launcher package provides a launcher for kubevirt

%package        virt-operator
Provides:       kubevirt-virt-operator = %{version}-%{release}
Obsoletes:      kubevirt-virt-operator < %{version}-%{release}
Provides:       kubevirt-1.8-virt-operator = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-operator < %{version}-%{release}
Summary:        Operator component for kubevirt
Group:          System/Packages

%description    virt-operator
The virt-opertor package provides an operator for kubevirt CRD

%package        virt-synchronization-controller
Provides:       kubevirt-virt-synchronization-controller = %{version}-%{release}
Obsoletes:      kubevirt-virt-synchronization-controller < %{version}-%{release}
Provides:       kubevirt-1.8-virt-synchronization-controller = %{version}-%{release}
Obsoletes:      kubevirt-1.8-virt-synchronization-controller < %{version}-%{release}
Summary:        Synchronization controller for kubevirt
Group:          System/Packages

%description    virt-synchronization-controller
The virt-synchronization-controller package provides a controller for
decentralized migration

%package        pr-helper-conf
Provides:       kubevirt-pr-helper-conf = %{version}-%{release}
Obsoletes:      kubevirt-pr-helper-conf < %{version}-%{release}
Provides:       kubevirt-1.8-pr-helper-conf = %{version}-%{release}
Obsoletes:      kubevirt-1.8-pr-helper-conf < %{version}-%{release}
Summary:        Configuration files for persistent reservation helper
Group:          System/Packages

%description    pr-helper-conf
The pr-helper-conf package provides configuration files for persistent
reservation helper

%package        sidecar-shim
Provides:       kubevirt-sidecar-shim = %{version}-%{release}
Obsoletes:      kubevirt-sidecar-shim < %{version}-%{release}
Provides:       kubevirt-1.8-sidecar-shim = %{version}-%{release}
Obsoletes:      kubevirt-1.8-sidecar-shim < %{version}-%{release}
Summary:        Entrypoint for the sidecar-shim container
Group:          System/Packages

%description    sidecar-shim
The package provides sidecar-shim binary than will call the respective
hooks with the proper command-line arguments.

%if 0%{?suse_version} >= 1699
%package        manifests
Provides:       kubevirt-manifests = %{version}-%{release}
Obsoletes:      kubevirt-manifests < %{version}-%{release}
Provides:       kubevirt-1.8-manifests = %{version}-%{release}
Obsoletes:      kubevirt-1.8-manifests < %{version}-%{release}
Summary:        YAML manifests used to install kubevirt
Group:          System/Packages

%description    manifests
This contains the built YAML manifests used to install kubevirt into a
kubernetes installation with kubectl apply.
%endif

%package        tests
Provides:       kubevirt-tests = %{version}-%{release}
Obsoletes:      kubevirt-tests < %{version}-%{release}
Provides:       kubevirt-1.8-tests = %{version}-%{release}
Obsoletes:      kubevirt-1.8-tests < %{version}-%{release}
Summary:        Kubevirt functional tests
Group:          System/Packages

%description    tests
The package provides Kubevirt end-to-end tests.

%if 0%{?suse_version} >= 1699
%package -n     obs-service-kubevirt1.8_containers_meta
Provides:       obs-service-kubevirt_containers_meta = %{version}-%{release}
Obsoletes:      obs-service-kubevirt_containers_meta < %{version}-%{release}
Provides:       obs-service-kubevirt-1.8_containers_meta = %{version}-%{release}
Obsoletes:      obs-service-kubevirt-1.8_containers_meta < %{version}-%{release}
Summary:        Kubevirt containers meta information (build service)
Group:          System/Packages

%description -n obs-service-kubevirt1.8_containers_meta
The package provides meta information that is used during the build of
the Kubevirt container images.
%endif

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
# For SLES 16.x, the registry path of the various kubevirt containers is
# handled by the BCI build machinery.
#
# For Tumbleweed, the 'kubevirt_registry_path' macro can be used to define
# an explicit path in the project config, e.g.
#
# Macros:
# %%kubevirt_registry_path registry.opensuse.org/Virtualization/container
# :Macros
#
# 'kubevirt_registry_path' can also be defined when building locally, e.g.
#
# osc build --define='kubevirt_registry_path registry.opensuse.org/foo/bar/baz' ...
#
# If 'kubevirt_registry_path' is not specified, the standard publish location
# for Tumbleweed-based containers is used.
#
%if 0%{?suse_version} >= 1699
    tagprefix=kubevirt
    labelprefix=org.opensuse.kubevirt
    registry=registry.opensuse.org

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
        -e "s#_DISTRO_#tumbleweed#g" \
        %{S:1}
%endif

mkdir -p go/src/kubevirt.io go/pkg
ln -s ../../../ go/src/kubevirt.io/kubevirt
export GOPATH=${PWD}/go
export GOFLAGS="-buildmode=pie"
# debugedit complains.
export GOEXPERIMENT=nodwarf5
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
    cmd/sidecars \
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
    cmd/synchronization-controller \
    cmd/virt-tail \
    cmd/virtctl \
    %{nil}

%if 0%{?suse_version} >= 1699
env DOCKER_PREFIX=$reg_path DOCKER_TAG=%{version}-%{release} KUBEVIRT_NO_BAZEL=true ./hack/build-manifests.sh
%endif

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 0755 _out/cmd/container-disk-v2alpha/container-disk %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/sidecars/sidecars %{buildroot}%{_bindir}/sidecar-shim
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
install -p -m 0755 _out/cmd/synchronization-controller/synchronization-controller %{buildroot}%{_bindir}/virt-synchronization-controller
install -p -m 0755 _out/cmd/virt-tail/virt-tail %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-operator/virt-operator %{buildroot}%{_bindir}/
install -p -m 0755 _out/tests/tests.test %{buildroot}%{_bindir}/virt-tests
install -p -m 0755 cmd/virt-launcher/node-labeller/node-labeller.sh %{buildroot}%{_bindir}/

# Install network stuff
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.8/virt-handler
install -p -m 0644 cmd/virt-handler/nsswitch.conf %{buildroot}%{_datadir}/kube-virt-1.8/virt-handler/

# Persistent reservation helper configuration files
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.8/pr-helper
install -p -m 0644 cmd/pr-helper/multipath.conf %{buildroot}%{_datadir}/kube-virt-1.8/pr-helper/

# Configuration files for libvirt
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.8/virt-launcher
install -p -m 0644 cmd/virt-launcher/virtqemud.conf %{buildroot}%{_datadir}/kube-virt-1.8/virt-launcher
install -p -m 0644 cmd/virt-launcher/qemu.conf %{buildroot}%{_datadir}/kube-virt-1.8/virt-launcher

%if 0%{?suse_version} >= 1699
# Install release manifests
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.8/manifests/release
install -m 0644 _out/manifests/release/kubevirt-operator.yaml %{buildroot}%{_datadir}/kube-virt-1.8/manifests/release/
install -m 0644 _out/manifests/release/kubevirt-cr.yaml %{buildroot}%{_datadir}/kube-virt-1.8/manifests/release/

# Install manifests for testing
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.8/manifests/testing
install -m 0644 _out/manifests/testing/* %{buildroot}%{_datadir}/kube-virt-1.8/manifests/testing/
# The generated disks-images-provider.yaml refers to nonexistent container
# images. Overwrite it with the upstream version for testing.
install -m 0644 %{S:3} %{buildroot}/%{_datadir}/kube-virt-1.8/manifests/testing/
install -m 0644 tests/default-config.json %{buildroot}%{_datadir}/kube-virt-1.8/manifests/testing/

# Install kubevirt_containers_meta build service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{S:1} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{S:2} %{buildroot}%{_prefix}/lib/obs/service
%endif

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
%dir %{_datadir}/kube-virt-1.8
%{_bindir}/virt-handler
%{_bindir}/virt-chroot
%{_datadir}/kube-virt-1.8/virt-handler

%files virt-launcher
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.8
%{_bindir}/virt-launcher
%{_bindir}/virt-launcher-monitor
%{_bindir}/virt-freezer
%{_bindir}/virt-probe
%{_bindir}/virt-tail
%{_bindir}/node-labeller.sh
%{_datadir}/kube-virt-1.8/virt-launcher

%files virt-operator
%license LICENSE
%doc README.md
%{_bindir}/virt-operator

%files virt-synchronization-controller
%license LICENSE
%doc README.md
%{_bindir}/virt-synchronization-controller

%files pr-helper-conf
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.8
%{_datadir}/kube-virt-1.8/pr-helper

%files sidecar-shim
%license LICENSE
%doc cmd/sidecars/README.md
%{_bindir}/sidecar-shim

%if 0%{?suse_version} >= 1699
%files manifests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.8
%dir %{_datadir}/kube-virt-1.8/manifests
%{_datadir}/kube-virt-1.8/manifests/release
%endif

%files tests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.8
%{_bindir}/virt-tests
%if 0%{?suse_version} >= 1699
%dir %{_datadir}/kube-virt-1.8/manifests
%{_datadir}/kube-virt-1.8/manifests/testing
%endif

%if 0%{?suse_version} >= 1699
%files -n obs-service-kubevirt1.8_containers_meta
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%endif

%changelog
