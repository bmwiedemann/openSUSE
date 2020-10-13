#
# spec file for package kwrited5
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
Name:           kwrited5
Version:        5.20.0
Release:        0
Summary:        Daemon listening for wall and write messages
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         kwrited-%{version}.tar.xz
%if %{with lang}
Source1:        kwrited-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%license COPYING
%{_kf5_plugindir}/
%{_kf5_notifydir}/

%changelog
