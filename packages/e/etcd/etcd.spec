#
# spec file for package etcd
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

%global etcd_default_file /etc/default/etcd

%define project go.etcd.io/etcd
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           etcd
Version:        3.6.6
Release:        0
Summary:        Reliable key-value store for the most critical data of a distributed system
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/etcd-io/etcd
Source:         %{name}-%{version}.tar.gz
Source1:        vendor-server.tar.gz
Source2:        vendor-etcdctl.tar.gz
Source3:        vendor-etcdutl.tar.gz
Source11:       %{name}.conf
Source12:       %{name}.service
Source13:       %{name}.sysconfig
Source14:       %{name}.sysuser
Source15:       README.security
Source16:       update-etcd-conf.sh
BuildRequires:  golang(API) >= 1.24
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xz
Requires(post): %fillup_prereq
Suggests:       etcdctl
Suggests:       etcdutl
ExcludeArch:    s390 %{ix86}
%sysusers_requires

%description
etcd is a distributed reliable key-value store for the most critical data of a
distributed system, with a focus on being:

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

%package -n etcdutl
Summary:        A simple command line client for etcd
Group:          System/Management

%description -n etcdutl
A command line administration utility for etcd.
It's designed to operate directly on etcd data files.

For operations over a network, please use `etcdctl`.

%prep
%autosetup
cp %{SOURCE15} .
tar -C server -xzf %{SOURCE1}
tar -C etcdctl -xzf %{SOURCE2}
tar -C etcdutl -xzf %{SOURCE3}

%build
%{goprep} %{project}

mkdir -p ./bin

dir=$(pwd)
for item in server etcdctl etcdutl;do
  cd "$dir/$item"
  go build -v \
    -buildmode=pie \
    -mod=vendor \
    -trimpath \
    -ldflags="-s -w -X main.Version=%{version}" \
    -o ../bin/"$item"
done
cd "$dir"

%sysusers_generate_pre %{SOURCE14} %{name} etcd.conf

%install
install -d %{buildroot}%{_sbindir}
install -D -m 0755 ./bin/server %{buildroot}%{_sbindir}/etcd

install -d %{buildroot}/%{_bindir}
install -D -m 0755 ./bin/etcdctl %{buildroot}%{_bindir}/etcdctl
install -D -m 0755 ./bin/etcdutl %{buildroot}%{_bindir}/etcdutl

# Service
install -D -p -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Sysconfig
install -D -p -m 0644 %{SOURCE13} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -D -p -m 0644 %{SOURCE11} %{buildroot}%{etcd_default_file}

# Additional
install -d -m 750 %{buildroot}%{_localstatedir}/lib/%{name}
install -Dm0644 %{SOURCE14} %{buildroot}%{_sysusersdir}/etcd.conf

%pre -f %{name}.pre
if [ ! -e %{etcd_default_file} -a -e /etc/sysconfig/etcd ] ; then
  echo "Migrating existing /etc/sysconfig/etcd to %{etcd_default_file}."
  echo "From now on only ETCD_OPTIONS should be in /etc/sysconfig/etcd"
  mv /etc/sysconfig/etcd %{etcd_default_file}
fi
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
%doc CONTRIBUTING.md README.md DCO README.security
%{_sbindir}/%{name}
%{_sysusersdir}/%{name}.conf

# Service
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

# Sysconfig
%{_fillupdir}/sysconfig.%{name}

%config(noreplace) %{etcd_default_file}

# Additional
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}

%files -n etcdctl
%{_bindir}/etcdctl
%doc etcdctl/README.md etcdctl/READMEv2.md

%files -n etcdutl
%{_bindir}/etcdutl
%doc etcdutl/README.md

%changelog
