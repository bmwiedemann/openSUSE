#
# spec file for package brisk-menu
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


Name:           brisk-menu
Version:        0.6.2
Release:        0
Summary:        Modern, efficient menu for MATE
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
URL:            https://github.com/getsolus/brisk-menu
Source:         https://github.com/getsolus/brisk-menu/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        https://github.com/getsolus/brisk-menu/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM brisk-menu-gsettings-icon-properties.patch ionic@ionic.de -- Add icon properties to the gsettings schema for runtime configuration.
Patch0:         %{name}-gsettings-icon-properties.patch
# PATCH-FIX-UPSTREAM brisk-menu-runtime-icon-updates.patch ionic@ionic.de -- Add support for runtime icon configuration.
Patch1:         %{name}-runtime-icon-updates.patch
# PATCH-FIX-UPSTREAM brisk-menu-fix-crash-on-desktop-file-changes-5f0be5741b5b37221fc8911c11f394ec498cd53d.patch anton.fadeev@red-soft.ru -- Fix crash in some random cases when .desktop files are changed.
Patch2:         %{name}-fix-crash-on-desktop-file-changes-5f0be5741b5b37221fc8911c11f394ec498cd53d.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libmate-menu) >= 1.22
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= 1.22
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Modern, efficient menu for the MATE Desktop Environment.

%prep
%autosetup -p1 -n %{name}-%{version}

%lang_package

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license LICENSE*
%{_libexecdir}/brisk-menu
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/*brisk*.mate-panel-applet
%{_datadir}/icons/hicolor/scalable/actions/brisk*.*
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%{_datadir}/dbus-1/services/org.mate.panel.applet.BriskMenuFactory.service

%files lang -f %{name}.lang

%changelog
