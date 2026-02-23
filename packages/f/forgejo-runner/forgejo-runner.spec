#
# spec file for package forgejo-runner
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


%define services %{name}.service
Name:           forgejo-runner
Version:        12.7.0
Release:        0
Summary:        Daemon that connects to a Forgejo instance and runs CI jobs
License:        GPL-3.0-or-later
URL:            https://code.forgejo.org/forgejo/runner
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.25
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
Requires:       git-core
Requires:       (podman or docker)
%{?systemd_ordering}

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
   -ldflags="-X code.forgejo.org/forgejo/runner/v11/internal/pkg/ver.version=v%{version}" \
   -o bin/%{name}

bin/%{name} generate-config > config.yaml

perl -p -i -e 's|file: \.runner|file: /etc/forgejo-runner/runners|g' config.yaml

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# Install the service file.
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/%{name}.service

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/%{name}

install -D -m 0750 -d          %{buildroot}%{_sysconfdir}/%{name}
install    -m 0640 config.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml
install    -m 0640 /dev/null   %{buildroot}%{_sysconfdir}/%{name}/runners
install -D -m 0750 -d          %{buildroot}%{_localstatedir}/lib/%{name}

%pre
%service_add_pre %{services}

%preun
%service_del_preun %{services}

%post
%service_add_post %{services}

%postun
%service_del_postun %{services}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/forgejo-runner.service
%config(noreplace) %{_sysconfdir}/%{name}
%dir %{_localstatedir}/lib/%{name}

%files -n %{name}-bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datadir}/zsh/site-functions/%{name}

%changelog
