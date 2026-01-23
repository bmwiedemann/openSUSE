#
# spec file for package kured
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# nodebuginfo


Name:           kured
Version:        1.21.0
Release:        0
Summary:        Kubernetes daemonset to perform safe automatic node reboots
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/weaveworks/kured
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         systemctl-path.patch
Patch1:         kured-imagePullPolicy.patch
BuildRequires:  golang(API) >= 1.24

%description
Kured (KUbernetes REboot Daemon) is a Kubernetes daemonset that
performs safe automatic node reboots when the need to do so is
indicated by the package management system of the underlying OS.

- Watches for the presence of a reboot sentinel e.g. %{_localstatedir}/run/reboot-required

- Utilises a lock in the API server to ensure only one node reboots at a time

- Optionally defers reboots in the presence of active Prometheus alerts

- Cordons & drains worker nodes before reboot, uncordoning them after

%package k8s-yaml
Summary:        Kubernetes yaml file to run kured container
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml file requried to download and run the
kured container in a kubernetes cluster.

%prep
%autosetup -a 1 -p 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

%check
# execute the binary as a basic check
# temporarily disable until upstream restores a --help flag
# ./%{name} --help

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Install provided yaml file to download and run the kured container
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/kured
cat kured-rbac.yaml kured-ds.yaml > %{buildroot}%{_datadir}/k8s-yaml/kured/kured.yaml
chmod 644  %{buildroot}%{_datadir}/k8s-yaml/kured/kured.yaml
sed -i -e 's|image: .*|image: registry.opensuse.org/kubic/kured:%{version}|g' %{buildroot}%{_datadir}/k8s-yaml/kured/kured.yaml

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/kured
%{_datarootdir}/k8s-yaml/kured/kured.yaml

%changelog
