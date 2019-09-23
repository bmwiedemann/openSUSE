#
# spec file for package kaffeine
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


Name:           kaffeine
Version:        2.0.18
Release:        0
Summary:        VLC-based Multimedia Player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://kaffeine.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE kaffeine-fixsplitter.patch -- GUI improvement (allow more flexibly set splitters)
Patch0:         kaffeine-fixsplitter.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
Requires:       libQt5Sql5-sqlite
Requires:       vlc-noX
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     %{name}-lang = %{version}
Recommends:     vlc-codecs
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?sle_version} >= 120300)
BuildRequires:  pkgconfig(libdvbv5)
%endif

%description
Kaffeine is a media player.
What makes it different from the others is its excellent support of digital TV (DVB).
Kaffeine has a user-friendly interface so that even first-time users can start immediately
playing their movies: from DVD (including DVD menus, titles, chapters, etc.), VCD, or a file.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

# place desktop entry in video and tv
%suse_update_desktop_file -r org.kde.%{name} Qt KDE AudioVideo Video Player TV

%find_lang %{name} --without-kde --with-man
%if 0%{?suse_version} == 1315 && 0%{?sle_version} <= 120200
  # %%kf5_find_htmldocs is only defined since Leap 42.3
  CURDIR=`pwd`
  pushd %{buildroot}%{_kf5_htmldir}
  for i in *; do
    if ! [ -d "%{_datadir}/locale/${i}" ]; then
        echo "Removing unsupported translation %{_kf5_htmldir}/${i}"
        rm -rf "$i"
    elif [ "$i" != "en" ]; then
        echo "%doc %lang($i) %{_kf5_htmldir}/${i}" >> $CURDIR/%{name}.lang
    fi
  done
  echo "%doc %lang(uk) %{_kf5_mandir}/uk" >> $CURDIR/%{name}.lang
  popd
%else
%{kf5_find_htmldocs}
%endif

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc COPYING-DOCS Changelog NOTES README.md
%{_kf5_bindir}/kaffeine
%if 0%{?sle_version} == 120100
%dir %{_kf5_sharedir}/appdata
%endif
%{_kf5_appstreamdir}/org.kde.kaffeine.appdata.xml
%{_kf5_applicationsdir}/org.kde.kaffeine.desktop
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_sharedir}/kaffeine/
%{_kf5_sharedir}/profiles/
%{_kf5_sharedir}/solid/actions/
%{_kf5_htmldir}/en/
%{_kf5_mandir}/man1/*

%files lang -f %{name}.lang

%changelog
