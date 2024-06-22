#
# spec file for package breeze6
#
# Copyright (c) 2024 SUSE LLC
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


%global kf6_version 6.0.0
%define qt6_version 6.6.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released

# Breeze6 builds a decoration plugin compatible with KF5/Qt5
%bcond_without plasma5
%if %{with plasma5}
%define kf5_version 5.103.0
%define qt5_version 5.15.2
%endif
%define rname breeze
Name:           breeze6
Version:        6.1.0
Release:        0
Summary:        Plasma Desktop artwork, styles and assets
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# W: desktopfile-without-binary /usr/share/applications/kcm_breezedecoration.desktop
BuildRequires:  kf6-kcmutils >= %{kf6_version}
# Needed for Plasma/LookAndFeel service type declaration (kde#367923)
BuildRequires:  plasma6-framework >= %{_plasma6_bugfix}
BuildRequires:  pkgconfig
%if %{with plasma5}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5FrameworkIntegration) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
%endif
BuildRequires:  cmake(KDecoration2) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FrameworkIntegration) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       breeze6-cursors >= %{version}
Requires:       breeze6-style >= %{version}
Requires:       kf6-breeze-icons >= %{kf6_version}
Recommends:     breeze6-decoration >= %{version}
Recommends:     breeze6-wallpapers >= %{version}
Provides:       breeze = %{version}
Obsoletes:      breeze < %{version}

%description
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.

%package -n breeze6-cursors
Summary:        Plasma Desktop artwork, styles and assets
Provides:       breeze5-cursors = %{version}
Obsoletes:      breeze5-cursors < %{version}
BuildArch:      noarch

%description -n breeze6-cursors
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze cursor theme.

%package -n breeze6-style
Summary:        Plasma Desktop artwork, styles and assets
Requires:       kconf_update6
Provides:       breeze5-style = %{version}
Obsoletes:      breeze5-style < %{version}
Obsoletes:      breeze5-style-lang < %{version}

%description -n breeze6-style
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze style, color-scheme and aditional assets.

%package -n breeze6-wallpapers
Summary:        Plasma Desktop artwork, styles and assets
Provides:       breeze5-wallpapers = %{version}
Obsoletes:      breeze5-wallpapers < %{version}
BuildArch:      noarch

%description -n breeze6-wallpapers
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze wallpaper theme.

%package -n breeze6-decoration
Summary:        Plasma Desktop artwork, styles and assets
Obsoletes:      breeze5-decoration < %{version}

%description -n breeze6-decoration
Artwork, styles and assets for the Breeze visual style for the Plasma Desktop.
This package provides Breeze KWin decoration.



# NOTE: The CMake files were split from breeze*-style and don't require anything on purpose.
# Otherwise, BuildRequires: cmake(Breeze) would pull some Qt5 and KF5 packages.
%package devel
Summary:        Information about breeze setup
Conflicts:      breeze5-style < 6.0.0

%description devel
This package ships a CMake config file used to get information about Breeze.

%lang_package -n breeze6-style

%prep
%autosetup -p1 -n %{rname}-%{version}

# Empty file used by the breeze6 packages
cat >> meta_package << EOF
This is a meta package, it does not contain any file
EOF

%build
%cmake_kf6 \
  -DBUILD_QT6:BOOL=TRUE \
%if %{with plasma5}
  -DBUILD_QT5:BOOL=TRUE
%else
  -DBUILD_QT5:BOOL=FALSE
%endif

%kf6_build

%install
%kf6_install

%find_lang breeze6-style --all-name

%fdupes %{buildroot}

# TODO remove when breeze5 decoration won't be needed
mv %{buildroot}%{_kf6_applicationsdir}/kcm_breezedecoration.desktop %{buildroot}%{_kf6_applicationsdir}/kcm_breezedecoration6.desktop

%files
%doc meta_package

%files -n breeze6-cursors
%license LICENSES/*
%{_kf6_iconsdir}/breeze_cursors
%{_kf6_iconsdir}/Breeze_Light/

%files -n breeze6-style
%license LICENSES/*
%{_kf6_applicationsdir}/breezestyleconfig.desktop
%{_kf6_bindir}/breeze-settings6
%{_kf6_iconsdir}/hicolor/scalable/apps/breeze-settings.svgz
%dir %{_kf6_plugindir}/kstyle_config
%{_kf6_plugindir}/kstyle_config/breezestyleconfig.so
%dir %{_kf6_plugindir}/styles
%if %{with plasma5}
%dir %{_kf5_plugindir}/styles
%{_kf5_plugindir}/styles/breeze5.so
%endif
%{_kf6_plugindir}/styles/breeze6.so
%dir %{_kf6_sharedir}/QtCurve
%{_kf6_sharedir}/QtCurve/Breeze.qtcurve
%dir %{_kf6_sharedir}/color-schemes
%{_kf6_sharedir}/color-schemes/BreezeClassic.colors
%{_kf6_sharedir}/color-schemes/BreezeDark.colors
%{_kf6_sharedir}/color-schemes/BreezeLight.colors
%dir %{_kf6_sharedir}/kstyle
%dir %{_kf6_sharedir}/kstyle/themes
%{_kf6_sharedir}/kstyle/themes/breeze.themerc

%files -n breeze6-wallpapers
%license LICENSES/*
%dir %{_kf6_sharedir}/wallpapers
%{_kf6_sharedir}/wallpapers/Next/

%files -n breeze6-decoration
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_breezedecoration6.desktop
%dir %{_kf6_plugindir}/org.kde.kdecoration2.kcm
%{_kf6_plugindir}/org.kde.kdecoration2.kcm/kcm_breezedecoration.so
%dir %{_kf6_plugindir}/org.kde.kdecoration2
%{_kf6_plugindir}/org.kde.kdecoration2/org.kde.breeze.so

%files devel
%{_kf6_cmakedir}/Breeze/

%files -n breeze6-style-lang -f breeze6-style.lang

%changelog
