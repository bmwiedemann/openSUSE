#
# spec file for package golang-github-prometheus-node_exporter
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Silvio Moioli <moio@suse.com>
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

Name:           golang-github-prometheus-node_exporter
Version:        0.18.1
Release:        0
Summary:        Prometheus exporter for machine metrics
License:        Apache-2.0
Group:          System/Management
Url:            https://prometheus.io/
Source:         node_exporter-v%{version}.tar.xz
Source1:        prometheus-node_exporter.service
Source2:        README
Source3:        update-tarball.sh
BuildRequires:  fdupes
BuildRequires:  go1.11
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow
%{go_provides}
Provides:       node_exporter
Provides:       prometheus(node_exporter)

%description
Prometheus exporter for hardware and OS metrics exposed by *NIX kernels, written in Go with pluggable metric collectors.

%prep
%setup -q -n node_exporter

%build
make collector/fixtures/sys/.unpacked  # unpacks text fixtures required by gotest
%goprep github.com/prometheus/node_exporter
%gobuild -mod=vendor ""

%install
%goinstall
%gosrc
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/prometheus-node_exporter.service
install -Dd -m 0755 %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcprometheus-node_exporter
%gofilelist
%fdupes %{buildroot}

%check
%gotest github.com/prometheus/node_exporter -mod=vendor

%pre
%service_add_pre prometheus-node_exporter.service
getent group prometheus >/dev/null || %{_sbindir}/groupadd -r prometheus
getent passwd prometheus >/dev/null || %{_sbindir}/useradd -r -g prometheus -d %{_localstatedir}/lib/prometheus -M -s /sbin/nologin prometheus

%post
%service_add_post prometheus-node_exporter.service

%preun
%service_del_preun prometheus-node_exporter.service

%postun
%service_del_postun prometheus-node_exporter.service

%files -f file.lst
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/node_exporter
%{_unitdir}/prometheus-node_exporter.service
%{_sbindir}/rcprometheus-node_exporter

%changelog
