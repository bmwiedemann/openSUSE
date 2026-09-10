#
# spec file for package virt-template0.2
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


%define upstream_name virt-template
Name:           virt-template0.2
Version:        0.2.2
Release:        0
Summary:        Virtual machine templates add-on for KubeVirt
License:        Apache-2.0
Group:          System/Packages
URL:            https://github.com/kubevirt/virt-template
# Upstream release tarball rebuilt with re-vendored Go dependencies
# (go.mod/go.sum/vendor only, no source changes); see the changelog.
Source0:        %{upstream_name}-%{version}.tar.gz
Source100:      %{name}-rpmlintrc
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.26
ExclusiveArch:  x86_64 aarch64

%description
virt-template is a KubeVirt add-on that provides native, user-friendly
templating workflows for KubeVirt virtual machines: VirtualMachineTemplate
resources, an aggregated API server that processes them and a controller
that reconciles them. virt-operator deploys the two components when the
Template feature gate is enabled.

This package ships the 0.2 minor of virt-template, the release pinned by
KubeVirt 1.9.

%package        apiserver
Summary:        Aggregated API server for KubeVirt virtual machine templates
Group:          System/Packages
# every parallel minor provides and conflicts the unversioned
# name, so only one minor installs at a time
Provides:       virt-template-apiserver = %{version}-%{release}
Conflicts:      virt-template-apiserver

%description    apiserver
The aggregated API server that serves the template.kubevirt.io API group
and processes VirtualMachineTemplate resources into virtual machines.

%package        controller
Summary:        Controller for KubeVirt virtual machine templates
Group:          System/Packages
Provides:       virt-template-controller = %{version}-%{release}
Conflicts:      virt-template-controller

%description    controller
The controller that reconciles VirtualMachineTemplate resources and their
validating webhooks.

%package        tests
Summary:        Functional test suite for virt-template
Group:          System/Packages
Provides:       virt-template-tests = %{version}-%{release}
Conflicts:      virt-template-tests

%description    tests
The compiled ginkgo functional test suite of virt-template. It runs against
a cluster where KubeVirt and virt-template are deployed (KUBECONFIG).

%prep
%setup -q -n %{upstream_name}-%{version}

%build
# hack/ldflags.sh embeds the version from _out/version, which upstream
# generates from git metadata the release tarball does not carry.
mkdir -p _out
cat > _out/version <<VERSION
KUBE_GIT_COMMIT=v%{version}
KUBE_GIT_TREE_STATE=clean
KUBE_GIT_VERSION=v%{version}
KUBE_GIT_MAJOR=0
KUBE_GIT_MINOR=2
VERSION

export GOFLAGS="-mod=vendor"
export GOPROXY=off
export GOTOOLCHAIN=local
# static binaries: the container images run them on a minimal base
export CGO_ENABLED=0

go build -buildmode=pie -trimpath -ldflags "$(hack/ldflags.sh)" \
    -o _out/virt-template-apiserver ./cmd/apiserver
go build -buildmode=pie -trimpath -ldflags "$(hack/ldflags.sh)" \
    -o _out/virt-template-controller ./cmd

# compiled functional suite (-tests subpackage), run from a test-runner
# container against a live cluster like CDI's cdi-tests
go test -c -buildmode=pie -trimpath -o _out/virt-template-tests ./tests/

%install
install -D -p -m 0755 _out/virt-template-apiserver %{buildroot}%{_bindir}/virt-template-apiserver
install -D -p -m 0755 _out/virt-template-controller %{buildroot}%{_bindir}/virt-template-controller
install -D -p -m 0755 _out/virt-template-tests %{buildroot}%{_bindir}/virt-template-tests

%check
export GOFLAGS="-mod=vendor"
export GOPROXY=off
export GOTOOLCHAIN=local
export CGO_ENABLED=0
go vet ./cmd/... ./internal/... ./api/...
# The controller and webhook suites need envtest (a kube-apiserver
# binary) and are excluded; everything else runs.
go test ./internal/apimachinery/... ./internal/apiserver/... \
    ./staging/src/kubevirt.io/virt-template-engine/...

%files apiserver
%license LICENSE
%doc README.md
%{_bindir}/virt-template-apiserver

%files controller
%license LICENSE
%doc README.md
%{_bindir}/virt-template-controller

%files tests
%license LICENSE
%{_bindir}/virt-template-tests

%changelog
