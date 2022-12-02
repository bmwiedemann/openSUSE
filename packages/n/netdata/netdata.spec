#
# spec file for package netdata
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


%define netdata_user    netdata
%define netdata_group   netdata
%define godplugin_version 0.45.0
Name:           netdata
Version:        1.37.0
Release:        0
Summary:        A system for distributed real-time performance and health monitoring
# netdata is GPL-3.0+, other licenses refer to included third-party software (see REDISTRIBUTED.md)
License:        Apache-2.0 AND BSD-2-Clause AND GPL-3.0-or-later AND MIT AND BSD-3-Clause AND LGPL-2.1-or-later AND OFL-1.1 AND CC-BY-4.0 AND WTFPL
Group:          System/Monitoring
URL:            http://my-netdata.io/
Source0:        https://github.com/netdata/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1:        https://github.com/netdata/go.d.plugin/archive/v%{godplugin_version}.tar.gz#/go.d.plugin-v%{godplugin_version}.tar.gz
Source2:        vendor.tar.gz
Source3:        netdata-rpmlintrc
Patch0:         netdata-logrotate-su.patch
BuildRequires:  cups-devel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  judy-devel
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libmosquitto)
BuildRequires:  pkgconfig(libnetfilter_acct)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(yajl)
BuildRequires:  pkgconfig(zlib)
Requires(pre):  shadow
Recommends:     PyYAML
Recommends:     curl
Recommends:     iproute-tc
Recommends:     lm_sensors
Recommends:     nmap-ncat
Recommends:     openssl(cli)
Suggests:       logrotate
Suggests:       nodejs
# suse_version is set to 1500 even for 15.2
%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
BuildRequires:  go >= 1.13
BuildRequires:  python3
%else
BuildRequires:  python2
%endif
%ifnarch ppc64 ppc64le armv7l s390x
BuildRequires:  pkgconfig(xenstat)
%endif
%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
Recommends:     python3
Recommends:     python3-PyMySQL
Recommends:     python3-psycopg2
%else
Recommends:     python
Recommends:     python2-PyMySQL
Recommends:     python2-psycopg2
%endif
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
sed -i 's,%{_bindir}/env bash,/bin/bash,' claim/%{name}-claim.sh.in

%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
sed -i 's,^pybinary=.*,pybinary=%{_bindir}/python3,' collectors/python.d.plugin/python.d.plugin.in

tar xf %{SOURCE1}
cd go.d.plugin-%{godplugin_version}
tar xf %{SOURCE2}
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

%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
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

# Respect FHS
mv %{buildroot}%{_sysconfdir}/%{name}/edit-config %{buildroot}%{_libexecdir}/%{name}
sed -i 's|%{_prefix}/lib|%{_libdir}|' %{buildroot}%{_libexecdir}/%{name}/edit-config

# This should be opt-in, not opt-out.
# Disable statistics by default.
touch %{buildroot}%{_sysconfdir}/%{name}/.opt-out-from-anonymous-statistics

%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
pushd go.d.plugin-%{godplugin_version}

install -d -m 0755 %{buildroot}/%{_libdir}/%{name}/conf.d
cp -a config/* %{buildroot}/%{_libdir}/%{name}/conf.d

install -m0755 -p bin/go.d.plugin %{buildroot}%{_libexecdir}/%{name}/plugins.d/go.d.plugin
popd
%endif

install -m 755 -d %{buildroot}%{_localstatedir}/cache/%{name}
install -m 755 -d %{buildroot}%{_localstatedir}/log/%{name}
install -m 755 -d %{buildroot}%{_localstatedir}/lib/%{name}/registry

%fdupes %{buildroot}%{_libdir} %{buildroot}%{_libexecdir} %{buildroot}%{_datadir}

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
%doc README.md CHANGELOG.md
%license LICENSE REDISTRIBUTED.md

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%{_libexecdir}/%{name}
%{_libdir}/%{name}

%{_sbindir}/%{name}
%{_sbindir}/%{name}-claim.sh
%{_sbindir}/%{name}cli
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service

%attr(-,root,%{netdata_group}) %dir %{_datadir}/%{name}
%attr(-,root,%{netdata_group}) %{_datadir}/%{name}/web

%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/cache/%{name}
%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/log/%{name}
%attr(0750,%{netdata_user},root) %dir %{_localstatedir}/lib/%{name}

# Do not allow users to read netdata config dir and files as they can
# contain passwords!
%defattr(0640,root,%{netdata_group},0750)

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/health.d
%dir %{_sysconfdir}/%{name}/python.d
%dir %{_sysconfdir}/%{name}/statsd.d

%config(noreplace) %{_sysconfdir}/%{name}/.opt-out-from-anonymous-statistics
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
# used for statistics
%config %{_sysconfdir}/%{name}/.install-type

%attr(0750,root,%{netdata_group}) %{_libexecdir}/%{name}/edit-config

%changelog
