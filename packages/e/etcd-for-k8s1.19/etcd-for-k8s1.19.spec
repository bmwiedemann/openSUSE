#
# spec file for package etcd-for-k8s1.19
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


%define project go.etcd.io/etcd

Name:           etcd-for-k8s1.19
Version:        3.4.13
Release:        0
Summary:        Etcd and etcdtl for k8s image
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/etcd-io/etcd
Source:         etcd-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.12 >= 1.12.17
BuildRequires:  golang-packaging
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.12
ExcludeArch:    %ix86
ExcludeArch:    s390
Conflicts:      etcd
Conflicts:      etcdctl
Provides:       etcd-for-k8s = %{version}
Conflicts:      etcd-for-k8s

%description
etcd is a distributed, consistent key-value store for shared configuration and
service discovery. This package contains different versions of etcd and
etcdctl for the kubernetes container image.

%prep
%setup -q -n etcd-%{version} 

%build
# Can't use goprep and gobuild macros due to the packagename and projectname confusing things
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
rm -rf $HOME/go/src
mkdir -pv $HOME/go/src/%{project}
find . -mindepth 1 -maxdepth 1 -exec cp -r {} $HOME/go/src/%{project} \;

cd $HOME/go/src/%{project}
go build -v -buildmode=pie -o bin/etcd %{project}
go build -v -buildmode=pie -o bin/etcdctl %{project}/etcdctl
mkdir -p $HOME/rpmbuild/BUILD/etcd-%{version}/bin
mv bin/etcd* $HOME/rpmbuild/BUILD/etcd-%{version}/bin

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
install -m 0755 bin/etcd %{buildroot}%{_sbindir}/etcd-%{version}
install -m 0755 bin/etcdctl %{buildroot}%{_bindir}/etcdctl-%{version}
#ln -sf etcd-%{version} %{buildroot}%{_sbindir}/etcd
# we need a wrapper script to be able to set some environment
# variables.
echo "#!/bin/bash" > %{buildroot}%{_sbindir}/etcd
%ifarch aarch64
echo "export ETCD_UNSUPPORTED_ARCH=arm64" >> %{buildroot}%{_sbindir}/etcd
%endif
echo "exec %{_sbindir}/etcd-%{version} \"\$@\"" >> %{buildroot}%{_sbindir}/etcd
chmod 755 %{buildroot}%{_sbindir}/etcd
ln -sf etcdctl-%{version} %{buildroot}%{_bindir}/etcdctl

%files
%defattr(-,root,root)
%license LICENSE
%{_sbindir}/etcd
%{_sbindir}/etcd-%{version}
%{_bindir}/etcdctl
%{_bindir}/etcdctl-%{version}

%changelog
