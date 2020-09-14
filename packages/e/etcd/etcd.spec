#
# spec file for package etcd
#
# Copyright (c) 2020 SUSE LLC
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


%define project go.etcd.io/etcd
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           etcd
Version:        3.4.13
Release:        0
Summary:        Highly-available key value store for configuration and service discovery
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/etcd-io/etcd
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source11:       %{name}.conf
Source12:       %{name}.service
Source15:       README.security
BuildRequires:  golang(API) = 1.14
BuildRequires:  golang-packaging
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires(post): %fillup_prereq
ExcludeArch:    s390 %ix86
%{?systemd_requires}
%{go_provides}
# Make sure that the binary is not getting stripped.
%{go_nostrip}

%description
etcd is a distributed, consistent key-value store for shared configuration and
service discovery, with a focus on being:

- Simple: well-defined, user-facing API (gRPC)
- Secure: automatic TLS with optional client cert authentication
- Fast: benchmarked 10,000 writes/sec
- Reliable: properly distributed using Raft

%package -n etcdctl
Summary:        A simple command line client for etcd
Group:          System/Management

%description -n etcdctl
A command line client for etcd. It can be used in scripts or for administrators
to explore an etcd cluster.

%prep
%setup -q -a1
cp %{SOURCE15} .

%build
%{goprep} go.etcd.io/etcd
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}

cd $HOME/go/src/%{project}
go build -v -buildmode=pie -o etcd

cd $HOME/go/src/%{project}/etcdctl
go build -v -buildmode=pie -o etcdctl

%install
cd $HOME/go/src/%{project}

install -d %{buildroot}/%{_sbindir}
install -D -m 0755 etcd %{buildroot}/%{_sbindir}/etcd

install -d %{buildroot}/%{_bindir}
install -D -m 0755 etcdctl/etcdctl %{buildroot}/%{_bindir}/etcdctl

# Service
install -D -p -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Sysconfig
install -D -p -m 0644 %{SOURCE11} %{buildroot}%{_fillupdir}/sysconfig.%{name}
%ifarch aarch64
# arm64 is not yet officially supported
echo -e "\n#Enable arm64\nETCD_UNSUPPORTED_ARCH=arm64\n" >> %{buildroot}%{_fillupdir}/sysconfig.%{name}
%endif

# Additional
install -d -m 750 %{buildroot}%{_localstatedir}/lib/%{name}

%pre
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /bin/false -c "etcd daemon" %{name}
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
%doc CONTRIBUTING.md README.md DCO NOTICE README.security
%{_sbindir}/%{name}

# Service
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

# Sysconfig
%{_fillupdir}/sysconfig.%{name}

# Additional
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}

%files -n etcdctl
%{_bindir}/etcdctl

%changelog
