#
# spec file for package sound-juicer
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


Name:           sound-juicer
Version:        3.38.0
Release:        0
Summary:        Clean and Lean GNOME CD Ripper
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            http://www.burtonini.com/blog/computers/sound-juicer/
Source0:        https://download.gnome.org/sources/sound-juicer/3.38/%{name}-%{version}.tar.xz
BuildRequires:  brasero-devel
BuildRequires:  fdupes
BuildRequires:  meson
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
Recommends:     gstreamer-plugins-ugly
%glib2_gsettings_schema_requires

%description
GStreamer-based CD ripping tool. Saves audio CDs to Ogg/vorbis.

%lang_package

%prep
%setup -q
translation-update-upstream po %{name}

%build
%meson
%meson_build

%install
%meson_install
# we do not want to pollute /usr/doc as a namespace
rm -rf %{buildroot}%{_prefix}/doc
%suse_update_desktop_file org.gnome.SoundJuicer AudioVideo Player Audio
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS NEWS TODO README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/*
%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/sound-juicer
%{_mandir}/man1/sound-juicer.1%{ext_man}

%files lang -f %{name}.lang

%changelog
