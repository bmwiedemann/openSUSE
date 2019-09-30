#
# spec file for package helm
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


%define git_commit b9a54967f838723fe241172a6b94d18caf8bcdca
Name:           helm
Version:        3.0.0beta.3
Release:        0
Summary:        The Kubernetes Package Manager
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/kubernetes/helm
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  go1.12
Source99:       README.packaging
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
%{go_nostrip}
%{go_provides}

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

%prep
%setup -q
tar xJf %{SOURCE1}
%{goprep} helm.sh/helm

%build
export GOPATH="%{_builddir}/go:$GOPATH"
GOBIN=$PWD/bin go install -tags '' -ldflags ' -X helm.sh/helm/pkg/version.Version=v%{version} -X helm.sh/helm/pkg/version.BuildMetadata= -X helm.sh/helm/pkg/version.GitCommit=%{git_commit} -X helm.sh/helm/pkg/version.GitTreeState=clean' helm.sh/helm/cmd/...

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 bin/helm %{buildroot}/%{_bindir}/helm

%files
%doc README.md
%license LICENSE
%{_bindir}/helm

%changelog
