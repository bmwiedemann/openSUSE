#
# spec file for package rook
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


Name:           rook
Version:        1.4.5+git5.ge3c837f8
Release:        0
Summary:        Orchestrator for distributed storage systems in cloud-native environments
License:        Apache-2.0
Group:          System/Filesystems
URL:            https://rook.io/

Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source97:       SUSE-helm-notes.txt
Source98:       README
Source99:       update-tarball.sh

# When possible, a patch is preferred over link-time overrides because the patch will fail if the
# upstream source is updated without the package maintainers knowing. Patches reduce user error when
# creating a new SUSE release branch of Rook.

# Change CSI images to SUSE specific values.
Patch0:         csi-images-SUSE.patch
# Change the default FlexVolume dir path to support Kubic.
Patch1:         flexvolume-dir.patch

%if 0%{?suse_version}
# _insert_obs_source_lines_here
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le
%endif

# Go and spec requirements
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.14

# Rook requirements
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  grep

# Ceph version is needed to set correct container tag in manifests
BuildRequires:  ceph
# ceph-csi and sidecars are needed to update versions in manifest/chart
BuildRequires:  ceph-csi
BuildRequires:  csi-external-attacher
BuildRequires:  csi-external-provisioner
BuildRequires:  csi-external-resizer
BuildRequires:  csi-external-snapshotter
BuildRequires:  csi-node-driver-registrar

# Rook runtime requirements - referenced from packages installed in Rook images
# From images/ceph/Dockerfile
Requires:       tini
# From Ceph base container: github.com/ceph/ceph-container/src/daemon-base/...
Requires:       pattern() = ceph_base

%description
Rook is a cloud-native storage orchestrator for Kubernetes, providing
the platform, framework, and support for a diverse set of storage
solutions to integrate with cloud-native environments.

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
BuildRequires:  ceph

%description k8s-yaml
This package contains examples of yaml files required to deploy and run the
Rook-Ceph operator and Ceph clusters in a Kubernetes cluster.

################################################################################
# Rook ceph operator helm charts
################################################################################
%package ceph-helm-charts
Summary:        Rook Ceph operator helm charts
Group:          System/Management
BuildArch:      noarch

%description ceph-helm-charts
Helm helps manage Kubernetes applications. Helm Charts define,
install, and upgrade Kubernetes applications. Rook is a
cloud-native storage orchestrator for Kubernetes, providing
the platform, framework, and support for a diverse set of storage
solutions to integrate with cloud-native environments.

This package contains Helm Charts for Rook.

################################################################################
# Rook integration test binary metadata
################################################################################
%package integration
Summary:        Application which runs Rook integration tests
Group:          System/Benchmark

%description integration
This package is intended to be used only for testing. Please don't install it
in production environments.

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
%define _buildshell /bin/bash

%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}
tar zxf %{SOURCE1}

%patch0 -p1
%patch1 -p1

# determine image names to use in manifests depending on the base os type
# %CEPH_VERSION%, and all CSI sidecar versions are replaced at build time by _service
%global rook_container_version 1.4.5.5  # this is updated by update-tarball.sh
%if 0%{?is_opensuse}
%define registry registry.opensuse.org/opensuse
%else # is SES
%if 0%{?sle_version} >= 150200
%define registry registry.suse.com/ses/7
%else
%define registry registry.suse.com/ses/6
%endif
%endif

%define spec_go pkg/operator/ceph/csi/spec.go
%define chart_yaml cluster/charts/rook-ceph/Chart.yaml
%define values_yaml cluster/charts/rook-ceph/values.yaml
sed -i -e "s|\(.*\)SUSE_REGISTRY\(.*\)|\1%{registry}\2|" %{spec_go}
sed -i -e "s|\(.*\)SUSE_REGISTRY\(.*\)|\1%{registry}\2|" %{chart_yaml}
sed -i -e "s|\(.*\)SUSE_REGISTRY\(.*\)|\1%{registry}\2|" %{values_yaml}

%global rook_image       %{registry}/rook/ceph:%{rook_container_version}.%{release}
%global ceph_image       %{registry}/ceph/ceph:%CEPH_VERSION%
%global ceph_csi_image   %{registry}/cephcsi/cephcsi:v%CSI_VERSION%.%CSI_OFFSET%
%global csi_reg_image    %{registry}/cephcsi/csi-node-driver-registrar:v%CSI_REG_VERSION%
%global csi_prov_image   %{registry}/cephcsi/csi-provisioner:v%CSI_PROV_VERSION%
%global csi_attach_image %{registry}/cephcsi/csi-attacher:v%CSI_ATTACH_VERSION%
%global csi_snap_image   %{registry}/cephcsi/csi-snapshotter:v%CSI_SNAP_VERSION%
%global csi_resize_image %{registry}/cephcsi/csi-resizer:v%CSI_RESIZE_VERSION%

%build

# remove symbols unsupported by k8s (+) from version
version_full=%{version}
version_noplus="${version_full//[+]/_}"
%global version_parsed "${version_noplus}-%{release}"

