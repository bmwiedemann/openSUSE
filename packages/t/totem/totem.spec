#
# spec file for package totem
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


%define build_zeitgeist_plugin 0
Name:           totem
Version:        3.34.1
Release:        0
Summary:        Movie Player for the GNOME Desktop
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://wiki.gnome.org/Apps/Videos
Source0:        https://download.gnome.org/sources/totem/3.34/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM totem-Fix-bracket-keys-and-backspace.patch -- variable-rate: Fix bracket keys and backspace not working
Patch1:         totem-Fix-bracket-keys-and-backspace.patch

BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gstreamer-plugins-good >= 0.11.93
# For gst-inspect tool
BuildRequires:  gstreamer-utils >= 0.11.93
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-pylint
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.14.1
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.17.3
BuildRequires:  pkgconfig(clutter-gst-3.0) >= 2.99.2
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.8.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.35.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.6.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.4
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libepc-ui-1.0) > 0.4.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.1.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(totem-plparser) >= 3.25.90
BuildRequires:  pkgconfig(x11)
# We want a useful set of plugins
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       iso-codes
# Required for cluttersink
Recommends:     gstreamer-plugin-cluttergst3
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
Recommends:     totem-plugins
# totem-plugin-brasero has been removed.
Obsoletes:      totem-plugin-brasero
# totem-plugin-upnp has been substituted by a grilo plugin.
Obsoletes:      totem-plugin-upnp <= %{version}
# The browser plugins were dropped with totem 3.13.90
Obsoletes:      nautilus-totem < 3.31.92
Obsoletes:      totem-browser-plugin < 3.13.90
Obsoletes:      totem-browser-plugin-gmp < 3.13.90
Obsoletes:      totem-browser-plugin-vegas < 3.13.90
%glib2_gsettings_schema_requires
%if %{build_zeitgeist_plugin}
BuildRequires:  pkgconfig(zeitgeist-2.0) >= 0.9.12
%endif
%if ! %{build_zeitgeist_plugin}
Obsoletes:      totem-plugin-zeitgeist <= %{version}
%endif

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

%if %{build_zeitgeist_plugin}
%package plugin-zeitgeist
Summary:        Zeitgeist support for the Totem movie player
Group:          Productivity/Multimedia/Video/Players
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:zeitgeist)

%description plugin-zeitgeist
Totem is a movie player for the GNOME desktop based on GStreamer.

This package includes the Zeitgeist plugin for Totem.
%endif

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
sed -i 's/\[.*\]//g' po/POTFILES.in 
translation-update-upstream po totem

%build
%meson \
	-D enable-easy-codec-installation=yes \
	-D enable-gtk-doc=true \
	-D enable-introspection=yes \
	-D enable-python=yes \
	-D enable-vala=yes \
	%{nil}
# workaround parallel build breakage (bgo#786248)
%meson_build src/Totem-1.0.gir
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
%{_datadir}/icons/hicolor/*/apps/org.gnome.Totem*.svg
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/totem.thumbnailer
%{_libexecdir}/totem-gallery-thumbnailer
%{_datadir}/totem/
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
%{_libdir}/totem/plugins/dbus/
%{_libdir}/totem/plugins/im-status/
%{_libdir}/totem/plugins/media-player-keys/
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

%if %{build_zeitgeist_plugin}
%files plugin-zeitgeist
%{_libdir}/totem/plugins/zeitgeist-dp/
%endif

%files devel
%doc AUTHORS NEWS README
%{_datadir}/gtk-doc/html/totem/
%{_includedir}/totem/
%{_libdir}/libtotem.so
%{_libdir}/pkgconfig/totem.pc
%{_datadir}/gir-1.0/*.gir

%changelog
