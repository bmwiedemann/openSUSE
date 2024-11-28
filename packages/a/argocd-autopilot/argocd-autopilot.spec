#
# spec file for package argocd-autopilot
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


Name:           argocd-autopilot
Version:        0.4.18
Release:        0
Summary:        Opinionated way of installing Argo-CD
License:        Apache-2.0
URL:            https://github.com/argoproj-labs/argocd-autopilot
Source:         argocd-autopilot-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22
BuildRequires:  zsh

%description
New users to GitOps and Argo CD are not often sure how they should structure
their repos, add applications, promote apps across environments, and manage the
Argo CD installation itself using GitOps.

Argo CD Autopilot saves operators time by:
* Installing and managing the Argo CD application using GitOps.
* Providing a clear structure for how applications are to be added and updated,
  all from git.
* Creating a simple pattern for making updates to applications and promoting
  those changes across environments.
* Enabling better disaster recovery by being able to bootstrap new clusters
  with all the applications previously installed.
* Handling secrets for Argo CD to prevent them from spilling into plaintext
  git. (Soon to come)

The Argo-CD Autopilot is a tool which offers an opinionated way of installing
Argo-CD and managing GitOps repositories.

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
# hash will be shortended by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

INSTALLATION_MANIFESTS_URL="github.com/argoproj-labs/argocd-autopilot/manifests/base?ref=v%{version}"
INSTALLATION_MANIFESTS_NAMESPACED_URL=""

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
    -X 'github.com/argoproj-labs/argocd-autopilot/pkg/store.binaryName=%{name}' \
    -X 'github.com/argoproj-labs/argocd-autopilot/pkg/store.version=%{version}' \
    -X 'github.com/argoproj-labs/argocd-autopilot/pkg/store.buildDate=${BUILD_DATE}' \
    -X 'github.com/argoproj-labs/argocd-autopilot/pkg/store.gitCommit=${COMMIT_HASH:0:8}' \
    -X 'github.com/argoproj-labs/argocd-autopilot/pkg/store.installationManifestsURL=${INSTALLATION_MANIFESTS_URL}' \
    -X 'github.com/argoproj-labs/argocd-autopilot/pkg/store.installationManifestsNamespacedURL=${INSTALLATION_MANIFESTS_NAMESPACED_URL}'" \
   -o bin/argocd-autopilot ./cmd/

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

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
