#
# spec file for package helm
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


Name:           helm
Version:        4.1.1
Release:        0
Summary:        The Kubernetes Package Manager
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/helm/helm
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
# go is not available on Framework one for x86
ExcludeArch:    %ix86
%endif
BuildRequires:  golang(API) = 1.25

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of
pre-configured Kubernetes resources.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p1 -a1

%build
export K8S_MODULES_MAJOR_VER=1
export K8S_MODULES_MINOR_VER=$(grep k8s.io/client-go go.mod | cut -d. -f3)

echo "K8S_MODULES_MAJOR_VER is set to $K8S_MODULES_MAJOR_VER"
echo "K8S_MODULES_MINOR_VER is set to $K8S_MODULES_MINOR_VER"

%ifnarch %ix86 s390x riscv64
export CGO_ENABLED=0
%endif
go build \
  -trimpath \
  -tags '' \
  -mod vendor \
  -buildmode pie \
  -ldflags \
    "-X helm.sh/helm/v4/internal/version.version=v%{version} \
     -X helm.sh/helm/v4/internal/version.gitCommit=$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo) \
     -X helm.sh/helm/v4/internal/version.gitTreeState=clean \
     -X helm.sh/helm/v4/internal/version.kubeClientVersionMajor=${K8S_MODULES_MAJOR_VER} \
     -X helm.sh/helm/v4/internal/version.kubeClientVersionMinor=${K8S_MODULES_MINOR_VER} \
     -X helm.sh/helm/v4/pkg/chart/common.k8sVersionMajor=${K8S_MODULES_MAJOR_VER} \
     -X helm.sh/helm/v4/pkg/chart/common.k8sVersionMinor=${K8S_MODULES_MINOR_VER} \
     -X helm.sh/helm/v4/pkg/chart/v2/lint/rules.k8sVersionMajor=${K8S_MODULES_MAJOR_VER} \
     -X helm.sh/helm/v4/pkg/chart/v2/lint/rules.k8sVersionMinor=${K8S_MODULES_MINOR_VER} \
     -X helm.sh/helm/v4/pkg/chartutil.k8sVersionMajor=${K8S_MODULES_MAJOR_VER} \
     -X helm.sh/helm/v4/pkg/chartutil.k8sVersionMinor=${K8S_MODULES_MINOR_VER} \
     -X helm.sh/helm/v4/pkg/internal/v3/lint/rules.k8sVersionMajor=${K8S_MODULES_MAJOR_VER} \
     -X helm.sh/helm/v4/pkg/internal/v3/lint/rules.k8sVersionMinor=${K8S_MODULES_MINOR_VER} \
     -X helm.sh/helm/v4/pkg/lint/rules.k8sVersionMajor=${K8S_MODULES_MAJOR_VER} \
     -X helm.sh/helm/v4/pkg/lint/rules.k8sVersionMinor=${K8S_MODULES_MINOR_VER}" \
  -o bin/%{name} ./cmd/helm

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/helm completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
%{buildroot}/%{_bindir}/helm completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/helm completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%check
rm -fv internal/plugin/installer/base_test.go
rm -fv internal/plugin/installer/http_installer_test.go
rm -fv internal/plugin/installer/installer_test.go
rm -fv internal/plugin/installer/vcs_installer_test.go
rm -fv internal/plugin/runtime_extismv1_test.go
rm -fv pkg/action/pull_test.go
rm -fv pkg/downloader/cache_test.go
rm -fv pkg/downloader/chart_downloader_test.go
rm -fv pkg/downloader/manager_test.go
rm -fv pkg/engine/engine_test.go

go test -p 2 ./...

%files
%doc README.md
%license LICENSE
%{_bindir}/helm

%files bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%files fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
