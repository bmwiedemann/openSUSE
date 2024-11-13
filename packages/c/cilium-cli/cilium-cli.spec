#
# spec file for package cilium-cli
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


%define executable_name cilium

Name:           cilium-cli
Version:        0.16.20
Release:        0
Summary:        CLI to install, manage & troubleshoot Kubernetes clusters running Cilium
License:        Apache-2.0
URL:            https://github.com/cilium/cilium-cli
Source:         cilium-cli-%{version}.tar.gz
Source1:        vendor.tar.gz
# download the file to make maintenance easier
Source11:       https://raw.githubusercontent.com/cilium/cilium/main/stable.txt
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.23
BuildRequires:  zsh

%description
CLI to install, manage and troubleshoot Kubernetes clusters running Cilium

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
CILIUM_VERSION="$(cat %{SOURCE11})"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/cilium/cilium/cilium-cli/defaults.Version=${CILIUM_VERSION} \
   -X github.com/cilium/cilium/cilium-cli/defaults.CLIVersion=v%{version}" \
   -o %{executable_name} ./cmd/cilium/

%install
# Install the binary.
install -D -m 0755 %{executable_name} %{buildroot}/%{_bindir}/%{executable_name}
cd %{buildroot}/%{_bindir}/
ln -s %{executable_name} %{name}

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

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{executable_name}

%changelog
