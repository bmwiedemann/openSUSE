#
# spec file for package iio-sensor-proxy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.8
Release:        0
Summary:        Proxy for IIO and input subsystems
License:        GPL-3.0-only
Group:          System/Monitoring
URL:            https://github.com/hadess/iio-sensor-proxy
Source0:        https://github.com/hadess/iio-sensor-proxy/releases/download/%{version}/%{name}-%{version}.tar.xz
Source99:       iio-sensor-proxy-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(systemd) >= 219
BuildRequires:  pkgconfig(udev) >= 219
Requires:       user(srvGeoClue)
%{?systemd_requires}

%description
This proxy reads sensor data from the IIO subsystem and serves to the input subsystem

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-gtk-tests --with-geoclue-user=srvGeoClue
make %{?_smp_mflags}

%install
%make_install

%post
%udev_hwdb_update
%udev_rules_update

%postun
%udev_hwdb_update
%udev_rules_update

%files
%{_bindir}/monitor-sensor
%{_sbindir}/iio-sensor-proxy
%{_udevrulesdir}/*.rules
%{_unitdir}/iio-sensor-proxy.service
# Own dirs to avoid depending on dbus while building.
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/net.hadess.SensorProxy.conf

%files doc
%{_datadir}/gtk-doc/html/%{name}/

%changelog
