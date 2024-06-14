#
# spec file for package accessibility-inspector
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           accessibility-inspector
Version:        24.05.1
Release:        0
Summary:        Accessibility inspector
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/accessibilityinspector
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(QAccessibilityClient6) >= 0.6.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Accessibility Inspector is an inspector for your application accessibility tree.
It lets you check all the items exposed via At-SPI.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.accessibilityinspector.desktop
%{_kf6_appstreamdir}/org.kde.accessibilityinspector.metainfo.xml
%{_kf6_bindir}/accessibilityinspector
%{_kf6_debugdir}/accessibilityinspector.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.accessibilityinspector.svg
%{_kf6_libdir}/libaccessibilityinspector.so.*

%files lang -f %{name}.lang

%changelog

