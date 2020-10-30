#
# spec file for package breeze
#
# Copyright (c) 2020 SUSE LLC
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


# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           breeze
Version:        5.20.2
Release:        0
Summary:        Plasma Desktop artwork, styles and assets
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/breeze-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/breeze-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules >= 0.0.13
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
# Needed for Plasma/LookAndFeel service type declaration (kde#367923)
BuildRequires:  plasma-framework
BuildRequires:  cmake(KDecoration2) >= %{_plasma5_version}
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
Requires:       breeze5-cursors >= %{version}
Requires:       breeze5-icons >= %{version}
Requires:       breeze5-style >= %{version}
Requires:       breeze5-wallpapers >= %{version}
Recommends:     breeze5-decoration >= %{version}

%description
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.

%package -n breeze5-cursors
Summary:        Plasma Desktop artwork, styles and assets
Group:          System/GUI/KDE
BuildArch:      noarch

%description -n breeze5-cursors
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze cursor theme.

%package -n breeze5-style
Summary:        Plasma Desktop artwork, styles and assets
Group:          System/GUI/KDE
Requires:       kconf_update5
Recommends:     breeze5-style-lang

%description -n breeze5-style
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze style, color-scheme and aditional assets.

%package -n breeze5-wallpapers
Summary:        Plasma Desktop artwork, styles and assets
Group:          System/GUI/KDE
BuildArch:      noarch

%description -n breeze5-wallpapers
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze wallpaper theme.

%package -n breeze5-decoration
Summary:        Plasma Desktop artwork, styles and assets
Group:          System/GUI/KDE

%description -n breeze5-decoration
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze KWin decoration.

%lang_package -n breeze5-style

%package -n libbreezecommon5-5
Summary:        Library containing support code for the Breeze Qt5 style
Group:          System/Libraries

%description -n libbreezecommon5-5
Library containing support code for the Breeze Qt5 style.

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %{kf5_find_lang}
%endif
%fdupes %{buildroot}/%{_prefix}

%post   -p /sbin/ldconfig -n libbreezecommon5-5
%postun -p /sbin/ldconfig -n libbreezecommon5-5

%if %{with lang}
%files -n breeze5-style-lang -f %{name}.lang
%license LICENSES/*
%endif

%files -n breeze5-cursors
%license LICENSES/*
%{_kf5_iconsdir}/breeze_cursors
%{_kf5_iconsdir}/Breeze_Snow/

%files -n breeze5-style
%license LICENSES/*
%{_kf5_bindir}/breeze-settings5
%dir %{_kf5_iconsdir}/hicolor/scalable
%dir %{_kf5_iconsdir}/hicolor/scalable/apps
%{_kf5_iconsdir}/hicolor/scalable/apps/breeze-settings.*
%{_kf5_sharedir}/QtCurve/
%{_kf5_sharedir}/color-schemes/
%dir %{_kf5_sharedir}/plasma
%{_kf5_sharedir}/plasma/look-and-feel/
%{_kf5_libdir}/kconf_update_bin/
%{_kf5_sharedir}/kconf_update/
%dir %{_kf5_plugindir}
%{_kf5_plugindir}/kstyle_breeze_config.so
%{_kf5_plugindir}/styles/
%{_kf5_sharedir}/kstyle/
%dir %{_kf5_servicesdir}
%{_kf5_servicesdir}/breezestyleconfig.desktop
%{_kf5_libdir}/cmake/Breeze/
%dir %{_kf5_appstreamdir}/
%{_kf5_appstreamdir}/org.kde.breezedark.desktop.appdata.xml

%files -n breeze5-wallpapers
%license LICENSES/*
%dir %{_kf5_sharedir}/wallpapers
%{_kf5_sharedir}/wallpapers/Next/

%files -n breeze5-decoration
%license LICENSES/*
%dir %{_kf5_plugindir}
%{_kf5_plugindir}/org.kde.kdecoration2/
%dir %{_kf5_servicesdir}
%{_kf5_servicesdir}/breezedecorationconfig.desktop

%files
%license LICENSES/*

%files -n libbreezecommon5-5
%license LICENSES/*
%{_libdir}/libbreezecommon5.so.*

%changelog
