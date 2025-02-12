#
# spec file for package digger-cli
#
# Copyright (c) 2025 SUSE LLC
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


%define executable_name digger

Name:           digger-cli
Version:        0.6.85
Release:        0
Summary:        CLI for the digger open source IaC orchestration tool
License:        Apache-2.0
URL:            https://github.com/diggerhq/digger
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22
BuildRequires:  zsh

%description
CI/CD for Terraform is tricky. To make life easier, specialised CI systems aka
TACOS exist - Terraform Cloud, Spacelift, Atlantis, etc.

But why have 2 CI systems? Why not reuse the async jobs infrastructure with
compute, orchestration, logs, etc of your existing CI?

Digger runs terraform natively in your CI. This is:

* Secure, because cloud access secrets aren't shared with a third-party
* Cost-effective, because you are not paying for additional compute just to run
  your terraform

Features

* Terraform plan and apply in pull request comments
* Private runners - thanks to the fact that there are no separate runners! Your
  existing CI's compute environment is used
* Open Policy Agent (OPA) support for RBAC
* PR-level locks (on top of Terraform native state locks, similar to Atlantis)
  to avoid race conditions across multiple PRs
* Terragrunt, Workspaces, multiple Terraform versions, static analysis via
  Checkov, plan persistence, ...
* Drift detection

This package contains the digger CLI.

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
%autosetup -p 1
tar xvf %{SOURCE1} -C ./cli/

%build
cd ./cli/
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X digger/pkg/utils.version=v%{version}" \
   -o ../bin/%{executable_name} ./cmd/digger

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{executable_name}

%changelog
