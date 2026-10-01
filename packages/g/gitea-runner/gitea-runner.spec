#
# spec file for package gitea-runner
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


Name:           gitea-runner
Version:        4.0.1
Release:        0
Summary:        Gitea Runner for Gitea Actions
License:        MIT
URL:            https://gitea.com/gitea/runner
Source:         runner-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        gitea-runner.service
Source3:        gitea-runner.sysusers
Source4:        gitea-runner.rpmlintrc
BuildRequires:  golang(API) >= 1.27
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%sysusers_requires

%description
Gitea Runner for Gitea Actions is based on Gitea's fork of act.
By default, this runner runs as root, providing full, zero-configuration
compatibility with the host's system-wide Docker and Podman sockets.

A system group 'gitea-runner' is created, and the configuration and state
directories are owned by this group with secure permissions (0750 for config
dir, 0640 for config.yaml, and 0770 for state dir). This allows administrators
to easily run the service under an unprivileged user in the 'gitea-runner' group
by overriding the service file settings (User and Group) via systemd drop-ins.

%prep
%autosetup -p1 -n runner-%{version} -a 1

%build
%sysusers_generate_pre %{SOURCE3} gitea-runner
export GOFLAGS="$GOFLAGS -buildmode=pie -mod=vendor -trimpath"
go build -ldflags "-X gitea.com/gitea/runner/internal/pkg/ver.version=v%{version}" -o %{name}
./%{name} config generate > config.yaml

%install
install -D -m 0644 %{SOURCE2}  %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3}  %{buildroot}%{_sysusersdir}/gitea-runner.conf
install -D -m 0755 %{name}     %{buildroot}%{_bindir}/gitea-runner
install -D -m 0770 -d          %{buildroot}%{_localstatedir}/lib/gitea-runner
install -D -m 0750 -d          %{buildroot}%{_sysconfdir}/%{name}
install    -m 0640 config.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml

%check
./%{name} --version

%pre -f gitea-runner.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/gitea-runner
%{_unitdir}/%{name}.service
%{_sysusersdir}/gitea-runner.conf
%attr(0750,root,gitea-runner) %dir %{_sysconfdir}/%{name}
%attr(0640,root,gitea-runner) %config(noreplace) %{_sysconfdir}/%{name}/config.yaml
%attr(0770,root,gitea-runner) %dir %{_localstatedir}/lib/gitea-runner

%changelog
