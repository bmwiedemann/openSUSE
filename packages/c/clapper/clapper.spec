#
# spec file for package clapper
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


%global uuid com.github.rafostar.Clapper
%global libver 0.0
%global libsuffix 0.6.1
%global sover 0
%global gstlib Clapper

%global gst_version 1.20.0
%global gtk4_version 4.10.0
%global meson_version 0.64
%global glib2_version 2.76.0
%global adw_version 1.4.0

%bcond_without server

Name:           clapper
Version:        0.6.1
Release:        0
Summary:        A GNOME media player built using GJS with GTK4
Group:          Productivity/Multimedia/Video/Players
License:        GPL-3.0-or-later
URL:            https://github.com/Rafostar/clapper
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  Mesa-libGL-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gobject-introspection
BuildRequires:  meson >= %{meson_version}
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= %{gst_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{adw_version}

%if %{with server}
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(microdns) >= 0.2.0
%endif

%define altlibver %(sed s/[.]/_/g <<< %{libver})
Requires:       lib%{name}-%{altlibver}-%{sover} = %{version}
Requires:       lib%{name}-gtk-%{altlibver}-%{sover} = %{version}

Requires:       gstreamer >= %{gst_version}
Requires:       gstreamer-plugins-bad >= %{gst_version}
Requires:       gstreamer-plugins-base >= %{gst_version}
Requires:       gstreamer-plugins-good >= %{gst_version}
# Popular video decoders
Recommends:     gstreamer-plugins-libav >= %{gst_version}
# CD Playback
Suggests:       gstreamer-plugins-ugly
# Intel/AMD video acceleration
Suggests:       gstreamer-plugins-vaapi

%global _description %{expand:
A modern media player powered by GStreamer and built for the GNOME desktop environment.}

%package -n lib%{name}-%{altlibver}-%{sover}
Summary:        Media player components
Group:          Productivity/Multimedia/Video/Players
License:        LGPL-2.1-or-later

%package -n typelib-1_0-%{gstlib}-%{altlibver}
Summary:        Introspection bindings for lib%{name}-%{altlibver}-%{sover}
Group:          System/Libraries
License:        LGPL-2.1-or-later
Requires:       lib%{name}-%{altlibver}-%{sover} = %{version}

%package -n lib%{name}-gtk-%{altlibver}-%{sover}
Summary:        GTK media player component
Group:          Productivity/Multimedia/Video/Players
License:        LGPL-2.1-or-later
Requires:       lib%{name}-%{altlibver}-%{sover} = %{version}

%package -n typelib-1_0-%{gstlib}Gtk-%{altlibver}
Summary:        Introspection bindings for lib%{name}-gtk-%{altlibver}-%{sover}
Group:          System/Libraries
License:        LGPL-2.1-or-later
Requires:       lib%{name}-gtk-%{altlibver}-%{sover} = %{version}

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
License:        LGPL-2.1-or-later
Requires:       lib%{name}-%{altlibver}-%{sover} = %{version}
Requires:       lib%{name}-gtk-%{altlibver}-%{sover} = %{version}

%description %{_description}

%description -n lib%{name}-%{altlibver}-%{sover} %{_description}

%description -n typelib-1_0-%{gstlib}-%{altlibver} %{_description}
This subpackage provides the GObject Introspection bindings for
lib%{name}-%{altlibver}-%{sover}.

%description -n lib%{name}-gtk-%{altlibver}-%{sover} %{_description}

%description -n typelib-1_0-%{gstlib}Gtk-%{altlibver} %{_description}
This subpackage provides the GObject Introspection bindings for
lib%{name}-gtk-%{altlibver}-%{sover}.

%description devel %{_description}

This subpackage holds the required files to compile against
lib%{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dserver=%{?with_server:enabled}%{!?with_server:disabled} \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file %{uuid}

%find_lang %{name}-app
%find_lang %{name}-gtk

%ldconfig_scriptlets -n lib%{name}-%{altlibver}-%{sover}
%ldconfig_scriptlets -n lib%{name}-gtk-%{altlibver}-%{sover}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop

%files
%license COPYING-GPL
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/dbus-1/services/%{uuid}.service
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{uuid}*.svg
%{_datadir}/metainfo/%{uuid}.metainfo.xml
%{_datadir}/mime/packages/%{uuid}.xml

%files -n lib%{name}-%{altlibver}-%{sover}
%license COPYING-LGPL
%{_libdir}/lib%{name}-%{libver}.so.%{sover}
%{_libdir}/lib%{name}-%{libver}.so.%{libsuffix}

%{_libdir}/libgst%{name}glcontexthandler.so.%{sover}
%{_libdir}/libgst%{name}glcontexthandler.so.%{libsuffix}
%{_libdir}/gstreamer-1.0/libgst%{name}.so
%{_libdir}/%{name}-%{libver}/

%files -n typelib-1_0-%{gstlib}-%{altlibver}
%{_libdir}/girepository-1.0/%{gstlib}-%{libver}.typelib

%files -n lib%{name}-gtk-%{altlibver}-%{sover}
%license COPYING-LGPL
%{_libdir}/lib%{name}-gtk-%{libver}.so.%{sover}
%{_libdir}/lib%{name}-gtk-%{libver}.so.%{libsuffix}

%files -n typelib-1_0-%{gstlib}Gtk-%{altlibver}
%{_libdir}/girepository-1.0/%{gstlib}Gtk-%{libver}.typelib

%files devel
%{_datadir}/gir-1.0/%{gstlib}-%{libver}.gir
%{_datadir}/gir-1.0/%{gstlib}Gtk-%{libver}.gir
%{_datadir}/vala/vapi/%{name}-%{libver}.{deps,vapi}
%{_datadir}/vala/vapi/%{name}-gtk-%{libver}.{deps,vapi}
%{_includedir}/%{name}-%{libver}/
%{_libdir}/lib%{name}-%{libver}.so
%{_libdir}/lib%{name}-gtk-%{libver}.so
%{_libdir}/libgst%{name}glcontexthandler.so
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_libdir}/pkgconfig/%{name}-gtk-%{libver}.pc

%files lang -f %{name}-app.lang -f %{name}-gtk.lang

%changelog
