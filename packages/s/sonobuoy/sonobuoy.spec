#
# spec file for package sonobuoy
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


%define git_commit %{version}
Name:           sonobuoy
Version:        0.13.0
Release:        0
Summary:        Conformance test suite for diagnosing a Kubernetes cluster
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/heptio/sonobuoy
Source:         %{name}-%{version}.tar.xz
BuildRequires:  go >= 1.8
BuildRequires:  golang-packaging
BuildRequires:  xz
%{go_nostrip}
%{go_provides}

%description
Sonobuoy is a diagnostic tool for understanding the state of a
Kubernetes cluster by running a set of Kubernetes conformance tests
in an accessible and non-destructive manner.

%prep
%setup -q
%{goprep} github.com/heptio/sonobuoy

%build
export GOPATH="%{_builddir}/go:$GOPATH"
GOBIN=$PWD/bin go install -tags '' -ldflags '-s -w -X github.com/heptio/sonobuoy/pkg/buildinfo.Version=v%{version}' github.com/heptio/sonobuoy

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 bin/sonobuoy %{buildroot}/%{_bindir}/sonobuoy

%files
%doc README.md
%license LICENSE
%{_bindir}/sonobuoy

%changelog
