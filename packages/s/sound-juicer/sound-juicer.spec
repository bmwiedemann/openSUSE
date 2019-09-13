#
# spec file for package sound-juicer
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


Name:           sound-juicer
Version:        3.24.0
Release:        0
Summary:        Clean and Lean GNOME CD Ripper
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            http://www.burtonini.com/blog/computers/sound-juicer/
Source0:        http://download.gnome.org/sources/sound-juicer/3.24/%{name}-%{version}.tar.xz
BuildRequires:  brasero-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.49.5
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.21.6
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libdiscid) >= 0.4.0
BuildRequires:  pkgconfig(libmusicbrainz5)
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-ugly
%glib2_gsettings_schema_requires

%description
GStreamer-based CD ripping tool. Saves audio CDs to Ogg/vorbis.

%lang_package

%prep
%setup -q
translation-update-upstream po %{name}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file org.gnome.SoundJuicer AudioVideo Player Audio
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%post
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/*
%{_datadir}/appdata/org.gnome.SoundJuicer.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/sound-juicer
%{_mandir}/man1/sound-juicer.1%{ext_man}

%files lang -f %{name}.lang

%changelog
