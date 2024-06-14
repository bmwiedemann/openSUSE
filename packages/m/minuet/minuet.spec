#
# spec file for package minuet
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
Name:           minuet
Version:        24.05.1
Release:        0
Summary:        A KDE Software for Music Education
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/minuet
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  pkgconfig(fluidsynth)
# Runtime requirement
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
Application for Music Education.

Minuet aims at supporting students and teachers in many aspects
of music education, such as ear training, first-sight reading,
solfa, scales, rhythm, harmony, and improvisation.
Minuet makes extensive use of MIDI capabilities to provide a
full-fledged set of features regarding volume, tempo, and pitch
changes, which makes Minuet a valuable tool for both novice and
experienced musicians.

%package devel
Summary:        Minuet: Build Environment
Requires:       minuet = %{version}

%description devel
Development headers and libraries for Minuet.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%doc README*
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/minuet/
%{_kf6_applicationsdir}/org.kde.minuet.desktop
%{_kf6_appstreamdir}/org.kde.minuet.metainfo.xml
%{_kf6_bindir}/minuet
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_libdir}/libminuetinterfaces.so.*
%{_kf6_plugindir}/minuet/
%{_kf6_sharedir}/minuet/

%files devel
%{_includedir}/minuet/
%{_kf6_libdir}/libminuetinterfaces.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/minuet/

%changelog
