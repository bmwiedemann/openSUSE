#
# spec file for package klevernotes
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


%define kf6_version 6.0
%define qt6_version 6.5

%bcond_without released
Name:           klevernotes
Version:        1.0.0
Release:        0
Summary:        Note taking and management application
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/klevernotes/
Source0:        https://download.kde.org/stable/klevernotes/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/klevernotes/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        klevernotes.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
KleverNotes allows you to create and preview a Markdown note while giving you
the freedom to customize the preview from settings or using a CSS theme.
You can organize your notes however you want with a combination of categories
and groups, which will be directly reflected on your system in the hierarchy of
your KleverNotes storage folders. Simply choose your storage location and
you're ready to write!

You can print your notes, add small sketches and even create specific tasks for
each of them.

Notes are saved as Markdown files in your KleverNotes storage for easy access.
They support the entire CommonMark specification with extensive syntax.
KleverNotes also introduces a small collection of opt-in “plugins” to extend
basic markdown features, such as: code highlighting, note linking, quick
emoji, etc.

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
%{_kf6_applicationsdir}/org.kde.klevernotes.desktop
%{_kf6_appstreamdir}/org.kde.klevernotes.metainfo.xml
%{_kf6_bindir}/klevernotes
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.klevernotes.svg

%files lang -f %{name}.lang

%changelog

