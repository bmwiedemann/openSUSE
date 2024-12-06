#
# spec file for package desktopfolder
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


%define         appid com.github.spheras.desktopfolder
Name:           desktopfolder
Version:        1.1.3
Release:        0
Summary:        Tool for organizing the desktop with panels, notes and photos
License:        GPL-3.0-or-later
URL:            https://github.com/spheras/desktopfolder
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/spheras/desktopfolder/pull/328
Patch0:         000-drop-gsettings-schema.patch
# PATCH-FIX-UPSTREAM -- https://github.com/spheras/desktopfolder/pull/328
Patch1:         001-dark-mode-support.patch
# PATCH-FIX-UPSTREAM -- https://github.com/spheras/desktopfolder/pull/335/commits
Patch2:         002-drop-deprecated-arguments.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libwnck-3.0)

%description
A program with which the desktop can be organized with panels that hold things.
  * Access files, folders and apps from your desktop
  * Drop files, folders, links and .desktop launchers inside panels
  * Resize, position and color panels
  * Display photos and keep notes on your desktop
  * Reveal the desktop with ⌘-D (Command-D)

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}

# https://github.com/spheras/desktopfolder/issues/69
find %{buildroot} -name '*.svg' -exec chmod 0644 {} \;

%if 0%{?suse_version} >= 1600
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/xdg/autostart/%{appid}-autostart.desktop \
   %{buildroot}%{_distconfdir}/xdg/autostart/%{appid}-autostart.desktop
%endif

%fdupes -s %{buildroot}

%files
%license LICENSE
%doc AUTHORS.md README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%if 0%{?suse_version} >= 1600
%{_distconfdir}/xdg/autostart/%{appid}-autostart.desktop
%else
%{_sysconfdir}/xdg/autostart/%{appid}-autostart.desktop
%endif

%files lang -f %{appid}.lang

%changelog
