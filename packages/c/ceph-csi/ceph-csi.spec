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
Version:        3.1.0+git0.5d4847358
Release:        0
Summary:        Container Storage Interface driver for Ceph block and file
License:        Apache-2.0
URL:            https://github.com/ceph/ceph-csi

Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source98:       README

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

# Rook runtime requirements - referenced from packages installed in Rook images
# From Ceph base container: github.com/ceph/ceph-container/src/daemon-base/...
Requires:       pattern() = ceph_base

%description
Ceph CSI plugins implement an interface between CSI enabled Container
Orchestrator (CO) and Ceph cluster. It allows dynamically provisioning
Ceph block and file volumes and attaching them to workloads.

See https://github.com/ceph/ceph-csi for more information.

################################################################################
# The tasty, meaty build section
################################################################################

%prep
%setup -q
# make sure we use the content from the vendor tarball
rm -rf vendor/
%setup -q -T -D -a 1

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

################################################################################
# Specify which files we built belong to each package
################################################################################
# ceph-csi.arch.rpm
%files
%defattr(-,root,root,-)
%{_bindir}/cephcsi

################################################################################
# Finalize
################################################################################

# ceph-csi RPMs aren't for users to install, just to be put in containers, so
# don't bother adding docs or changelog or anything

%changelog
