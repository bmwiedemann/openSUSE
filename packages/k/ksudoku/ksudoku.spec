#
# spec file for package ksudoku
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           ksudoku
Version:        24.05.1
Release:        0
Summary:        Program to generate and solve Sudoku puzzles in 2D or 3D
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ksudoku
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(opengl)
Obsoletes:      ksudoku5 < %{version}
Provides:       ksudoku5 = %{version}

%description
KSudoku is a program that can generate and solve sudoku puzzles. The
word Sudoku means "single number in an alloted place" in Japanese. Some
cells are filled with a number at the beginnning: the remaining are to
be filled by the player using numbers from 1 to 9, without repeating a
number twice on each column, row, or subsquare.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license COPYING*
%config %{_kf6_configdir}/ksudokurc
%doc %lang(en) %{_kf6_htmldir}/en/ksudoku/
%{_kf6_applicationsdir}/org.kde.ksudoku.desktop
%{_kf6_appstreamdir}/org.kde.ksudoku.appdata.xml
%{_kf6_bindir}/ksudoku
%{_kf6_iconsdir}/hicolor/*/*/ksudoku*
%{_kf6_sharedir}/ksudoku/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ksudoku/

%changelog
