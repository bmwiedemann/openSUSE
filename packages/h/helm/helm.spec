#
# spec file for package helm
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


%define goipath helm.sh/helm/v3
%define git_dirty clean
Name:           helm
Version:        3.15.1
Release:        0
Summary:        The Kubernetes Package Manager
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/helm/helm
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.22
%{go_provides}

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p1 -a1

%build
%goprep %{goipath}
export K8S_MINOR=$(grep k8s.io/client-go go.mod | cut -d. -f3)
export GO111MODULE=on
export CGO_ENABLED=0
%gobuild -trimpath -tags '' -mod vendor -buildmode pie -ldflags \
    "-X %{goipath}/internal/version.version=v%{version} \
     -X %{goipath}/internal/version.gitCommit=$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo) \
     -X %{goipath}/pkg/lint/rules.k8sVersionMajor=1 \
     -X %{goipath}/pkg/lint/rules.k8sVersionMinor=$K8S_MINOR \
     -X %{goipath}/pkg/chartutil.k8sVersionMajor=1 \
     -X %{goipath}/pkg/chartutil.k8sVersionMinor=$K8S_MINOR \
     -X %{goipath}/internal/version.gitTreeState=%{git_dirty}" cmd/helm

%install
export GO111MODULE=on
export CGO_ENABLED=0
%goinstall
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/helm completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/helm completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/helm completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%check
# requires network
rm -v pkg/plugin/installer/*installer_test.go
rm -v pkg/engine/engine_test.go
GO111MODULE=on go test ./...

%files
%doc README.md
%license LICENSE
%{_bindir}/helm

%files bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%files fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
