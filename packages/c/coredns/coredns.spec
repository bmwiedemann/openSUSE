#
# spec file for package coredns
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


%define project github.com/coredns/coredns
Name:           coredns
Version:        1.11.4
Release:        0
Summary:        DNS server written in Go
License:        Apache-2.0
Group:          Productivity/Networking/DNS/Servers
URL:            https://coredns.io
Provides:       dns_daemon
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source10:       Corefile
Source11:       coredns.service
BuildRequires:  fdupes
BuildRequires:  golang(API) >= 1.21

%description
CoreDNS is a DNS server in Go. It has a plugin architecture for
extending it.

CoreDNS can listen for DNS request coming in over UDP/TCP (RFC 1035),
TLS (RFC 7858) and gRPC (not a standard).

%package extras
Summary:        Extra components for the %{name} package
Group:          Productivity/Networking/DNS/Servers
Requires:       %{name} = %{version}
Supplements:    %{name}
BuildArch:      noarch
BuildRequires:  pkgconfig(systemd)

%description extras
Extra components for the %{name} package, to make %{name} usable in a
non-containerized environment (man pages, configuration, unit file).

%prep
%autosetup -a1 -p1

%build

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
rm -rf $HOME/go/src
mkdir -pv $HOME/go/src/%{project}
find . -mindepth 1 -maxdepth 1 -exec cp -r {} $HOME/go/src/%{project} \;

cd $HOME/go/src/%{project}
go generate coredns.go
go build -mod=vendor -v -buildmode=pie -o coredns

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.
go test ./... -skip="TestZoneExternalCNAMELookupWithProxy|TestReadme|TestCorefile1|TestView"

%install
cd $HOME/go/src/%{project}

# Binaries
install -D -m 0755 %{name} %{buildroot}%{_sbindir}/%{name}
ln -s service %{buildroot}%{_sbindir}/rccoredns
# Configuration
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/%{name}/Corefile
# systemd service
install -D -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}.service
# Manpages
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 man/coredns*.1 %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_mandir}/man5
install -m 0644 man/corefile*.5 %{buildroot}/%{_mandir}/man5
install -d %{buildroot}/%{_mandir}/man7
install -m 0644 man/coredns-*.7 %{buildroot}/%{_mandir}/man7

%fdupes %{buildroot}/%{_prefix}

%pre extras
%service_add_pre %{name}.service

%post extras
%service_add_post %{name}.service
%{fillup_only -n coredns}

%preun extras
%service_del_preun %{name}.service

%postun extras
%service_del_postun %{name}.service

%files
# Binaries
%{_sbindir}/coredns
# License
%license LICENSE

%files extras
%{_sbindir}/rccoredns
# Manpages
%{_mandir}/man1/coredns*
%{_mandir}/man5/corefile*
%{_mandir}/man7/coredns-*
# Configs
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/Corefile
%{_unitdir}/%{name}.service

%changelog
