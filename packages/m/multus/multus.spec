#
# spec file for package multus
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


%define commit f4431cd010bbf2d68444f5746ca9ff2eae30fc2a

Name:           multus
Version:        3.3
Release:        0
Summary:        CNI plugin providing multiple interfaces in containers
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/intel/multus-cni
Source:         %{name}-%{version}.tar.xz
Patch0:         0001-build-Allow-to-define-VERSION-and-COMMIT-without-git.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.8

%description
Multus is a CNI plugin which provides multiple network interfaces in
containers. It allows to use many CNI plugins at the same time and supports all
plugins which implement the CNI specification.

%package k8s-yaml
Summary:        Kubernetes yaml file to run Multus containers
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
Multus is a CNI plugin which provides multiple network interfaces in
containers. It allows to use many CNI plugins at the same time and supports all
plugins which implement the CNI specification.

This package contains the yaml file requried to download and run Multus
containers in a Kubernetes cluster.

%prep
%autosetup -p1

%build
VERSION=%{version} COMMIT=%{commit} GO111MODULE=off ./build

%install
install -D -m0755 bin/multus %{buildroot}%{_bindir}/multus
install -D -m0755 images/entrypoint.sh %{buildroot}%{_bindir}/multus-entrypoint
install -D -m0644 images/multus-daemonset-crio.yml %{buildroot}%{_datadir}/k8s-yaml/multus/multus.yaml
sed -i \
    -e 's|image: nfvpe/multus.*|image: registry.opensuse.org/devel/kubic/containers/container/kubic/%{name}:%{version}|' \
    -e 's|/entrypoint.sh|multus-entrypoint|g' \
    %{buildroot}%{_datadir}/k8s-yaml/multus/multus.yaml

%files
%license LICENSE
%doc README.md
%{_bindir}/multus
%{_bindir}/multus-entrypoint

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/multus
%{_datarootdir}/k8s-yaml/multus/multus.yaml

%changelog
