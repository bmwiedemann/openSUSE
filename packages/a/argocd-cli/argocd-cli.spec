#
# spec file for package argocd-cli
#
# Copyright (c) 2024 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define executable_name argocd

Name:           argocd-cli
Version:        2.11.4
Release:        0
Summary:        CLI for the ArgoCD declarative continuous deployment tool
License:        Apache-2.0
URL:            https://github.com/argoproj/argo-cd
Source:         argo-cd-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.20

%description
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

This packages contains the CLI to interact with the ArgoCD installation in a Kubernetes cluster.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1 -n argo-cd-%{version}

%build
KUBECTL_VERSION=$(awk '/=> k8s.io\/kubectl v/ {print $4}' go.mod)
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="\
   -X github.com/argoproj/argo-cd/v2/common.version=%{version} \
   -X github.com/argoproj/argo-cd/v2/common.buildDate=$BUILD_DATE \
   -X github.com/argoproj/argo-cd/v2/common.gitCommit=v%{version} \
   -X github.com/argoproj/argo-cd/v2/common.gitTag=v%{version} \
   -X github.com/argoproj/argo-cd/v2/common.gitTreeState=clean \
   -X github.com/argoproj/argo-cd/v2/common.kubectlVersion=$KUBECTL_VERSION" \
   -o bin/%{executable_name} ./cmd/

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} "%{buildroot}/%{_bindir}/%{executable_name}"

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{executable_name}

%changelog
