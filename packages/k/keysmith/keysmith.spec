#
# spec file for package keysmith
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


%bcond_without  released
Name:           keysmith
Version:        23.04.2
Release:        0
Summary:        OTP client
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/keysmith
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  AppStream
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libsodium-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
Requires:       kirigami2

%description
OTP client for Plasma Mobile and Desktop

%lang_package

%prep
%autosetup -p1

%build

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%files
%doc README.md
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.keysmith.desktop
%{_kf5_appstreamdir}/org.kde.keysmith.appdata.xml
%{_kf5_bindir}/keysmith
%{_kf5_iconsdir}/hicolor/*/*/*.svg

%files lang -f %{name}.lang

%changelog
