#
# spec file for package golang-github-QubitProducts-exporter_exporter
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        exporter_exporter.yaml
Source3:        prometheus-exporter_exporter.service

# Coreutils required for deterministic Build ID generation (sha1sum, cat)
BuildRequires:  coreutils

BuildRequires:  fdupes
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
BuildRequires:  gcc11-c++
%endif
BuildRequires:  golang(API) >= 1.23
Requires(post): %fillup_prereq
Requires(pre):  shadow
ExcludeArch:    s390
%{?systemd_ordering}

%if ! 0%{?suse_version}
ExclusiveArch:  do_not_build
%endif

%description
Reverse proxy designed for Prometheus exporters

%prep
%autosetup -a1 -n %{repo}-%{version}

%build
%ifarch s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl
export CGO_ENABLED=1
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
export CC=gcc-11
export CXX=g++-11
%endif
%endif
go build

%install
install -D -m 0755 %{repo} %{buildroot}/%{_bindir}/%{repo}

# Service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/prometheus-exporter_exporter.service

# Configuration
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{repo}.yaml
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{repo}.d

%fdupes %{buildroot}/%{_prefix}

%check
./%{repo} --help

%pre
%service_add_pre prometheus-exporter_exporter.service
getent group prometheus >/dev/null || %{_sbindir}/groupadd -r prometheus
getent passwd prometheus >/dev/null || %{_sbindir}/useradd -r -g prometheus -d %{_localstatedir}/lib/prometheus -M -s /sbin/nologin prometheus

%post
%service_add_post prometheus-exporter_exporter.service
%fillup_only -n prometheus-exporter_exporter

%preun
%service_del_preun prometheus-exporter_exporter.service

%postun
%systemd_postun prometheus-exporter_exporter.service

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{_bindir}/%{repo}
%{_unitdir}/prometheus-exporter_exporter.service
%config %{_sysconfdir}/%{repo}.yaml
%{_sysconfdir}/%{repo}.d

%changelog
