#
# spec file for package desktopfolder
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


Name:           desktopfolder
Version:        1.1.3
Release:        0
Summary:        Tool for organizing the desktop with panels, notes and photos
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/spheras/desktopfolder/
Source:         https://github.com/spheras/desktopfolder/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libwnck-3.0)
Recommends:     %{name}-lang

%description
A program with which the desktop can be organized with panels that hold things.
  * Access files, folders and apps from your desktop
  * Drop files, folders, links and .desktop launchers inside panels
  * Resize, position and color panels
  * Display photos and keep notes on your desktop
  * Reveal the desktop with ⌘-D (Command-D)

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

# https://github.com/spheras/desktopfolder/issues/69
find %{buildroot} -name \*.??g -exec chmod 0644 {} \;

%{suse_update_desktop_file -r \
  %{buildroot}%{_datadir}/applications/com.github.spheras.desktopfolder.desktop GTK Utility DesktopSettings}
%find_lang com.github.spheras.desktopfolder %{name}.lang
%fdupes %{buildroot}/%{_datadir}

# Add OnlyShowIn key
if ! grep OnlyShowIn.*Pantheon %{buildroot}%{_sysconfdir}/xdg/autostart/com.github.spheras.desktopfolder-autostart.desktop; then
	sed -i '$aOnlyShowIn=Pantheon;' %{buildroot}%{_sysconfdir}/xdg/autostart/com.github.spheras.desktopfolder-autostart.desktop
else
	'This entry already exists' 2> /dev/null
fi
#

%files
%license LICENSE*
%doc AUTHORS* README.md
%{_bindir}/com.github.spheras.desktopfolder
%{_datadir}/applications/com.github.spheras.desktopfolder.desktop
%{_datadir}/glib-2.0/schemas/com.github.spheras.desktopfolder.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.spheras.desktopfolder.??g
%{_datadir}/metainfo/com.github.spheras.desktopfolder.appdata.xml
%{_sysconfdir}/xdg/autostart/com.github.spheras.desktopfolder-autostart.desktop

%files lang -f %{name}.lang

%changelog
