#
# spec file for package caddy
#
# Copyright (c) 2023 SUSE LLC
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


%define project github.com/caddyserver/caddy

Name:           caddy
Version:        2.6.3
Release:        0
Summary:        Fast, multi-platform web server with automatic HTTPS
License:        Apache-2.0
Group:          Productivity/Networking/Web/Proxy
URL:            https://caddyserver.com/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        Caddyfile
Source3:        caddy.service
Source4:        index.html
Source5:        bash-completion
Source6:        zsh-completion
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.18
%{?systemd_requires}
%{go_provides}
# Make sure that the binary is not getting stripped.
%{go_nostrip}

%description
Caddy is a powerful, extensible platform to serve your sites, services, and
apps, written in Go.

It operates primarily at L4 (transport layer) and L7 (application layer) of
the OSI model, though it has the ability to work with other layers.

%prep
%setup -q

%build
%{goprep} %{project}

# tarball causes "inconsistent vendoring"
tar -xf %{SOURCE1}

CGO_ENABLED=0

go build -v -buildmode=pie -mod=vendor -ldflags "-s -w" -o caddy cmd/caddy/main.go

%install
install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# configuration
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/Caddyfile

# service
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/%{name}

# welcome page
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/index.html

# bash completion
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%pre
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /bin/false -c "Caddy web server" %{name}
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
%{_bindir}/%{name}
%{_datadir}/%{name}

%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/Caddyfile
%attr(0750,%{name},%{name}) %dir %{_sharedstatedir}/%{name}
# filesystem owns all the parent directories here
%{_datadir}/bash-completion/completions/%{name}
# own parent directories in case zsh is not installed
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
