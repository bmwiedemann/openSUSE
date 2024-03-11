#
# spec file for package kblackbox
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


%define kf6_version 5.246.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kblackbox
Version:        24.02.0
Release:        0
Summary:        Logic game with elements of hide-and-seek
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kblackbox
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kblackbox5 < %{version}
Provides:       kblackbox5 = %{version}

%description
KBlackbox is a graphical logical game, inspired by emacs's blackbox. It
is a game of hide and seek played on an grid of boxes.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kblackbox/
%{_kf6_applicationsdir}/org.kde.kblackbox.desktop
%{_kf6_appstreamdir}/org.kde.kblackbox.appdata.xml
%{_kf6_bindir}/kblackbox
%{_kf6_iconsdir}/hicolor/*/apps/kblackbox.*
%{_kf6_sharedir}/kblackbox/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kblackbox/

%changelog
