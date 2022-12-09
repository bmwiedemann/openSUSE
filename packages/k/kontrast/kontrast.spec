#
# spec file for package kontrast
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


%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kontrast
Version:        22.12.0
Release:        0
Summary:        Contrast checker
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/kontrast
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols
%lang_package

%description
Kontrast allows choosing background and text color that are easy to read when
used together.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.kontrast Qt KDE Utility Accessibility

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kontrast/
%{_kf5_applicationsdir}/org.kde.kontrast.desktop
%{_kf5_appstreamdir}/org.kde.kontrast.appdata.xml
%{_kf5_bindir}/kontrast
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.kontrast.svg

%files lang -f %{name}.lang

%changelog
