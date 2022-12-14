#
# spec file for package cheese
#
# Copyright (c) 2022 SUSE LLC
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


%define lib_major 8
%define lib_gtk_major 25
%define typelib_major 3
%define typelib_minor 0

Name:           cheese
Version:        43.0
Release:        0
Summary:        Webcam Booth for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://wiki.gnome.org/Apps/Cheese
Source0:        https://download.gnome.org/sources/cheese/43/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.25.2
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(clutter-1.0) >= 1.13.2
BuildRequires:  pkgconfig(clutter-gst-3.0) >= 3.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39.90
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-video-effects)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 0.11.0
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.4
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.4
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(x11)
Requires:       gnome-video-effects
Recommends:     yelp

%description
Cheese is an application to take photos and videos with your webcam,
with fun graphical effects.

%package -n libcheese%{lib_major}
Summary:        Library implementing a webcam booth for GNOME
# won't start without those:
Group:          System/Libraries
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
# The library is using gsettings key that are defined in the -common package
Requires:       libcheese-common >= %{version}

%description -n libcheese%{lib_major}
Cheese is an application to take photos and videos with your webcam,
with fun graphical effects.

%package -n typelib-1_0-Cheese-%{typelib_major}_%{typelib_minor}
Summary:        Introspection bindings for libcheese
Group:          System/Libraries

%description -n typelib-1_0-Cheese-%{typelib_major}_%{typelib_minor}
Cheese is an application to take photos and videos with your webcam,
with fun graphical effects.

This package provides the GObject Introspection bindings for the
libcheese library.

%package -n libcheese-gtk%{lib_gtk_major}
Summary:        UI library for the Cheese a webcam booth
# The library is using gsettings keys that are defined in the -common package
Group:          System/Libraries
Requires:       libcheese-common >= %{version}

%description -n libcheese-gtk%{lib_gtk_major}
Cheese is an application to take photos and videos with your webcam,
with fun graphical effects.

This package contains a library providing widgets to allow third
party applications to include parts of cheese functionality.

%package -n libcheese-common
Summary:        Common data files for the Cheese webcam booth
Group:          System/Libraries
BuildArch:      noarch

%description -n libcheese-common
Cheese is an application to take photos and videos with your webcam,
with fun graphical effects.

This package contains common data that is used by the cheese libraries,
like schemas.

%package devel
Summary:        Development files for the Cheese webcam booth
Group:          Development/Libraries/GNOME
Requires:       libcheese%{lib_major} = %{version}
Requires:       libcheese-gtk%{lib_gtk_major} = %{version}
Requires:       typelib-1_0-Cheese-%{typelib_major}_%{typelib_minor} = %{version}

%description devel
Cheese is an application to take photos and videos with your webcam,
with fun graphical effects.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file org.gnome.Cheese
%fdupes %{buildroot}%{_datadir}/help/

%ldconfig_scriptlets -n libcheese%{lib_major}
%ldconfig_scriptlets -n libcheese-gtk%{lib_gtk_major}

%files
%license COPYING
%doc NEWS
%{_datadir}/help/C/%{name}/
%{_bindir}/cheese
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Cheese.appdata.xml
%{_datadir}/applications/org.gnome.Cheese.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Cheese*.*
%{_mandir}/man1/cheese.1%{?ext_man}
%{_datadir}/dbus-1/services/org.gnome.Cheese.service

%files -n libcheese%{lib_major}
%{_libdir}/libcheese.so.%{lib_major}*

%files -n typelib-1_0-Cheese-%{typelib_major}_%{typelib_minor}
%{_libdir}/girepository-1.0/Cheese-%{typelib_major}.%{typelib_minor}.typelib

%files -n libcheese-gtk%{lib_gtk_major}
%{_libdir}/libcheese-gtk.so.%{lib_gtk_major}*

%files -n libcheese-common
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml

%files devel
%doc AUTHORS README ChangeLog
%{_includedir}/cheese/
%{_libdir}/pkgconfig/cheese.pc
%{_libdir}/pkgconfig/cheese-gtk.pc
%{_libdir}/libcheese.so
%{_libdir}/libcheese-gtk.so
%{_datadir}/gir-1.0/Cheese-%{typelib_major}.%{typelib_minor}.gir
%{_datadir}/gtk-doc/html/cheese/

%files lang -f %{name}.lang

%changelog
