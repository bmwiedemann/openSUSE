#
# spec file for package marknote
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
%define kpim6_version 6.1.0

%bcond_without released
Name:           marknote
Version:        1.3.0
Release:        0
Summary:        Rich text notes editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/marknote
Source:         https://download.kde.org/stable/marknote/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/marknote/%{name}-%{version}.tar.xz.sig
Source2:        marknote.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(md4c)
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 1.3.0
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 1.3.0
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
Marknote lets you create rich text notes and easily organise them into notebooks.
You can personalise your notebooks by choosing an icon and accent color for each 
one, making it easy to distinguish between them and keep your notes at your
fingertips. Your notes are saved as Markdown files in your Documents folder,
making it easy to use your notes outside of Marknote as well as inside the app.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.marknote.desktop
%{_kf6_appstreamdir}/org.kde.marknote.metainfo.xml
%{_kf6_bindir}/marknote
%{_kf6_debugdir}/marknote.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.marknote.svg

%files lang -f %{name}.lang

%changelog
