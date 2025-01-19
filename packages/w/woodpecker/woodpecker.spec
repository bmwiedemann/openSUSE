#
# spec file for package woodpecker
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


%define cli_package_name woodpecker-cli
%define cli_executable_name woodpecker-cli

%define agent_package_name woodpecker-agent
%define agent_executable_name woodpecker-agent

%define server_package_name woodpecker-server
%define server_executable_name woodpecker-server

Name:           woodpecker
Version:        3.0.0
Release:        0
Summary:        Simple yet powerful CI/CD engine with great extensibility
License:        Apache-2.0
URL:            https://github.com/woodpecker-ci/woodpecker
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        web-%{version}.tar.gz
Source3:        PACKAGING_README.md
Source4:        Makefile
Source11:       woodpecker-server.service
Source12:       woodpecker-agent.service
Source21:       system-user-woodpecker.conf
BuildRequires:  go >= 1.22

%description
Woodpecker is a simple yet powerful CI/CD engine with great extensibility

%package -n %{cli_package_name}
Summary:        CLI for the WoodpeckerCI system

%description -n %{cli_package_name}
Woodpecker is a simple yet powerful CI/CD engine with great extensibility. This
package contains the command line utility for the WoodpeckerCI system

%package -n %{agent_package_name}
Summary:        Agent for the WoodpeckerCI system
Requires:       user(woodpecker)

%description -n %{agent_package_name}
Woodpecker is a simple yet powerful CI/CD engine with great extensibility. This
package contains the agent binary and service.

%package -n %{server_package_name}
Summary:        WoodpeckerCI server
Requires:       user(woodpecker)

%description -n %{server_package_name}
Woodpecker is a simple yet powerful CI/CD engine with great extensibility. This
package contains the server binary and service.

%package -n system-user-%{name}
Summary:        System user and group woodpecker
BuildRequires:  sysuser-tools
BuildArch:      noarch
%sysusers_requires

%description -n system-user-%{name}
This package provides the system user for the woodpecker CI system.

%prep
%autosetup -p 1 -a 1
rm -rf web/
tar xvf %{SOURCE2}

%build
# CLI executable
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X go.woodpecker-ci.org/woodpecker/v3/version.Version=v%{version}" \
   -o bin/%{cli_executable_name} ./cmd/cli

# Agent executable
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X go.woodpecker-ci.org/woodpecker/v3/version.Version=v%{version}" \
   -o bin/%{agent_executable_name} ./cmd/agent

# Server
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X go.woodpecker-ci.org/woodpecker/v3/version.Version=v%{version}" \
   -o bin/%{server_executable_name} ./cmd/server

# system-user
%sysusers_generate_pre %{SOURCE21} user

%install
install -D -m 0755 bin/%{cli_executable_name} %{buildroot}/%{_bindir}/%{cli_executable_name}
install -D -m 0755 bin/%{agent_executable_name} %{buildroot}/%{_bindir}/%{agent_executable_name}
install -D -m 0755 bin/%{server_executable_name} %{buildroot}/%{_bindir}/%{server_executable_name}

install -d -m 0750 %{buildroot}%{_sysconfdir}/woodpecker/

install -d -m 0750 %{buildroot}%{_sharedstatedir}/woodpecker/

install -d -m 0755 %{buildroot}%{_unitdir}/
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/woodpecker-server.service
install -D -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/woodpecker-agent.service

# system user
install -Dm644 %{SOURCE21} %{buildroot}%{_sysusersdir}/system-user-woodpecker.conf

%check
bin/%{cli_executable_name} --version | grep %{version}
bin/%{agent_executable_name} --version | grep %{version}
bin/%{server_executable_name} --version | grep %{version}

%pre -n system-user-%{name} -f user.pre

%pre -n %{name}-server
%service_add_pre woodpecker-server.service

%post -n %{name}-server
%service_add_post woodpecker-server.service

%preun -n %{name}-server
%service_del_preun woodpecker-server.service

%postun -n %{name}-server
%service_del_postun woodpecker-server.service

%pre -n %{name}-agent
%service_add_pre woodpecker-agent.service

%post -n %{name}-agent
%service_add_post woodpecker-agent.service

%preun -n %{name}-agent
%service_del_preun woodpecker-agent.service

%postun -n %{name}-agent
%service_del_postun woodpecker-agent.service

%files -n %{cli_package_name}
%doc README.md
%license LICENSE
%{_bindir}/%{cli_executable_name}

%files -n %{agent_package_name}
%doc README.md
%license LICENSE
%{_bindir}/%{agent_executable_name}
%{_unitdir}/woodpecker-agent.service
%dir %attr(750,woodpecker,woodpecker) %{_sysconfdir}/woodpecker/
%config(noreplace) %attr(640,woodpecker,woodpecker) %ghost %{_sysconfdir}/woodpecker/woodpecker-agent.env
%dir %attr(750,woodpecker,woodpecker) %{_sharedstatedir}/woodpecker/

%files -n %{server_package_name}
%doc README.md
%license LICENSE
%{_bindir}/%{server_executable_name}
%{_unitdir}/woodpecker-server.service
%dir %attr(750,woodpecker,woodpecker) %{_sysconfdir}/woodpecker/
%config(noreplace) %attr(640,woodpecker,woodpecker) %ghost %{_sysconfdir}/woodpecker/woodpecker-server.env
%dir %attr(750,woodpecker,woodpecker) %{_sharedstatedir}/woodpecker/

%files -n system-user-%{name}
%{_sysusersdir}/system-user-woodpecker.conf

%changelog
