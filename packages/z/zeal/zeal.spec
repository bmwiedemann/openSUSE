#
# spec file for package zeal
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


Name:           zeal
Version:        2.7.0~git20200517.404c3aa
Release:        0
Summary:        Offline API documentation browser
License:        GPL-3.0-only
Group:          Development/Tools/Other
URL:            https://zealdocs.org
Source0:        %{name}-%{version}.tar.xz
# `help2man zeal > zeal.1` can't be run without X started.
Source9:        zeal.1
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel >= 5.2.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.2.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2.0
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xcb-keysyms)
Requires:       libQt5Sql5-sqlite >= 5.2.0
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description
Zeal is an offline API documentation browser inspired by Dash
(OS X app).
 * Quickly search documentation using Alt+Space (or a customised)
   hotkey to display Zeal from any place in your workspace.
 * Search in multiple sets of documentation at once.
 * Don't be dependent on your internet connection.
 * Integrate Zeal with Emacs, Sublime Text, or Vim. See Usage »
   Editor plugins for details.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -r org.zealdocs.Zeal Office Viewer
%fdupes -s %{buildroot}%{_datadir}

# Man pages:
mkdir -p %{buildroot}%{_mandir}/man1
cp %{SOURCE9} %{buildroot}%{_mandir}/man1

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/applications/org.zealdocs.Zeal.desktop
%{_datadir}/metainfo/org.zealdocs.Zeal.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}*

%changelog
