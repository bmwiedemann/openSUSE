#
# spec file for package prometheus-blackbox_exporter
#
# Copyright (c) 2023 SUSE LLC
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

Name:           prometheus-blackbox_exporter
Version:        0.19.0
Release:        0
Summary:        Prometheus blackbox prober exporter
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://prometheus.io/
Source0:        blackbox_exporter-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        prometheus-blackbox_exporter.service
BuildRequires:  fdupes
BuildRequires:  golang-packaging
%if 0%{?rhel}
BuildRequires:  golang >= 1.14
BuildRequires:  libcap
%else
%if 0%{?sle_version} == 150300
# Needed due to bsc#1203599
BuildRequires:  golang(API) = 1.18
%else
BuildRequires:  golang(API) >= 1.19
%endif
BuildRequires:  libcap-progs
%endif
%{?systemd_ordering}
%if 0%{?suse_version}
Requires(pre):  user(prometheus)
Requires(pre):  group(prometheus)
Requires(post): permissions
%endif
ExcludeArch:    s390

%description
Prometheus blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

%prep
%autosetup -a1 -n blackbox_exporter-%{version}

%build
%goprep github.com/prometheus/blackbox_exporter
%gobuild -mod=vendor "" ...

%install
%goinstall
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/prometheus-blackbox_exporter.service
install -D -m0644 %{_builddir}/blackbox_exporter-%{version}/blackbox.yml %{buildroot}%{_sysconfdir}/prometheus/blackbox.yml
%fdupes %{buildroot}/%{_prefix}

%check
# Fix OBS debug_package execution.
rm -f %{buildroot}/usr/lib/debug/%{_bindir}/blackbox_exporter-%{version}-*.debug

%pre
%if 0%{?rhel}
%define serviceuser   prometheus
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
%endif
# Because of more relaxed ping_group_range setting in sysctl in SLE/openSUSE 15
# everyone is allowed to create IPPROTO_ICMP sockets
# and hence no need to set capability
%if 0%{?suse_version} == 1315
  %set_permissions %{_bindir}/blackbox_exporter
%endif

%verifyscript
%if 0%{?suse_version} == 1315
  %verify_permissions -e %{_bindir}/blackbox_exporter
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
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%license LICENSE
%verify(not caps) %attr(755,root,root) %{_bindir}/blackbox_exporter
%{_unitdir}/prometheus-blackbox_exporter.service
%dir %{_sysconfdir}/prometheus
%config(noreplace) %{_sysconfdir}/prometheus/blackbox.yml

%changelog
