#
# spec file for package soundconverter
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global __requires_exclude typelib\\(GConf\\)|typelib\\(Unity\\)

Name:           soundconverter
Version:        3.0.0
Release:        0
Summary:        Sound Converter Application for the GNOME Desktop
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://soundconverter.org/
Source0:        https://launchpad.net/soundconverter/trunk/%{version}/+download/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM Only-fetch-profiles-if-GConf-is-still-available.patch -- No longer mandate gconf2
Patch0:         Only-fetch-profiles-if-GConf-is-still-available.patch

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  update-desktop-files
BuildRequires:  typelib(Gst) = 1.0
BuildRequires:  typelib(Gtk) = 3.0

Requires:       gstreamer
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
Suggests:       gstreamer-plugins-bad-orig-addon
Suggests:       gstreamer-plugins-ugly-orig-addon

%description
A sound converter application for the GNOME environment.

It reads anything the GStreamer library can read, and offers writing
to WAV, FLAC, MP3, AAC, and Ogg Vorbis, also with the help of
GStreamer.

%lang_package

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install
chmod a+x %{buildroot}%{_libdir}/%{name}/python/%{name}/*py

%find_lang %{name}
%suse_update_desktop_file -r %{name} AudioVideo AudioVideoEditing
%fdupes %{buildroot}%{_prefix}/

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
%doc ChangeLog README TODO
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/glib-2.0/schemas/org.soundconverter.gschema.xml

%files lang -f %{name}.lang

%changelog
