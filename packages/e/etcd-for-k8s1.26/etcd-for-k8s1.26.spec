#
# spec file for package etcd-for-k8s1.26
#
# Copyright (c) 2023 SUSE LLC
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

Name:           etcd-for-k8s1.26
Version:        3.5.6
Release:        0
Summary:        Etcd and etcdtl for k8s image
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/etcd-io/etcd
Source:         etcd-%{version}.tar.gz
Source1:        vendor-etcdctl.tar.gz
Source2:        vendor-server.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.19
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
%{goprep} %{project}

tar -xf %{SOURCE1} -C ./etcdctl
tar -xf %{SOURCE2} -C ./server

mkdir ./bin

cd ./etcdctl
go build -v -buildmode=pie -mod=vendor -o ../bin/etcdctl
cd ..

cd ./server
go build -v -buildmode=pie -mod=vendor -o ../bin/etcd
cd ..

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 bin/etcdctl %{buildroot}%{_bindir}/etcdctl-%{version}
install -D -p -m 0755 bin/etcd %{buildroot}%{_sbindir}/etcd-%{version}

ln -sf etcdctl-%{version} %{buildroot}%{_bindir}/etcdctl
# ln -sf etcd-%{version} %{buildroot}%{_sbindir}/etcd
# we need a wrapper script to be able to set some environment variables.
echo "#!/bin/bash" > %{buildroot}%{_sbindir}/etcd
%ifarch aarch64
echo "export ETCD_UNSUPPORTED_ARCH=arm64" >> %{buildroot}%{_sbindir}/etcd
%endif
echo "exec %{_sbindir}/etcd-%{version} \"\$@\"" >> %{buildroot}%{_sbindir}/etcd
chmod 755 %{buildroot}%{_sbindir}/etcd

%files
%defattr(-,root,root)
%license LICENSE
%{_sbindir}/etcd
%{_sbindir}/etcd-%{version}
%{_bindir}/etcdctl
%{_bindir}/etcdctl-%{version}

%changelog
