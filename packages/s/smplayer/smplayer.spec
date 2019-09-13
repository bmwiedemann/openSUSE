#
# spec file for package smplayer
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


Name:           smplayer
Version:        19.5.0
Release:        0
Summary:        Complete frontend for MPV
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://smplayer.info/
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE smplayer-makeflags.patch
Patch0:         %{name}-makeflags.patch
# PATCH-FEATURE-OPENSUSE smplayer-defaults.patch sor.alexei@meowr.ru -- Use PulseAudio, system Qt5 theme, and "Papirus" icon theme by default.
Patch1:         %{name}-defaults.patch
# PATCH-FIX-UPSTREAM smplayer-add_kde_protocols_to_desktop_file.patch -- To play network shared video correctly: #PM-48.
Patch2:         %{name}-add_kde_protocols_to_desktop_file.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
# Either mpv >= 0.6.2 or MPlayer >= 1.0rc4_r32607.
Requires:       mpv >= 0.6.2
Recommends:     smplayer-lang
Recommends:     smplayer-skins
Suggests:       smplayer-themes
# smplayer-core was last used in openSUSE 13.2.
Provides:       smplayer-core = %{version}
Obsoletes:      smplayer-core < %{version}
# smplayer-qt5 was last used in openSUSE 13.2.
Provides:       smplayer-qt5 = %{version}
Obsoletes:      smplayer-qt5 < %{version}
Obsoletes:      smplayer-qt5-lang < %{version}

%description
SMPlayer is a front-end for MPV/MPlayer, from basic features like
playing videos, DVDs, and VCDs to more advanced features like support
for MPV filters and more.

SMPlayer remembers the settings of all files you play. Opening a
movie again will resume at the same point it was left, and with the
same chosen audio track, subtitles and volume level.

%lang_package

%prep
%autosetup -p1

# Fix CRLF in .txt files.
sed -i 's/\r$//' *.txt

find . -type f -name '*.pro' | while read f; do
cat << EOF >> "$f"

DEFINES += NO_DEBUG_ON_CONSOLE
# I really dislike networks such as Facebook, Twitter.
DEFINES -= SHARE_WIDGET
DEFINES -= UPDATE_CHECKER
QMAKE_CFLAGS += %{optflags}
QMAKE_CXXFLAGS += %{optflags}
EOF
done

%build
make \
  MAKEFLAGS="%{?_smp_mflags} V=1"     \
  QMAKE=%{_libqt5_bindir}/qmake       \
  LRELEASE=%{_libqt5_bindir}/lrelease \
  PREFIX=%{_prefix}

%install
%make_install \
  DOC_PATH=%{_docdir}/%{name} \
  PREFIX=%{_prefix}
rm -rf %{buildroot}%{_docdir}/%{name}/*

mv %{buildroot}%{_bindir}/{,%{name}-}simple_web_server

%suse_update_desktop_file %{name}
%suse_update_desktop_file %{name}_enqueue

%find_lang %{name} --with-qt
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license Copying*.txt
%doc Changelog Finding_subtitles.txt Readme.txt Release_notes.txt Not_so_obvious_things.txt Watching_TV.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-simple_web_server
%{_datadir}/applications/%{name}*.desktop
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations/
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations/

%changelog
