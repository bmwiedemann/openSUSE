#
# spec file for package gnome-font-viewer
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


Name:           gnome-font-viewer
Version:        3.34.0
Release:        0
Summary:        A font viewer utility for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-font-viewer
Source0:        https://download.gnome.org/sources/gnome-font-viewer/3.34/%{name}-%{version}.tar.xz

BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.9
Recommends:     %{name}-lang
Conflicts:      gnome-utils < 3.3.1

%description
A utility to let you see the installed fonts at a glance.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file org.gnome.font-viewer Settings Utility
%find_lang %{name}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/metainfo/org.gnome.font-viewer.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.font-viewer*.svg

%files lang -f %{name}.lang

%changelog
