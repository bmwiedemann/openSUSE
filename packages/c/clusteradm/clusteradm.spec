#
# spec file for package clusteradm
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


Name:           clusteradm
Version:        1.2.0
Release:        0
Summary:        CLI to bootstrap the open-cluster-management control plane
License:        Apache-2.0
URL:            https://github.com/open-cluster-management-io/clusteradm
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  golang(API) >= 1.25
BuildRequires:  zsh

%description
clusteradm is the command-line tool for Open Cluster Management (OCM),
providing a unified interface to manage multi-cluster Kubernetes environments
from the command line.

Open Cluster Management (OCM) is a CNCF sandbox project that enables end-to-end
visibility and control across your Kubernetes clusters using a powerful
hub-agent architecture. OCM provides:
- Cluster Lifecycle Management: Register, manage, and monitor multiple
  Kubernetes clusters
- Application Distribution: Deploy and manage applications across multiple
  clusters
- Policy & Governance: Enforce security policies and compliance across your
  fleet
- Add-on Extensibility: Extend functionality with a rich ecosystem of add-ons

clusteradm serves as the primary CLI tool for interacting with OCM, enabling
administrators to:
- Initialize hub clusters and register managed clusters
- Deploy and manage multi-cluster applications
- Configure policies and governance
- Manage cluster sets and placements
- Install and configure add-ons

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
   -mod=vendor \
   -buildmode=pie \
   -tags="osusergo netgo release" \
   -ldflags=" \
   -X open-cluster-management.io/clusteradm/pkg/version.versionFromGit=v%{version} \
   -X open-cluster-management.io/clusteradm/pkg/version.commitFromGit=${COMMIT_HASH} \
   -X open-cluster-management.io/clusteradm/pkg/version.gitTreeState=clean \
   -X open-cluster-management.io/clusteradm/pkg/version.buildDate=${BUILD_DATE}" \
   -o bin/%{name} ./cmd/%{name}/%{name}.go

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%check
%{buildroot}/%{_bindir}/%{name} --help

# currently the 'version client' command exits with error code 1
# if there is no cluster reachable
# https://github.com/open-cluster-management-io/clusteradm/issues/536

#%{buildroot}/%{_bindir}/%{name} version client
#%{buildroot}/%{_bindir}/%{name} version client | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
