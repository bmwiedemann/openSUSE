#
# spec file for package bluejay
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Callum Farmer <gmbr3@opensuse.org>
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

%define org io.github.ebonjaeger.bluejay
Name:           bluejay
Version:        1.0.3+0
Release:        0
Summary:        Bluetooth manager written in Qt
License:        MPL-2.0
Group:          System/GUI/Other
URL:            https://github.com/EbonJaeger/bluejay
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  kf6-filesystem
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(Qt6QuickControls2)

%description
A Bluetooth manager and Bluez front-end. With it, you can pair devices, connect to and remove devices, turn Bluetooth on and off, and more.
Bluejay is powered by the Qt6 graphical toolkit and KDE Frameworks.

%lang_package

%prep
%autosetup

%build
%cmake_kf6
%kf6_build

%install
%kf6_install
%find_lang %{name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{org}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{org}.svg
%{_datadir}/metainfo/%{org}.metainfo.xml

%files lang -f %{name}.lang

%changelog
