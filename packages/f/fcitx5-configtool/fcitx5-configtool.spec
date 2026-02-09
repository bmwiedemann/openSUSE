#
# spec file for package fcitx5-configtool
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        5.1.12
Release:        0
Summary:        Configuration tool for fcitx5
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-configtool
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Patch0:         %{name}-revert-drop-qt5.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zstd
%if 0%{?suse_version} < 1600
BuildRequires:  gcc15-c++
BuildRequires:  libQt5QuickControls2-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  plasma-framework-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5WindowSystem)
%else
BuildRequires:  gcc-c++
BuildRequires:  libplasma6-devel
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  qt6-widgets-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
Obsoletes:      %{name}-qt6 <= 5.10.9
%endif
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
Supplements:    fcitx5
Provides:       fcitx-config-gtk3 = %{version}
Obsoletes:      fcitx-config-gtk3 <= 0.4.10

%description
Configuration tool for fcitx5

%if 0%{?suse_version} < 1600
%package -n kcm_fcitx5
Summary:        Configuration module for fcitx5
Group:          System/I18n/Chinese
Supplements:    (fcitx5 and plasma5-workspace)
Provides:       kcm5-fcitx = %{version}
Provides:       kf5-kcm-fcitx = %{version}
Provides:       kf5-kcm-fcitx-icons = %{version}
Obsoletes:      kcm5-fcitx <= 0.5.6
Obsoletes:      kf5-kcm-fcitx <= 0.5.6
Obsoletes:      kf5-kcm-fcitx-icons <= 0.5.6

%description -n kcm_fcitx5
Configuration module for fcitx5

%else

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

%endif

%prep
%setup -q
%if 0%{?suse_version} < 1600
%patch -P 0 -p 1
%endif

%build
%if 0%{?suse_version} < 1600
%cmake -DUSE_QT6=OFF \
  -DCMAKE_CXX_COMPILER=%{_bindir}/g++-15 \
  -DCMAKE_C_COMPILER=%{_bindir}/gcc-15
%else
%cmake
%endif
%make_build

%install
%cmake_install

%find_lang kcm_fcitx5
%find_lang %{name}
%suse_update_desktop_file kbd-layout-viewer5 Qt KDE Utility DesktopUtility
%suse_update_desktop_file org.fcitx.fcitx5-migrator Qt KDE Utility DesktopUtility

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%if 0%{?suse_version} < 1600
%post -n kcm_fcitx5 -p /sbin/ldconfig
%postun -n kcm_fcitx5 -p /sbin/ldconfig
%else
%post -n %{name}-kcm6 -p /sbin/ldconfig
%postun -n %{name}-kcm6 -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%license LICENSES
%{_bindir}/fcitx5-config-qt
%{_bindir}/fcitx5-migrator
%{_bindir}/kbd-layout-viewer5
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop
%{_libdir}/libFcitx5Migrator.so*
%{_datadir}/applications/kbd-layout-viewer5.desktop

%if 0%{?suse_version} < 1600
%files -n kcm_fcitx5 -f kcm_fcitx5.lang
%{_bindir}/fcitx5-plasma-theme-generator
%dir %{_datadir}/kpackage
%dir %{_datadir}/kpackage/kcms
%dir %{_libdir}/qt5/plugins/plasma
%dir %{_libdir}/qt5/plugins/plasma/kcms
%dir %{_libdir}/qt5/plugins/plasma/kcms/systemsettings
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_fcitx5.so
%{_datadir}/applications/kcm_fcitx5.desktop
%{_datadir}/kpackage/kcms/kcm_fcitx5

%else

%files -n %{name}-kcm6 -f kcm_fcitx5.lang
%{_bindir}/fcitx5-plasma-theme-generator
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_fcitx5.so
%{_datadir}/applications/kcm_fcitx5.desktop
%endif

%changelog
