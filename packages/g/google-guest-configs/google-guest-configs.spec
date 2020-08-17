#
# spec file for package google-guest-configs
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

Name:           google-guest-configs
Version:        20200626.00
Release:        0
Summary:        Google Cloud Guest Configs
License:        Apache-2.0
Group:          System/Daemons
URL:            https://github.com/GoogleCloudPlatform/guest-configs
Source0:        %{name}-%{version}.tar.gz
Source1:        google-optimize-local-ssd.service
Source2:        google-set-multiqueue.service
BuildRequires:  systemd-rpm-macros
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
BuildRequires:  pkgconfig(udev)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildArch:      noarch

%description
Google Cloud Guest Configs

%prep
%setup -q -n guest-configs-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
cp -av src/etc/modprobe.d/* %{buildroot}%{_sysconfdir}/modprobe.d/
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d
cp -av src/etc/rsyslog.d/* %{buildroot}%{_sysconfdir}/rsyslog.d/
mkdir -p %{buildroot}%{_sysconfdir}/sysctl.d
cp -av src/etc/sysctl.d/* %{buildroot}%{_sysconfdir}/sysctl.d/
mkdir -p %{buildroot}%{_unitdir}
cp -av %{SOURCE1} %{buildroot}%{_unitdir}/
cp -av %{SOURCE2} %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_udevrulesdir}
cp -av src/lib/udev/rules.d/* %{buildroot}%{_udevrulesdir}/
mkdir -p %{buildroot}%{_bindir}
cp -av src/usr/bin/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sbindir}
for srv_name in %{buildroot}%{_unitdir}/*.service; do rc_name=$(basename -s '.service' $srv_name); ln -s service %{buildroot}%{_sbindir}/rc$rc_name; done

%pre
%service_add_pre google-optimize-local-ssd.service google-set-multiqueue.service

%preun
%service_del_preun google-optimize-local-ssd.service google-set-multiqueue.service

%post
%service_add_post google-optimize-local-ssd.service google-set-multiqueue.service

%postun
%service_del_postun google-optimize-local-ssd.service google-set-multiqueue.service

%files
%defattr(0644,root,root,0755)
%doc README.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/google_optimize_local_ssd
%exclude %attr(0755,root,root) %{_bindir}/google_set_hostname
%attr(0755,root,root) %{_bindir}/google_set_multiqueue
%dir %{_sysconfdir}/modprobe.d
%dir %{_sysconfdir}/rsyslog.d
%dir %{_sysconfdir}/sysctl.d
%config %{_sysconfdir}/modprobe.d/gce-blacklist.conf
%config %{_sysconfdir}/rsyslog.d/*
%config %{_sysconfdir}/sysctl.d/*
%{_sbindir}/*
%{_udevrulesdir}/*
%{_unitdir}/*

%changelog
