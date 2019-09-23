#
# spec file for package patterns-ceph-containers
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patterns-ceph-containers
Version:        1.0
Release:        0
Summary:        Patterns for the Ceph containers
License:        MIT
Group:          Metapackages
Url:            http://en.opensuse.org/Patterns
Source:         %name-rpmlintrc
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package ceph_base
Summary:        Ceph base
Group:          Metapackages
Provides:       pattern() = ceph_base
Provides:       pattern-category() = Containers
Provides:       pattern-visible()
Requires:       ceph
Requires:       ceph-common
Requires:       ceph-fuse
Requires:       ceph-mds
Requires:       ceph-mgr
Requires:       ceph-mon
Requires:       ceph-osd
Requires:       ceph-radosgw
Requires:       ceph-mgr-dashboard
Requires:       ceph-mgr-rook
Requires:       ceph-mgr-diskprediction-local
Requires:       nfs-ganesha
Requires:       nfs-ganesha-ceph
Requires:       nfs-ganesha-rgw
Requires:       nfs-ganesha-rados-grace
Requires:       rbd-mirror
Requires:       rbd-nbd
Requires:       ca-certificates
Requires:       e2fsprogs
Requires:       kmod
Requires:       lvm2
Requires:       gptfdisk

%description ceph_base
This provides base for the Ceph, Rook, Ceph CSI driver packages.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %buildroot/usr/share/doc/packages/patterns-ceph-containers/
echo 'This file marks the pattern ceph-base to be installed.' >%buildroot/usr/share/doc/packages/patterns-ceph-containers/ceph_base.txt

%files ceph_base
%defattr(-,root,root)
%dir %{_docdir}/patterns-ceph-containers
%{_docdir}/patterns-ceph-containers/ceph_base.txt

%changelog

