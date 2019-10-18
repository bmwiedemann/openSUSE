#
# spec file for package sushi
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


Name:           sushi
Version:        3.34.0
Release:        0
Summary:        Quick Previewer for Nautilus
License:        SUSE-GPL-2.0-with-plugin-exception
Group:          Productivity/File utilities
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/sushi/3.34/%{name}-%{version}.tar.xz
Source99:       sushi-rpmlintrc

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(evince-document-3.0)
BuildRequires:  pkgconfig(evince-view-3.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gjs-1.0) >= 1.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.29.14
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.2
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.3
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.9
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang
Supplements:    nautilus

%description
Sushi is a quick previewer for Nautilus, the GNOME desktop file manager.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.NautilusPreviewer.service
%{_datadir}/metainfo/org.gnome.NautilusPreviewer.appdata.xml
%dir %{_datadir}/%{name}/gtksourceview-4
%dir %{_datadir}/%{name}/gtksourceview-4/styles
%{_datadir}/%{name}/gtksourceview-4/styles/builder-dark.style-scheme.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/gir-1.0
%{_datadir}/%{name}/gir-1.0/Sushi-1.0.gir
%{_datadir}/%{name}/org.gnome.NautilusPreviewer.data.gresource
%{_datadir}/%{name}/org.gnome.NautilusPreviewer.src.gresource
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Sushi-1.0.typelib
%{_libdir}/%{name}/libsushi-1.0.so
%{_libexecdir}/org.gnome.NautilusPreviewer

%files lang -f %{name}.lang

%changelog
