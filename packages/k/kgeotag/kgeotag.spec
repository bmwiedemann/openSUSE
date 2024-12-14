#
# spec file for package kgeotag
#
# Copyright (c) 2021 SUSE LLC
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
Name:           kgeotag
Version:        1.7.0
Release:        0
Summary:        A photo geotagging utility
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/kgeotag/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kgeotag.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KExiv2Qt6) >= 5.1.0
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Marble) >= 24.12.0
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Recommends:     marble

%description
KGeoTag is a standalone geotagging program.
Images can be associated with geographic coordinates by different means: On the
one hand, a matching with GPX encoded geodata can be done, on the other hand,
the coordinates can be set manually, either via drag and drop onto a map, via
bookmarks or by manually supplying them. The coordinates can be stored in the
images' Exif header and/or in XMP sidecar files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE -DQT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html

%files
%license LICENSES/*
%doc CHANGELOG.rst README.md
%doc %lang(en) %{_kf6_htmldir}/en/kgeotag
%{_kf6_applicationsdir}/org.kde.kgeotag.desktop
%{_kf6_appstreamdir}/org.kde.kgeotag.appdata.xml
%{_kf6_bindir}/kgeotag
%{_kf6_iconsdir}/hicolor/*/apps/kgeotag.png
%{_kf6_sharedir}/kgeotag/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kgeotag

%changelog
