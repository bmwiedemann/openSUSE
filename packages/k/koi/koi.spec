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
Version:        0.2.4
Release:        0
Summary:        Theme scheduling for the KDE Plasma Desktop
License:        LGPL-3.0-only
URL:            https://github.com/baduhai/Koi
Source:         https://github.com/baduhai/Koi/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       hicolor-icon-theme
Requires:       plasma-framework
Requires:       plasma-framework-components
Requires:       plasma-framework-desktoptheme
Requires:       plasma5-desktop
Requires:       plasma5-workspace

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
%cmake
%cmake_build
popd

%install
pushd src
%cmake_install
popd

%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/koi
%{_datadir}/applications/koi.desktop
%{_datadir}/icons/hicolor/scalable/apps/*

%changelog
