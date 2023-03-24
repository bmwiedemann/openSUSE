#
# spec file for package gsettings-desktop-schemas
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


Name:           gsettings-desktop-schemas
Version:        44.0
Release:        0
Summary:        Shared GSettings Schemas for the Desktop
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://gnome.org/
Source0:        https://download.gnome.org/sources/gsettings-desktop-schemas/44/%{name}-%{version}.tar.xz
# SOURCE-FIX-SLE 00_org.gnome.desktop.peripherals.gschema.override bsc#1171593 alynx.zhou@suse.com -- Change touchpad click method to default
Source1:        00_org.gnome.desktop.peripherals.gschema.override

# PATCH-FEATURE-OPENSUSE gsettings-desktop-schemas-fate324570-Add-key-for-GDM-background-configuration.patch fate#324570, glgo#GNOME/gnome-shell#680 qkzhu@suse.com -- This key is used by gnome-shell-fate324570-Make-GDM-background-image-configurable.patch
Patch0:         gsettings-desktop-schemas-fate324570-Add-key-for-GDM-background-configuration.patch

BuildRequires:  gobject-introspection-devel >= 1.31.0
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
# Default fonts in the schemas
Recommends:     cantarell-fonts
Recommends:     adobe-sourcecodepro-fonts

%description
A collection of GSettings schemas for settings shared by various
components of a desktop.

%package devel
Summary:        Shared GSettings Schemas for the Desktop -- Development Files
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
A collection of GSettings schemas for settings shared by various
components of a desktop.

This package contains development files.

%lang_package

%prep
%setup -q
%patch0 -p1
%if 0%{?sle_version}
cp -a %{SOURCE1} .
%endif

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%if 0%{?sle_version}
install -D -m0644 00_org.gnome.desktop.peripherals.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/00_org.gnome.desktop.peripherals.gschema.override
%endif
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc NEWS README
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.interface.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.magnifier.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.app-folders.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.background.lockdialog.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.calendar.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.datetime.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.input-sources.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.media-handling.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.notifications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.peripherals.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.privacy.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.screensaver.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.search-providers.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.session.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.sound.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.thumbnail-cache.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.thumbnailers.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.wm.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.wm.preferences.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.locale.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.location.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.proxy.gschema.xml
%if 0%{?sle_version}
%{_datadir}/glib-2.0/schemas/00_org.gnome.desktop.peripherals.gschema.override
%endif
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/gsettings-desktop-schemas.convert
%{_datadir}/GConf/gsettings/wm-schemas.convert
%{_libdir}/girepository-1.0/GDesktopEnums-3.0.typelib

%files devel
%doc AUTHORS ChangeLog HACKING MAINTAINERS
%{_includedir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/GDesktopEnums-3.0.gir

%files lang -f %{name}.lang

%changelog
