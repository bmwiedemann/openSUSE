#
# spec file for package totem
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


Name:           totem
Version:        43.0
Release:        0
Summary:        Movie Player for the GNOME Desktop
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://wiki.gnome.org/Apps/Videos
Source0:        https://download.gnome.org/sources/totem/43/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gstreamer-plugins-good
BuildRequires:  gstreamer-plugins-good-gtk
# For gst-inspect tool
BuildRequires:  gstreamer-utils >= 0.11.93
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.6.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.1.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(totem-plparser) >= 3.26.5
BuildRequires:  pkgconfig(x11)

# We want a useful set of plugins
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-good-gtk
Requires:       iso-codes
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
Recommends:     totem-plugins

# totem-plugin-brasero has been removed.
Obsoletes:      totem-plugin-brasero < 3.38.0
# totem-plugin-upnp has been substituted by a grilo plugin.
Obsoletes:      totem-plugin-upnp < 3.38.0
# The browser plugins were dropped with totem 3.13.90
Obsoletes:      nautilus-totem < 3.31.92
Obsoletes:      totem-browser-plugin < 3.13.90
Obsoletes:      totem-browser-plugin-gmp < 3.13.90
Obsoletes:      totem-browser-plugin-vegas < 3.13.90
%glib2_gsettings_schema_requires
Obsoletes:      totem-plugin-zeitgeist < 3.38.0

%description
Totem is a movie player for the GNOME desktop based on GStreamer. It
features a playlist, a full-screen mode, seek and volume controls, and
complete keyboard navigation.

%package plugins
Summary:        Plugins for Totem Movie Player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name} = %{version}
# Gromit Annotation plugin
Suggests:       gromit
%glib2_gsettings_schema_requires

%description plugins
Totem is a movie player for the GNOME desktop based on GStreamer.

This package includes plugins for Totem, to add advanced features.

%package devel
Summary:        Developer Documentation for Totem Movie Player
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
Totem is a movie player for the GNOME desktop based on GStreamer.

This package contains developer documentation.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D enable-easy-codec-installation=yes \
	-D enable-gtk-doc=true \
	-D enable-python=yes \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Totem.desktop

%files
%license COPYING
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/*
%{_datadir}/GConf/gsettings/totem.convert
%{_datadir}/dbus-1/services/org.gnome.Totem.service
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.totem.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.totem.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/totem.thumbnailer
%{_libexecdir}/totem-gallery-thumbnailer
%{_mandir}/man?/*%{ext_man}
# Own directories for plugins
%dir %{_libdir}/totem
%dir %{_libdir}/totem/plugins
%{_libdir}/libtotem.so.0*
%{_libdir}/girepository-1.0/Totem-1.0.typelib

%files lang -f %{name}.lang

%files plugins
# Explicitly list plugins
%{_libdir}/totem/plugins/apple-trailers/
%{_libdir}/totem/plugins/autoload-subtitles/
%{_libdir}/totem/plugins/im-status/
%{_libdir}/totem/plugins/mpris/
%{_libdir}/totem/plugins/open-directory/
%{_libdir}/totem/plugins/opensubtitles/
%{_libdir}/totem/plugins/properties/
%{_libdir}/totem/plugins/pythonconsole/
%{_libdir}/totem/plugins/recent/
%{_libdir}/totem/plugins/rotation/
%{_libdir}/totem/plugins/save-file/
%{_libdir}/totem/plugins/screensaver/
%{_libdir}/totem/plugins/screenshot/
%{_libdir}/totem/plugins/skipto/
%{_libdir}/totem/plugins/vimeo/
%{_libdir}/totem/plugins/variable-rate/
%{_datadir}/GConf/gsettings/opensubtitles.convert
%{_datadir}/GConf/gsettings/pythonconsole.convert
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.opensubtitles.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.pythonconsole.gschema.xml

%files devel
%doc AUTHORS NEWS README
%{_datadir}/gtk-doc/html/totem/
%{_includedir}/totem/
%{_libdir}/libtotem.so
%{_libdir}/pkgconfig/totem.pc
%{_datadir}/gir-1.0/*.gir

%changelog
