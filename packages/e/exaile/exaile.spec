#
# spec file for package exaile
#
# Copyright (c) 2025 SUSE LLC
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


%define __requires_exclude typelib\\((GtkosxApplication)\\)
%define _name   Exaile
Name:           exaile
Version:        4.1.3
Release:        0
Summary:        GTK Amarok-like music player
License:        GPL-3.0-or-later
URL:            https://www.exaile.org/
Source:         https://github.com/exaile/exaile/releases/download/%{version}/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE exaile-no-splash-default.patch sor.alexei@meowr.ru -- Do not show splash screen on startup by default.
Patch0:         %{name}-no-splash-default.patch
# PATCH-FEATURE-OPENSUSE exaile-mate-screensaver.patch sor.alexei@meowr.ru -- Make the screensaverpause plugin work with MATE Screensaver.
Patch1:         %{name}-mate-screensaver.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  help2man
BuildRequires:  python3
BuildRequires:  python3-gobject
BuildRequires:  update-desktop-files
Requires:       gdk-pixbuf-loader-rsvg
Requires:       gstreamer
Requires:       gstreamer-plugins-good
Requires:       python3-berkeleydb
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-feedparser
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-mutagen >= 1.10
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
# Will be python3-discid in Exaile 4.1.3
Recommends:     python3-CDDB
Recommends:     python3-Pillow
Recommends:     python3-gpod
Recommends:     python3-zeroconf
Recommends:     udisks2
BuildArch:      noarch

%description
Exaile is a media player aiming to be similar to Clementine, but
written in GTK+.

It incorporates many of the cool things from Amarok (and other
media players) like automatic fetching of album art, handling of
large libraries, lyrics fetching, artist/album information via the
wikipedia, last.fm support, optional iPod support (assuming you
have python-gpod installed).

In addition, Exaile also includes a built in shoutcast directory
browser, tabbed playlists (so you can have more than one playlist
open at a time), blacklisting of tracks (so they don't get scanned
into your library), downloading of guitar tablature from
fretplay.com, and submitting played tracks on your iPod to last.fm.

%lang_package

%prep
%autosetup -p1

%build
%make_build

%install
%make_install \
  LIBINSTALLDIR=%{_datadir} \
  PREFIX=%{_prefix}

dirname $(find %{buildroot}%{_datadir} -type f -name '*.py') | sort -u | while read dir; do
    pushd "$dir"
    # Fix wrong-script-end-of-line-encoding.
    dos2unix *.py
    # Fix python-bytecode-inconsistent-mtime (hacky).
    rm -f *.pyc *.pyo
    touch -c *.py
    %py3_compile .
    popd
done

%fdupes %{buildroot}%{_prefix}/
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/org.%{name}.%{_name}.service
%dir %{_sysconfdir}/xdg/%{name}/
%config %{_sysconfdir}/xdg/%{name}/settings.ini
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files lang -f %{name}.lang

%changelog
