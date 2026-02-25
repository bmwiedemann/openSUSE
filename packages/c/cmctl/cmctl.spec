#
# spec file for package cmctl
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


%define kubectl_plugin_name kubectl-cert_manager

Name:           cmctl
Version:        2.4.1
Release:        0
Summary:        CLI tool that can help you to manage cert-manager resources inside your cluster
License:        Apache-2.0
URL:            https://github.com/cert-manager/cmctl
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        README.md
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.25

%description
cmctl is a CLI tool that can help you to manage cert-manager resources inside your cluster.
While also available as a kubectl plugin, it is recommended to use as a stand alone binary as this allows the use of command auto-completion.

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
%autosetup -p1 -a 1
cp %{S:2} .

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-w -s -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build.name=cmctl \
   -X github.com/cert-manager/cert-manager/cmd/ctl/pkg/build/commands.registerCompletion=true \
   -X github.com/cert-manager/cert-manager/pkg/util.AppVersion=%{version} \
   -X github.com/cert-manager/cert-manager/pkg/util.AppGitCommit=v%{version}" \
   -o bin/cmctl ./

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"
cd %{buildroot}/%{_bindir}/
ln -s %{name} kubectl-cert_manager

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
%{buildroot}/%{_bindir}/%{kubectl_plugin_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{kubectl_plugin_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish
%{buildroot}/%{_bindir}/%{kubectl_plugin_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{kubectl_plugin_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}
%{buildroot}/%{_bindir}/%{kubectl_plugin_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{kubectl_plugin_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{kubectl_plugin_name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}
%{_datarootdir}/bash-completion/completions/%{kubectl_plugin_name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish
%{_datarootdir}/fish/vendor_completions.d/%{kubectl_plugin_name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}
%{_datarootdir}/zsh/site-functions/_%{kubectl_plugin_name}

%changelog
