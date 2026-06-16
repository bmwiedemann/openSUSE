#
# spec file for package mcp-server-systemd
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


%define gitname systemd-mcp
%define vers 0.3.4
#%%define verssuf -preview3
#%%define verssuf_plain %%(echo %%{verssuf} | sed 's/^-//')
Name:           mcp-server-systemd
Version:        %{vers}%{?verssuf_plain}
Release:        0
Summary:        Bindings to systemd via mcp
License:        MIT
URL:            https://github.com/openSUSE/systemd-mcp
Source0:        https://github.com/openSUSE/systemd-mcp/archive/refs/tags/v%{vers}%{?verssuf}.tar.gz#/%{name}-%{vers}%{?verssuf}.tar.gz
Source1:        vendor.tar.gz
Source2:        README-TESTING.md
BuildRequires:  dbus-1
BuildRequires:  go >= 1.24
BuildRequires:  libcap-progs
BuildRequires:  polkit
BuildRequires:  systemd-devel
# the server now itself checks if man is available
Recommends:      man
Recommends:     %{name}-gatekeeper

%description
mcp server which allows to
* list units/services
* start/stop/restart units/services
* enable/disable services
* list log

%package gatekeeper
Summary:        Contains the gatekeeper service to allow user access to system log
Requires:       %{name} = %{version}
%description gatekeeper
Contains the gatekeeper service which allows the user to access the system
logs. The service itself listens to a socket to which is sends the file descriptors
to the system log if authorized via polkit.

# integrated tests checking also the man tool call, so man is needed here
%package testsuite
Summary:        Internal test files for %{name} DO NOT INSTALL
Obsoletes:      %{name}-test <= %{version}
BuildArch:      noarch
Requires:       bats
Requires:       podman
Requires:       man
Requires:       go >= 1.24

%description testsuite
The bats based tests. For testing the rpm itself the env variables TEST_CONTAINER
TEST_BINARY must be set accordingly.

NOTE: THIS PACKAGE IS FOR TESTING PURPOSES ONLY.
IT IS INTENDED FOR USE BY QUALITY ASSURANCE AND REQUIRES A
DEDICATED TESTING ENVIRONMENT.

DO NOT INSTALL ON A PRODUCTION SYSTEM!

%prep
%autosetup -p1 -a1 -n %{gitname}-%{vers}%{?verssuf}

%build
make GOFLAGS="-buildmode=pie"
cp %{S:2} .

%install
make install DESTDIR=%{buildroot} GOFLAGS="-buildmode=pie"
# RPM automatically stores hardlinked files only once
ln %{buildroot}/%{_bindir}/%{gitname} %{buildroot}/%{_bindir}/%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcgatekeeper
#install tests
install -D -m 0755 test/integrated-tests.bats %{buildroot}%{_docdir}/%{name}/test/integrated-tests.bats
install -D -m 0755 test/keycloak-tests.bats %{buildroot}%{_docdir}/%{name}/test/keycloak-tests.bats
install -D -m 0755 test/unit-test.bats %{buildroot}%{_docdir}/%{name}/test/unit-test.bats
install -D -m 0644 test/bci-init-build.docker %{buildroot}%{_docdir}/%{name}/test/bci-init-build.docker

%pre gatekeeper
%service_add_pre gatekeeper.service gatekeeper.socket

%post gatekeeper
%service_add_post gatekeeper.service gatekeeper.socket

%preun gatekeeper
%service_del_preun gatekeeper.service gatekeeper.socket

%postun gatekeeper
%service_del_postun gatekeeper.service gatekeeper.socket

%check
# call test manul as man will fail in build env due to missing man pages
# and sdjournald due to wrong vendor in build env 
go test \
    github.com/openSUSE/systemd-mcp \
  	github.com/openSUSE/systemd-mcp/authkeeper	\
  	github.com/openSUSE/systemd-mcp/dbus \
  	github.com/openSUSE/systemd-mcp/internal/pkg/file	\
  	github.com/openSUSE/systemd-mcp/internal/pkg/journal \
  	github.com/openSUSE/systemd-mcp/internal/pkg/systemd \
  	github.com/openSUSE/systemd-mcp/internal/pkg/util	\
  	github.com/openSUSE/systemd-mcp/remoteauth \
    %{nil}

%files
%{_bindir}/%{gitname}
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%files gatekeeper
%{_sbindir}/gatekeeper
%{_sbindir}/rcgatekeeper
%{_datadir}/polkit-1/actions/com.suse.gatekeeper.policy
%{_unitdir}/gatekeeper.service
%{_unitdir}/gatekeeper.socket

%files testsuite
%doc README-TESTING.md
%dir %{_docdir}/%{name}/test
%{_docdir}/%{name}/test/integrated-tests.bats
%{_docdir}/%{name}/test/bci-init-build.docker
%{_docdir}/%{name}/test/keycloak-tests.bats
%{_docdir}/%{name}/test/unit-test.bats

%changelog
