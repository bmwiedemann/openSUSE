#
# spec file for package libvirt-dbus
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


Name:           libvirt-dbus
Version:        1.4.0
Release:        0
Summary:        D-Bus API binding for libvirt
License:        LGPL-2.1-or-later
URL:            https://libvirt.org/
Source0:        https://libvirt.org/sources/dbus/%{name}-%{version}.tar.xz
Source1:        system-user-%{name}.conf
# PATCH-FIX-UPSTREAM
Patch:          libvirt-dbus-systemd.diff
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  polkit
BuildRequires:  python3-docutils
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libvirt)
BuildRequires:  pkgconfig(libvirt-glib-1.0)
BuildRequires:  pkgconfig(systemd)
Requires:       polkit
Requires:       user(libvirtdbus)

%description
This package provides D-Bus API for libvirt

%package -n system-user-libvirt-dbus
Summary:        System user for libvirt-dbus
%sysusers_requires

%description -n system-user-libvirt-dbus
System user for libvirt-dbus.

%prep
%autosetup -p1

%build
%meson -Dinit_script=systemd
%meson_build
%sysusers_generate_pre %{SOURCE1} system-user-%{name}

%install
%meson_install
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
ln -s service %{buildroot}%{_sbindir}/rclibvirt-dbus

%pre
%service_add_pre libvirt-dbus.service

%post
%service_add_post libvirt-dbus.service

%preun
%service_del_preun libvirt-dbus.service

%postun
%service_del_postun libvirt-dbus.service

%pre -n system-user-%{name} -f system-user-%{name}.pre

%files
%doc AUTHORS.rst NEWS.rst
%license COPYING
%{_sbindir}/rclibvirt-dbus
%{_sbindir}/libvirt-dbus
%{_datadir}/dbus-1/services/org.libvirt.service
%{_datadir}/dbus-1/system-services/org.libvirt.service
%{_datadir}/dbus-1/system.d/org.libvirt.conf
%{_datadir}/dbus-1/interfaces/org.libvirt.*.xml
%{_datadir}/polkit-1/rules.d/libvirt-dbus.rules
%{_mandir}/man8/libvirt-dbus.8%{?ext_man}
%{_unitdir}/libvirt-dbus.service
%{_userunitdir}/libvirt-dbus.service

%files -n system-user-%{name}
%{_sysusersdir}/system-user-%{name}.conf

%changelog
