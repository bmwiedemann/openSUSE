#
# spec file for package heapster
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define git_commit %{version}

Name:           heapster
Version:        1.4.3
Release:        1%{?dist}
Summary:        The Kubernetes Monitoring Agent
License:        Apache-2.0
Group:          System/Monitoring
Url:            https://github.com/kubernetes/heapster
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.11
%{go_nostrip}
%{go_provides}

%description
Heapster is a monitoring solution for Kubernetes clusters

%prep
%setup -q -n %{name}-%{version} -a 1
%{goprep} k8s.io/heapster

%build
export GOPATH="%{_builddir}/go:$GOPATH"
GOBIN=$PWD/bin go install -tags '' -ldflags ' -X k8s.io/heapster/version.HeapsterVersion=v%{version} -X k8s.io/heapster/version.GitCommit=%{git_commit}' k8s.io/heapster/metrics
GOBIN=$PWD/bin go install -tags '' -ldflags ' -X k8s.io/heapster/version.HeapsterVersion=v%{version} -X k8s.io/heapster/version.GitCommit=%{git_commit}' k8s.io/heapster/events

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 "%{_builddir}/heapster-1.4.3/bin/metrics" "%{buildroot}/%{_bindir}/"
install -m755 "%{_builddir}/heapster-1.4.3/bin/events" "%{buildroot}/%{_bindir}/"

%files
%defattr(-,root,root)
%{_bindir}/metrics
%{_bindir}/events
%doc CONTRIBUTING.md code-of-conduct.md
%license LICENSE

%changelog
