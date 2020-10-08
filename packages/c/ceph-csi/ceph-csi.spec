#
# spec file for package ceph-csi
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


# Remove stripping of Go binaries.
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           ceph-csi
Version:        3.1.1+git0.22b631e99
Release:        0
Summary:        Container Storage Interface driver for Ceph block and file
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/ceph/ceph-csi

Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source98:       README

# Change CSI images to SUSE specific values.
Patch0:         csi-images-SUSE.patch

%if 0%{?suse_version}
# _insert_obs_source_lines_here
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le
%endif

# Go and spec requirements
BuildRequires:  golang(API) >= 1.13

# for go-ceph bindings
BuildRequires:  libcephfs-devel
BuildRequires:  librados-devel
BuildRequires:  librbd-devel

# csi sidecars are needed to update versions in charts
BuildRequires:  csi-external-attacher
BuildRequires:  csi-external-provisioner
BuildRequires:  csi-external-resizer
BuildRequires:  csi-external-snapshotter
BuildRequires:  csi-node-driver-registrar

# Rook runtime requirements - referenced from packages installed in Rook images
# From Ceph base container: github.com/ceph/ceph-container/src/daemon-base/...
Requires:       pattern() = ceph_base

%description
Ceph CSI plugins implement an interface between CSI enabled Container
Orchestrator (CO) and Ceph cluster. It allows dynamically provisioning
Ceph block and file volumes and attaching them to workloads.

See https://github.com/ceph/ceph-csi for more information.

################################################################################
# ceph-csi helm charts
################################################################################
%package helm-charts
Summary:        Ceph CSI helm charts
Group:          System/Management
BuildArch:      noarch

%description helm-charts
Helm charts for CephFS and RBD access through ceph-csi.

################################################################################
# The tasty, meaty build section
################################################################################

%prep
%setup -q
# make sure we use the content from the vendor tarball
rm -rf vendor/
%setup -q -T -D -a 1

%patch0 -p1

# Set chart registry source depending on the base os type
%if 0%{?is_opensuse}
%define registry registry.opensuse.org/opensuse
%else # is SES
%if 0%{?sle_version} >= 150200
%define registry registry.suse.com/ses/7
%else
%define registry registry.suse.com/ses/6
%endif
%endif

%define cephfs_values_yaml "charts/ceph-csi-cephfs/values.yaml"
%define rbd_values_yaml "charts/ceph-csi-rbd/values.yaml"
sed -i -e "s|\(.*\)SUSE_REGISTRY\(.*\)|\1%{registry}\2|" %{cephfs_values_yaml}
sed -i -e "s|\(.*\)SUSE_REGISTRY\(.*\)|\1%{registry}\2|" %{rbd_values_yaml}

%build

# version format is defined in _service
version_parsed=`echo %{version} | cut -d '+' -f 1`
git_commit_parsed=`echo %{version} | sed 's/.*\.//'`

go build \
  -mod=vendor \
  -buildmode=pie \
  -a \
  -ldflags " \
  -X github.com/ceph/ceph-csi/internal/util.GitCommit=$git_commit_parsed \
  -X github.com/ceph/ceph-csi/internal/util.DriverVersion=v$version_parsed" \
  -o _output/cephcsi \
  ./cmd/

%install
install --mode=755 --directory %{buildroot}%{_bindir}
install --preserve-timestamps --mode=755 --target-directory=%{buildroot}%{_bindir} _output/cephcsi

# Set versions for helm charts
helm_appVersion=`echo %{version} | cut -d '+' -f 1`
helm_version="${helm_appVersion}_%{RELEASE}"

# Install the helm charts
%define cephfs_chart_yaml "%{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-cephfs/Chart.yaml"
%define cephfs_values_yaml "%{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-cephfs/values.yaml"
%define rbd_chart_yaml "%{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-rbd/Chart.yaml"
%define rbd_values_yaml "%{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-rbd/values.yaml"
mkdir -p %{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-{cephfs,rbd}
cp -pr charts/ceph-csi-cephfs/* %{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-cephfs
cp -pr charts/ceph-csi-rbd/* %{buildroot}%{_datadir}/%{name}-helm-charts/ceph-csi-rbd

# Set SUSE required values
sed -i -e "1 i\#!BuildTag: ceph-csi-cephfs:"${helm_version} %{cephfs_chart_yaml}
sed -i -e "1 i\#!BuildTag: ceph-csi-rbd:"${helm_version} %{rbd_chart_yaml}
sed -i -e "s|\(appVersion: \).*|\1v${helm_appVersion}|" %{cephfs_chart_yaml}
sed -i -e "s|\(appVersion: \).*|\1v${helm_appVersion}|" %{rbd_chart_yaml}
sed -i -e "s|\(version: \).*|\1${helm_version}|" %{cephfs_chart_yaml}
sed -i -e "s|\(version: \).*|\1${helm_version}|" %{rbd_chart_yaml}

# Set CSI version at build time from helm_appVersion (same as version_parsed)
sed -i -e "s|\%CSI_VERSION\%|${helm_appVersion}|" %{cephfs_values_yaml}
sed -i -e "s|\%CSI_VERSION\%|${helm_appVersion}|" %{rbd_values_yaml}

################################################################################
# Specify which files we built belong to each package
################################################################################
# ceph-csi.arch.rpm
%files
%defattr(-,root,root,-)
%{_bindir}/cephcsi

%files helm-charts
%defattr(-,root,root,-)
%doc %{_datadir}/%{name}-helm-charts/ceph-csi-cephfs/README.md
%doc %{_datadir}/%{name}-helm-charts/ceph-csi-rbd/README.md
%{_datadir}/%{name}-helm-charts

################################################################################
# Finalize
################################################################################

# ceph-csi RPMs aren't for users to install, just to be put in containers, so
# don't bother adding docs or changelog or anything

%changelog
