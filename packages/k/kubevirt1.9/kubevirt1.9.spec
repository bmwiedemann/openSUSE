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
Name:           kubevirt1.9
Version:        1.9.0
Release:        0
Summary:        Container native virtualization
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/kubevirt
Source0:        %{upstream_name}-%{version}.tar.gz
Source3:        %{url}/releases/download/v%{version}/disks-images-provider.yaml
Source100:      %{name}-rpmlintrc
BuildRequires:  glibc-devel-static
BuildRequires:  golang-packaging
BuildRequires:  libnbd-devel
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  golang(API) >= 1.26
BuildRequires:  pkgconfig(libvirt)
ExclusiveArch:  %{_exclusive_arch}

%description
Kubevirt is a virtual machine management add-on for Kubernetes

%package        virtctl
Summary:        Client for managing kubevirt
Group:          System/Packages
# every parallel minor provides and conflicts the unversioned
# name, so only one minor installs at a time
Provides:       kubevirt-virtctl = %{version}-%{release}
Conflicts:      kubevirt-virtctl

%description    virtctl
The virtctl client is a command-line utility for managing container native virtualization resources

%package        virt-api
Summary:        Kubevirt API server
Group:          System/Packages
Provides:       kubevirt-virt-api = %{version}-%{release}
Conflicts:      kubevirt-virt-api

%description    virt-api
The virt-api package provides the kubernetes API extension for kubevirt

%package        container-disk
Summary:        Container disk for kubevirt
Group:          System/Packages
Provides:       kubevirt-container-disk = %{version}-%{release}
Conflicts:      kubevirt-container-disk

%description    container-disk
The containter-disk package provides a container disk functionality for kubevirt

%package        virt-controller
Summary:        Controller for kubevirt
Group:          System/Packages
Provides:       kubevirt-virt-controller = %{version}-%{release}
Conflicts:      kubevirt-virt-controller

%description    virt-controller
The virt-controller package provides a controller for kubevirt

%package        virt-exportproxy
Summary:        Export proxy for kubevirt
Group:          System/Packages
Provides:       kubevirt-virt-exportproxy = %{version}-%{release}
Conflicts:      kubevirt-virt-exportproxy

%description    virt-exportproxy
The virt-exportproxy package provides a proxy for kubevirt to pass
requests to virt-exportserver

%package        virt-exportserver
Summary:        Export server for kubevirt
Group:          System/Packages
Provides:       kubevirt-virt-exportserver = %{version}-%{release}
Conflicts:      kubevirt-virt-exportserver

%description    virt-exportserver
The virt-exportserver package provides an http server for kubevirt to
serve the data of VirtualMachineExport resource in different formats

%package        virt-handler
Summary:        Handler component for kubevirt
Group:          System/Packages
Provides:       kubevirt-virt-handler = %{version}-%{release}
Conflicts:      kubevirt-virt-handler

%description    virt-handler
The virt-handler package provides a handler for kubevirt

%package        virt-launcher
Summary:        Launcher component for kubevirt
Group:          System/Packages
# Starting from v1.1.0, KubeVirt ships /usr/bin/virt-tail which conflicts with
# the respective guestfs tool.
Conflicts:      guestfs-tools
Provides:       kubevirt-virt-launcher = %{version}-%{release}
Conflicts:      kubevirt-virt-launcher

%description    virt-launcher
The virt-launcher package provides a launcher for kubevirt

%package        virt-operator
Summary:        Operator component for kubevirt
Group:          System/Packages
Provides:       kubevirt-virt-operator = %{version}-%{release}
Conflicts:      kubevirt-virt-operator

%description    virt-operator
The virt-opertor package provides an operator for kubevirt CRD

%package        virt-synchronization-controller
Summary:        Synchronization controller for kubevirt
Group:          System/Packages
Provides:       kubevirt-virt-synchronization-controller = %{version}-%{release}
Conflicts:      kubevirt-virt-synchronization-controller

