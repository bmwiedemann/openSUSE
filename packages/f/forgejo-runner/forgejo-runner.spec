#
# spec file for package forgejo-runner
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


Name:           forgejo-runner
Version:        5.0.2
Release:        0
Summary:        Daemon that connects to a Forgejo instance and runs CI jobs
License:        MIT
URL:            https://code.forgejo.org/forgejo/runner
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.23
Requires:       (podman or docker)

%description
A daemon that connects to a Forgejo instance and runs jobs for continous
integration. The installation and usage instructions are part of the Forgejo
documentation.
https://forgejo.org/docs/next/admin/actions/

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
%autosetup -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -tags="netgo osusergo" \
   -ldflags="-X gitea.com/gitea/act_runner/internal/pkg/ver.version=v%{version}" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# Install the service file.
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_userunitdir}/%{name}.service

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/%{name}

%check
bin/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_userunitdir}/forgejo-runner.service

%files -n %{name}-bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datadir}/zsh/site-functions/%{name}

%changelog
