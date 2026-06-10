#
# spec file for package prometheus-blackbox_exporter
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


Name:           prometheus-blackbox_exporter
Version:        0.26.0
Release:        0
Summary:        Prometheus blackbox prober exporter
License:        Apache-2.0
Group:          System/Monitoring
URL:            https://prometheus.io/
Source0:        https://github.com/prometheus/blackbox_exporter/archive/refs/tags/v%{version}.tar.gz#/blackbox_exporter-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        prometheus-blackbox_exporter.service
BuildRequires:  fdupes
BuildRequires:  golang-github-prometheus-promu >= 0.17.0
BuildRequires:  libcap-progs
BuildRequires:  golang(API) >= 1.23
%{?systemd_ordering}
Requires(pre):  user(prometheus)
Requires(pre):  group(prometheus)
Requires(post): permissions
ExcludeArch:    s390

%if ! 0%{?suse_version} || 0%{?suse_version} == 1315
ExclusiveArch:  do_not_build
%endif

%description
Prometheus blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

%prep
%autosetup -a1 -p1 -n blackbox_exporter-%{version}

%build
%ifarch i586 s390x armv7hl armv7l armv7l:armv6l:armv5tel armv6hl
export BUILD_CGO_FLAG="--cgo"
%endif
export GOFLAGS="-buildmode=pie"
promu build -v $BUILD_CGO_FLAG

%install
install -D -m0755 %{_builddir}/blackbox_exporter-%{version}/blackbox_exporter-%{version} %{buildroot}%{_bindir}/blackbox_exporter
install -D -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/prometheus-blackbox_exporter.service
install -D -m0644 %{_builddir}/blackbox_exporter-%{version}/blackbox.yml %{buildroot}%{_sysconfdir}/prometheus/blackbox.yml
install -Dd -m0755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%fdupes %{buildroot}/%{_prefix}

%check
# Fix OBS debug_package execution.
rm -f %{buildroot}/usr/lib/debug/%{_bindir}/blackbox_exporter-%{version}-*.debug
go test -x .
%{buildroot}%{_bindir}/blackbox_exporter --version

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%license LICENSE
%verify(not caps) %attr(755,root,root) %{_bindir}/blackbox_exporter
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%dir %{_sysconfdir}/prometheus
%config(noreplace) %{_sysconfdir}/prometheus/blackbox.yml

%changelog
