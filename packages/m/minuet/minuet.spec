#
# spec file for package minuet
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           minuet
Version:        22.12.1
Release:        0
Summary:        A KDE Software for Music Education
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/minuet
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  pkgconfig(fluidsynth)
# Runtime requirement
Requires:       libqt5-qtquickcontrols2

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
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.minuet Music

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README*
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/minuet/
%{_kf5_applicationsdir}/org.kde.minuet.desktop
%{_kf5_appstreamdir}/org.kde.minuet.appdata.xml
%{_kf5_bindir}/minuet
%{_kf5_iconsdir}/hicolor
%{_kf5_libdir}/libminuetinterfaces.so.*
%{_kf5_plugindir}/minuet/
%{_kf5_sharedir}/minuet/

%files devel
%{_includedir}/minuet/
%{_kf5_libdir}/libminuetinterfaces.so

%files lang -f %{name}.lang

%changelog
