#
# spec file for package grafana
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           grafana
Version:        11.3.0
Release:        0
Summary:        The open-source platform for monitoring and observability
License:        AGPL-3.0-only
Group:          System/Monitoring
URL:            http://grafana.org/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}-rpmlintrc
# Instructions on the build process
Source3:        README
# Makefile to automate build process
Source4:        Makefile
Source5:        0001-Add-source-code-reference.patch
Patch2:         0002-Use-bash-instead-of-env.patch
# CVE-2024-45337 Bump golang.org/x/crypto
Patch4:         0004-Bump-crypto.patch
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  wire
BuildRequires:  golang(API) >= 1.21
Requires(post): %fillup_prereq
Requires:       group(grafana)
Requires:       user(grafana)
%systemd_ordering

# Exclude s390 on SLE12, since golang 1.14 itself is not built for this arch on SLE12
# See https://build.suse.de/package/view_file/SUSE:SLE-12:Update/go1.14/go1.14.spec?expand=1
%if 0%{?suse_version} == 1315
ExcludeArch:    s390
%endif

%description
A graph and dashboard builder for visualizing time series metrics.

Grafana provides ways to create, explore, and share
dashboards and data with teams.

%prep
%setup -q -n grafana-%{version}
%autosetup -T -D -a 1 -p1 -n grafana-%{version}

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
wire gen -tags 'oss' ./pkg/server
go build -o . -ldflags '-X main.version=%{version}' ./pkg/cmd/...

%install

# install binaries and service
install -Dm755 %{name} %{buildroot}%{_libexecdir}/%{name}/%{name}
install -Dm755 %{name}-server %{buildroot}%{_libexecdir}/%{name}/%{name}-server
install -Dm755 %{name}-cli %{buildroot}%{_libexecdir}/%{name}/%{name}-cli
install -Dm644 {packaging/rpm/systemd/,%{buildroot}%{_unitdir}/}%{name}-server.service
install -dm755 %{buildroot}%{_sbindir}
install -m755 --target-directory=%{buildroot}%{_sbindir} packaging/wrappers/%{name}*

# create "rc symlink" (https://en.opensuse.org/openSUSE:Systemd_packaging_guidelines#rc_symlink)
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-server

# add symlink to binary where systemd unit file expects it to be
install -dm755 %{buildroot}%{_datadir}/%{name}/bin
ln -s %{_libexecdir}/%{name}/%{name} %{buildroot}%{_datadir}/%{name}/bin/%{name}

install -Dm644 packaging/rpm/sysconfig/%{name}-server \
%{buildroot}%{_fillupdir}/sysconfig.%{name}-server

install -d -m0750 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m0750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m0755 %{buildroot}/%{_localstatedir}/lib/%{name}/plugins
install -d -m0755 %{buildroot}/%{_localstatedir}/lib/%{name}/dashboards
install -d -m0755 %{buildroot}%{_sysconfdir}/%{name}/provisioning/dashboards

install -Dm640 conf/sample.ini %{buildroot}%{_sysconfdir}/%{name}/%{name}.ini
install -Dm640 {conf/,%{buildroot}%{_sysconfdir}/%{name}/}ldap.toml
install -Dm644 {conf/,%{buildroot}%{_datadir}/%{name}/conf/}defaults.ini
install -m644 {conf/,%{buildroot}%{_datadir}/%{name}/conf/}sample.ini
install -Dm644 {conf/provisioning/dashboards/,%{buildroot}%{_datadir}/%{name}/conf/provisioning/dashboards/}sample.yaml
install -Dm644 {conf/provisioning/datasources/,%{buildroot}%{_datadir}/%{name}/conf/provisioning/datasources/}sample.yaml
cp -pr public %{buildroot}%{_datadir}/%{name}/
install -d -m755 %{buildroot}%{_datadir}/%{name}/vendor
install -d -m755 %{buildroot}%{_datadir}/%{name}/tools

# Do *not* use %%fudpes -s -- this will result in grafana failing to load
# all the plugins (something in the plugin scanner can't cope with files
# in there being symlinks).
%fdupes %{buildroot}/%{_datadir}

%check
#gotest github.com/grafana/grafana/pkg...

%pre
%service_add_pre %{name}-server.service

%post
%{fillup_only -n %{name}-server}
%service_add_post %{name}-server.service

%preun
%service_del_preun %{name}-server.service

%postun
%service_del_postun %{name}-server.service

%files
%defattr(-,root,root)
%license LICENSE*
%doc CHANGELOG*
%{_sbindir}/%{name}*
%{_sbindir}/rc%{name}-server
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}*
%{_unitdir}/%{name}-server.service
%{_fillupdir}/sysconfig.%{name}-server
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/provisioning
%attr(0755,root,root) %dir %{_sysconfdir}/%{name}/provisioning/dashboards
%attr(0755,root,grafana) %dir %{_datadir}/%{name}/conf
%attr(0640,root,grafana) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.ini
%attr(0640,root,grafana) %config(noreplace) %{_sysconfdir}/%{name}/ldap.toml
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/%{name}
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/%{name}/plugins
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/%{name}/dashboards
%attr(0750,grafana,grafana) %dir %{_localstatedir}/log/%{name}
%doc %{_datadir}/%{name}/conf/sample.ini
%doc %{_datadir}/%{name}/conf/provisioning/dashboards/sample.yaml
%doc %{_datadir}/%{name}/conf/provisioning/datasources/sample.yaml
%config %{_datadir}/%{name}/conf/defaults.ini
%{_datadir}/%{name}

%changelog
