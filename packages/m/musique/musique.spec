#
# spec file for package musique
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


Name:           musique
Version:        1.10
Release:        0
Summary:        A different take on the music player
License:        GPL-3.0-only AND LGPL-2.1-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://flavio.tordini.org/musique
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(mpv) >= 0.29.0
BuildRequires:  pkgconfig(taglib)

%description
Musique is a music player designed by and for people that love
music. Musique does its best to stay out the way and keep you
focused on the only thing that really matters: Music.
You need to try it to really get it.
To set expectations right — Musique is not about podcasts or
internet radio; it's not about managing mobile devices and it has
no integrated music store.
It's about listening to beautiful music.

%lang_package

%prep
%setup -q

%if 0%{?suse_version} < 1500
SOURCE_DATE="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
export SOURCE_DATE_EPOCH="$(date -d "$SOURCE_DATE" '+%%s')"
%endif
# Remove build time references so build-compare can do its work
FAKE_BUILDDATE="$(LC_ALL=C date -u -d "@${SOURCE_DATE_EPOCH}" '+%%b %%e %%Y')"
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" src/aboutview.cpp

%build
%qmake5 \
  PREFIX=%{_prefix}            \
  QMAKE_CFLAGS="%{optflags}"   \
  QMAKE_CXXFLAGS="%{optflags}"
%make_build

%install
%qmake5_install
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc CHANGES TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/locale/
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}*

%files lang
%{_datadir}/%{name}/locale/

%changelog
