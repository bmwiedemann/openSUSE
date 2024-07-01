#
# spec file for package golang-github-prometheus-prometheus
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017 Silvio Moioli <moio@suse.com>
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


# Compatibility with systems older than Nov 2017
# See https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros
%if ! %{defined _fillupdir}
%define _fillupdir /var/adm/fillup-templates
%endif
%if 0%{?suse_version} < 1500
%define _sharedstatedir /var/lib
%endif

Name:           golang-github-prometheus-prometheus
Version:        2.53.0
Release:        0
Summary:        The Prometheus monitoring system and time series database
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://prometheus.io/
# also includes web assets generated with `make assets`
Source:         prometheus-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        web-ui-%{version}.tar.gz
Source3:        prometheus.service
Source4:        prometheus.yml
Source5:        prometheus.sysconfig
Source6:        prometheus.firewall.xml
Source7:        npm_licenses.tar.bz2
Source8:        Makefile
Source9:        PACKAGING_README.md
Patch1:         0001-Do-not-force-the-pure-Go-name-resolver.patch
# Lifted from Debian's prometheus package
Patch2:         0002-Default-settings.patch
BuildRequires:  fdupes
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150300
BuildRequires:  firewall-macros
%endif
# Adding glibc-devel-static seems to be required for linking if building
# with -buildmode=pie
BuildRequires:  glibc-devel-static
BuildRequires:  golang-github-prometheus-promu >= 0.14.0
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.21
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1500
Recommends:     firewalld-prometheus-config
%endif
Requires(pre):  user(prometheus)
Requires(pre):  group(prometheus)
Requires(post): %fillup_prereq
Provides:       prometheus = %{version}
ExcludeArch:    s390
%systemd_ordering

%go_nostrip

%description
Prometheus's main features are:
 - a multi-dimensional data model (time series identified by metric name and key/value pairs)
 - a flexible query language to leverage this dimensionality
 - no reliance on distributed storage; single server nodes are autonomous
 - time series collection happens via a pull model over HTTP
 - pushing time series is supported via an intermediary gateway
 - targets are discovered via service discovery or static configuration
 - multiple modes of graphing and dashboarding support

%prep
%setup -q -a1 -n prometheus-%{version}
%autosetup -D -a2 -p1 -n prometheus-%{version}

%build
%goprep github.com/prometheus/prometheus
GOPATH=%{_builddir}/go promu build -v

%install
install -D -m0755 %{_builddir}/prometheus-%{version}/prometheus %{buildroot}/%{_bindir}/prometheus
install -D -m0755 %{_builddir}/prometheus-%{version}/promtool %{buildroot}/%{_bindir}/promtool
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/prometheus.service

install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/prometheus/prometheus.yml

install -d -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcprometheus

install -m 0755 -d %{buildroot}%{_datarootdir}/prometheus
cp -fr console_libraries/ consoles/ %{buildroot}%{_datarootdir}/prometheus

install -m 0755 -d %{buildroot}%{_fillupdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.prometheus

%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150300
install -m 0755 -d %{buildroot}%{_prefix}/lib/firewalld/services/
install -m 0644 %{SOURCE6} %{buildroot}%{_prefix}/lib/firewalld/services/prometheus.xml
%endif

install -Dd -m 0750 %{buildroot}%{_localstatedir}/lib/prometheus
install -Dd -m 0750 %{buildroot}%{_localstatedir}/lib/prometheus/data
install -Dd -m 0750 %{buildroot}%{_localstatedir}/lib/prometheus/metrics

install -D -m0644 %{SOURCE7} %{buildroot}/%{_defaultlicensedir}/%{name}/npm_licenses.tar.bz2
%gofilelist

%fdupes %{buildroot}/%{_prefix}

%pre
%service_add_pre prometheus.service

%post
%fillup_only -n prometheus
%service_add_post prometheus.service
%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150300
%firewalld_reload
%endif

%preun
%service_del_preun prometheus.service

%postun
%service_del_postun prometheus.service

%verifyscript
%fillup_only -n prometheus

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%license %{_defaultlicensedir}/%{name}
%{_bindir}/prometheus
%{_bindir}/promtool
%{_unitdir}/prometheus.service
%{_sbindir}/rcprometheus
%{_datarootdir}/prometheus
%{_fillupdir}/sysconfig.prometheus
%dir %attr(0700,prometheus,prometheus) %{_sharedstatedir}/prometheus
%dir %attr(0700,prometheus,prometheus) %{_sharedstatedir}/prometheus/data
%dir %attr(0700,prometheus,prometheus) %{_sharedstatedir}/prometheus/metrics
%dir %{_sysconfdir}/prometheus
%config(noreplace) %{_sysconfdir}/prometheus/prometheus.yml

%if 0%{?suse_version} == 1500 && 0%{?sle_version} < 150300
%package -n firewalld-prometheus-config
Summary:        Firewalld configuration file for Prometheus
Group:          Productivity/Networking/Security
Version:        0.1
Release:        0
License:        GPL-2.0-or-later
Requires:       firewalld

%description -n firewalld-prometheus-config
This package contains configuration file for Prometheus for older versions of
Firewalld which do not provide this in own package.

%files -n firewalld-prometheus-config
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/prometheus.xml
%endif

%changelog
