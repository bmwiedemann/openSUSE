#
# spec file for package gnome-system-monitor
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


Name:           gnome-system-monitor
Version:        50.0
Release:        0
Summary:        A process monitor for the GNOME desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/SystemMonitor
Source0:        %{name}-%{version}.tar.xz
Patch0:         gnome-system-monitor-fix-crash.patch

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(catch2-with-main)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(giomm-2.68) >= 2.84
BuildRequires:  pkgconfig(glib-2.0) >= 2.80
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.46
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.17.5
BuildRequires:  pkgconfig(gtkmm-4.0) >= 4.17.5
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8.alpha
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.41.2
BuildRequires:  pkgconfig(libhandy-1) >= 1.5.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(libsystemd) >= 44

%description
GNOME-system-monitor is a process and system monitor for the GNOME
Desktop. It shows you what programs are running and how much
processor time, memory, and disk space are being used.

%lang_package

%prep
%autosetup -p1

%build
%meson \
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
%{_datadir}/applications/gnome-system-monitor-kde.desktop
%{_datadir}/applications/org.gnome.SystemMonitor.desktop
%{_datadir}/dbus-1/services/org.gnome.SystemMonitor.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-monitor.gschema.xml
%{_datadir}/metainfo/org.gnome.SystemMonitor.metainfo.xml
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.gnome.gnome-system-monitor.policy
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/gsm-kill
%{_libexecdir}/%{name}/gsm-renice
%{_libexecdir}/%{name}/gsm-taskset
%{_datadir}/icons/hicolor/*/apps/*.svg

%files lang -f %{name}.lang

%changelog
