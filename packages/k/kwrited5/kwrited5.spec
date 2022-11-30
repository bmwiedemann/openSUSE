#
# spec file for package kwrited5
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without released
Name:           kwrited5
Version:        5.26.4
Release:        0
Summary:        Daemon listening for wall and write messages
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kwrited-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kwrited-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0

%description
KDE daemon listening for wall and write messages.

%prep
%setup -q -n kwrited-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_AS_EXECUTABLE=OFF -DBUILD_po=OFF
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license LICENSES/*
%{_kf5_plugindir}/
%{_kf5_notifydir}/

%changelog
