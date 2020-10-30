#
# spec file for package golang-github-QubitProducts-exporter_exporter
#
# Copyright (c) 2020 SUSE LLC
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


# build ids are not currently generated on RHEL/CentOS
%if 0%{?rhel}
%global debug_package %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         QubitProducts
%global repo            exporter_exporter
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0.4.0
Release:        0
Summary:        Reverse proxy designed for Prometheus exporters
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://%{provider_prefix}
Source0:        %{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        exporter_exporter.yaml
Source3:        prometheus-exporter_exporter.service
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14
%else
BuildRequires:  golang >= 1.14
%endif
%if 0%{?suse_version}
Requires(post): %fillup_prereq
Requires(pre):  shadow
%endif
%{?systemd_ordering}

%if 0%{?suse_version}
%{go_nostrip}
%{go_provides}
%endif

%description
Reverse proxy designed for Prometheus exporters

%prep
%autosetup -a1 -n %{repo}-%{version}

%build
%if 0%{?suse_version}
%goprep %{import_path}
%gobuild --mod=vendor "" ...
%else
mkdir -pv $HOME/go/src && cp -avr vendor/* $HOME/go/src/
go build -mod=vendor -ldflags "-v -buildmode=pie -compressdwarf=false" -o %{repo}
%endif

%install
# Binary
%if 0%{?suse_version}
%goinstall
%else
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{repo} %{buildroot}%{_bindir}/
%endif

# Service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/prometheus-exporter_exporter.service

# Configuration
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{repo}.yaml
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{repo}.d

%if 0%{?suse_version}
  %fdupes %{buildroot}/%{_prefix}
%endif

%check
%if 0%{?suse_version}
  %gotest --mod=vendor "" ...
%endif

%pre
%if 0%{?suse_version}
  %service_add_pre prometheus-exporter_exporter.service
%endif
getent group prometheus >/dev/null || %{_sbindir}/groupadd -r prometheus
getent passwd prometheus >/dev/null || %{_sbindir}/useradd -r -g prometheus -d %{_localstatedir}/lib/prometheus -M -s /sbin/nologin prometheus

%post
%if 0%{?suse_version}
  %service_add_post prometheus-exporter_exporter.service
  %fillup_only -n prometheus-exporter_exporter
%else
  %systemd_post prometheus-exporter_exporter.service
%endif

%preun
%if 0%{?suse_version}
  %service_del_preun prometheus-exporter_exporter.service
%else
  %systemd_preun prometheus-exporter_exporter.service
%endif

%postun
%if 0%{?suse_version}
  %service_del_postun prometheus-exporter_exporter.service
%else
  %systemd_postun prometheus-exporter_exporter.service
%endif

%files
%doc README.md LICENSE
%{_bindir}/%{repo}
%{_unitdir}/prometheus-exporter_exporter.service
%config %{_sysconfdir}/%{repo}.yaml
%{_sysconfdir}/%{repo}.d

%license LICENSE

%changelog
