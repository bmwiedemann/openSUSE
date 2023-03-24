#
# spec file for package gnome-font-viewer
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


Name:           gnome-font-viewer
Version:        44.0
Release:        0
Summary:        A font viewer utility for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-font-viewer
Source0:        https://download.gnome.org/sources/gnome-font-viewer/44/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4) >= 4.5.0
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.9
BuildRequires:  pkgconfig(libadwaita-1)
Conflicts:      gnome-utils < 3.3.1

%description
A utility to let you see the installed fonts at a glance.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.font-viewer.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.font-viewer.appdata.xml
%meson_test

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
