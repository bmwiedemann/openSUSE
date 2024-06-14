#
# spec file for package caddy
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


Name:           caddy
Version:        2.8.4
Release:        0
Summary:        Fast, multi-platform web server with automatic HTTPS
License:        Apache-2.0
Group:          Productivity/Networking/Web/Proxy
URL:            https://caddyserver.com/
# bug https://github.com/golang/go/issues/29228
Source0:        https://github.com/caddyserver/%{name}/releases/download/v%{version}/%{name}_%{version}_buildable-artifact.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        https://github.com/caddyserver/dist/raw/v%{version}/config/Caddyfile
Source3:        caddy.service
Source4:        https://github.com/caddyserver/dist/raw/v%{version}/welcome/index.html
Source5:        caddy.sysusers
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  golang(API) >= 1.22
%{?systemd_requires}
%{sysusers_requires}

%description
Caddy is a powerful, extensible platform to serve your sites, services, and
apps, written in Go.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH completion script for %{name}, generated during the build.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish shell completion script for %{name}, generated during the build.

%prep
%autosetup -a 1 -c

%build
# Build the binary.
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -v -x

%check
# Execute binary and check version
[[ "$(./%{name} version)" == "v%{version}" ]] || exit 1

%install
install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# configuration
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/Caddyfile

# service
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/%{name}

# welcome page
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/index.html

# bash completion
install -d -p -m 0755 %{buildroot}%{_datadir}/bash-completion/completions
./%{name} completion bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# zsh completion
install -d -p -m 0755 %{buildroot}%{_datadir}/zsh/site-functions
./%{name} completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

# fish completion
install -d -p -m 0755 %{buildroot}%{_datadir}/fish/vendor_completions.d
./%{name} completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# man pages
./%{name} manpage --directory %{buildroot}%{_mandir}/man8

%sysusers_generate_pre %{SOURCE5} %{name} %{name}.conf

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -n %{name}}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc AUTHORS README.md
%{_mandir}/man8/caddy*.8%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_sysusersdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/Caddyfile
%dir %attr(0750, %{name}, %{name}) %{_sharedstatedir}/%{name}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
