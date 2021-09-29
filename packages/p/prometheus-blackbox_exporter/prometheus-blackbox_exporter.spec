#
# spec file for package prometheus-blackbox_exporter
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
BuildRequires:  libcap-progs
BuildRequires:  golang(API) >= 1.14
%{go_nostrip}
%{?systemd_ordering}
Requires(pre):  user(prometheus)
Requires(pre):  group(prometheus)

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

%pre
%service_add_pre prometheus-blackbox_exporter.service

%post
%service_add_post prometheus-blackbox_exporter.service
if [ -x %{_sbindir}/setcap ]; then
    %{_sbindir}/setcap cap_net_raw=ep %{_bindir}/blackbox_exporter
fi

%preun
%service_del_preun prometheus-blackbox_exporter.service

%postun
%service_del_postun prometheus-blackbox_exporter.service

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/blackbox_exporter
%{_unitdir}/prometheus-blackbox_exporter.service
%dir %{_sysconfdir}/prometheus
%config(noreplace) %{_sysconfdir}/prometheus/blackbox.yml

%changelog
