#
# spec file for package google-guest-configs
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150300
%define _udevdir %(pkg-config --variable udevdir udev)
%define _modprobedir %{_sysconfdir}/modprobe.d
%else
%define _udevdir %(pkg-config --variable udev_dir udev)
%endif
Name:           google-guest-configs
Version:        20240607.00
Release:        0
Summary:        Google Cloud Guest Configs
License:        Apache-2.0
Group:          System/Daemons
URL:            https://github.com/GoogleCloudPlatform/guest-configs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  systemd-rpm-macros
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
BuildRequires:  pkg-config
%endif
BuildRequires:  pkgconfig(udev)
Requires:       nvme-cli
BuildArch:      noarch

%description
Google Cloud Guest Configs

%prep
%setup -q -n guest-configs-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_modprobedir}
cp -av src/etc/modprobe.d/* %{buildroot}%{_modprobedir}
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d
cp -av src/etc/rsyslog.d/* %{buildroot}%{_sysconfdir}/rsyslog.d/
mkdir -p %{buildroot}%{_sysctldir}
cp -av src/etc/sysctl.d/* %{buildroot}%{_sysctldir}
mkdir -p %{buildroot}%{_udevrulesdir}
cp -av src/lib/udev/rules.d/* %{buildroot}%{_udevrulesdir}/
cp -av src/lib/udev/google_nvme_id %{buildroot}/%{_udevdir}/
mkdir -p %{buildroot}%{_bindir}
cp -av src/usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0644,root,root,0755)
%doc README.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/google_optimize_local_ssd
%exclude %attr(0755,root,root) %{_bindir}/google_set_hostname
%attr(0755,root,root) %{_bindir}/google_set_multiqueue
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150300
%dir %{_modprobedir}
%endif
%dir %{_sysconfdir}/rsyslog.d
%{_modprobedir}/gce-blacklist.conf
%config %{_sysconfdir}/rsyslog.d/*
%{_sysctldir}/*
%attr(0755,root,root) %{_udevdir}/google_nvme_id
%{_udevrulesdir}/*

%changelog
