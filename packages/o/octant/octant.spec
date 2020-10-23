#
# spec file for package octant
#
# Copyright (c) 2020 SUSE LLC, Nuernberg, Germany.
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

%define goipath github.com/vmware-tanzu/octant
%define commit 8aebb34922f83894fb02ad393740e96ee1b3d8fe
%define time %(date +%%Y-%%m-%%dT%%H:%%M:%%S)

Name:           octant
Version:        0.16.1
Release:        0
Summary:        A platform to better understand the complexity of Kubernetes clusters
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/vmware-tanzu/octant
Source:         https://github.com/vmware-tanzu/octant/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14

%description
Octant is a tool for developers to understand how applications run on a Kubernetes cluster.
It aims to be part of the developer's toolkit for gaining insight and approaching complexity found in Kubernetes.
Octant offers a combination of introspective tooling, cluster navigation, and object management along with a plugin system to further extend its capabilities.
It will ensure certificates are valid and up to date periodically, and attempt to renew certificates at an appropriate time before expiry.

%prep
%setup -q -n %{name}-%{version}

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -mod vendor -ldflags "-X main.version=%{version} -X main.gitCommit=%{commit} -X main.buildTime=%{time}" cmd/octant

%install
%goinstall

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
