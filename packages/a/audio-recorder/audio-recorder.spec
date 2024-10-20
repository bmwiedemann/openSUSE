#
# spec file for package audio-recorder
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


%define ubuntuversion jammy
Name:           audio-recorder
Version:        3.3.4
Release:        0
Summary:        An audio recorder application for the GNOME 2/3
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://launchpad.net/~audio-recorder
Source:         %{url}/+archive/ubuntu/ppa/+sourcefiles/audio-recorder/%{version}~%{ubuntuversion}/audio-recorder_%{version}~%{ubuntuversion}.tar.gz
# PATCH-FIX-OPENSUSE audio-recorder-correct-desktop-menu.patch badshah400@gmail.com -- Fixes the .desktop file by removing unity related tags from it.
Patch0:         audio-recorder-correct-desktop-menu.patch
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appindicator3-0.1) >= 0.3
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.4
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpulse)
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly

%description
Audio-recorder allows you to record music or audio to
a file. It can record audio from your system's soundcard,
microphones, browsers and webcams. Put simply: if it plays out of
your loudspeakers, you can record it.

It has an advanced timer that can:
* Start, stop or pause recording at a given clock time.
* Start, stop or pause after a time period.
* Stop when the recorded file size exceeds a limit.
* Start recording on voice or sound.
* Stop or pause recording on "silence".

The recording can be automatically controlled by all MPRIS2
compatible players.

This program supports several audio (output) formats such as Ogg Vorbis
audio, FLAC, Opus, MP3 and WAV.

%lang_package

%prep
%autosetup -n trunk -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/*/audio-recorder*.svg
%{_datadir}/pixmaps/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.audio-recorder.gschema.xml
%{_mandir}/man1/%{name}.1%{ext_man}

%files lang -f %{name}.lang

%changelog
