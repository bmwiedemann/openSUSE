#
# spec file for package fcitx5-configtool
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


Name:           fcitx5-configtool
Version:        5.0.16
Release:        0
Summary:        Configuration tool for fcitx5
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-configtool
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Patch1:         %{name}-gcc7.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  libQt5QuickControls2-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
Supplements:    fcitx5
Provides:       fcitx-config-gtk3 = %{version}
Obsoletes:      fcitx-config-gtk3 <= 0.4.10

%description
Configuration tool for fcitx5

%if 0%{?sle_version} > 150100 || 0%{?suse_version} >= 1550
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
%endif

%prep
%setup -q
%autopatch -p1

%build
%if 0%{?sle_version} == 150100
%cmake -DENABLE_KCM=OFF
%else
%cmake
%endif
%make_build

%install
%cmake_install
%find_lang org.fcitx.fcitx5.kcm
%find_lang %{name}
%suse_update_desktop_file kbd-layout-viewer5 Qt KDE Utility DesktopUtility
%suse_update_desktop_file org.fcitx.fcitx5-migrator Qt KDE Utility DesktopUtility

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n kcm_fcitx5 -p /sbin/ldconfig
%postun -n kcm_fcitx5 -p /sbin/ldconfig

%files -f %{name}.lang
%license LICENSES
%{_bindir}/fcitx5-config-qt
%{_bindir}/fcitx5-migrator
%{_bindir}/kbd-layout-viewer5
%{_datadir}/applications/org.fcitx.fcitx5-config-qt.desktop
%{_datadir}/applications/org.fcitx.fcitx5-migrator.desktop
%{_libdir}/libFcitx5Migrator.so*
%{_datadir}/applications/kbd-layout-viewer5.desktop

%if 0%{?sle_version} > 150100 || 0%{?suse_version} >= 1550
%files -n kcm_fcitx5 -f org.fcitx.fcitx5.kcm.lang
%{_bindir}/fcitx5-plasma-theme-generator
%dir %{_libdir}/qt5/plugins/kcms
%dir %{_datadir}/kpackage
%dir %{_datadir}/kpackage/kcms
%{_libdir}/qt5/plugins/kcms/kcm_fcitx5.so
%{_datadir}/kpackage/kcms/org.fcitx.fcitx5.kcm
%{_datadir}/kservices5/kcm_fcitx5.desktop
%{_datadir}/metainfo/org.fcitx.fcitx5.kcm.appdata.xml
%endif

%changelog
