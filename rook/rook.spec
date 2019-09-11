#
# spec file for package rook
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rook
Version:        1.0.0+git1862.ge9abbf48
Release:        0
Summary:        Orchestrator for distributed storage systems in cloud-native environments
License:        Apache-2.0
Group:          System/Filesystems
Url:            https://rook.io/

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{version}-vendor.tar.xz
Source98:       README
Source99:       update-tarball.sh
%if 0%{?suse_version}
# _insert_obs_source_lines_here
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le
%endif

# Go and spec requirements
BuildRequires:  go
BuildRequires:  golang-packaging
BuildRequires:  xz

# Rook requirements
BuildRequires:  curl
BuildRequires:  git

# Ceph version is needed to set correct container tag in manifests
BuildRequires:  ceph
# ceph-csi driver version is needed to update manifest with it
BuildRequires:  ceph-csi

# Rook runtime requirements - referenced from packages installed in Rook images
# From images/ceph/Dockerfile
Requires:       tini
# From Ceph base container: github.com/ceph/ceph-container/src/daemon-base/...
Requires:       pattern() = ceph_base

%description
Rook is an open source cloud-native storage orchestrator for Kubernetes,
providing the platform, framework, and support for a diverse set of storage
solutions to natively integrate with cloud-native environments.

See https://github.com/rook/rook for more information.

################################################################################
# Rook FlexVolume driver metadata
################################################################################
%package rookflex
Summary:        Rook FlexVolume driver
Group:          System/Filesystems

%description rookflex
Rook uses FlexVolume to integrate with Kubernetes for performing storage
operations.

################################################################################
# Rook and Ceph manifests metadata
################################################################################
%package k8s-yaml
Summary:        Kubernetes YAML file manifests for deploying a Ceph cluster
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml files requried deploy and run the
Rook-Ceph operator and Ceph clusters in a Kubernetes cluster.

################################################################################
# Rook integration test binary metadata
################################################################################
%package integration
Summary:        Application which runs Rook integration tests
Group:          System/Benchmark

%description integration
This package is intended to be used only for testing. Please don't install in 
production.

Rook's integration tests conveniently get built into a standalone binary. The
tests require a running Kubernetes cluster, and the image being tested must be
pushed to all Kubernetes cluster nodes as 'rook/ceph:master'. They also require
that 'kubectl' works without additional connection arguments from the system
which will run the binary. The integration tests can be flaky and are best run
on a Kubernetes cluster which has not previously run the integration tests.

The list of possible integration test suites can be gotten from the integration
binary with the argument [-test.list '.*']. A subset of test suites can be run
by specifying a regular expression (or a specific test suite name) as an
argument to [-test.run]. All Ceph test suites can be run with the argument
[-test.run 'TestCeph'].

################################################################################
# The tasty, meaty build section
################################################################################
%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}
%setup -q -n %{name} -T -D -b 1 # unpack Source1, don't delete what was unpacked before

%build

#we need to remove unsupported by Rook symbols from version
version_parsed=%{version}

linker_flags=("-X" "github.com/rook/rook/pkg/version.Version=${version_parsed//[+]/-}")
build_flags=("-ldflags" "${linker_flags[*]}")

%goprep github.com/rook/rook
%gobuild "${build_flags[@]}" cmd/rook
%gobuild "${build_flags[@]}" cmd/rookflex

# BUILDING TEST BINARIES, NOTES:
# Building test binaries works differently than main binaries; test binaries are built by 'go test',
#     not 'go build' or 'go install'.
# Spec build tooling provides 'gotest', but it expects to run the tests, which we cannot do with
#     the integration tests at build time, so we run this manually. This may be fragile.
# To compile but not run test binaries, we don't need the build flags needed by main binaries, but
#     we do need: -c (compile test binary) and -o=<output-location> (output file)
# 'goprep' does not set GOTPATH or GOBIN despite what the documentation might say; that is set in
#     'gobuild', so we need to set it for our manual run of 'go test'.
# Because this is a test binary which we SHOULD NOT ship to customers, we shouldn't need to follow
#     every single go build best practice, and we don't need to worry about this becoming too out of
#     date. We can specify some important flags for debugging bad builds:
#         -v (orint package names), -x (print commands)]
#    and flags to get rid of RPMLINT report warnings/errors:
#         -buildmode=pie (position-independent executable)
GOPATH=%{_builddir}/go GOBIN="${GOPATH}"/bin \
    go test -v -x -buildmode=pie -c \
        -o %{_builddir}/go/bin/rook-integration github.com/rook/rook/tests/integration

