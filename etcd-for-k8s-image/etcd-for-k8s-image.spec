#
# spec file for package etcd-for-k8s-image
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           etcd-for-k8s-image
Version:        3.3.10
Release:        0
Summary:        Etcd and etcdtl for k8s image
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/coreos/etcd
Source:         etcd-%{version}.tar.xz
Source1:        etcd-3.2.24.tar.xz
BuildRequires:  golang-packaging
BuildRequires:	go
ExcludeArch:    %ix86
ExcludeArch:    s390
Conflicts:      etcd
Conflicts:      etcdctl

%description
etcd is a distributed, consistent key-value store for shared configuration and
service discovery. This package contains different versions of etcd and
etcdctl for the kubernetes container image.

%prep
%setup -q -n etcd-%{version} -b1

%build
%{goprep} github.com/coreos/etcd
%{gobuild} cmd/etcd
%{gobuild} cmd/etcdctl
mkdir bin
mv ../go/bin/etcd* bin

#cd ../etcd-3.2.24
#rm -rf ../go/*
#%{goprep} github.com/coreos/etcd
#%{gobuild} cmd/etcd
#%{gobuild} cmd/etcdctl
#mkdir bin
#mv ../go/bin/etcd* bin


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 bin/etcd %{buildroot}%{_sbindir}/etcd-%{version}
install -m 0755 bin/etcdctl %{buildroot}%{_bindir}/etcdctl-%{version}
ln -sf etcd-%{version} %{buildroot}%{_sbindir}/etcd
ln -sf etcdctl-%{version} %{buildroot}%{_bindir}/etcdctl

#cd ../etcd-3.2.24
#install -m 0755 bin/etcd %{buildroot}%{_sbindir}/etcd-3.2.24
#install -m 0755 bin/etcdctl %{buildroot}%{_bindir}/etcdctl-3.2.24

%files
%defattr(-,root,root)
%license LICENSE
%{_sbindir}/etcd
%{_sbindir}/etcd-%{version}
#%{_sbindir}/etcd-3.2.24
%{_bindir}/etcdctl
%{_bindir}/etcdctl-%{version}
#%{_bindir}/etcdctl-3.2.24

%changelog
