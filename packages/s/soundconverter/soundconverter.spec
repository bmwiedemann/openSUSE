#
# spec file for package soundconverter
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


%global __requires_exclude typelib\\(GConf\\)|typelib\\(Unity\\)
%define pythons python3
Name:           soundconverter
Version:        4.0.5
Release:        0
Summary:        Sound Converter Application for the GNOME Desktop
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://soundconverter.org
Source0:        https://launchpad.net/soundconverter/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-pytest
BuildRequires:  typelib(Gst) = 1.0
BuildRequires:  typelib(GstPbutils) = 1.0
BuildRequires:  typelib(Gtk) = 3.0
Requires:       gstreamer
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
Suggests:       gstreamer-plugins-bad-orig-addon
Suggests:       gstreamer-plugins-ugly-orig-addon

%description
A sound converter application for the GNOME environment.

It reads anything the GStreamer library can read, and offers writing
to WAV, FLAC, MP3, AAC, and Ogg Vorbis, also with the help of GStreamer.

%lang_package

%prep
%autosetup -p1

%build
%python_build

%install
%python_install

%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category X-OutputGeneration \
  --delete-original \
  build/share/applications/%{name}.desktop

rm -f %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled
rm -rf %{buildroot}/usr/share/doc/soundconverter

%fdupes %{buildroot}%{_prefix}

%check
#%%pytest tests

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/org.soundconverter.gschema.xml
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.egg-info

%files lang -f %{name}.lang

%changelog
