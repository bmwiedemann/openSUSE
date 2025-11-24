#
# spec file for package musique
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        1.12
Release:        0
Summary:        A different take on the music player
License:        GPL-3.0-only AND LGPL-2.1-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://flavio.tordini.org/musique
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-taglib2-compatibility.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-tools-linguist
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(mpv) >= 0.29.0
BuildRequires:  pkgconfig(taglib)
Requires:       qt6-sql-sqlite

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
%autosetup -p1

# Remove build time references so build-compare can do its work
YEAR=$(date -u -d "@${SOURCE_DATE_EPOCH}" +%Y)
sed -i "s/^BUILD_YEAR =.*/BUILD_YEAR = $YEAR/" musique.pro

%build
%qmake6 \
  PREFIX=%{_prefix}            \
  QMAKE_LRELEASE=lrelease6     \
  QMAKE_CFLAGS="%{optflags}"   \
  QMAKE_CXXFLAGS="%{optflags}"
%make_build

%install
%qmake6_install
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
