#
# spec file for package cryptctl
#
# Copyright (c) 2022 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           cryptctl
Version:        2.4
Release:        0
Summary:        A utility for setting up LUKS-based disk encryption
License:        GPL-3.0-only
Group:          System/Management
URL:            https://www.suse.com/products/sles-for-sap
Source0:        %{name}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  go
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       btrfsprogs
Requires:       cryptsetup
Requires:       e2fsprogs
Requires:       rsync
Requires:       util-linux
Requires:       xfsprogs
ExclusiveArch:  x86_64 ppc64le
%{?systemd_requires}

%define SRCDIR  src/github.com/SUSE

%description
A disk encryption utility that helps setting up LUKS-based disk encryption using
randomly generated keys, and keep all keys on a dedicated key server.

%prep
mkdir -p %{SRCDIR}
cd %{SRCDIR}
tar xf %{S:0}

%build
export GOPATH=$(pwd)
cd %{SRCDIR}/%{name}
gzip ospackage/man/cryptctl.8
go mod init
go build -buildmode=pie

%install
cd %{SRCDIR}/%{name}
mkdir -p %{buildroot}/%{_sbindir}
install -m 0755 %{name} %{buildroot}/%{_sbindir}/

# Sysconfig files
mkdir -p %{buildroot}/%{_fillupdir}/
pushd ospackage/etc/sysconfig
for conf in *; do
    install -m 0644 "$conf" "%{buildroot}/%{_fillupdir}/sysconfig.$conf"
done
popd

# One manual page
install -D -m 0644 ospackage/man/cryptctl.8.gz %{buildroot}/%{_mandir}/man8/cryptctl.8.gz

# Three systemd services
install -D -m 0644 ospackage/svc/cryptctl-auto-unlock@.service %{buildroot}/%{_unitdir}/cryptctl-auto-unlock@.service
install -D -m 0644 ospackage/svc/cryptctl-server.service %{buildroot}/%{_unitdir}/cryptctl-server.service
install -D -m 0644 ospackage/svc/cryptctl-client.service %{buildroot}/%{_unitdir}/cryptctl-client.service
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rccryptctl-server
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rccryptctl-client

# One udev rule
install -D -m 0644 ospackage/udev/99-cryptctl-auto-unlock.rules %{buildroot}/%{_udevrulesdir}/99-cryptctl-auto-unlock.rules

# Runtime and TLS certificate dir
install -d -m 0700 %{buildroot}/%{_localstatedir}/lib/%{name}
install -d -m 0700 %{buildroot}/%{_sysconfdir}/%{name}/servertls

%pre
%service_add_pre cryptctl-server.service cryptctl-client.service

%post
%service_add_post cryptctl-server.service cryptctl-client.service
%fillup_only -n cryptctl-server
%fillup_only -n cryptctl-client

%preun
%service_del_preun cryptctl-server.service cryptctl-client.service

%postun
%service_del_postun cryptctl-server.service cryptctl-client.service

%files
%defattr(-,root,root)
%{_fillupdir}/*
%dir %{_localstatedir}/lib/%{name}
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/servertls
%{_sbindir}/%{name}
%{_sbindir}/rccryptctl-server
%{_sbindir}/rccryptctl-client
%{_mandir}/man8/*
%{_unitdir}/cryptctl-server.service
%{_unitdir}/cryptctl-client.service
%{_unitdir}/cryptctl-auto-unlock@.service
%{_udevrulesdir}/99-cryptctl-auto-unlock.rules
%doc %{SRCDIR}/%{name}/LICENSE

%changelog
