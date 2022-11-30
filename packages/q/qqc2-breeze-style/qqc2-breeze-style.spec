#
# spec file for package qqc2-breeze-style
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
Name:           qqc2-breeze-style
Version:        5.26.4
Release:        0
Summary:        Breeze Style for Qt Quick Controls 2
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/qqc2-breeze-style-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/qqc2-breeze-style-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config) >= 5.76.0
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5QuickTemplates2)
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols2

%description
A Qt Quick Controls 2 style engine that uses the desktop style
to draw controls with QStyle.

%package devel
Summary:        Development Files for the Breeze Qt Quick Controls 2 Style
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules

%description devel
This file contains cmake files to be used by projects that depend on
qqc2-breeze-style.
Usually not needed as it is only a runtime dependency.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5/kirigami/
%{_kf5_plugindir}/kf5/kirigami/org.kde.breeze.so
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/QtQuick/Controls.2/org.kde.breeze/
%{_kf5_qmldir}/org/kde/breeze/
%dir %{_kf5_qmldir}/org/kde/kirigami.2/
%dir %{_kf5_qmldir}/org/kde/kirigami.2/styles/
%{_kf5_qmldir}/org/kde/kirigami.2/styles/org.kde.breeze/

%files devel
%{_kf5_libdir}/cmake/KF5QQC2BreezeStyle/

%changelog
