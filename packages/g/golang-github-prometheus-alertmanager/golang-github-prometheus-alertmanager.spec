#
# spec file for package golang-github-prometheus-alertmanager
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


Name:           golang-github-prometheus-alertmanager
Version:        0.28.1
Release:        0
Summary:        Prometheus Alertmanager
License:        Apache-2.0
URL:            https://prometheus.io/
Group:          System/Monitoring
Source:         alertmanager-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        prometheus-alertmanager.service
Source3:        alertmanager.yml
# Lifted from Debian's alertmanager package
Patch1:         0001-Default-settings.patch
Patch2:         0002-Bump-x-net.patch
BuildRequires:  fdupes
BuildRequires:  golang-github-prometheus-promu >= 0.12.0
BuildRequires:  golang(API) >= 1.23
Requires(pre):  group(prometheus)
Requires(pre):  user(prometheus)
Provides:       prometheus-alertmanager = %{version}
ExcludeArch:    s390
%{?systemd_ordering}

%description
The Alertmanager handles alerts sent by client applications such as the
Prometheus server. It takes care of deduplicating, grouping, and routing
them to the correct receiver integration such as email, PagerDuty, or
OpsGenie. It also takes care of silencing and inhibition of alerts.

%prep
%autosetup -a1 -p1 -n alertmanager-%{version}

%build
%ifarch %{ix86} armv7l armv7hl s390x
export BUILD_CGO_FLAG="--cgo"
%endif
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
promu build -v $BUILD_CGO_FLAG

%install
install -D -m0755 %{_builddir}/alertmanager-%{version}/alertmanager %{buildroot}/%{_bindir}/prometheus-alertmanager
install -D -m0755 %{_builddir}/alertmanager-%{version}/amtool %{buildroot}/%{_bindir}/amtool
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/prometheus-alertmanager.service
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcprometheus-alertmanager
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/prometheus/alertmanager.yml
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/prometheus/alertmanager_templates
install -Dd -m 0750 %{buildroot}%{_localstatedir}/lib/prometheus
install -Dd -m 0750 %{buildroot}%{_localstatedir}/lib/prometheus/alertmanager
%fdupes %{buildroot}/%{_prefix}

%check
go test -short -x `go list ./... | grep -v cluster`
%{buildroot}%{_bindir}/prometheus-alertmanager --version
%{buildroot}%{_bindir}/amtool --version

%pre
%service_add_pre prometheus-alertmanager.service

%post
%service_add_post prometheus-alertmanager.service

%preun
%service_del_preun prometheus-alertmanager.service

%postun
%service_del_postun prometheus-alertmanager.service

%files
%doc README.md
%license LICENSE
%{_bindir}/prometheus-alertmanager
%{_bindir}/amtool
%{_unitdir}/prometheus-alertmanager.service
%{_sbindir}/rcprometheus-alertmanager
%dir %attr(0700, prometheus, prometheus) %{_localstatedir}/lib/prometheus
%dir %attr(0700, prometheus, prometheus) %{_localstatedir}/lib/prometheus/alertmanager
%dir %{_sysconfdir}/prometheus
%dir %{_sysconfdir}/prometheus/alertmanager_templates
%config(noreplace) %{_sysconfdir}/prometheus/alertmanager.yml

%changelog
