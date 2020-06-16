#
# spec file for package sonobuoy
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


%define project github.com/vmware-tanzu/sonobuoy
Name:           sonobuoy
Version:        0.18.3
Release:        0
Summary:        Conformance test suite for diagnosing a Kubernetes cluster
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/vmware-tanzu/sonobuoy
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
%{go_nostrip}
%{go_provides}

%description
Sonobuoy is a diagnostic tool for understanding the state of a
Kubernetes cluster by running a set of Kubernetes conformance tests
in an accessible and non-destructive manner.

%prep
%setup -q -a1

%build
%{goprep} github.com/vmware-tanzu/sonobuoy
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}

cd $HOME/go/src/%{project}
CGO_ENABLED=0 go build -o sonobuoy -ldflags="-s -w -X %{project}/pkg/buildinfo.Version=v%{version}" %{project}

%install
cd $HOME/go/src/%{project}
install -m755 sonobuoy %{buildroot}/%{_bindir}/sonobuoy

%files
%doc README.md
%license LICENSE
%{_bindir}/sonobuoy

%changelog
