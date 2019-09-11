#
# spec file for package ksudoku
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ksudoku
Version:        19.08.1
Release:        0
Summary:        Program to generate and solve Sudoku puzzles in 2D or 3D
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(glu)
Obsoletes:      ksudoku5 < %{version}
Provides:       ksudoku5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KSudoku is a program that can generate and solve sudoku puzzles. The
word Sudoku means "single number in an alloted place" in Japanese. Some
cells are filled with a number at the beginnning: the remaining are to
be filled by the player using numbers from 1 to 9, without repeating a
number twice on each column, row, or subsquare.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -G "Sudoku Puzzles" org.kde.ksudoku Game LogicGame

%files
%license COPYING*
%config %{_kf5_configdir}/ksudokurc
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/ksudoku/
%{_kf5_applicationsdir}/org.kde.ksudoku.desktop
%{_kf5_appstreamdir}/org.kde.ksudoku.appdata.xml
%{_kf5_bindir}/ksudoku
%{_kf5_iconsdir}/hicolor/*/*/ksudoku*
%{_kf5_kxmlguidir}/ksudoku/
%{_kf5_sharedir}/ksudoku/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
