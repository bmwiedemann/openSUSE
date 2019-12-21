#
# spec file for package golang-github-vpenso-prometheus_slurm_exporter
#
# Copyright (c) 2019 SUSE LLC
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

%define version 0.8

Name:           golang-github-vpenso-prometheus_slurm_exporter
Version:        0.8
Release:        0
Summary:        Prometheus exporter for Slurm metrics
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/vpenso/prometheus-slurm-exporter
Source0:        prometheus-slurm-exporter-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        go.mod
Source3:        README.packaging     
Source4:        update-tarball.sh
Patch0:         use_sbin.patch          
BuildRequires:  golang-packaging 
%{?systemd_requires}
Requires(pre):  shadow
%{go_provides}
Requires: /usr/bin/sinfo
Requires: /usr/bin/squeue

%description
Prometheus collector and exporter for metrics extracted from the Slurm 
resource scheduling system.

%prep
%setup -q -n prometheus-slurm-exporter-%{version}
%setup -q -n prometheus-slurm-exporter-%{version} -T -D -a 1
%patch0 -p1

%build
%{goprep} github.com/vpenso/prometheus-slurm-exporter
%{gobuild} -mod=vendor ""

%install
%{goinstall}
%{gosrc}
install -D -m 0644 lib/systemd/prometheus-slurm-exporter.service %{buildroot}%{_unitdir}/prometheus-slurm_exporter.service
mv %{buildroot}%{_bindir}/ %{buildroot}%{_sbindir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcprometheus-slurm_exporter
%{gofilelist}

%pre
%service_add_pre prometheus-slurm_exporter.service
getent group prometheus >/dev/null || %{_sbindir}/groupadd -r prometheus
getent passwd prometheus >/dev/null || %{_sbindir}/useradd -r -g prometheus -d %{_localstatedir}/lib/prometheus -M -s /sbin/nologin prometheus

%post
%service_add_post prometheus-slurm_exporter.service

%preun
%service_del_preun prometheus-slurm_exporter.service

%postun
%service_del_postun prometheus-slurm_exporter.service

%files -f file.lst
%license LICENSE
%doc README.md
%{_sbindir}/prometheus-slurm-exporter
%{_unitdir}/prometheus-slurm_exporter.service
%{_sbindir}/rcprometheus-slurm_exporter

%changelog
