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
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14
Requires(post): %fillup_prereq
Requires(pre):  shadow
%{?systemd_ordering}

%{go_nostrip}
%{go_provides}

%description
Reverse proxy designed for Prometheus exporters

%prep
%autosetup -a1 -n %{repo}-%{version}

%build
%goprep %{import_path}
%gobuild --mod=vendor "" ...

%install
%goinstall
%gosrc
%gofilelist

install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/prometheus-exporter_exporter.service
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcprometheus-exporter_exporter
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{repo}.yaml
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{repo}.d

%fdupes %{buildroot}/%{_prefix}

%check
%gotest --mod=vendor "" ...

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
%service_del_postun prometheus-exporter_exporter.service

%files -f file.lst
%doc README.md LICENSE
%{_bindir}/%{repo}
%{_unitdir}/prometheus-exporter_exporter.service
%{_sbindir}/rcprometheus-exporter_exporter
%config %{_sysconfdir}/%{repo}.yaml
%{_sysconfdir}/%{repo}.d

%license LICENSE

%changelog
