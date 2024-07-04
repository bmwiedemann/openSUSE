#
# spec file for package libplasma6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname libplasma
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libplasma6
Version:        6.1.2
Release:        0
Summary:        Plasma library and runtime components based upon KF6 and Qt6
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.10.0
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
%ifarch %{arm} aarch64
BuildRequires:  pkgconfig(glesv2)
%endif
BuildRequires:  pkgconfig(wayland-client) >= 1.9
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)

%description
Plasma library and runtime components based upon KF6 and Qt6

%package -n libPlasma6
Summary:        Plasma 6 core libraries
Requires:       %{name}-components >= %{version}
Provides:       qt6qmlimport(org.kde.plasma.configuration)
Provides:       qt6qmlimport(org.kde.plasma.configuration.2) = 0
Provides:       qt6qmlimport(org.kde.plasma.plasmoid)
Provides:       qt6qmlimport(org.kde.plasma.plasmoid.2) = 0

%description -n libPlasma6
This package contains the core libraries needed by the Plasma framework.

%package components
Summary:        Plasma QML components
Requires:       %{name}-desktoptheme
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       plasma6-framework = %{version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Provides:       plasma6-framework = %{version}
Obsoletes:      plasma6-framework < %{version}
# Only in KUF before 6.0
Provides:       plasma6-framework-components = %{version}
Obsoletes:      plasma6-framework-components < %{version}

%description components
Plasma QML and runtime components based upon KF6 and Qt6

%package desktoptheme
Summary:        Desktop theme files usable by Plasma 5 and Plasma 6
# Can be used by both plasma 5 and 6
Conflicts:      plasma-framework < 5.110.0
Provides:       plasma-framework-desktoptheme = %{version}
Obsoletes:      plasma-framework-desktoptheme < %{version}
# Only in KUF before 6.0
Provides:       plasma6-framework-desktoptheme = %{version}
Obsoletes:      plasma6-framework-desktoptheme < %{version}

%description desktoptheme
Desktop themes usable by both plasma 5 and plasma 6.

%package devel
Summary:        Plasma library and runtime components
Requires:       libPlasma6 = %{version}
Requires:       plasma6-framework >= %{version}
Requires:       plasma6-framework-components = %{version}
Requires:       cmake(KF6Package) >= %{kf6_version}
Requires:       cmake(KF6WindowSystem) >= %{kf6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}
Conflicts:      plasma-framework-devel
# Only in KUF before 6.0
Provides:       plasma6-framework-devel = %{version}
Obsoletes:      plasma6-framework-devel < %{version}

%description devel
Plasma library and runtime components based upon KF6 and Qt6

%package -n libPlasma6-lang
Summary:        Translations for package libPlasma6
Requires:       libPlasma6 = %{version}
Provides:       libPlasma6-lang-all = %{version}
BuildArch:      noarch
# Only in KUF before 6.0
Provides:       plasma6-framework-lang = %{version}
Obsoletes:      plasma6-framework-lang < %{version}

%description -n libPlasma6-lang
Provides translations for the "libPlasma6" package.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang libplasma6

%pre -n libPlasma6
# boo#1221405: When upgrading from plasma5-workspace to plasma6-workspace,
# preun of the previous package does not know it's actually an upgrade
# (because the package name differs) and it does systemctl --disable --now
# on all units, which immediately kills the session :-( The old preun can't be
# disabled so a hack is needed: Set RefuseManualStop=true on all plasma-* user
# units for the entirety of the transaction. This package should be early
# enough during the transaction as various plasma6 packages require it.
# Only perform the workaround if systemd is running and plasma5-workspace
# is currently still installed.
if [ -x /usr/lib/systemd/systemd-update-helper ] && [ -d /run/systemd/system ] \
   && [ -e /usr/share/qlogging-categories5/plasma-workspace.categories ]; then
  for unit in $(ls /usr/lib/systemd/user/ | grep '^plasma-.*\.service$'); do
    mkdir -p "/run/systemd/user/${unit}.d"
    echo -e '[Unit]\nRefuseManualStop=true' > "/run/systemd/user/${unit}.d/boo1221405.conf"
  done
  touch /run/plasma-boo1221405-workaround
  /usr/lib/systemd/systemd-update-helper user-reload
fi

%ldconfig_scriptlets -n libPlasma6

%posttrans -n libPlasma6
# Remove the temporary dropin files from pre again.
if [ -e /run/plasma-boo1221405-workaround ]; then
  rm /run/systemd/user/plasma-*.service.d/boo1221405.conf
  /usr/lib/systemd/systemd-update-helper user-reload
  rm /run/plasma-boo1221405-workaround
fi

%files components
%{_kf6_debugdir}/plasma-framework.categories
%{_kf6_debugdir}/plasma-framework.renamecategories
%{_kf6_plugindir}/kf6/kirigami/
%{_kf6_plugindir}/kf6/packagestructure/
%{_kf6_qmldir}/org/kde/kirigami/
%{_kf6_qmldir}/org/kde/plasma/

%files -n libPlasma6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libPlasma.so.*
%{_kf6_libdir}/libPlasmaQuick.so.*

%files desktoptheme
%{_kf6_plasmadir}/desktoptheme/

%files devel
%doc %{_kf6_qchdir}/Plasma.*
%{_kf6_cmakedir}/Plasma/
%{_kf6_cmakedir}/PlasmaQuick/
%{_includedir}/Plasma/
%{_includedir}/PlasmaQuick/
%{_kf6_libdir}/libPlasma.so
%{_kf6_libdir}/libPlasmaQuick.so
%{_kf6_sharedir}/kdevappwizard/

%files -n libPlasma6-lang -f libplasma6.lang

%changelog
