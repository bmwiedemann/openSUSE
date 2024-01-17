#
# spec file for package golang-github-vpenso-prometheus_slurm_exporter
#
# Copyright (c) 2021 SUSE LLC
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

Name:           golang-github-vpenso-prometheus_slurm_exporter
Version:        0.20
Release:        0
Summary:        Prometheus exporter for Slurm metrics
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/vpenso/prometheus-slurm-exporter
Source0:        https://github.com/vpenso/prometheus-slurm-exporter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        README.SUSE
Patch0:         use_sbin.patch
Patch1:         Adjust-GPU-data-gathering-to-work-with-all-Slurm-versions-since-18.08.patch
BuildRequires:  golang-packaging
%{?systemd_requires}
Requires(pre):  shadow
%{go_provides}
Requires:       /usr/bin/sinfo
Requires:       /usr/bin/squeue

%description
Prometheus collector and exporter for metrics extracted from the Slurm
resource scheduling system.

%prep
%setup -q -n prometheus-slurm-exporter-%{version}
%setup -q -n prometheus-slurm-exporter-%{version} -T -D -a 1
%autopatch -p1

%build
%{goprep} github.com/vpenso/prometheus-slurm-exporter
%{gobuild} -mod=vendor ""

%install
%{goinstall}
# No %%{gosrc}
install -D -m 0644 lib/systemd/prometheus-slurm-exporter.service %{buildroot}%{_unitdir}/prometheus-slurm-exporter.service
sed -i -e '/ExecStart/s@^\(.*\)$@\1 $PROMETHEUS_SLURM_EXPORTER_ARGS@' \
    -e '/\[Service\]/a EnvironmentFile=-%{_sysconfdir}/sysconfig/prometheus-slurm-exporter' \
    %{buildroot}%{_unitdir}/prometheus-slurm-exporter.service
# To handle service file rename
ln -sf prometheus-slurm-exporter.service %{buildroot}%{_unitdir}/prometheus-slurm_exporter.service
install -m 0755 -d %{buildroot}%{_fillupdir}
echo -e '# prometheus-slurm-exporter args\n'\
'# possible values: -gpus-acct, -listen-address string\n'\
'PROMETHEUS_SLURM_EXPORTER_ARGS=""' > \
    %{buildroot}%{_fillupdir}/sysconfig.prometheus-slurm-exporter
mv %{buildroot}%{_bindir}/ %{buildroot}%{_sbindir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcprometheus-slurm-exporter
cp %{S:2} .
%{gofilelist}

%pre
%service_add_pre prometheus-slurm-exporter.service
getent group prometheus >/dev/null || %{_sbindir}/groupadd -r prometheus
getent passwd prometheus >/dev/null || %{_sbindir}/useradd -r -g prometheus -d %{_localstatedir}/lib/prometheus -M -s /sbin/nologin prometheus

%post
%service_add_post prometheus-slurm-exporter.service
%{fillup_only -n prometheus-slurm-exporter}

%preun
%service_del_preun prometheus-slurm-exporter.service

%postun
%service_del_postun prometheus-slurm-exporter.service

%files -f file.lst
%license LICENSE
%doc README.md
%doc %{basename:cp %{S:2}}
%{_fillupdir}/sysconfig.prometheus-slurm-exporter
%{_sbindir}/prometheus-slurm-exporter
%{_unitdir}/prometheus-slurm-exporter.service
%{_unitdir}/prometheus-slurm_exporter.service
%{_sbindir}/rcprometheus-slurm-exporter

%changelog
