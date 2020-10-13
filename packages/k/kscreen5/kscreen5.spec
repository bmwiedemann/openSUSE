#
# spec file for package kscreen5
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


%bcond_without lang
Name:           kscreen5
Version:        5.20.0
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Screen management software by KDE
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         kscreen-%{version}.tar.xz
%if %{with lang}
Source1:        kscreen-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules >= 1.6.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Screen) >= %{_plasma5_version}
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.4.0
BuildRequires:  cmake(Qt5Sensors) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
Requires:       kded
Requires:       libkscreen2-plugin >= %{_plasma5_version}
Recommends:     %{name}-lang
Recommends:     %{name}-plasmoid
Supplements:    packageand(libkscreen2-plugin:plasma5-workspace)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       kscreen = %{version}
Obsoletes:      kscreen < %{version}
%else
Conflicts:      kscreen
%endif

%description
KScreen handles screen management for both X11 and Wayland sessions, including rotation, size, refresh rate, and scaling.

%lang_package
%prep
%setup -q -n kscreen-%{version}

%package plasmoid
Summary:        Plasma widget to control screen configuration
Group:          System/GUI/KDE
Requires:       %{name} = %{version}

%description plasmoid
This package provides a Plasma widget to control common screen configuration options.

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

%files
%license COPYING*
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_bindir}/kscreen-console
%{_kf5_plugindir}/
%{_kf5_sharedir}/kpackage/kcms/kcm_kscreen/
%dir %{_kf5_sharedir}/kded_kscreen/
%dir %{_kf5_sharedir}/kded_kscreen/qml
%{_kf5_sharedir}/kded_kscreen/qml/*.qml
%{_kf5_servicesdir}/
%{_kf5_debugdir}/kscreen.categories
%{_kf5_appstreamdir}/org.kde.kscreen.appdata.xml

%files plasmoid
%license COPYING*
%dir %{_kf5_plasmadir}/plasmoids/
%dir %{_kf5_plasmadir}/plasmoids/org.kde.kscreen
%{_kf5_plasmadir}/plasmoids/org.kde.kscreen/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
