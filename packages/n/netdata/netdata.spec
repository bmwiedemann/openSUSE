#
# spec file for package netdata
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


%define netdata_user    netdata
%define netdata_group   netdata
%define godplugin_version 0.18.0
Name:           netdata
Version:        1.22.1
Release:        0
Summary:        A system for distributed real-time performance and health monitoring
# netdata is GPL-3.0+, other licenses refer to included third-party software (see REDISTRIBUTED.md)
License:        GPL-3.0-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-or-later AND OFL-1.1 AND CC-BY-4.0 AND Apache-2.0 AND WTFPL
Group:          System/Monitoring
URL:            http://my-netdata.io/
Source0:        https://github.com/netdata/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1:        https://github.com/netdata/go.d.plugin/archive/v%{godplugin_version}.tar.gz#/go.d.plugin-v%{godplugin_version}.tar.gz
Source2:        vendor.tar.gz
Source3:        netdata-rpmlintrc
Patch0:         netdata-logrotate-su.patch
Patch2:         netdata-smartd-log-path.patch
BuildRequires:  cups-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  git-core
%if 0%{?suse_version} > 1500
BuildRequires:  go >= 1.13
%endif
BuildRequires:  judy-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnetfilter_acct)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
Requires(pre):  shadow
Recommends:     PyYAML
Recommends:     curl
Recommends:     iproute-tc
Recommends:     lm_sensors
Recommends:     nmap-ncat curl openssl(cli)
Recommends:     python
Recommends:     python2-PyMySQL
Recommends:     python2-psycopg2
Suggests:       logrotate
Suggests:       nodejs
%ifarch i586 x86_64
BuildRequires:  pkgconfig(libipmimonitoring)
%endif

%description
netdata is a system for distributed real-time performance and health monitoring.
It provides insights, in real-time, of everything happening on the system it
runs on (including applications such as web and database servers),
using interactive web dashboards.

%prep
%setup -q -n %{name}-v%{version}
%patch0
%patch2 -p1
sed -i 's,/usr/bin/env bash,/bin/bash,' claim/%{name}-claim.sh.in

%if 0%{?suse_version} > 1500
tar xf %{S:1}
cd go.d.plugin-%{godplugin_version}
tar xf %{S:2}
%endif

%build
export GOFLAGS=-mod=vendor
%configure \
    --docdir="%{_docdir}/%{name}-%{version}" \
    --enable-plugin-nfacct \
%ifarch i586 x86_64
    --enable-plugin-freeipmi \
%endif
    --enable-plugin-cups \
    --with-zlib \
    --with-math \
    --with-user=%{netdata_user} \
    %{?conf}
%make_build

%if 0%{?suse_version} > 1500
cd go.d.plugin-%{godplugin_version}
go vet ./...

go build -ldflags='-s -w' \
%ifnarch ppc64
    -buildmode=pie \
%endif
    -o bin/go.d.plugin github.com/netdata/go.d.plugin/cmd/godplugin
%endif

%install
%make_install
find %{buildroot} -name .keep -delete
install -D -m 0644 system/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 system/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -m 0644 system/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

sed -i 's,^#!%{_bindir}/env bash,#!/bin/bash,;s,^#!%{_bindir}/env sh,#!/bin/sh,' \
    %{buildroot}%{_libexecdir}/%{name}/plugins.d/* \
    %{buildroot}%{_sysconfdir}/%{name}/edit-config
%fdupes -s %{buildroot}

# This should be opt-in, not opt-out. I do not believe most users would agree
# with sending usage data to Google Analytics, whether anonymized or not.
# Hence, disable statistics by default.
touch %{buildroot}%{_sysconfdir}/%{name}/.opt-out-from-anonymous-statistics

%if 0%{?suse_version} > 1500
cd go.d.plugin-%{godplugin_version}
cp -r config/* %{buildroot}%{_libdir}/%{name}/conf.d
install -m0755 -p bin/go.d.plugin %{buildroot}%{_libexecdir}/%{name}/plugins.d/go.d.plugin
%endif

install -m 755 -d %{buildroot}%{_localstatedir}/cache/%{name}
install -m 755 -d %{buildroot}%{_localstatedir}/log/%{name}
install -m 755 -d %{buildroot}%{_localstatedir}/lib/%{name}/registry

%pre
getent group %{netdata_group} >/dev/null || \
    %{_sbindir}/groupadd -r %{netdata_group}
getent passwd %{netdata_user} >/dev/null || \
    %{_sbindir}/useradd -r -g %{netdata_group} -s /bin/false \
    -c "netdata daemon user" -d %{_localstatedir}/lib/empty %{netdata_user}
%{_sbindir}/usermod -g %{netdata_group} %{netdata_user} >/dev/null
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE REDISTRIBUTED.md

%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/edit-config
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%config(noreplace) %{_sysconfdir}/%{name}/.opt-out-from-anonymous-statistics
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%{_libexecdir}/%{name}
%{_libdir}/%{name}

%{_sbindir}/%{name}
%{_sbindir}/%{name}-claim.sh
%{_sbindir}/%{name}cli
%{_sbindir}/rc%{name}

%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/cache/%{name}
%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/log/%{name}
%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/lib/%{name}

%attr(-,root,%{netdata_group}) %dir %{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}/health.d
%dir %{_sysconfdir}/%{name}/python.d
%dir %{_sysconfdir}/%{name}/statsd.d

%{_unitdir}/%{name}.service

%defattr(0644,root,%{netdata_group},0755)
%{_datadir}/%{name}/web

%changelog
