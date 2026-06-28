#
# spec file for package drawy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.19.0
%define qt6_version 6.9.0

%bcond_without released
Name:           drawy
Version:        1.0.2
Release:        0
Summary:        Whiteboard application
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/drawy
Source0:        https://download.kde.org/stable/drawy/%{version}/drawy-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/drawy/%{version}/drawy-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/raw/master/keys/prayag@key1.asc?ref_type=heads
Source2:        drawy.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         0001-Define-soversion-for-drawyconfig.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libzstd)

%description
Drawy lets you create ideas, diagrams, and visual notes on an infinite
whiteboard with a smooth and responsive canvas. You can draw with
pressure-sensitive tablet support, add text, insert images, and use basic
shapes such as rectangles, ellipses, arrows, and lines to organise your content
clearly. You can choose your own color palette and export your work as image
files whenever needed.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# No use for development files
rm -r %{buildroot}%{_includedir}/DrawyCore
rm %{buildroot}%{_kf6_libdir}/*.so

%find_lang %{name} --all-name --with-html

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc CHANGELOG.md
%doc %lang(en) %{_kf6_htmldir}/en/drawy
%{_kf6_applicationsdir}/org.kde.drawy.desktop
%{_kf6_appstreamdir}/org.kde.drawy.metainfo.xml
%{_kf6_bindir}/drawy
%{_kf6_configkcfgdir}/drawyglobalconfig.kcfg
%{_kf6_debugdir}/drawy.categories
%{_kf6_iconsdir}/hicolor/*/apps/drawy.*
%{_kf6_iconsdir}/hicolor/*/mimetypes/application-x-drawy.png
%{_kf6_libdir}/libdrawyconfig.so.*
%{_kf6_libdir}/libdrawygui.so.*
%{_kf6_libdir}/libdrawywidgets.so.*
%{_kf6_libdir}/libstandardformplugin.so.*
%{_kf6_pluginsdir}/drawypluginforms/
%{_kf6_sharedir}/mime/packages/application-x-drawy.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/drawy

%changelog
