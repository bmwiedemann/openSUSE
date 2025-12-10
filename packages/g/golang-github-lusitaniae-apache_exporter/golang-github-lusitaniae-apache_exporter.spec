#
# spec file for package golang-github-lusitaniae-apache_exporter
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2019 João Cavalheiro <jcavalheiro@suse.com>
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


%if 0%{?rhel}
%if 0%{?rhel} >= 8
# Found compressed .debug_abbrev section, not attempting dwz compression
# DWARF version 0 unhandled
%global debug_package %{nil}
%endif
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

%if 0%{?suse_version} && 0%{?suse_version} < 1600
%bcond_without apparmor
%else
%bcond_with apparmor
%endif

%if %{with apparmor} && 0%{?suse_version} > 1320
%bcond_without apparmor_reload
%else
%bcond_with apparmor_reload
%endif

# Templating vars to simplify and standardize Prometheus exporters spec files
%define	githubrepo    github.com/lusitaniae/apache_exporter
%define	upstreamname  apache_exporter
%define	targetname    prometheus-apache_exporter
%define	serviceuser   prometheus

Name:           golang-github-lusitaniae-apache_exporter
Version:        1.0.10
Release:        0
Summary:        Apache Exporter for Prometheus
License:        MIT
Group:          System/Management
URL:            http://%{githubrepo}
Source:         %{upstreamname}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{targetname}.service
Source3:        apparmor-usr.bin.%{targetname}
BuildRequires:  fdupes
BuildRequires:  golang-github-prometheus-promu
%if 0%{?rhel}
BuildRequires:  golang >= 1.20
Requires(pre):  shadow-utils
%else
BuildRequires:  golang(API) >= 1.23
Requires(pre):  shadow
%if %{with apparmor}
%if %{with apparmor_reload}
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Recommends:     apparmor-abstractions
%else
BuildRequires:  apparmor-profiles
%endif
%endif
%endif
ExcludeArch:    s390
%{?systemd_ordering}

%description
Exports apache mod_status statistics via HTTP for Prometheus consumption.

%prep
%autosetup -a1 -n %{upstreamname}-%{version}

%build
GOPATH=%{_builddir}/go promu build -v

%install
install -D -m 0755 %{_builddir}/%{upstreamname}-%{version}/%{upstreamname}-%{version} %{buildroot}/%{_bindir}/%{targetname}
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{targetname}
%if %{with apparmor}
# AppArmor profile
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.%{targetname}
%endif

%check
%if 0%{?rhel}
# Fix OBS debug_package execution.
rm -f %{buildroot}/usr/lib/debug%{_bindir}/%{targetname}-%{version}-*.debug
rm -rf %{buildroot}%{_usrsrc}/debug/%{name}-%{version}-*
%endif

%pre
%if 0%{?suse_version}
%service_add_pre %{targetname}.service
%endif
getent group %{serviceuser} >/dev/null || %{_sbindir}/groupadd -r %{serviceuser}
getent passwd %{serviceuser} >/dev/null || %{_sbindir}/useradd -r -g %{serviceuser} -d %{_localstatedir}/lib/%{serviceuser} -M -s /sbin/nologin %{serviceuser}

%post
%if 0%{?rhel}
%systemd_post %{targetname}.service
%else
%service_add_post %{targetname}.service
%if %{with apparmor_reload}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.%{targetname}
%endif
%endif

%preun
%if 0%{?rhel}
%systemd_preun %{targetname}.service
%else
%service_del_preun %{targetname}.service
%endif

%postun
%if 0%{?rhel}
%systemd_postun %{targetname}.service
%else
%service_del_postun %{targetname}.service
%endif

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{targetname}
%{_unitdir}/%{targetname}.service
%{_sbindir}/rc%{targetname}
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.bin.%{targetname}
%endif

%changelog
