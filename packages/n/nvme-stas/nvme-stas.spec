#
# spec file for package nvme-stas
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


Name:           nvme-stas
Version:        2.3
Release:        0
Summary:        NVMe STorage Appliance Services
License:        Apache-2.0
URL:            https://github.com/linux-nvme/nvme-stas
Source0:        nvme-stas-%{version}.tar.gz
BuildRequires:  gobject-introspection
BuildRequires:  libnvme-devel >= 1.3
BuildRequires:  meson >= 0.52.0
BuildRequires:  python3
BuildRequires:  python3-dasbus
BuildRequires:  python3-gobject
BuildRequires:  python3-libnvme >= 1.3
BuildRequires:  python3-pyudev
BuildRequires:  python3-systemd
BuildRequires:  systemd-rpm-macros
Requires:       avahi
Requires:       python3-dasbus
Requires:       python3-gobject
Requires:       python3-libnvme >= 1.3
Requires:       python3-pyudev
Requires:       python3-systemd

%description
nvme-stas is a Central Discovery Controller (CDC) client for Linux. It
handles Asynchronous Event Notifications (AEN) handling, Automated,
NVMe subsystem connection controls, Error handling and reporting and
Automatic (zeroconf) and Manual configuration.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%define services stacd.service stafd.service

%pre
%service_add_pre %services

%post
%service_add_post %services

%preun
%service_del_preun %services

%postun
%service_del_postun %services

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/stas
%config(noreplace) %{_sysconfdir}/stas/stacd.conf
%config(noreplace) %{_sysconfdir}/stas/stafd.conf
%config(noreplace) %{_sysconfdir}/stas/sys.conf.doc
%{_datadir}/dbus-1/system.d/org.nvmexpress.stac.conf
%{_datadir}/dbus-1/system.d/org.nvmexpress.staf.conf
%{_bindir}/stacctl
%{_bindir}/stafctl
%{_bindir}/stasadm
%{_sbindir}/stacd
%{_sbindir}/stafd
%{_unitdir}/stacd.service
%{_unitdir}/stafd.service
%{python3_sitelib}/staslib
%{_unitdir}/stas*

%changelog
