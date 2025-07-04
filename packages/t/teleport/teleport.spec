#
# spec file for package teleport
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


Name:           teleport
Version:        17.5.3
Release:        0
Summary:        Identity-aware, multi-protocol access proxy
License:        AGPL-3.0-only
URL:            https://github.com/gravitational/teleport
Source:         %{name}-%{version}.tar.gz
# go vendoring
Source1:        vendor.tar.gz
Source2:        webassets.tar.gz
Source3:        teleport.service
Source4:        teleport.yaml
Source5:        tbot.yaml
# Rust vendoring
Source6:        vendor.tar.zst
BuildRequires:  bash-completion
BuildRequires:  cargo >= 1.82
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  go >= 1.23.7
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zsh
Requires:       teleport-tctl

%description
Teleport is the easiest, most secure way to access all your infrastructure.
Teleport is an identity-aware, multi-protocol access proxy which understands
SSH, HTTPS, RDP, Kubernetes API, MySQL, MongoDB and PostgreSQL wire protocols.

On the server-side, Teleport is a single binary which enables convenient secure
access to behind-NAT resources such as:
* SSH nodes - SSH works in browsers too!
* Kubernetes clusters
* PostgreSQL, MongoDB, CockroachDB and MySQL databases
* Internal Web apps
* Windows Hosts
* Networked servers

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%package -n %{name}-tctl
Summary:        CLI tool for managing a teleport server
License:        Apache-2.0

%package -n %{name}-tctl-bash-completion
Summary:        Bash Completion for %{name}-tctl
Group:          System/Shells
Requires:       %{name}-tctl = %{version}
Requires:       bash-completion
Supplements:    (%{name}-tctl and bash-completion)
BuildArch:      noarch

%description -n %{name}-tctl-bash-completion
Bash command line completion support for %{name}-tctl.

%package -n %{name}-tctl-zsh-completion
Summary:        Zsh Completion for %{name}-tctl
Group:          System/Shells
Requires:       %{name}-tctl = %{version}
Supplements:    (%{name}-tctl and zsh)
BuildArch:      noarch

%description -n %{name}-tctl-zsh-completion
zsh command line completion support for %{name}-tctl.

%description -n %{name}-tctl
An administrative tool that can configure Teleport Auth Service.

%package -n %{name}-tsh
Summary:        CLI tool for logging into nodes via Teleport SSH
License:        Apache-2.0

%description -n %{name}-tsh
A tool that lets end users interact with Teleport nodes. This replaces ssh.

%package -n %{name}-tsh-bash-completion
Summary:        Bash Completion for %{name}-tsh
Group:          System/Shells
Requires:       %{name}-tsh = %{version}
Requires:       bash-completion
Supplements:    (%{name}-tsh and bash-completion)
BuildArch:      noarch

%description -n %{name}-tsh-bash-completion
Bash command line completion support for %{name}-tsh.

%package -n %{name}-tsh-zsh-completion
Summary:        Zsh Completion for %{name}-tsh
Group:          System/Shells
Requires:       %{name}-tsh = %{version}
Supplements:    (%{name}-tsh and zsh)
BuildArch:      noarch

%description -n %{name}-tsh-zsh-completion
zsh command line completion support for %{name}-tsh.

%package -n teleport-tbot
Summary:        CLI tool for Machine ID
License:        Apache-2.0

%description -n teleport-tbot
Machine ID is a service that programmatically issues and renews short-lived
certificates to any service account (e.g., a CI/CD server) by retrieving
credentials from the Teleport Auth Service. This enables fine-grained
role-based access controls and audit.
tbot is the executable belonging to the Machine ID service.

%package -n %{name}-tbot-bash-completion
Summary:        Bash Completion for %{name}-tbot
Group:          System/Shells
Requires:       %{name}-tbot = %{version}
Requires:       bash-completion
Supplements:    (%{name}-tbot and bash-completion)
BuildArch:      noarch

%description -n %{name}-tbot-bash-completion
Bash command line completion support for %{name}-tbot.

%package -n %{name}-tbot-zsh-completion
Summary:        Zsh Completion for %{name}-tbot
Group:          System/Shells
Requires:       %{name}-tbot = %{version}
Supplements:    (%{name}-tbot and zsh)
BuildArch:      noarch

%description -n %{name}-tbot-zsh-completion
zsh command line completion support for %{name}-tbot.

%package -n teleport-fdpass-teleport
Summary:        Significantly reduce resource consumption by large numbers of SSH connections
License:        Apache-2.0

