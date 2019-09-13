#
# spec file for package golang-github-lusitaniae-apache_exporter
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# Templating vars to simplify and standardize Prometheus exporters spec files
%define	githubrepo    github.com/boynux/squid-exporter
%define	upstreamname  squid-exporter
%define	targetname    prometheus-squid_exporter
%define	serviceuser   prometheus

Name:           golang-github-boynux-squid_exporter
Version:        1.6
Release:        0
License:        MIT
Summary:        Squid Prometheus Exporter
Url:            http://%{githubrepo}
Group:          System/Management
Source:         %{upstreamname}-%{version}.tar.gz
Source1:        %{targetname}.service
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow

%description
Exports squid metrics in Prometheus format

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
