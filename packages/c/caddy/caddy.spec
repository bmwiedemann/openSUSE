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


# SLE-12 _sharedstatedir was /usr/com, _localstatedir is /var as expected
# SLE-15+ _sharedstatedir is /var/lib, _localstatedir is /var
# _sharedstatedir used here as home directory for newly created user caddy
# If not redefined build fails with empty /usr/com not owned by any package
%if 0%{?suse_version} < 1500
%define _sharedstatedir /var/lib
%endif

Name:           caddy
Version:        2.8.4
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
Source7:        caddy.sysusers
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  golang(API) >= 1.21
%{?systemd_requires}
%{sysusers_requires}

%description
Caddy is a powerful, extensible platform to serve your sites, services, and
apps, written in Go.

It operates primarily at L4 (transport layer) and L7 (application layer) of
the OSI model, though it has the ability to work with other layers.

%prep
%autosetup -a 1

%build
# Build the binary.
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

%check
# execute the binary as a basic check
./%{name} --help

%install
install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# configuration
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/Caddyfile

# service
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
install -Dpm0644 %{SOURCE7} %{buildroot}%{_sysusersdir}/%{name}.conf

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/%{name}

# welcome page
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/index.html

# bash completion
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%sysusers_generate_pre %{SOURCE7} %{name} %{name}.conf

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
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_sysusersdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/Caddyfile
%dir %attr(0750, %{name}, %{name}) %{_sharedstatedir}/%{name}
# filesystem owns all the parent directories here
%{_datadir}/bash-completion/completions/%{name}
# own parent directories in case zsh is not installed
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