%install
rook_bin_location=%{_builddir}/go/bin/
install_location=%{buildroot}%{_bindir}

install --mode=755 --directory "${install_location}"

for binary in rook rookflex rook-integration; do
    install --preserve-timestamps --mode=755 \
        --target-directory="${install_location}" \
        "${rook_bin_location}"/"${binary}"
done

# install Rook's toolbox script alongside main binary
install --preserve-timestamps --mode=755 \
    --target-directory="${install_location}" \
    images/ceph/toolbox.sh

# Install provided yaml files to download and run the Rook operator and Ceph containers
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/rook/ceph
cp -pr cluster/examples/kubernetes/ceph/* %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/

################################################################################
# Update manifests with images coming from Build Service
################################################################################
rook_container_version='1.0.0.1862'  # this is udpated by update-tarball.sh

# determine image names to use in manifests depending on the base os type
# %CEPH_VERSION% is replaced at build time by the _service
%if 0%{?is_opensuse}
rook_image=registry.opensuse.org/opensuse/rook/ceph:${rook_container_version}
ceph_image=registry.opensuse.org/opensuse/ceph/ceph:%CEPH_VERSION%
ceph_csi_image=registry.opensuse.org/opensuse/cephcsi/cephcsi:%CSI_VERSION%.%CSI_OFFSET%
%else # is SES
rook_image=registry.suse.com/ses/6/rook/ceph:${rook_container_version}
ceph_image=registry.suse.com/ses/6/ceph/ceph:%CEPH_VERSION%
ceph_csi_image=registry.suse.com/ses/6/cephcsi/cephcsi:%CSI_VERSION%.%CSI_OFFSET%
%endif

# set rook, ceph and ceph-csi container versions
sed -i -e "s|image: .*|image: ${rook_image}|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/operator*
sed -i -e "s|\".*/cephcsi/cephcsi:.*|\"${ceph_csi_image}\"|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/operator*
sed -i -e "s|image: .*|image: ${ceph_image}|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/cluster*
sed -i -e "s|image: .*|image: ${rook_image}|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/toolbox*
sed -i -e "s|/usr/local/bin/toolbox.sh|%{_bindir}/toolbox.sh|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/toolbox*

# For the integration test tooling, store files with the current Rook and Ceph image names
# These files can be cat'ed to get these without needing to do special processing
%define rook_integration_dir %{buildroot}%{_datadir}/rook-integration
mkdir -p %{rook_integration_dir}
echo -n ${rook_image}     > %{rook_integration_dir}/rook-image-name
echo -n ${ceph_image}     > %{rook_integration_dir}/ceph-image-name
echo -n ${ceph_csi_image} > %{rook_integration_dir}/ceph-csi-image-name
ls %{rook_integration_dir}

################################################################################
# Specify which files we built belong to each package
################################################################################
# rook-version-build.arch.rpm
%files
%defattr(-,root,root,-)
%{_bindir}/rook
%{_bindir}/toolbox.sh

# rook-rookflex-version-build.arch.rpm
%files rookflex
%{_bindir}/rookflex

# rook-k8s-yaml-version-build.arch.rpm
%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/rook
%dir %{_datarootdir}/k8s-yaml/rook/ceph
%{_datadir}/k8s-yaml/rook/ceph/

# rook-integration-version-build.arch.rpm
%files integration
# integration test binary
%{_bindir}/rook-integration
# integration test helper files
%dir %{_datarootdir}/rook-integration
%{_datadir}/rook-integration

################################################################################
# Finalize
################################################################################

# Rook RPMs aren't for users to install, just to be put in containers, so don't
# bother adding docs or changelog or anything

%changelog
