#
# spec file for package flux2-cli
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

%define repo_name flux2
# temporarily added to accomodate pre-release versioning while making sure
# the upstream version is preserved in the CLI
%define raw_version 2.0.0-rc.4

Name:           flux2-cli
Version:        2.0.0~rc4
Release:        0
Summary:        CLI for Flux2CD
License:        Apache-2.0
URL:            https://github.com/fluxcd/flux2
Source:         %{repo_name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source11:	helm-controller.crds.yaml
Source12:       helm-controller.deployment.yaml
Source13:       image-automation-controller.crds.yaml
Source14:       image-automation-controller.deployment.yaml
Source15:       image-reflector-controller.crds.yaml
Source16:       image-reflector-controller.deployment.yaml
Source17:       kustomize-controller.crds.yaml
Source18:       kustomize-controller.deployment.yaml
Source19:       notification-controller.crds.yaml
Source20:       notification-controller.deployment.yaml
Source21:       source-controller.crds.yaml
Source22:       source-controller.deployment.yaml
Source101:      Packaging_README.md
Source102:      download_yaml.sh
BuildRequires:  go >= 1.20
BuildRequires:  kustomize
BuildRequires:  helm
BuildRequires:  git-core

%description
Flux is a tool for keeping Kubernetes clusters in sync with sources of configuration (like Git repositories and OCI artifacts), and automating updates to configuration when there is new code to deploy.

Flux version 2 ("v2") is built from the ground up to use Kubernetes' API extension system, and to integrate with Prometheus and other core components of the Kubernetes ecosystem. In version 2, Flux supports multi-tenancy and support for syncing an arbitrary number of Git repositories, among other long-requested features.

Flux v2 is constructed with the GitOps Toolkit, a set of composable APIs and specialized tools for building Continuous Delivery on top of Kubernetes.

Flux is a Cloud Native Computing Foundation (CNCF) project, used in production by various organisations and cloud providers.

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
%setup -q -n %{repo_name}-%{version}
%setup -q -n %{repo_name}-%{version} -T -D -a 1

%build
cp %{SOURCE11} ./manifests/bases/helm-controller/
cp %{SOURCE12} ./manifests/bases/helm-controller/
sed -i 's_https://github.com/fluxcd/helm-controller/releases/download/v0.34.0/__g' manifests/bases/helm-controller/kustomization.yaml
cat manifests/bases/helm-controller/kustomization.yaml

cp %{SOURCE13} ./manifests/bases/image-automation-controller/
cp %{SOURCE14} ./manifests/bases/image-automation-controller/
sed -i 's_https://github.com/fluxcd/image-automation-controller/releases/download/v0.34.0/__g' manifests/bases/image-automation-controller/kustomization.yaml
cat manifests/bases/image-automation-controller/kustomization.yaml

cp %{SOURCE15} ./manifests/bases/image-reflector-controller/
cp %{SOURCE16} ./manifests/bases/image-reflector-controller/
sed -i 's_https://github.com/fluxcd/image-reflector-controller/releases/download/v0.28.0/__g' manifests/bases/image-reflector-controller/kustomization.yaml
cat manifests/bases/image-reflector-controller/kustomization.yaml

cp %{SOURCE17} ./manifests/bases/kustomize-controller/
cp %{SOURCE18} ./manifests/bases/kustomize-controller/
sed -i 's_https://github.com/fluxcd/kustomize-controller/releases/download/v1.0.0-rc.4/__g' manifests/bases/kustomize-controller/kustomization.yaml
cat manifests/bases/kustomize-controller/kustomization.yaml

cp %{SOURCE19} ./manifests/bases/notification-controller/
cp %{SOURCE20} ./manifests/bases/notification-controller/
sed -i 's_https://github.com/fluxcd/notification-controller/releases/download/v1.0.0-rc.4/__g' manifests/bases/notification-controller/kustomization.yaml
cat manifests/bases/notification-controller/kustomization.yaml

cp %{SOURCE21} ./manifests/bases/source-controller/
cp %{SOURCE22} ./manifests/bases/source-controller/
sed -i 's_https://github.com/fluxcd/source-controller/releases/download/v1.0.0-rc.4/__g' manifests/bases/source-controller/kustomization.yaml
cat manifests/bases/source-controller/kustomization.yaml

./manifests/scripts/bundle.sh

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-s -w -X main.VERSION=%{raw_version}" \
   -o bin/flux ./cmd/flux

%install
# Install the binary.
install -D -m 0755 bin/flux "%{buildroot}/%{_bindir}/flux"

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/flux completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/flux completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/flux completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/flux.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/flux

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
%{_datarootdir}/fish/vendor_completions.d/flux.fish

%changelog
