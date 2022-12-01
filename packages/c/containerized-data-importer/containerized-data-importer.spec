#
# spec file for package containerized-data-importer
#
# Copyright (c) 2022 SUSE LLC
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


Name:           containerized-data-importer
Version:        1.55.0
Release:        0
Summary:        Container native virtualization
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/containerized-data-importer
Source0:        %{name}-%{version}.tar.gz
Source1:        cdi_containers_meta
Source2:        cdi_containers_meta.service
Source100:      %{name}-rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  libnbd-devel
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sed
BuildRequires:  golang(API) = 1.18
ExclusiveArch:  x86_64 aarch64

%description
Containerized-Data-Importer (CDI) is a persistent storage management add-on for Kubernetes

%package        api
Summary:        CDI API server
Group:          System/Packages

%description    api
The containerized-data-importer-api package provides the kubernetes API extension for CDI

%package        cloner
Summary:        Cloner for host assisted cloning
Group:          System/Packages

%description    cloner
Source and Target cloner image for host assisted cloning

%package        controller
Summary:        Controller for the data fetching service
Group:          System/Packages

%description    controller
Controller for the data fetching service for VM container images

%package        importer
Summary:        Data fetching service
Group:          System/Packages

%description    importer
Data fetching service for VM container imagess

%package        operator
Summary:        Operator for the data fetching service
Group:          System/Packages

%description    operator
Operator for the data fetching service for VM container images

%package        uploadproxy
Summary:        Upload proxy for the data fetching service
Group:          System/Packages

%description    uploadproxy
Upload proxy for the data fetching service for VM container images

%package        uploadserver
Summary:        Upload server for the data fetching service
Group:          System/Packages

%description    uploadserver
Upload server for the data fetching service for VM container images

%package        manifests
Summary:        YAML manifests used to install CDI
Group:          System/Packages

%description    manifests
This contains the built YAML manifests used to install CDI into a
kubernetes installation with kubectl apply.

%package -n     obs-service-cdi_containers_meta
Summary:        CDI containers meta information (build service)
Group:          System/Packages

%description -n obs-service-cdi_containers_meta
The package provides meta information that is used during the build of
the CDI container images.

%prep
# Unpack the sources respecting the GOPATH directory structure expected by the
# go imports resolver. I.e. if DIR is in GOPATH then DIR/src/foo/bar can be
# imported as "foo/bar". The same 'visibility' rules apply to the local copies
# of external dependencies placed in 'vendor' directory when imported from the
# 'parent' package.
#
# Note: having bar symlink'ed to DIR/src/foo/bar does not seem to work. Looks
# like symlinks in go path are not resolved correctly. Hence the sources need
# to be 'physically' placed into the proper location.
%setup -n go/src/kubevirt.io/%{name} -c -T
tar --strip-components=1 -xf %{S:0}

%build
# Hackery to determine which registry path to use in cdi-operator.yaml
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
# If 'kubevirt_registry_path' is not specified, the standard publish location for
# SLE and openSUSE-based containers is used.
#
distro='%{?sle_version}:%{?is_opensuse}%{!?is_opensuse:0}'
case "${distro}" in
150200:0)
    tagprefix=suse/sles/15.2
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
    ;;
150300:0)
    tagprefix=suse/sles/15.3
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
    ;;
150400:0)
    tagprefix=suse/sles/15.4
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
    ;;
150500:0)
    tagprefix=suse/sles/15.5
    labelprefix=com.suse.kubevirt
    registry=registry.suse.com
    ;;
*:1)
    tagprefix=kubevirt
    labelprefix=org.opensuse.kubevirt
    registry=registry.opensuse.org
    ;;
*)
    echo "Unsupported distro: ${distro}" >&2
    exit 1
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

export GOPATH=%{_builddir}/go
export GOFLAGS="-mod=vendor"
export CDI_SOURCE_DATE_EPOCH="$(date -r LICENSE +%s)"
export CDI_GIT_COMMIT='v%{version}'
export CDI_GIT_VERSION='v%{version}'
export CDI_GIT_TREE_STATE="clean"

