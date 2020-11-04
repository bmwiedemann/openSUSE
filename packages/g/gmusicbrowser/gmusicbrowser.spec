#
# spec file for package gmusicbrowser
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


# gmusicbrowser has no external API.
%define __provides_exclude perl\\(.*\\)
Name:           gmusicbrowser
Version:        1.1.15
Release:        0
Summary:        Gtk2 jukebox for large music collections
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            http://gmusicbrowser.org/
Source:         http://gmusicbrowser.org/download/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gmusicbrowser-1.1.15-fix-perl-5.24.patch -- Fix an error with perl 5.24 (commit 853840e).
Patch0:         %{name}-1.1.15-fix-perl-5.24.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  perl
BuildRequires:  update-desktop-files
Requires:       typelib-1_0-Gst-1_0
Requires:       typelib-1_0-GstApp-1_0
Requires:       perl(Glib::Object::Introspection)
Requires:       perl(Gtk2)
Recommends:     %{name}-lang
Recommends:     perl(Gtk2::AppIndicator)
Recommends:     perl(Gtk2::Notify)
Recommends:     perl(Gtk2::WebKit)
Recommends:     perl(HTML::Parser)
Recommends:     perl(Locale::gettext)
Recommends:     perl(Net::DBus)
Suggests:       mpv
BuildArch:      noarch
%perl_requires

%description
Customisable jukebox based on Gtk2 for large music collections.

Main features:
 - Made with big libraries in mind.
 - Customisable window layouts.
 - Artist/album lock: restrict playlist to current artist/album.
 - Easy access to songs related to the currently playing song:
   * songs from the same album.
   * album(s) from the same artist(s).
   * songs with same title (other versions, covers, ...).
 - Supports Ogg Vorbis, MP3, FLAC files and other formats.
 - Simple mass-tagging and mass-renaming.
 - Notification icon, with a customisable tip window, which can be
   used to control the player.
 - Customisable SongTree widget for a pretty list of songs.
 - Support multiple genres for a song and multiple artists for each
   song by separating them.
 - Customisable labels can be set for each song (like bootleg,
   live, -'s favourites, ...).
 - Filters with unlimited nesting of conditions.
 - Customisable weighted random mode (based on rating, last time
   played, label, ...).
 - The possibility to act as a icecast server, to listen to your
   music remotely.
 - Plugins: nowplaying (external program song updates), last.fm,
   find pictures, simple lyrics, display Wikipedia artist page and
   search lyrics with Google.

%lang_package

%prep
%setup -q
%patch0 -p1

# Trim Unity actions.
lines=$(( $(grep -m1 -no '^Actions=' %{name}.desktop | sed 's/^\([[:digit:]]*\):.*$/\1/') - 1 ))
head -n $lines %{name}.desktop > %{name}.desktop.new
mv -f %{name}.desktop{.new,}

%build
# Nothing to build.

%install
%make_install \
  docdir=%{buildroot}%{_docdir}/%{name}

rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
%suse_update_desktop_file -r -G %{name} %{name} AudioVideo Music
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/20x20/
%dir %{_datadir}/icons/hicolor/20x20/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
