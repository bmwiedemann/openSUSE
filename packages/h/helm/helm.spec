#
# spec file for package helm
#
# Copyright (c) 2021 SUSE LLC
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
%define git_commit c4e74854886b2efe3321e185578e6db9be0a6e29
%define git_dirty clean

Name:           helm
Version:        3.5.4
Release:        0
Summary:        The Kubernetes Package Manager
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/helm/helm
Source0:        https://github.com/helm/helm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.14
%{go_provides}

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -qa1

%build
%goprep %{goipath}
%gobuild -mod vendor -buildmode pie -ldflags "-X %{goipath}/internal/version.version=%{version} -X %{goipath}/internal/version.gitCommit=%{git_commit} -X %{goipath}/internal/version.gitTreeState=%{git_dirty}" cmd/helm

%install
%goinstall
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/helm completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/helm completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/helm

%files bash-completion
%defattr(-,root,root)
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%changelog
