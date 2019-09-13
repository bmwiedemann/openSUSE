#
# spec file for package applet-window-appmenu
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.38
%define qt5_version 5.9

Name:           applet-window-appmenu
Version:        0.5.1
Release:        0
Summary:        Plasma 5 applet to show the window appmenu
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/psifidotos/applet-window-appmenu
Source0:        https://github.com/psifidotos/applet-window-appmenu/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  kdeclarative-devel >= %{kf5_version}
BuildRequires:  kdoctools-devel >= %{kf5_version}
BuildRequires:  kglobalaccel-devel >= %{kf5_version}
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kwindowsystem-devel >= %{kf5_version}
BuildRequires:  kxmlgui-devel >= %{kf5_version}
BuildRequires:  libSM-devel
BuildRequires:  plasma-framework-devel >= %{kf5_version}
BuildRequires:  plasma5-workspace-devel >= 5.12
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}

%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels (as a global menu). This plasmoid supports both
latte-dock and standard Plasma panels.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%files
%license LICENSE
%{_kf5_qmldir}/org/kde/private/windowAppMenu
%dir %{_kf5_plugindir}/plasma/applets
%{_kf5_plugindir}/plasma/applets/plasma_applet_windowappmenu.so
%dir %{_kf5_plasmadir}/plasmoids
%{_kf5_plasmadir}/plasmoids/org.kde.windowappmenu
%{_kf5_servicesdir}/plasma-applet-org.kde.windowappmenu.desktop
%{_kf5_appstreamdir}/org.kde.windowappmenu.appdata.xml

%changelog
