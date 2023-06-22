#
# spec file for package weave-gitops
#
# Copyright (c) 2023 SUSE LLC
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

Name:           weave-gitops
Version:        0.26.0
Release:        0
Summary:        Weave Gitops CLI
License:        MPL-2.0
URL:            https://github.com/weaveworks/weave-gitops
Source:         weave-gitops-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.18

%description
Weave GitOps is a simple open source developer platform for people who want cloud native applications, without needing Kubernetes expertise. Experience how easy it is to enable GitOps and run your apps in a cluster. Use git to collaborate with team members making new deployments easy and secure. Start with what developers need to run apps, and then easily extend to define and run your own enterprise platform.

From Kubernetes run Weave GitOps to get:

* Application Operations: manage and automate deployment pipelines for apps and more
* Platforms: the easy way to have your own custom PaaS on cloud or on premise
* Extensions: coordinate Kubernetes rollouts with eg. VMs, DBs and cloud services

Our vision is that all cloud native applications should be easy for developers, including operations which should be automated and secure. Weave GitOps is a highly extensible tool to achieve this by placing Kubernetes and GitOps at the core and building a platform around that.

We use GitOps tools throughout. Today Weave GitOps defaults are Flux, Kustomize, Helm, Sops and Kubernetes CAPI. If you use Flux already then you can easily add Weave GitOps to create a platform management overlay.

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

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%prep
%setup -q
%setup -q -T -D -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/weaveworks/weave-gitops/cmd/gitops/version.Version=%{version} -X github.com/weaveworks/weave-gitops/cmd/gitops/version.BuildTime=$BUILD_DATE \
   -X github.com/weaveworks/weave-gitops/cmd/gitops/version.GitCommit=v%{version} -X github.com/weaveworks/weave-gitops/cmd/gitops/version.Branch=main" \
   -o bin/gitops ./cmd/gitops/

%install
# Install the binary.
install -D -m 0755 bin/gitops "%{buildroot}/%{_bindir}/gitops"

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/gitops completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/gitops completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/gitops completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/gitops

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%files -n %{name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