GOFLAGS="-buildmode=pie ${GOFLAGS}" ./hack/build/build-go.sh build \
    cmd/cdi-apiserver \
    cmd/cdi-cloner \
    cmd/cdi-controller \
    cmd/cdi-importer \
    cmd/cdi-uploadproxy \
    cmd/cdi-uploadserver \
    cmd/cdi-operator \
    tools/cdi-image-size-detection \
    tools/cdi-source-update-poller \
    %{nil}

# Disable cgo to build static binaries, so they can run on scratch images
CGO_ENABLED=0 ./hack/build/build-go.sh build \
    tools/cdi-containerimage-server \
    %{nil}

env DOCKER_PREFIX=$reg_path DOCKER_TAG=%{version}-%{release} ./hack/build/build-manifests.sh

%install
mkdir -p %{buildroot}%{_bindir}

install -p -m 0755 _out/cmd/cdi-apiserver/cdi-apiserver %{buildroot}%{_bindir}/virt-cdi-apiserver

install -p -m 0755 cmd/cdi-cloner/cloner_startup.sh %{buildroot}%{_bindir}/
install -p -m 0755 _out/cmd/cdi-cloner/cdi-cloner %{buildroot}%{_bindir}/

install -p -m 0755 _out/cmd/cdi-controller/cdi-controller %{buildroot}%{_bindir}/virt-cdi-controller

install -p -m 0755 _out/cmd/cdi-importer/cdi-importer %{buildroot}%{_bindir}/virt-cdi-importer
install -p -m 0755 _out/tools/cdi-containerimage-server/cdi-containerimage-server %{buildroot}%{_bindir}/
install -p -m 0755 _out/tools/cdi-image-size-detection/cdi-image-size-detection %{buildroot}%{_bindir}/
install -p -m 0755 _out/tools/cdi-source-update-poller/cdi-source-update-poller %{buildroot}%{_bindir}/

install -p -m 0755 _out/cmd/cdi-operator/cdi-operator %{buildroot}%{_bindir}/virt-cdi-operator

install -p -m 0755 _out/cmd/cdi-uploadproxy/cdi-uploadproxy %{buildroot}%{_bindir}/virt-cdi-uploadproxy

install -p -m 0755 _out/cmd/cdi-uploadserver/cdi-uploadserver %{buildroot}%{_bindir}/virt-cdi-uploadserver

# Install release manifests
mkdir -p %{buildroot}%{_datadir}/cdi/manifests/release
install -m 0644 _out/manifests/release/cdi-operator.yaml %{buildroot}%{_datadir}/cdi/manifests/release/
install -m 0644 _out/manifests/release/cdi-cr.yaml %{buildroot}%{_datadir}/cdi/manifests/release/

# Install cdi_containers_meta build service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{S:1} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{S:2} %{buildroot}%{_prefix}/lib/obs/service

%files api
%license LICENSE
%doc README.md
%{_bindir}/virt-cdi-apiserver

%files cloner
%license LICENSE
%doc README.md
%{_bindir}/cloner_startup.sh
%{_bindir}/cdi-cloner

%files controller
%license LICENSE
%doc README.md
%{_bindir}/virt-cdi-controller

%files importer
%license LICENSE
%doc README.md
%{_bindir}/virt-cdi-importer
%{_bindir}/cdi-containerimage-server
%{_bindir}/cdi-image-size-detection
%{_bindir}/cdi-source-update-poller

%files operator
%license LICENSE
%doc README.md
%{_bindir}/virt-cdi-operator

%files uploadproxy
%license LICENSE
%doc README.md
%{_bindir}/virt-cdi-uploadproxy

%files uploadserver
%license LICENSE
%doc README.md
%{_bindir}/virt-cdi-uploadserver

%files manifests
%license LICENSE
%doc README.md
%dir %{_datadir}/cdi
%{_datadir}/cdi/manifests

%files -n obs-service-cdi_containers_meta
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
