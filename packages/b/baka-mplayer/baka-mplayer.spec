#
# spec file for package baka-mplayer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           baka-mplayer
Version:        2.0.4
Release:        0
Summary:        A media player with UI using libmpv
License:        GPL-2.0-or-later AND Apache-2.0
Group:          Productivity/Multimedia/Video/Players
URL:            http://bakamplayer.u8sand.net/
Source0:        https://github.com/u8sand/Baka-MPlayer/archive/v%{version}.tar.gz#/Baka-MPlayer-%{version}.tar.gz
Patch0:         ceil.patch
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(mpv)

%description
Baka MPlayer is a libmpv-based multimedia player. It supports gesture
seeking, desktop dimming, hardware accelerated playback (vdpau,
vaapi, vda) and Youtube playback support (and others).

%prep
%setup -q -n Baka-MPlayer-%{version}
%patch0 -p1

%build
%qmake5 src/Baka-MPlayer.pro CONFIG+="release install_translations man.extra" \
    lupdate=lupdate-qt5 lrelease=lrelease-qt5  \
    DOCDIR=%{_docdir}

%make_jobs

%install
%qmake5_install
%suse_update_desktop_file %{name} AudioVideo Video Player

%files
%license LICENSE
%doc DOCS/%{name}.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}

%changelog
