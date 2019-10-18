#
# spec file for package gnome-sound-recorder
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           gnome-sound-recorder
Version:        3.34.0
Release:        0
Summary:        Sound Recorder
License:        BSD-3-Clause AND LGPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://wiki.gnome.org/Design/Apps/SoundRecorder
Source0:        https://download.gnome.org/sources/gnome-sound-recorder/3.34/%{name}-%{version}.tar.xz
Source99:       gnome-sound-recorder-rpmlintrc

BuildRequires:  appstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.46
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Recommends:     %{name}-lang
BuildArch:      noarch

%description
A simple, modern sound recorder.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -G "Sound Recorder" -r org.gnome.SoundRecorder GNOME AudioVideo Recorder
%find_lang %{name}

%files
%license COPYING
%doc README.md NEWS AUTHORS
%{_bindir}/%{name}
%dir %{_datadir}/org.gnome.SoundRecorder
%{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder
%{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder.data.gresource
%{_datadir}/org.gnome.SoundRecorder/org.gnome.SoundRecorder.src.gresource
%{_datadir}/applications/org.gnome.SoundRecorder.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SoundRecorder.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.SoundRecorder*
%{_datadir}/metainfo/org.gnome.SoundRecorder.appdata.xml

%files lang -f %{name}.lang

%changelog
