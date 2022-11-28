#
# spec file for package kgeotag
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


%bcond_without released
Name:           kgeotag
Version:        1.3.1
Release:        0
Summary:        A photo geotagging utility
License:        GPL-3.0-only
URL:            https://kgeotag.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KExiv2)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets) >= 5.14.0
Recommends:     marble

%description
KGeoTag is a standalone geotagging program.
Images can be associated with geographic coordinates
by different means: On the one hand, a matching with
GPX encoded geodata can be done, on the other hand,
the coordinates can be set manually, either via drag
and drop onto a map, via bookmarks or by manually
supplying them. The coordinates can be stored in the
images' Exif header and/or in XMP sidecar files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%if %{with released}
%find_lang %{name}
%endif

%files
%license LICENSES/*
%doc ChangeLog.rst README.md
%{_kf5_applicationsdir}/org.kde.kgeotag.desktop
%{_kf5_appstreamdir}/org.kde.kgeotag.appdata.xml
%{_kf5_bindir}/kgeotag
%{_kf5_htmldir}/en/kgeotag/
%{_kf5_iconsdir}/hicolor/*/apps/kgeotag.png
%{_kf5_kxmlguidir}/kgeotag/
%{_kf5_sharedir}/kgeotag/

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
