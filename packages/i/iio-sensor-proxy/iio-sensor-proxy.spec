#
# spec file for package iio-sensor-proxy
#
# Copyright (c) 2025 SUSE LLC
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


Name:           iio-sensor-proxy
Version:        3.6
Release:        0
Summary:        Proxy for IIO and input subsystems
License:        GPL-3.0-only
Group:          System/Monitoring
URL:            https://gitlab.freedesktop.org/hadess/iio-sensor-proxy
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM iio-sensor-proxy-compass-check-claim-perm.patch bsc#1236290 badshah400@gmail.com -- avoid unauthenticated permissions for compass
Patch0:         https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/-/merge_requests/393.patch#/iio-sensor-proxy-compass-check-claim-perm.patch
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 237
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd) >= 219
BuildRequires:  pkgconfig(udev) >= 219
Requires:       user(srvGeoClue)
%{?systemd_requires}

%description
This proxy reads sensor data from the IIO subsystem and serves to
the input subsystem

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1

%build
%meson -Dgtk-tests=false \
       -Dgtk_doc=true \
       -Dgeoclue-user=srvGeoClue
%meson_build

%install
%meson_install

%pre
%service_add_pre iio-sensor-proxy.service

%preun
%service_del_preun iio-sensor-proxy.service

%post
%udev_hwdb_update
%udev_rules_update
%service_add_post iio-sensor-proxy.service

%postun
%udev_hwdb_update
%udev_rules_update
%service_del_postun iio-sensor-proxy.service

%files
%{_bindir}/monitor-sensor
%{_libexecdir}/iio-sensor-proxy
%{_udevrulesdir}/*.rules
%{_unitdir}/iio-sensor-proxy.service
%{_datadir}/polkit-1/actions/net.hadess.SensorProxy.policy
# Own dirs to avoid depending on dbus while building.
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/net.hadess.SensorProxy.conf

%files doc
%{_datadir}/gtk-doc/html/%{name}/

%changelog
