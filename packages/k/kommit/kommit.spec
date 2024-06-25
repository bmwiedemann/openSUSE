#
# spec file for package kommit
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Matteo De Carlo
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
Name:           kommit
Version:        1.6.0
Release:        0
Summary:        Graphical Git Client
License:        GPL-3.0-only
URL:            https://apps.kde.org/kommit
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kommit.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(DolphinVcs)
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Charts) >= %{qt6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libgit2) >= 1.0

%description
Graphical Git Client

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name --with-html

%ldconfig_scriptlets

%files
%doc README.md
# Docs looks broken in upstream release
# %%doc %%lang(en) %%{_kf6_htmldir}/en/
%license LICENSE
%{_kf6_applicationsdir}/org.kde.kommit.desktop
%{_kf6_applicationsdir}/org.kde.kommit.diff.desktop
%{_kf6_applicationsdir}/org.kde.kommit.merge.desktop
%{_kf6_appstreamdir}/org.kde.kommit.appdata.xml
%{_kf6_bindir}/kommit
%{_kf6_bindir}/kommitdiff
%{_kf6_bindir}/kommitmerge
%{_kf6_debugdir}/kommit.categories
%{_kf6_iconsdir}/hicolor/*/apps/kommit.*
%{_kf6_iconsdir}/hicolor/scalable/actions/*.svg
%{_kf6_libdir}/libkommit.so.*
%{_kf6_libdir}/libkommitdiff.so.*
%{_kf6_libdir}/libkommitgui.so.*
%{_kf6_libdir}/libkommitwidgets.so.*
%dir %{_kf6_plugindir}/dolphin
%dir %{_kf6_plugindir}/dolphin/vcs
%{_kf6_plugindir}/dolphin/vcs/kommitdolphinplugin.so

%files lang -f %{name}.lang
# %%exclude %%{_kf6_htmldir}/en/

%changelog
