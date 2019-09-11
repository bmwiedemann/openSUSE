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
Version:        3.32.1
Release:        0
Summary:        Quick Previewer for Nautilus
License:        SUSE-GPL-2.0-with-plugin-exception
Group:          Productivity/File utilities
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/sushi/3.32/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM sushi-port-to-gtksourceview4.patch -- Port to gtksourceview4
Patch0:         sushi-port-to-gtksourceview4.patch

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(clutter-1.0) >= 1.11.4
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(clutter-x11-1.0)
BuildRequires:  pkgconfig(evince-document-3.0)
BuildRequires:  pkgconfig(evince-view-3.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gjs-1.0) >= 1.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.29.14
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.2
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.3
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.9
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang
Supplements:    nautilus
# libsushi and the typelib were erronously installed in the system libdir...
Obsoletes:      libsushi-1_0-0 < %{version}
Obsoletes:      typelib-1_0-Sushi-1_0 < %{version}

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
%{_bindir}/sushi
%{_datadir}/dbus-1/services/org.gnome.NautilusPreviewer.service
%{_datadir}/sushi/
%{_libdir}/sushi/
%{_libexecdir}/sushi-start

%files lang -f %{name}.lang

%changelog
