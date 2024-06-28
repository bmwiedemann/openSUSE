#
# spec file for package koi
#
# Copyright (c) 2023 SUSE LLC
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


Name:           koi
Version:        0.3.1
Release:        0
Summary:        Theme scheduling for the KDE Plasma Desktop
License:        LGPL-3.0-only
URL:            https://github.com/baduhai/Koi
Source0:        https://github.com/baduhai/Koi/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
Requires:       hicolor-icon-theme
Requires:       libplasma6-components
Requires:       libplasma6-desktoptheme
Requires:       plasma6-desktop
Requires:       plasma6-workspace

%description
Koi is a program designed to provide the KDE Plasma Desktop functionality
to automatically switch between light and dark themes. Koi is under active
development, and while it is stable enough to use daily, expect bugs. Koi is
designed to be used with Plasma, and while some features may function under
different desktop environments, they are unlikely to work and untested.

%prep
%autosetup -p1 -n Koi-%{version}

%build
pushd src
%cmake_kf6

%kf6_build
popd

%install
pushd src
%kf6_install
popd

%files
%license LICENSE
%doc README.md
%{_bindir}/koi
%{_datadir}/applications/koi.desktop
%{_datadir}/icons/hicolor/scalable/apps/koi.svg
%{_datadir}/icons/hicolor/scalable/apps/koi_tray.svg

%changelog
