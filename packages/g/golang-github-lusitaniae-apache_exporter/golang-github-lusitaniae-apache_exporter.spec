#
# spec file for package golang-github-lusitaniae-apache_exporter
#
# Copyright (c) 2022 SUSE LLC
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
%global debug_package %{nil}
# Fix ERROR: No build ID note found in
%undefine _missing_build_ids_terminate_build
%endif

%bcond_without  apparmor

# Templating vars to simplify and standardize Prometheus exporters spec files
%define	githubrepo    github.com/lusitaniae/apache_exporter
%define	upstreamname  apache_exporter
%define	targetname    prometheus-apache_exporter
%define	serviceuser   prometheus

Name:           golang-github-lusitaniae-apache_exporter
Version:        0.11.0
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
BuildRequires:  golang-packaging
BuildRequires:  xz
%if 0%{?rhel}
BuildRequires:  golang >= 1.15
Requires(pre):  shadow-utils
%else
BuildRequires:  golang(API) = 1.15
Requires(pre):  shadow
%endif
%if %{with apparmor}
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Recommends:     apparmor-abstractions
%endif
ExcludeArch:    s390
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
Exports apache mod_status statistics via HTTP for Prometheus consumption.

%prep
%autosetup -a1 -n %{upstreamname}-%{version}

%build
%goprep %{githubrepo}
%gobuild -mod=vendor "" ...

%install
install -D -m0755 %{_builddir}/go/bin/%{upstreamname} %{buildroot}/%{_bindir}/%{targetname}
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{targetname}
%if %{with apparmor}
# AppArmor profile
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.%{targetname}
%endif

%check
%if 0%{?rhel}
# Fix OBS debug_package execution.
rm -f %{buildroot}/usr/lib/debug/%{_bindir}/%{targetname}-%{version}-*.debug
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
%endif
%if %{with apparmor}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.%{targetname}
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
