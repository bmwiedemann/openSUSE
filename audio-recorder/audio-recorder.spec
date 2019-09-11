#
# spec file for package audio-recorder
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           audio-recorder
Version:        3.0.5
Release:        0
Summary:        An audio recorder application for the GNOME 2/3
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Utilities
Url:            https://launchpad.net/~audio-recorder
Source:         https://launchpad.net/~audio-recorder/+archive/ubuntu/ppa/+sourcefiles/audio-recorder/%{version}~disco/audio-recorder_%{version}~disco.tar.gz
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
Recommends:     %{name}-lang

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

The recording can be automatically controlled by:
* RhythmBox audio player.
* Banshee audio player.
* Amarok and other MPRIS compatible players.
* Skype. It can automatically record all your Skype calls without
  any user interaction.

This program supports several audio (output) formats such as Ogg Vorbis
audio, FLAC, MP3 and WAV.

User can also control the recorder from command line with
--command <arg> option.

%lang_package

%prep
%setup -q -n trunk
%patch0 -p1

%build
aclocal && autoconf && automake -a
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun

%files
%doc ChangeLog README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/%{name}/
%{_datadir}/glib-2.0/schemas/org.gnome.audio-recorder.gschema.xml
%{_mandir}/man1/%{name}.1%{ext_man}

%files lang -f %{name}.lang

%changelog
