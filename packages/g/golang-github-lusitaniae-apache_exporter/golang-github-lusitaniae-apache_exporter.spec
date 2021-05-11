#
# spec file for package golang-github-lusitaniae-apache_exporter
#
# Copyright (c) 2021 SUSE LLC
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


# Templating vars to simplify and standardize Prometheus exporters spec files
%define	githubrepo    github.com/lusitaniae/apache_exporter
%define	upstreamname  apache_exporter
%define	targetname    prometheus-apache_exporter
%define	serviceuser   prometheus

Name:           golang-github-lusitaniae-apache_exporter
Version:        0.7.0
Release:        0
Summary:        Apache Exporter for Prometheus
License:        MIT
Group:          System/Management
URL:            http://%{githubrepo}
Source:         %{upstreamname}-%{version}.tar.gz
Source1:        %{targetname}.service
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) = 1.15
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow

%description
Exports apache mod_status statistics via HTTP for Prometheus consumption.

%prep
%setup -q -n %{upstreamname}-%{version}

%build
%goprep %{githubrepo}
%gobuild

%install
install -D -m0755 %{_builddir}/go/bin/%{upstreamname} %{buildroot}/%{_bindir}/%{targetname}
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{targetname}

%pre
%service_add_pre %{targetname}.service
getent group %{serviceuser} >/dev/null || %{_sbindir}/groupadd -r %{serviceuser}
getent passwd %{serviceuser} >/dev/null || %{_sbindir}/useradd -r -g %{serviceuser} -d %{_localstatedir}/lib/%{serviceuser} -M -s /sbin/nologin %{serviceuser}

%post
%service_add_post %{targetname}.service

%preun
%service_del_preun %{targetname}.service

%postun
%service_del_postun %{targetname}.service

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{targetname}
%{_unitdir}/%{targetname}.service
%{_sbindir}/rc%{targetname}

%changelog
