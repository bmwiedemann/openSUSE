#
# spec file for package applet-window-buttons
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

Name:           applet-window-buttons
Version:        0.5.0
Release:        0
Summary:        Plasma 5 applet to show window buttons in panels
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/psifidotos/applet-window-buttons
Source:         https://github.com/psifidotos/applet-window-buttons/archive/v%{version}/%{name}-%{version}.tar.gz
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
BuildRequires:  cmake(KDecoration2) >= 5.12
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}

%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

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
%{_kf5_qmldir}/org/kde/appletdecoration
%dir %{_kf5_plasmadir}/plasmoids
%{_kf5_plasmadir}/plasmoids/org.kde.windowbuttons
%{_kf5_servicesdir}/plasma-applet-org.kde.windowbuttons.desktop
%{_kf5_appstreamdir}/org.kde.windowbuttons.appdata.xml

%changelog
