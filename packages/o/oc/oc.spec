#
# spec file for package oc
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           oc
Version:        4.20.0
Release:        0
Summary:        Openshift / OKD Client CLI
License:        Apache-2.0
URL:            https://github.com/openshift/oc
Source:         oc-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22.5
BuildRequires:  krb5-devel
BuildRequires:  libgpgme-devel
BuildRequires:  zsh

# this package contains a kubectl link, so we need a Conflicts
Conflicts:      kubernetes-client
Conflicts:      kuberlr
Conflicts:      kubernetes-client-provider

%description
With OpenShift Client CLI (oc), you can create applications and manage
OpenShift resources. It is built on top of kubectl which means it provides its
full capabilities to connect with any kubernetes compliant cluster, and on top
adds commands simplifying interaction with an OpenShift cluster.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch
Conflicts:      kubernetes-client-bash-completion

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch
Conflicts:      kubernetes-client-fish-completion

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch
Conflicts:      kubernetes-client-zsh-completion

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
# hash will be shortened by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

OC_KUBE_GIT_VERSION="$(awk -F '"' '/^KUBE_GIT_VERSION/ {print $2}' Makefile)"
OC_KUBE_GIT_MAJOR_VERSION="$(awk -F '.' '/^KUBE_GIT_VERSION/ {gsub(/^.*v/, "", $1); print $1}' Makefile)"
OC_KUBE_GIT_MINOR_VERSION="$(awk -F '.' '/^KUBE_GIT_VERSION/ {print $2}' Makefile)"
OC_GO_TAGS="$(awk -F "'" '/^GO_BUILD_FLAGS :=/ {print $2}' Makefile)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X k8s.io/component-base/version.gitMajor=${OC_KUBE_GIT_MAJOR_VERSION} \
   -X k8s.io/component-base/version.gitMinor=${OC_KUBE_GIT_MINOR_VERSION} \
   -X k8s.io/component-base/version.gitVersion=${OC_KUBE_GIT_VERSION} \
   -X k8s.io/component-base/version.gitCommit=${COMMIT_HASH:0:8} \
   -X k8s.io/component-base/version.buildDate=${BUILD_DATE} \
   -X k8s.io/component-base/version.gitTreeState=clean \
   -X github.com/openshift/oc/pkg/version.versionFromGit=v%{version} \
   -X github.com/openshift/oc/pkg/version.commitFromGit=${COMMIT_HASH:0:8} \
   -X github.com/openshift/oc/pkg/version.gitTreeState=clean \
   -X github.com/openshift/oc/pkg/version.buildDate=${BUILD_DATE}" \
   -tags="${OC_GO_TAGS}" \
   -o bin/ ./cmd/oc ./tools/genman

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# Install man1 man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
./bin/genman %{buildroot}%{_mandir}/man1 oc

# create the kubectl link
cd %{buildroot}/%{_bindir}/
ln -s ./oc ./kubectl

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
%{buildroot}/%{_bindir}/kubectl completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/kubectl

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish
%{buildroot}/%{_bindir}/kubectl completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/kubectl.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}
%{buildroot}/%{_bindir}/kubectl completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_kubectl

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/kubectl
%{_mandir}/man1/oc*

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}
%{_datarootdir}/bash-completion/completions/kubectl

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish
%{_datarootdir}/fish/vendor_completions.d/kubectl.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}
%{_datarootdir}/zsh/site-functions/_kubectl

%changelog
