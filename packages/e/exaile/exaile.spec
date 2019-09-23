#
# spec file for package exaile
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define __requires_exclude typelib\\((GtkosxApplication)\\)
%define _name   Exaile
Name:           exaile
Version:        4.0.0
Release:        0
Summary:        Gtk3 Amarok-like music player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
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
BuildRequires:  update-desktop-files
Requires:       gdk-pixbuf-loader-rsvg
Requires:       gstreamer
Requires:       gstreamer-plugins-good
Recommends:     %{name}-lang
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
Recommends:     udisks2
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
BuildRequires:  python2-gobject
Requires:       python2-cairo
Requires:       python2-dbus-python
Requires:       python2-feedparser
Requires:       python2-gobject
Requires:       python2-gobject-Gdk
Requires:       python2-gobject-cairo
Requires:       python2-mutagen >= 1.10
Recommends:     python2-CDDB
Recommends:     python2-Pillow
Recommends:     python2-gpod
%else
BuildRequires:  python
BuildRequires:  python-gobject
Requires:       dbus-1-python
Requires:       python-cairo
Requires:       python-feedparser
Requires:       python-gobject
Requires:       python-gobject-Gdk
Requires:       python-gobject-cairo
Requires:       python-mutagen >= 1.10
Recommends:     python-CDDB
Recommends:     python-Pillow
Recommends:     python-gpod
%endif

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
make %{?_smp_mflags} V=1

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
    %py_compile .
    popd
done

%fdupes %{buildroot}%{_prefix}/
%find_lang %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/org.%{name}.%{_name}.service
%dir %{_sysconfdir}/xdg/%{name}/
%config %{_sysconfdir}/xdg/%{name}/settings.ini
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files lang -f %{name}.lang

%changelog
