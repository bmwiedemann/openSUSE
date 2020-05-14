#
# spec file for package gnome-logs
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           gnome-logs
Version:        3.36.0
Release:        0
Summary:        GNOME System Log Viewer
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/gnome-logs/3.36/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xsltproc
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.90
BuildRequires:  pkgconfig(glib-2.0) >= 2.43.90
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libsystemd)

Requires:       gsettings-desktop-schemas

%description
A utility for viewing detailed event logs for the system.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dman=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file -r org.gnome.Logs GTK GNOME System Monitor
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/gnome-logs/
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Logs.appdata.xml
%dir %{_datadir}/gnome-logs
%{_datadir}/gnome-logs/gl-style.css
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Logs*.svg
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/dbus-1/services/org.gnome.Logs.service

%files lang -f %{name}.lang

%changelog
