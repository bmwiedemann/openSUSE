#
# spec file for package clapper
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


%define typelib  typelib-1_0-GstClapper-1
%define libname  libgstclapper-1_0-0
%define libname2 libgstclapperglbaseimporter0
%define appname  com.github.rafostar.Clapper

Name:           clapper
Version:        0.5.2
Release:        0
Summary:        A GNOME media player built using GJS with GTK4
License:        GPL-3.0-or-later
URL:            https://github.com/Rafostar/clapper
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.18.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

%description
A GNOME media player built using GJS with GTK4 toolkit and powered by GStreamer with OpenGL rendering.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname2} = %{version}
Requires:       %{libname} = %{version}
Requires:       %{typelib} = %{version}

%description devel
%{summary}.

%package -n %{typelib}
Summary:        Clapper library typelib

%description -n %{typelib}
%{summary}.

%package -n %{libname}
Summary:        Library for %{name}
Obsoletes:      libgstclapper-1 < 0.5
Provides:       libgstclapper-1 = 0.5

%description -n %{libname}
%{summary}.

%package -n %{libname2}
Summary:        Library for %{name}

%description -n %{libname2}
%{summary}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{appname}

%ldconfig_scriptlets -n %{libname}
%ldconfig_scriptlets -n %{libname2}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{appname}
%{_datadir}/%{appname}/
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/mime/packages/%{appname}.xml
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%dir %{_libdir}/clapper-1.0
%dir %{_libdir}/clapper-1.0/gst
%dir %{_libdir}/clapper-1.0/gst/plugin
%dir %{_libdir}/clapper-1.0/gst/plugin/importers
%{_libdir}/clapper-1.0/gst/plugin/importers/*.so
%dir %{_libdir}/gstreamer-1.0
%{_libdir}/gstreamer-1.0/*.so

%files -n %{libname}
%dir %{_libdir}/%{appname}
%{_libdir}/%{appname}/*.so.*

%files -n %{libname2}
%{_libdir}/libgstclapperglbaseimporter.so.*

%files -n %{typelib}
%dir %{_libdir}/%{appname}/girepository-1.0
%{_libdir}/%{appname}/girepository-1.0/GstClapper-1.0.typelib

%files devel
%{_libdir}/%{appname}/*.so
%{_libdir}/*.so
%{_datadir}/gir-1.0/GstClapper-1.0.gir

%files lang -f %{appname}.lang

%changelog
