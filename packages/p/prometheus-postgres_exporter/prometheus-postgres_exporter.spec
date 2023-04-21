#
# spec file for package prometheus-postgres_exporter
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?rhel} == 8
%global debug_package %{nil}
%endif

%if 0%{?rhel}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

%{go_nostrip}

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define project github.com/prometheus-community/postgres_exporter
Name:           prometheus-postgres_exporter
Version:        0.10.1
Release:        0
Obsoletes:      golang-github-wrouesnel-postgres_exporter < %version-%release
Provides:       golang-github-wrouesnel-postgres_exporter = %version-%release
Summary:        Prometheus exporter for PostgreSQL
License:        Apache-2.0
Group:          System/Management
URL:            https://prometheus.io/
Source:         postgres_exporter-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        prometheus-postgres_exporter.service
Source3:        prometheus-postgres_exporter.sysconfig
# This patch has been applied before generating vendor tarball
Patch1:         0001-Update-prometheus-exporter-toolkit-to-0.7.3.patch
BuildRequires:  fdupes
BuildRequires:  golang-github-prometheus-promu
BuildRequires:  golang-packaging
ExcludeArch:    s390
%if 0%{?rhel}
BuildRequires:  golang >= 1.14
Requires(pre):  shadow-utils
%else
BuildRequires:  golang(API) >= 1.14
Requires(pre):  user(prometheus)
Requires(pre):  group(prometheus)
Requires(pre):  shadow
%endif
%{?systemd_requires}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
%{go_provides}

%description
Prometheus exporter for PostgreSQL server metrics. Supported PostgreSQL versions: 9.1 and up.

%prep
%autosetup -a 1 -n postgres_exporter-%{version}

# Avoid "Unknown lvalue 'XXX' in section 'Service'" errors from systemd on older releases
%if 0%{?sle_version} && 0%{?sle_version} < 150300 || 0%{?rhel} && 0%{?rhel} < 9
sed -r -i '/^(Protect(Clock|Home|Hostname|KernelLogs)|PrivateMounts)=/d' %{SOURCE2}
%endif

%build
%goprep github.com/prometheus-community/postgres_exporter
GOPATH=%{_builddir}/go promu build -v

%install
install -D -m 0755 %{_builddir}/postgres_exporter-%{version}/postgres_exporter %{buildroot}/%{_bindir}/prometheus-postgres_exporter

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/prometheus-postgres_exporter.service
install -D -m 0645 %{SOURCE3} %buildroot%{_fillupdir}/sysconfig.prometheus-postgres_exporter
%fdupes %{buildroot}

%pre
%if 0%{?rhel}
%define serviceuser prometheus
getent group %{serviceuser} >/dev/null || %{_sbindir}/groupadd -r %{serviceuser}
getent passwd %{serviceuser} >/dev/null || %{_sbindir}/useradd -r -g %{serviceuser} -d %{_localstatedir}/lib/%{serviceuser} -M -s /sbin/nologin %{serviceuser}
%else
%service_add_pre %{name}.service
%endif

%post
%if 0%{?rhel}
%systemd_post %{name}.service
%else
%service_add_post %{name}.service
%fillup_only -n %{name}
%endif

%preun
%if 0%{?rhel}
%systemd_preun %{name}.service
%else
%service_del_preun %{name}.service
%endif

%postun
%if 0%{?rhel}
%systemd_postun %{name}.service
%else
%service_del_postun %{name}.service
%endif

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/prometheus-postgres_exporter
%{_fillupdir}/sysconfig.prometheus-postgres_exporter
%{_unitdir}/prometheus-postgres_exporter.service

%changelog
