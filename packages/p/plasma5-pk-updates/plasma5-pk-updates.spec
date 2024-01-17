#
# spec file for package plasma5-pk-updates
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


Name:           plasma5-pk-updates
Version:        0.3.2+git70
Release:        0
Summary:        Software Update Manager for Plasma
License:        GPL-3.0-or-later
Group:          System/Packages
URL:            https://www.kde.org/
Source:         plasma-pk-updates-%{version}.tar.xz
# Updated translations
Source1:        plasma5-pk-updates-lang.tar.xz
# PATCH-FIX-UPSTREAM
Patch1:         0001-Set-and-use-implicitHeight-instead-of-height.patch
BuildRequires:  PackageKit-Qt5-devel
BuildRequires:  cmake >= 3.0
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  kcoreaddons-devel >= 5.25.0
BuildRequires:  ki18n-devel >= 5.25.0
BuildRequires:  knotifications-devel >= 5.25.0
BuildRequires:  plasma-framework-devel >= 5.25.0
BuildRequires:  solid-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       PackageKit
Recommends:     %{name}-lang = %{version}
# Use a fake version number higher than the last provided apper version (0.9.2)
Provides:       apper = 1.0
Obsoletes:      apper < 1.0
Obsoletes:      apper-lang < 1.0

%description
Plasma applet for software updates using PackageKit.

%lang_package

%prep
%autosetup -p1 -n plasma-pk-updates-%{version} -a 1
echo -e 'find_package(KF5I18n CONFIG REQUIRED)\nki18n_install(po)' >> CMakeLists.txt

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %find_lang pkupdates plasma-pk-updates.lang
  %find_lang plasma_applet_org.kde.plasma.pkupdates plasma-pk-updates.lang

%files lang -f plasma-pk-updates.lang

%files
%license LICENSE
%{_kf5_qmldir}/
%{_kf5_plasmadir}/
%{_kf5_appstreamdir}/
%{_kf5_notifydir}/
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.pkupdates.desktop

%changelog