linker_flags=(
    # Set Rook version - absolutely required
    "-X" "github.com/rook/rook/pkg/version.Version=%{version_parsed}"
    # CSI images only known at build time, so use a linker flag instead of patch
    # NOTE - This currently doesn't seem to work without also patching spec.go
    "-X" "github.com/rook/rook/pkg/operator/ceph/csi.DefaultCSIPluginImage=%{ceph_csi_image}"
    "-X" "github.com/rook/rook/pkg/operator/ceph/csi.DefaultRegistrarImage=%{csi_reg_image}"
    "-X" "github.com/rook/rook/pkg/operator/ceph/csi.DefaultProvisionerImage=%{csi_prov_image}"
    "-X" "github.com/rook/rook/pkg/operator/ceph/csi.DefaultAttacherImage=%{csi_attach_image}"
    "-X" "github.com/rook/rook/pkg/operator/ceph/csi.DefaultSnapshotterImage=%{csi_snap_image}"
    "-X" "github.com/rook/rook/pkg/operator/ceph/csi.DefaultResizerImage=%{csi_resize_image}"
)
build_flags=("-ldflags" "${linker_flags[*]}" "-mod=vendor")

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
    go test -v -x -buildmode=pie -c -mod=vendor\
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

# Install ALL sample yaml files
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/rook/ceph
cp -pr cluster/examples/kubernetes/ceph/* %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/
# Include ceph/csi directory, but move templates to /etc
cp -pr cluster/examples/kubernetes/ceph/csi %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/
mkdir -p %{buildroot}%{_sysconfdir}/ceph-csi
mv %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/csi/template/* %{buildroot}%{_sysconfdir}/ceph-csi/
rmdir %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/csi/template
# Remove the flex directory as this is not supported at all
rm -rf %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/flex

################################################################################
# Check that linker flags are applied
################################################################################
# re-set version variables to match those used in the build step
# remove symbols unsupported by k8s (+) from version
version_full=%{version}
version_noplus="${version_full//[+]/_}"
%global version_parsed "${version_noplus}-%{release}"
# strip off everything following + for the helm appVersion
%global helm_appVersion "${version_full%+*}"
%global helm_version "%{helm_appVersion}_%{RELEASE}"

# Check Rook version is properly set
rook_bin="$rook_bin_location"rook
bin_version="$("$rook_bin" version)"

if [[ ! "$bin_version" =~ "$version" ]]; then
    echo "Rook version not set correctly!"
    exit 1
fi

# Check Ceph CSI default image is set
if grep -q --binary --text quay.io "$rook_bin"; then
    echo "Default CSI image was not set!"
    exit 1
fi
if ! grep -q --binary --text "%{ceph_csi_image}" "$rook_bin"; then
    echo "Default CSI image was set to wrong value!"
    exit 1
fi

################################################################################
# Update manifests with images coming from Build Service
################################################################################
# set rook, ceph and ceph-csi container versions
sed -i -e "s|image: .*|image: %{ceph_image}|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/cluster*
sed -i -e "s|image: .*|image: %{rook_image}|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/toolbox*
sed -i -e "s|image: .*|image: %{rook_image}|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/operator*
sed -i -e "s|/usr/local/bin/toolbox.sh|%{_bindir}/toolbox.sh|g" %{buildroot}%{_datadir}/k8s-yaml/rook/ceph/toolbox*

# Install the helm charts
%define chart_yaml "%{buildroot}%{_datadir}/%{name}-ceph-helm-charts/operator/Chart.yaml"
%define values_yaml "%{buildroot}%{_datadir}/%{name}-ceph-helm-charts/operator/values.yaml"
mkdir -p %{buildroot}%{_datadir}/%{name}-ceph-helm-charts/operator
cp -pr cluster/charts/rook-ceph/* %{buildroot}%{_datadir}/%{name}-ceph-helm-charts/operator
sed -i -e "1 i\#!BuildTag: rook-ceph:"%{helm_version} %{chart_yaml}
# appVersion should being with a 'v', even though the image tag currently does not
sed -i -e "/apiVersion/a appVersion: v%{helm_appVersion}" %{chart_yaml}
sed -i -e "s|\(version: \).*|\1%{helm_version}|" %{chart_yaml}
sed -i -e "s|\(.*tag: \)VERSION|\1%{helm_appVersion}|" %{values_yaml}
# Install SUSE specific helm chart NOTES.txt
cp %SOURCE97 %{buildroot}%{_datadir}/%{name}-ceph-helm-charts/operator/templates/NOTES.txt

# For the integration test tooling, store files with the current Rook and Ceph image names
# These files can be cat'ed to get these without needing to do special processing
%define rook_integration_dir %{buildroot}%{_datadir}/rook-integration
mkdir -p %{rook_integration_dir}
echo -n %{rook_image}     > %{rook_integration_dir}/rook-image-name
echo -n %{ceph_image}     > %{rook_integration_dir}/ceph-image-name
echo -n %{ceph_csi_image} > %{rook_integration_dir}/ceph-csi-image-name

################################################################################
# Specify which files we built belong to each package
################################################################################
%files
%defattr(-,root,root,-)
%{_bindir}/rook
%{_bindir}/toolbox.sh
%config %{_sysconfdir}/ceph-csi
# Due to upstream's use of /usr/local/bin in their example yamls, create
# symlinks to avoid a difficult to find configuration problem
%post
[[ -e /usr/local/bin/toolbox.sh ]] || ln -s %{_bindir}/toolbox.sh /usr/local/bin/toolbox.sh
[[ -e /usr/local/bin/rook ]] || ln -s %{_bindir}/rook /usr/local/bin/rook

%postun
[[ -e /usr/local/bin/toolbox.sh ]] && rm /usr/local/bin/toolbox.sh
[[ -e /usr/local/bin/rook ]] && rm /usr/local/bin/rook

%files rookflex
%{_bindir}/rookflex

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/rook
%dir %{_datarootdir}/k8s-yaml/rook/ceph
%{_datadir}/k8s-yaml/rook/ceph/

%files ceph-helm-charts
%doc %{_datadir}/%{name}-ceph-helm-charts/operator/README.md
%{_datadir}/%{name}-ceph-helm-charts

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
