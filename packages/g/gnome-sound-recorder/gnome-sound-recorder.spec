#
# spec file for package gnome-sound-recorder
#
# Copyright (c) 2022 SUSE LLC
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
Version:        43.beta
Release:        0
Summary:        Sound Recorder
License:        BSD-3-Clause AND LGPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://wiki.gnome.org/Design/Apps/SoundRecorder
Source0:        https://download.gnome.org/sources/gnome-sound-recorder/43/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.4
BuildRequires:  pkgconfig(gjs-1.0) >= 1.54.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.39.3
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.6
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.12
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       gjs
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
BuildArch:      noarch

%description
A simple, modern sound recorder.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	--libdir=/usr/unused-in-noarch
	%{nil}
%meson_build

%install
%meson_install
%find_lang org.gnome.SoundRecorder

%check
%meson_test

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
%{_datadir}/metainfo/org.gnome.SoundRecorder.metainfo.xml

%files lang -f org.gnome.SoundRecorder.lang

%changelog
