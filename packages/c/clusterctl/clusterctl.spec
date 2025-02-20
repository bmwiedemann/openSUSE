#
# spec file for package clusterctl
#
# Copyright (c) 2025 SUSE LLC
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


%define version_git_major 1
%define version_git_minor 8

Name:           clusterctl
Version:        1.9.5
Release:        0
Summary:        CLI tool to handle the lifecycle of a Cluster API management cluster
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/cluster-api
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.23
BuildRequires:  zsh

%description
The clusterctl CLI tool handles the lifecycle of a Cluster API management
cluster.

The clusterctl command line interface is specifically designed for providing a
simple “day 1 experience” and a quick start with Cluster API. It automates
fetching the YAML files defining provider components and installing them.

Additionally it encodes a set of best practices in managing providers, that
helps the user in avoiding mis-configurations or in managing day 2 operations
such as upgrades.

Below you can find a list of main clusterctl commands:

* clusterctl init: Initialize a management cluster.
* clusterctl upgrade plan: Provide a list of recommended target versions for
  upgrading Cluster API providers in a management cluster.
* clusterctl upgrade apply: Apply new versions of Cluster API core and providers
  in a management cluster.
* clusterctl delete: Delete one or more providers from the management cluster.
* clusterctl generate: cluster Generate templates for creating workload
  clusters.
* clusterctl generate yaml: Process yaml using clusterctl’s yaml processor.
* clusterctl get kubeconfig: Gets the kubeconfig file for accessing a workload
  cluster.
* clusterctl move: Move Cluster API objects and all their dependencies between
  management clusters.
* clusterctl alpha rollout: Manages the rollout of Cluster API resources. For
  example: MachineDeployments.

Avoiding GitHub rate limiting

While using providers hosted on GitHub, clusterctl is calling GitHub API which
are rate limited; for normal usage free tier is enough but when using
clusterctl extensively users might hit the rate limit.

To avoid rate limiting for the public repos set the GITHUB_TOKEN environment
variable. To generate a token follow this documentation. The token only needs
repo scope for clusterctl.

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
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
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
   -ldflags=" \
   -X sigs.k8s.io/cluster-api/version.gitVersion=v%{version} \
   -X sigs.k8s.io/cluster-api/version.gitCommit=${COMMIT_HASH} \
   -X sigs.k8s.io/cluster-api/version.gitTreeState=clean \
   -X sigs.k8s.io/cluster-api/version.gitMajor=%{version_git_major} \
   -X sigs.k8s.io/cluster-api/version.gitMinor=%{version_git_minor} \
   -X sigs.k8s.io/cluster-api/version.gitReleaseCommit=${COMMIT_HASH} \
   -X sigs.k8s.io/cluster-api/version.buildDate=$BUILD_DATE" \
   -o bin/%{name} ./cmd/%{name}

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