%description    virt-synchronization-controller
The virt-synchronization-controller package provides a controller for
decentralized migration

%package        pr-helper-conf
Summary:        Configuration files for persistent reservation helper
Group:          System/Packages
Provides:       kubevirt-pr-helper-conf = %{version}-%{release}
Conflicts:      kubevirt-pr-helper-conf

%description    pr-helper-conf
The pr-helper-conf package provides configuration files for persistent
reservation helper

%package        sidecar-shim
Summary:        Entrypoint for the sidecar-shim container
Group:          System/Packages
Provides:       kubevirt-sidecar-shim = %{version}-%{release}
Conflicts:      kubevirt-sidecar-shim

%description    sidecar-shim
The package provides sidecar-shim binary than will call the respective
hooks with the proper command-line arguments.

%package        libguestfs-tools
Summary:        Contents of the libguestfs-tools container
Group:          System/Packages
# The runtime closure of the libguestfs-tools container image (the pod
# spawned by virtctl guestfs): the guestfs stack plus the filesystem
# tools offered inside the appliance. Mirrors the rpm tree upstream
# keeps in rpm/BUILD.bazel for its quay.io/kubevirt/libguestfs-tools.
Requires:       btrfsprogs
Requires:       cryptsetup
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       gptfdisk
Requires:       guestfs-tools
Requires:       jfsutils
Requires:       ldmtool
Requires:       libguestfs
Requires:       libguestfs-appliance
Requires:       libguestfs-winsupport
Requires:       mdadm
Requires:       parted
Requires:       qemu-tools
Requires:       supermin
Requires:       xfsprogs
Requires:       xorriso
%ifarch x86_64
Requires:       qemu-x86
%endif
%ifarch aarch64
Requires:       qemu-arm
Requires:       qemu-uefi-aarch64
Requires:       qemu-x86
%endif
Provides:       kubevirt-libguestfs-tools = %{version}-%{release}
Conflicts:      kubevirt-libguestfs-tools

%description    libguestfs-tools
The libguestfs-tools package provides the entrypoint script and the
runtime dependency closure of the libguestfs-tools container image
used by virtctl guestfs.

%if 0%{?suse_version} >= 1699
%package        manifests
Summary:        YAML manifests used to install kubevirt
Group:          System/Packages
Provides:       kubevirt-manifests = %{version}-%{release}
Conflicts:      kubevirt-manifests

%description    manifests
This contains the built YAML manifests used to install kubevirt into a
kubernetes installation with kubectl apply.
%endif

%package        tests
Summary:        Kubevirt functional tests
Group:          System/Packages
Provides:       kubevirt-tests = %{version}-%{release}
Conflicts:      kubevirt-tests

%description    tests
The package provides Kubevirt end-to-end tests.

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
    %if "%{?kubevirt_registry_path}" == ""
        reg_path="registry.opensuse.org/opensuse"
    %else
        reg_path='%{kubevirt_registry_path}'
    %endif
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
    cmd/virt-launcher/libvirt-hook-client \
    cmd/virt-launcher-monitor \
    cmd/virt-operator \
    cmd/virt-probe \
    cmd/synchronization-controller \
    cmd/virt-tail \
    cmd/virtctl \
    %{nil}

%if 0%{?suse_version} >= 1699
env DOCKER_PREFIX=$reg_path DOCKER_TAG=%{version} KUBEVIRT_NO_BAZEL=true ./hack/build-manifests.sh
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
install -p -m 0755 _out/cmd/libvirt-hook-client/libvirt-hook-client %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-launcher-monitor/virt-launcher-monitor %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-freezer/virt-freezer %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-probe/virt-probe %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/synchronization-controller/synchronization-controller %{buildroot}%{_bindir}/virt-synchronization-controller
install -p -m 0755 _out/cmd/virt-tail/virt-tail %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/virt-operator/virt-operator %{buildroot}%{_bindir}/
install -p -m 0755 _out/tests/tests.test %{buildroot}%{_bindir}/virt-tests
install -p -m 0755 cmd/virt-launcher/node-labeller/node-labeller.sh %{buildroot}%{_bindir}/

