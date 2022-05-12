#
# spec file for package golang-github-czerwonk-ping_exporter
#
# Copyright (c) 2022 SUSE LLC
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

Name:           golang-github-czerwonk-ping_exporter
Version:        0.4.5
Release:        0
Summary:        Prometheus exporter for ICMP echo requests
License:        MIT
URL:            https://github.com/czerwonk/ping_exporter
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        ping_exporter.yaml
Source3:        ping_exporter.service
Patch0:         harden_ping_exporter.service.patch
BuildRequires:  golang-packaging
Requires(post): %fillup_prereq
ExcludeArch:    s390
%systemd_ordering

%description
This is a simple server that scrapes go-ping stats and exports them via HTTP
for Prometheus consumption.

%prep
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -T -D -a 1
%patch0 -p1

%build
%{goprep} github.com/czerwonk/ping_exporter
%{gobuild} -mod=vendor ""

%install
%{goinstall}
%{gosrc}
%{gofilelist}

install -Dm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/ping_exporter.yaml
install -Dm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/ping_exporter.service

%pre
%service_add_pre ping_exporter.service

%post
%{fillup_only -n ping_exporter}
%service_add_post ping_exporter.service

%preun
%service_del_preun ping_exporter.service

%postun
%service_del_postun ping_exporter.service

%files -f file.lst
%license LICENSE
%doc README.md
%{_bindir}/ping_exporter
%config(noreplace) %{_sysconfdir}/ping_exporter.yaml
%{_unitdir}/ping_exporter.service

%changelog
