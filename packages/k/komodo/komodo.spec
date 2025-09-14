#
# spec file for package komodo
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.13
%define qt6_version 6.6

%bcond_without released
Name:           komodo
Version:        1.5.0
Release:        0
Summary:        Todo manager that uses todo.txt specification
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/komodo/
Source0:        https://download.kde.org/stable/komodo/1.5.0/komodo-1.5.0.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/komodo/1.5.0/komodo-1.5.0.tar.xz.sig
Source2:        komodo.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 1.9
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kconfig-imports >= %{kf6_version}
Requires:       kf6-kcoreaddons-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 1.9
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
KomoDo is a todo manager that uses todo.txt specification. It parses any
compliant todo.txt files and turns them into easy to use list of tasks.
KomoDo has built-in help for the todo.txt specification.

Features
- Open and create new todo.txt files
- Add, delete and edit tasks
- Filter and search tasks

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/komodo/
%{_kf6_applicationsdir}/org.kde.komodo.desktop
%{_kf6_appstreamdir}/org.kde.komodo.metainfo.xml
%{_kf6_bindir}/komodo
%{_kf6_debugdir}/komodo.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.komodo.svg

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/komodo

%changelog

