#
# spec file for package prometheus-postgres_exporter
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Silvio Moioli <moio@suse.com>
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


%{go_nostrip}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define project github.com/prometheus-community/postgres_exporter
Name:           prometheus-postgres_exporter
Obsoletes:      golang-github-wrouesnel-postgres_exporter < %version-%release
Provides:       golang-github-wrouesnel-postgres_exporter = %version-%release
Version:        0.10.0
Release:        0
Summary:        Prometheus exporter for PostgreSQL
License:        Apache-2.0
Group:          System/Management
URL:            https://prometheus.io/
Source:         postgres_exporter-%{version}.tar.xz
Source1:        vendor.tar.gz
Source2:        prometheus-postgres_exporter.service
Source3:        prometheus-postgres_exporter.sysconfig
BuildRequires:  fdupes
BuildRequires:  golang-github-prometheus-promu
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.14
%{?systemd_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow
%{go_provides}

%description
Prometheus exporter for PostgreSQL server metrics. Supported PostgreSQL versions: 9.1 and up.

%prep
%autosetup -a 1 -n postgres_exporter-%{version}

%build
%goprep github.com/prometheus-community/postgres_exporter
GOPATH=%{_builddir}/go promu build -v

%install
install -D -m 0755 %{_builddir}/postgres_exporter-%{version}/postgres_exporter %{buildroot}/%{_bindir}/prometheus-postgres_exporter

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/prometheus-postgres_exporter.service
install -D -m 0645 %{SOURCE3} %buildroot%{_fillupdir}/sysconfig.prometheus-postgres_exporter
%fdupes %{buildroot}

%pre
%service_add_pre prometheus-postgres_exporter.service

%post
%fillup_only -n prometheus-postgres_exporter
%service_add_post prometheus-postgres_exporter.service

%preun
%service_del_preun prometheus-postgres_exporter.service

%postun
%service_del_postun prometheus-postgres_exporter.service

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/prometheus-postgres_exporter
%{_fillupdir}/sysconfig.prometheus-postgres_exporter
%{_unitdir}/prometheus-postgres_exporter.service

%changelog
