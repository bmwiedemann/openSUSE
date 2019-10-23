#
# spec file for package etcd-for-k8s-image
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


Name:           etcd-for-k8s-image
Version:        3.3.15
Release:        0
Summary:        Etcd and etcdtl for k8s image
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/coreos/etcd
Source:         etcd-%{version}.tar.xz
BuildRequires:  go1.12 >= 1.12.9
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.12
ExcludeArch:    %ix86
ExcludeArch:    s390
Conflicts:      etcd
Conflicts:      etcdctl

%description
etcd is a distributed, consistent key-value store for shared configuration and
service discovery. This package contains different versions of etcd and
etcdctl for the kubernetes container image.

%prep
%setup -q -n etcd-%{version} 

%build
%{goprep} github.com/coreos/etcd
%{gobuild} .
%{gobuild} etcdctl
mkdir bin
mv ../go/bin/etcd* bin

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
