#
# spec file for package etcd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           etcd
Version:        3.3.11
Release:        0
Summary:        Highly-available key value store for configuration and service discovery
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/coreos/etcd
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}.conf
Source2:        %{name}.service
Source5:        README.security
BuildRequires:  golang-packaging
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  golang(API) = 1.11
# go1.11.3 contains sec. fixes bsc#1118897(CVE-2018-16873) bsc#1118897(CVE-2018-16873) bsc#1118899(CVE-2018-16875)
BuildRequires:  go1.11 >= 1.11.3
ExcludeArch:    %ix86
Requires(post): %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390
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
%setup -q
cp %{SOURCE5} .

%build
%{goprep} github.com/coreos/etcd
%{gobuild} cmd/etcd
%{gobuild} cmd/etcdctl

%install
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib

# Service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}/%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Sysconfig
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
%ifarch aarch64
# arm64 is not yet officially supported
echo -e "\n#Enable arm64\nETCD_UNSUPPORTED_ARCH=arm64\n" >> %{buildroot}%{_fillupdir}/sysconfig.%{name}
%endif

# Additional
install -d -m 750 %{buildroot}%{_localstatedir}/lib/%{name}

# Move
mv %{buildroot}%{_bindir}/etcd %{buildroot}%{_sbindir}/%{name}

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
%defattr(-,root,root)
%doc CONTRIBUTING.md README.md DCO NOTICE README.security
%license LICENSE
%{_sbindir}/%{name}

# Service
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

# Sysconfig
%{_fillupdir}/sysconfig.%{name}

# Additional
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}

%files -n etcdctl
%defattr(-,root,root)
%{_bindir}/etcdctl

%changelog
