#
# spec file for package xnoise
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _libname libxnoise
%define _soname 0
Name:           xnoise
Version:        0.2.21
Release:        0
Summary:        Feature-rich Amarok-like media player in GTK+ with a smooth GUI
License:        SUSE-GPL-2.0-with-linking-exception
Group:          Productivity/Multimedia/Sound/Players
URL:            https://bitbucket.org/shuerhaaken/xnoise
Source:         https://bitbucket.org/shuerhaaken/%{name}/downloads/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM xnoise-compilation-fix.patch sor.alexei@meowr.ru -- Fix Vala compilation and a 64bit portability issue.
Patch0:         xnoise-compilation-fix.patch
# PATCH-FIX-UPSTREAM xnoise-ListStore.patch dimstar@opensuse.org -- error: `ListStore' is an ambiguous reference between `GLib.ListStore' and `Gtk.ListStore'
Patch1:         xnoise-ListStore.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.34
BuildRequires:  pkgconfig(glib-2.0) >= 2.34
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.34
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.1
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0.1
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.0.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2
BuildRequires:  pkgconfig(libtaginfo_c) >= 0.2.0
BuildRequires:  pkgconfig(sqlite3) >= 3.6
Requires:       %{_libname}%{_soname} = %{version}
Recommends:     %{name}-lang = %{version}
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-libav
Recommends:     gstreamer-plugins-ugly

%description
Xnoise uses a tracklist centric design like Amarok, Clementine, Exaile.
The tracklist is a list of video or music tracks that are played one by one
without being removed (right side of window). This gives you the possibility to
enqueue any track in any order, regardless if they are on the same album or
not. The tracks can be reordered at any time via drag and drop.

The media browser (left side of the window) contains all available media in a
hierarchical tree structure of the available metadata. It is easy to find a
single track, artist or album by going through this tree or by just entering a
search term. From the media browser, music or videos can be dragged into the
tracklist to every position.

Single or multiple tracks, streams, albums or artists can be dragged onto the
tracklist and be reordered. Within the playing track, it's possible to jump to
every position by clicking the position bar.

Xnoise can play every kind of audio/video data that GStreamer can handle.

%lang_package

%package -n %{_libname}%{_soname}
Summary:        Library for xnoise
Group:          System/Libraries

%description -n %{_libname}%{_soname}
This library comes from the xnoise application.

%package -n %{_libname}-devel
Summary:        Development files of libxnoise
Group:          Development/Libraries/C and C++
Requires:       %{_libname}%{_soname} = %{version}

%description -n %{_libname}-devel
The libxnoise development package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking application which will use libxnoise.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/%{name}/

%check
make check %{?_smp_mflags} V=1

%post -n %{_libname}%{_soname} -p /sbin/ldconfig

%postun -n %{_libname}%{_soname} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}_image_extractor_service
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/
%{_mandir}/man?/%{name}.?%{ext_man}

%files lang -f %{name}.lang

%files -n %{_libname}%{_soname}
%{_libdir}/%{_libname}.so.*

%files -n %{_libname}-devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/%{_libname}.so
%{_datadir}/vala/

%changelog
