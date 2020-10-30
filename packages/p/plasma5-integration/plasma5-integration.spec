#
# spec file for package plasma5-integration
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without lang
Name:           plasma5-integration
Version:        5.20.2
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-integration-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-integration-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.17.0
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Gui-private-headers-devel >= 5.5.0
BuildRequires:  libQt5QuickControls2-devel
BuildRequires:  cmake(Breeze) >= %{_plasma5_version}
BuildRequires:  cmake(KF5Config) >= 5.17.0
BuildRequires:  cmake(KF5ConfigWidgets) >= 5.17.0
BuildRequires:  cmake(KF5I18n) >= 5.17.0
BuildRequires:  cmake(KF5IconThemes) >= 5.17.0
BuildRequires:  cmake(KF5KIO) >= 5.17.0
BuildRequires:  cmake(KF5Notifications) >= 5.17.0
BuildRequires:  cmake(KF5Wayland) >= 5.5.0
BuildRequires:  cmake(KF5WidgetsAddons) >= 5.17.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.17.0
BuildRequires:  cmake(Qt5DBus) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.5.0
BuildRequires:  libQt5PlatformSupport-private-headers-devel  >= 5.5.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)

%description
Plasma Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%package plugin
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Group:          System/GUI/KDE
Requires:       hack-fonts
Requires:       noto-sans
%requires_eq libQt5Gui5
Recommends:     %{name}-plugin-lang

%description plugin
Plasma Integration is a set of plugins responsible for better
integration of Qt applications when running on a
KDE Plasma workspace.

Applications do not need to link to this directly.

%lang_package -n plasma5-integration-plugin

%prep
%setup -q -n plasma-integration-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%if %{with lang}
%find_lang plasmaintegration5
%endif

%files plugin
%license COPYING*
%{_kf5_plugindir}/
%{_kf5_sharedir}/kconf_update/

%if %{with lang}
%files -n plasma5-integration-plugin-lang -f plasmaintegration5.lang
%endif

%changelog
