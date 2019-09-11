#
# spec file for rook binaries
#
# Copyright (c) 2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

################################################################################
# Rook metadata
################################################################################

Name:          ceph-csi
Version:       1.1.0+git0.gc7ba26d2
Release:       0
Summary:       Container Storage Interface driver for Ceph block and file
License:       Apache-2.0
Group:         System/Filesystems
Url:           https://github.com/ceph/ceph-csi

Source0:       %{name}-%{version}.tar.xz
Source98:      README
Source99:      update-tarball.sh
%if 0%{?suse_version}
# _insert_obs_source_lines_here
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
%endif

# Go and spec requirements
BuildRequires: golang-packaging
BuildRequires: go
BuildRequires: xz

# Rook runtime requirements - referenced from packages installed in Rook images
# From Ceph base container: github.com/ceph/ceph-container/src/daemon-base/...
Requires:      pattern() = ceph_base

%description
Ceph CSI plugins implement an interface between CSI enabled Container
Orchestrator (CO) and Ceph cluster. It allows dynamically provisioning
Ceph block and file volumes and attaching them to workloads.

See https://github.com/ceph/ceph-csi for more information.

################################################################################
# The tasty, meaty build section
################################################################################
%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}

%build
%goprep github.com/ceph/ceph-csi
export CGO_ENABLED=0
%gobuild cmd  # builds a binary called 'cmd'

%install

bin_location=%{_builddir}/go/bin/
install_location=%{buildroot}%{_bindir}

install --mode=755 --directory "${install_location}"

mv ${bin_location}/cmd ${bin_location}/cephcsi
install --preserve-timestamps --mode=755 --target-directory="${install_location}" "${bin_location}"/cephcsi

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