# Install network stuff
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.9/virt-handler
install -p -m 0644 cmd/virt-handler/nsswitch.conf %{buildroot}%{_datadir}/kube-virt-1.9/virt-handler/

# Persistent reservation helper configuration files
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.9/pr-helper
install -p -m 0644 cmd/pr-helper/multipath.conf %{buildroot}%{_datadir}/kube-virt-1.9/pr-helper/
# entrypoint.sh is the command virt-operator gives the pr-helper container
# (RenderPrHelperContainer); it symlinks the multipath socket before exec'ing
# qemu-pr-helper. Without it the container cannot start at all.
install -p -m 0755 cmd/pr-helper/entrypoint.sh %{buildroot}%{_datadir}/kube-virt-1.9/pr-helper/

# Entrypoint for the libguestfs-tools container
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.9/libguestfs-tools
install -p -m 0755 cmd/libguestfs/entrypoint.sh %{buildroot}%{_datadir}/kube-virt-1.9/libguestfs-tools/

# Configuration files for libvirt
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.9/virt-launcher
install -p -m 0644 cmd/virt-launcher/virtqemud.conf %{buildroot}%{_datadir}/kube-virt-1.9/virt-launcher
install -p -m 0644 cmd/virt-launcher/qemu.conf %{buildroot}%{_datadir}/kube-virt-1.9/virt-launcher

%if 0%{?suse_version} >= 1699
# Install release manifests
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.9/manifests/release
install -m 0644 _out/manifests/release/kubevirt-operator.yaml %{buildroot}%{_datadir}/kube-virt-1.9/manifests/release/
install -m 0644 _out/manifests/release/kubevirt-cr.yaml %{buildroot}%{_datadir}/kube-virt-1.9/manifests/release/

# Install manifests for testing
mkdir -p %{buildroot}%{_datadir}/kube-virt-1.9/manifests/testing
install -m 0644 _out/manifests/testing/* %{buildroot}%{_datadir}/kube-virt-1.9/manifests/testing/
# The generated disks-images-provider.yaml refers to nonexistent container
# images. Overwrite it with the upstream version for testing.
install -m 0644 %{S:3} %{buildroot}/%{_datadir}/kube-virt-1.9/manifests/testing/
install -m 0644 tests/default-config.json %{buildroot}%{_datadir}/kube-virt-1.9/manifests/testing/
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
%dir %{_datadir}/kube-virt-1.9
%{_bindir}/virt-handler
%{_bindir}/virt-chroot
%{_datadir}/kube-virt-1.9/virt-handler

%files virt-launcher
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.9
%{_bindir}/virt-launcher
%{_bindir}/virt-launcher-monitor
%{_bindir}/libvirt-hook-client
%{_bindir}/virt-freezer
%{_bindir}/virt-probe
%{_bindir}/virt-tail
%{_bindir}/node-labeller.sh
%{_datadir}/kube-virt-1.9/virt-launcher

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
%dir %{_datadir}/kube-virt-1.9
%{_datadir}/kube-virt-1.9/pr-helper

%files libguestfs-tools
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.9
%{_datadir}/kube-virt-1.9/libguestfs-tools

%files sidecar-shim
%license LICENSE
%doc cmd/sidecars/README.md
%{_bindir}/sidecar-shim

%if 0%{?suse_version} >= 1699
%files manifests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.9
%dir %{_datadir}/kube-virt-1.9/manifests
%{_datadir}/kube-virt-1.9/manifests/release
%endif

%files tests
%license LICENSE
%doc README.md
%dir %{_datadir}/kube-virt-1.9
%{_bindir}/virt-tests
%if 0%{?suse_version} >= 1699
%dir %{_datadir}/kube-virt-1.9/manifests
%{_datadir}/kube-virt-1.9/manifests/testing
%endif

%changelog
