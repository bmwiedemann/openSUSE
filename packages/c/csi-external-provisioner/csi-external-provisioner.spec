#
# spec file for package csi-provisioner
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

%{go_nostrip}

%define project github.com/kubernetes-csi/external-provisioner
%define package csi-provisioner
%define source external-provisioner

Name:           csi-%{source}
Version:        1.6.0
Release:        0
Summary:        Dynamically provisions volumes of CSI drivers
License:        Apache-2.0
Group:          System/Management
Url:            https://%{project}
Source:         %{source}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
BuildRequires:  go1.12 >= 1.12.0

%description
Kubernetes external controller that monitors PersistentVolumeClaim objects created by user and creates/deletes volumes for them.

%prep
%setup -q -n %{source}-%{version}
%setup -q -T -D -a 1 -n %{source}-%{version}

%build
%goprep %{project}

export CGO_ENABLED=0
export GOOS=linux

%gobuild -a -mod=vendor -ldflags="-w -s -X main.version=%{version}" cmd/%{package}

%install
%goinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/%{package}

%changelog
