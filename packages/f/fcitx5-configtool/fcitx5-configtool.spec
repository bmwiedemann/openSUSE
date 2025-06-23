#
# spec file for package fcitx5-configtool
#
# Copyright (c) 2025 SUSE LLC
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


Name:           fcitx5-configtool
Version:        5.1.10
Release:        0
Summary:        Configuration tool for fcitx5
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-configtool
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  libplasma6-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  qt6-widgets-devel
BuildRequires:  update-desktop-files
BuildRequires:  zstd
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
Supplements:    fcitx5
Obsoletes:      %{name}-qt6 <= 5.10.9
Provides:       fcitx-config-gtk3 = %{version}
Obsoletes:      fcitx-config-gtk3 <= 0.4.10

%description
Configuration tool for fcitx5

%package kcm6
Summary:        Configuration module for fcitx5
Group:          System/I18n/Chinese
Supplements:    (fcitx5 and plasma5-workspace)
Supplements:    (fcitx5 and plasma6-workspace)
Obsoletes:      kcm_fcitx5 <= 5.1.9
Provides:       kcm5-fcitx = %{version}
Provides:       kf5-kcm-fcitx = %{version}
Provides:       kf5-kcm-fcitx-icons = %{version}
Obsoletes:      kcm5-fcitx <= 0.5.6
Obsoletes:      kf5-kcm-fcitx <= 0.5.6
Obsoletes:      kf5-kcm-fcitx-icons <= 0.5.6

%description kcm6
Configuration module for fcitx5

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install

%find_lang kcm_fcitx5
%find_lang %{name}
%suse_update_desktop_file kbd-layout-viewer5 Qt KDE Utility DesktopUtility
%suse_update_desktop_file org.fcitx.fcitx5-migrator Qt KDE Utility DesktopUtility

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n %{name}-kcm6 -p /sbin/ldconfig
%postun -n %{name}-kcm6 -p /sbin/ldconfig

%files -f %{name}.lang
%license LICENSES
%{_bindir}/fcitx5-config-qt
%{_bindir}/fcitx5-migrator
%{_bindir}/kbd-layout-viewer5
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop
%{_libdir}/libFcitx5Migrator.so*
%{_datadir}/applications/kbd-layout-viewer5.desktop

%files -n %{name}-kcm6 -f kcm_fcitx5.lang
%{_bindir}/fcitx5-plasma-theme-generator
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_fcitx5.so
%{_datadir}/applications/kcm_fcitx5.desktop

%changelog
