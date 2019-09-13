#
# spec file for package smtube
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%bcond_with restricted
Name:           smtube
Version:        19.6.0
Release:        0
Summary:        Small YouTube Browser
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://smtube.org/
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.1
# PATCH-FIX-OPENSUSE smtube-makeflags.patch
Patch0:         %{name}-makeflags.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
Recommends:     smplayer
Suggests:       MPlayer
Suggests:       dragon
Suggests:       gnome-mplayer
Suggests:       mpv
Suggests:       totem
Suggests:       vlc
Suggests:       youtube-dl
%if 0%{?suse_version} >= 1320 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
%else
BuildRequires:  libQtWebKit-devel
BuildRequires:  libqt4-devel
%endif

%description
SMTube is an application that allows to browse, search and play
YouTube videos. Videos are played back with a media player (by
default SMPlayer) instead of a web browser, this allows better
performance, particularly with HD content.

SMTube is included in SMPlayer's menus, to run it just select
YouTube browser in the Options menu in the SMPlayer main window, or
just press F11.

%lang_package

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} %{name}.1

# Fix CRLF in .txt files.
sed -i 's/\r$//' *.txt

find . -type f -name '*.pro' | while read f; do
%if %{without restricted}
    # Video downloading from YouTube seems to be illegal.
    cat << EOF >> "$f"
DEFINES -= D_BUTTON
EOF
%endif
    cat << EOF >> "$f"
QMAKE_CFLAGS += %{optflags}
QMAKE_CXXFLAGS += %{optflags}
EOF
done

%build
make \
  MAKEFLAGS="%{?_smp_mflags} V=1"      \
%if 0%{?suse_version} >= 1320 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
  QMAKE=%{_libqt5_bindir}/qmake        \
  LRELEASE=%{_libqt5_bindir}/lrelease  \
%else
  QMAKE=%{_libdir}/qt4/bin/qmake       \
  LRELEASE=%{_libdir}/qt4/bin/lrelease \
%endif
  PREFIX=%{_prefix}

%install
%make_install \
  PREFIX=%{_prefix}           \
  DOC_PATH=%{_docdir}/%{name}

install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

rm -rf %{buildroot}%{_docdir}/%{name}/*

%suse_update_desktop_file %{name}
%find_lang %{name} --with-qt

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license Copying.txt
%doc Changelog Readme.txt Release_notes.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang
%{_datadir}/%{name}/translations/

%changelog
