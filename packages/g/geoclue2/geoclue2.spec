#
# spec file for package geoclue2
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


%define _name geoclue

Name:           geoclue2
Version:        2.7.2
Release:        0
Summary:        GeoLocation Framework
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/geoclue/geoclue
Source0:        %{url}/-/archive/%{version}/geoclue-%{version}.tar.bz2
Source1:        srvGeoClue.conf
Source99:       geoclue2-rpmlintrc

# Compliance with BeaconDB
Patch0:         0001-ichnaea-include-ssid.patch
Patch1:         0002-ichnaea-replace-user-agent.patch
Patch2:         0003-user-agent-os-info.patch

BuildRequires:  intltool >= 0.40.0
BuildRequires:  meson >= 0.60.0
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  vala
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(avahi-client) >= 0.6.10
BuildRequires:  pkgconfig(avahi-glib) >= 0.6.10
BuildRequires:  pkgconfig(gio-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.74.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.14
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(mm-glib) >= 1.6
BuildRequires:  pkgconfig(systemd)
# This daemon runs as srvGeoClue
Requires:       user(srvGeoClue)
# Virtual provides for the dbus service
Provides:       dbus(org.freedesktop.GeoClue2) = %{version}
%{?systemd_requires}

%description
GeoClue is a software framework which can be used to enable geospatial
awareness in applications. GeoClue uses the D-Bus inter-process
communication mechanism to provide location information

%package -n system-user-srvGeoClue
Summary:        System user for the geoclue service
Group:          System/Base
BuildArch:      noarch
%sysusers_requires

%description -n system-user-srvGeoClue
System user for use by the geoclue service

%package -n typelib-1_0-Geoclue-2_0
Summary:        GeoLocation Framework --GObject Introspection
Group:          System/Libraries

%description -n typelib-1_0-Geoclue-2_0
GeoClue is a software framework which can be used to enable geospatial
awareness in applications. GeoClue uses the D-Bus inter-process
communication mechanism to provide location information

%package devel
Summary:        GeoLocation Framework -- Development files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Geoclue-2_0 = %{version}

%description devel
GeoClue is a software framework which can be used to enable geospatial
awareness in applications. GeoClue uses the D-Bus inter-process
communication mechanism to provide location information

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
	-Dgtk-doc=false \
	-Ddbus-srv-user=srvGeoClue \
	-Ddbus-sys-dir=%{_datadir}/dbus-1/system.d \
        -Ddefault-wifi-url="https://api.beacondb.net/v1/geolocate" \
        -Ddefault-wifi-submit-url="https://api.beacondb.net/v2/geosubmit" \
	%{nil}
%meson_build
%sysusers_generate_pre %{SOURCE1} srvGeoClue system-user-srvGeoClue.conf

%install
%meson_install

# Rename polkit rule to have specific ordering capabilities - boo#1199767#c1
mv %{buildroot}/usr/share/polkit-1/rules.d/org.freedesktop.GeoClue2.rules \
   %{buildroot}/usr/share/polkit-1/rules.d/50-org.freedesktop.GeoClue2.rules

install -d %{buildroot}%{_localstatedir}/lib/srvGeoClue
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-srvGeoClue.conf

# conf.d dir needed for drop-in configs (such as used by GNOME)
install -d %{buildroot}%{_sysconfdir}/geoclue/conf.d

# note: do not use systemd macros for geoclue2.service, they are not meant for dbus unit files.
%pre -n system-user-srvGeoClue -f srvGeoClue.pre
%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_mandir}/man5/geoclue.5%{ext_man}
# Not split per SLPP as the interface to the underlying daemon is
# too strict to allow parallel installations
%{_libdir}/libgeoclue-2.so.*
%{_libexecdir}/geoclue
%dir %{_libexecdir}/geoclue-2.0/
%{_libexecdir}/geoclue-2.0/demos/
%{_datadir}/applications/geoclue-where-am-i.desktop
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.Client.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.Manager.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.GeoClue2.service
%{_datadir}/polkit-1/rules.d/50-org.freedesktop.GeoClue2.rules
%dir %{_sysconfdir}/geoclue/
%dir %{_sysconfdir}/geoclue/conf.d
%config %{_sysconfdir}/geoclue/geoclue.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.GeoClue2.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
%{_unitdir}/geoclue.service
# Upstream is explicitly asking us to package these, so lets give it a go.
%{_sysconfdir}/xdg/autostart/geoclue-demo-agent.desktop
%{_datadir}/applications/geoclue-demo-agent.desktop

%files -n system-user-srvGeoClue
%attr(0700,srvGeoClue,root) %{_localstatedir}/lib/srvGeoClue
%{_sysusersdir}/system-user-srvGeoClue.conf

%files -n typelib-1_0-Geoclue-2_0
%{_libdir}/girepository-1.0/Geoclue-2.0.typelib

%files devel
%{_includedir}/libgeoclue-2.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/geoclue-2.0.pc
%{_libdir}/pkgconfig/libgeoclue-2.0.pc
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.Agent.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.GeoClue2.xml
%{_datadir}/gir-1.0/Geoclue-2.0.gir
%{_datadir}/vala/vapi/libgeoclue-2.0.*

%changelog
