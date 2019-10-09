#
# spec file for package coredns
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.3.1
Release:        0
Summary:        DNS server written in Go
License:        Apache-2.0
Group:          Productivity/Networking/DNS/Servers
URL:            https://coredns.io
Provides:       dns_daemon
Source0:        %{name}-%{version}.tar.xz
Source1:        golang-protobuf.tar.xz
Source2:        matttproud-golang_protobuf_extensions.tar.xz
Source3:        mholt-caddy.tar.xz
Source4:        miekg-dns.tar.xz
Source5:        prometheus-client_golang.tar.xz
Source6:        prometheus-client_model.tar.xz
Source7:        prometheus-common.tar.xz
Source8:        prometheus-procfs.tar.xz
Source9:        beorn7-perks.tar.xz
Source10:       Corefile
Source11:       coredns.service
BuildRequires:  fdupes
BuildRequires:  golang(API) >= 1.12

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
%setup -q -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 -b9

%build

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
rm -rf $HOME/go/src

declare -A sources2Path=( \
[%{SOURCE0}]=%{project} \
[%{SOURCE1}]=github.com/golang/protobuf \
[%{SOURCE2}]=github.com/matttproud/golang_protobuf_extensions \
[%{SOURCE3}]=github.com/mholt/caddy \
[%{SOURCE4}]=github.com/miekg/dns \
[%{SOURCE5}]=github.com/prometheus/client_golang \
[%{SOURCE6}]=github.com/prometheus/client_model \
[%{SOURCE7}]=github.com/prometheus/common \
[%{SOURCE8}]=github.com/prometheus/procfs \
[%{SOURCE9}]=github.com/beorn7/perks \
)
for s in "${!sources2Path[@]}"; do
    dest="$HOME/go/src/${sources2Path[$s]}"
    mkdir -pv "$dest"
    dir=$(basename "$s")
    dir=${dir%.tar.xz}
    cp -a "%{_builddir}/$dir"/* "$dest"
done

# code.google.com redirects to github.com/golang/protobuf, but code is still
# referencing to the code.google.com package
mkdir -pv $HOME/go/src/code.google.com/p
ln -s $HOME/go/src/github.com/golang/protobuf $HOME/go/src/code.google.com/p/goprotobuf

cd $HOME/go/src/%{project}
make %{?_smp_mflags} coredns CHECKS= BUILDOPTS="-v -buildmode=pie"

%check
# Too many tests fail due to the restricted permissions in the build enviroment.
# Updates must be tested manually.

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
