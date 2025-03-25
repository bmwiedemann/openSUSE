#
# spec file for package krename
#
# Copyright (c) 2025 SUSE LLC
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

%define kf6_version 6.6.0
%define qt6_version 6.5.0

Name:           krename
Version:        5.0.2git.20250321T014623~262bdbe
Release:        0
Summary:        A batch renamer by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/krename
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libpodofo-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(exiv2) >= 0.27
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(taglib)

%description
KRename is a powerful batch renamer for KDE. It allows you to easily rename
hundreds or even more files in one go. The filenames can be created by parts of
the original filename, numbering the files or accessing hundreds of informations
about the file, like creation date or Exif informations of an image.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

%files
%license LICENSES/*
%doc AUTHORS README.md
%{_kf6_applicationsdir}/org.kde.krename.desktop
%{_kf6_appstreamdir}/org.kde.krename.appdata.xml
%{_kf6_bindir}/krename
%{_kf6_iconsdir}/hicolor/*/apps/krename.png
%dir %{_kf6_sharedir}/kio/
%dir %{_kf6_sharedir}/kio/servicemenus/
%{_kf6_sharedir}/kio/servicemenus/krename_all_nonrec.desktop
%{_kf6_sharedir}/kio/servicemenus/krename_dir_rec.desktop

%files lang -f %{name}.lang

%changelog
