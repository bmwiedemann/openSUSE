#
# spec file for package fleet-cli
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


%define executable_name fleet

Name:           fleet-cli
Version:        0.15.0
Release:        0
Summary:        CLI for the Rancher Fleet GitOps tooling
License:        Apache-2.0
URL:            https://github.com/rancher/fleet
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# 16.0 fails with go.mod requires go >= 1.26.0 (running go 1.26rc3; GOTOOLCHAIN=local)
BuildRequires:  go1.26 >= 1.26.0
# for the shell completions
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
Provides:       fleet = %{version}

%description
Fleet is GitOps and HelmOps at scale. Fleet is designed to manage multiple
clusters. It's also lightweight enough that it works great for a single cluster
too, but it really shines when you get to a large scale. By large scale we mean
either a lot of clusters, a lot of deployments, or a lot of teams in a single
organization.

Fleet can manage deployments from git of raw Kubernetes YAML, Helm charts, or
Kustomize or any combination of the three. Regardless of the source all
resources are dynamically turned into Helm charts and Helm is used as the
engine to deploy everything in the cluster. This gives a high degree of
control, consistency, and auditability. Fleet focuses not only on the ability
to scale, but to give one a high degree of control and visibility to exactly
what is installed on the cluster.

This package contains the CLI to interact with Fleet.

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

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/rancher/fleet/pkg/version.Version=v%{version} \
   -X github.com/rancher/fleet/pkg/version.GitCommit=${COMMIT_HASH}" \
   -o bin/%{executable_name} ./cmd/fleetcli/

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{executable_name}

%check
%{buildroot}/%{_bindir}/%{executable_name} --version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{executable_name}

%changelog
