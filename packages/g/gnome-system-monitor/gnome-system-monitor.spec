#
# spec file for package gnome-system-monitor
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


Name:           gnome-system-monitor
Version:        44.0
Release:        0
Summary:        A process monitor for the GNOME desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/SystemMonitor
Source0:        https://download.gnome.org/sources/gnome-system-monitor/44/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(giomm-2.4) >= 2.46
BuildRequires:  pkgconfig(glib-2.0) >= 2.55.0
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.3.18
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.37.2
BuildRequires:  pkgconfig(libhandy-1) >= 1.5.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(libsystemd) >= 44
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0

%description
GNOME-system-monitor is a process and system monitor for the GNOME
Desktop. It shows you what programs are running and how much
processor time, memory, and disk space are being used.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dwnck=false \
	-Dsystemd=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-system-monitor
%{_datadir}/applications/gnome-system-monitor.desktop
%{_datadir}/applications/gnome-system-monitor-kde.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_datadir}/metainfo/gnome-system-monitor.appdata.xml
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/gsm-kill
%{_libexecdir}/%{name}/gsm-renice
%{_libexecdir}/%{name}/gsm-taskset
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/gsm.gresource
%{_datadir}/icons/hicolor/*/apps/org.gnome.SystemMonitor*.svg
%{_datadir}/icons/hicolor/symbolic/apps/speedometer-symbolic.svg

%files lang -f %{name}.lang

%changelog
