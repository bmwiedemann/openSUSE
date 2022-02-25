#
# spec file for package rage
#
# Copyright (c) 2022 SUSE LLC
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


Name:           rage
Version:        0.4.0
Release:        0
Summary:        A mplayer like video and audio player with some extra bells and whistles
License:        BSD-2-Clause
URL:            https://www.enlightenment.org/about-rage
Source:         https://download.enlightenment.org/rel/apps/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(ecore-evas)
BuildRequires:  pkgconfig(ecore-file)
BuildRequires:  pkgconfig(ecore-imf)
BuildRequires:  pkgconfig(ecore-imf-evas)
BuildRequires:  pkgconfig(ecore-input)
BuildRequires:  pkgconfig(ecore-ipc)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(eet)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(elementary) >= 1.22.3
BuildRequires:  pkgconfig(emotion) >= 1.22.3
BuildRequires:  pkgconfig(ethumb_client)
BuildRequires:  pkgconfig(evas)
Requires:       efl
Requires:       elementary >= 1.22.3
Requires:       evas-generic-loaders >= 1.22.3

%description
Rage is a simple video and audio player intended to be slick yet simplistic, much like Mplayer. You can provide 1 or
more files to play on the command-line or just DND files onto the rage window to insert them into the playlist.
You can get a visual representation of everything on the playlist by hitting the / key, or just hovering your mouse over
the right side of the window. Mouse back over the left side of the window ti dismiss it or press the key again.
It has a full complement of key controls if you see the README for the full list. It will automatically search for
album art for music files, if not already cached, and display that. It even generates thumbnails for the timeline
of a video and allows you to preview the position on mouseover of the position bar at the bottom of the window.

%prep
%autosetup
sed -i 's|icons/hicolor/128x128/apps|%{_datadir}/pixmaps|' data/icons/meson.build

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png

%changelog
