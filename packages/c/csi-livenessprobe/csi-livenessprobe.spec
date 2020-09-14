#
# spec file for package livenessprobe
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

%define project github.com/kubernetes-csi/livenessprobe
%define package livenessprobe

Name:           csi-%{package}
Version:        1.1.0
Release:        0
Summary:        Exposes an HTTP /healthz endpoint to monitor CSI driver
License:        Apache-2.0
Group:          System/Management
Url:            https://%{project}
Source:         %{package}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.13

%description
The liveness probe is a sidecar container that exposes an HTTP /healthz endpoint, which serves as kubelet's livenessProbe hook to monitor health of a CSI driver.

%prep
%setup -q -n %{package}-%{version}
%setup -q -T -D -a 1 -n %{package}-%{version}

%build
%goprep %{project}

export CGO_ENABLED=0

%gobuild -a -mod=vendor -ldflags "-X main.version=%{version}" cmd/%{package}

%install
%goinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/%{package}

%changelog