%description -n teleport-fdpass-teleport
fdpass-teleport can be optionally used by Machine ID to significantly reduce
resource consumption in use-cases that create large numbers of SSH connections
(e.g. Ansible).

%prep
%setup -q
%setup -q -T -D -a 1
%setup -q -T -D -a 2
tar xvf %{SOURCE6} -C tool/fdpass-teleport

%build

mkdir -p lib/web/build/webassets
cp -r webassets/teleport/* lib/web/build/webassets

go build \
   -tags "pam webassets_embed" \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-w -s -X main.VERSION=%{version}" \
   -o teleport ./tool/teleport
go build \
   -tags "pam" \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-w -s -X main.VERSION=%{version}" \
   -o tsh ./tool/tsh
go build \
   -tags "pam" \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-w -s -X main.VERSION=%{version}" \
   -o tbot ./tool/tbot
go build \
   -tags "pam" \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-w -s -X main.VERSION=%{version}" \
   -o tctl ./tool/tctl

cd tool/fdpass-teleport
%{cargo_build}

%install
# Install the binary.
install -D -m 0755 tsh "%{buildroot}/%{_bindir}/tsh"
install -D -m 0755 tctl "%{buildroot}/%{_bindir}/tctl"
install -D -m 0755 tbot "%{buildroot}/%{_bindir}/tbot"
install -D -m 0755 tool/fdpass-teleport/target/release/fdpass-teleport "%{buildroot}/%{_bindir}/fdpass-teleport"
install -D -m 0755 teleport "%{buildroot}/%{_sbindir}/teleport"
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/teleport.service
install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/teleport.yaml
install -D -m 644 examples/systemd/machine-id/machine-id.service %{buildroot}%{_unitdir}/
install -D -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/tbot.yaml

# teleport completions

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_sbindir}/teleport --completion-script-bash > %{buildroot}%{_datarootdir}/bash-completion/completions/teleport

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_sbindir}/teleport --completion-script-zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_teleport

# tctl completions

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/tctl --completion-script-bash > %{buildroot}%{_datarootdir}/bash-completion/completions/tctl

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/tctl --completion-script-zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_tctl

# tsh completions

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/tsh --completion-script-bash > %{buildroot}%{_datarootdir}/bash-completion/completions/tsh

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/tsh --completion-script-zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_tsh

# tbot completions

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/tbot --completion-script-bash > %{buildroot}%{_datarootdir}/bash-completion/completions/tbot

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/tbot --completion-script-zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_tbot

# teleport service

%pre -n teleport
%service_add_pre teleport.service

%post -n teleport
%service_add_post teleport.service

%preun -n teleport
%service_del_preun teleport.service

%postun -n teleport
%service_del_postun teleport.service

# machine-id service

%pre -n teleport-tbot
%service_add_pre machine-id.service

%post -n teleport-tbot
%service_add_post machine-id.service

%preun -n teleport-tbot
%service_del_preun machine-id.service

%postun -n teleport-tbot
%service_del_postun machine-id.service

%files -n teleport
%doc README.md
%license LICENSE
%{_sbindir}/teleport
%{_unitdir}/teleport.service
%config(noreplace) %{_sysconfdir}/teleport.yaml

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/teleport

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_teleport

%files -n teleport-tsh
%doc README.md
%license LICENSE
%{_bindir}/tsh

%files -n %{name}-tsh-bash-completion
%{_datarootdir}/bash-completion/completions/tsh

%files -n %{name}-tsh-zsh-completion
%{_datarootdir}/zsh/site-functions/_tsh

%files -n teleport-tctl
%doc README.md
%license LICENSE
%{_bindir}/tctl

%files -n %{name}-tctl-bash-completion
%{_datarootdir}/bash-completion/completions/tctl

%files -n %{name}-tctl-zsh-completion
%{_datarootdir}/zsh/site-functions/_tctl

%files -n teleport-tbot
%doc README.md
%license LICENSE
%{_bindir}/tbot
%{_unitdir}/machine-id.service
%config(noreplace) %{_sysconfdir}/tbot.yaml

%files -n %{name}-tbot-bash-completion
%{_datarootdir}/bash-completion/completions/tbot

%files -n %{name}-tbot-zsh-completion
%{_datarootdir}/zsh/site-functions/_tbot

%files -n teleport-fdpass-teleport
%doc README.md
%license LICENSE
%{_bindir}/fdpass-teleport

%changelog
