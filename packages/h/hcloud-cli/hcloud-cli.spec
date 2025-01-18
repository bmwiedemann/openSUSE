#
# spec file for package hcloud-cli
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


%define executable_name hcloud

Name:           hcloud-cli
Version:        1.50.0
Release:        0
Summary:        A command-line interface for Hetzner Cloud
License:        MIT
URL:            https://github.com/hetznercloud/cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22
BuildRequires:  zsh
Provides:       hcloud = %{version}

%description
hcloud is a command-line interface for interacting with Hetzner Cloud.

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
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -ldflags=" \
   -X github.com/hetznercloud/cli/internal/version.version=%{version} \
   -X github.com/hetznercloud/cli/internal/version.versionPrerelease=" \
   -o bin/%{executable_name} ./cmd/hcloud/main.go

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

%check
%{buildroot}/%{_bindir}/%{executable_name} version
%{buildroot}/%{_bindir}/%{executable_name} version | grep %{version}

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
