#
# spec file for package krename
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


Name:           krename
Version:        5.0.0
Release:        0
Summary:        A Batch Renamer by KDE
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://userbase.kde.org/KRename
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM servicemenus-files.patch asterios.dramis@gmail.com -- Make the desktop files KDE and XDG compatible
Patch0:         servicemenus-files.patch
# PATCH-FIX-UPSTREAM remove-gplv2-code.diff dmueller@suse.de -- Remove GPLv2 only code (only used for self-testing)
Patch1:         remove-gplv2-code.diff
# PATCH-FIX-UPSTREAM -- add support for exiv2 >= 0.27
Patch2:         0001-Use-cmakedefine01-instead-of-macro_bool_to_01.patch
Patch3:         0002-Fix-building-against-exiv2-0.27.patch
Patch4:         0003-Fix-the-previous-commits-and-the-build-with-exiv2-0..patch
# PATCH-FIX-OPENSUSE
Patch5:         lower-minimum-cmake-version.patch
# PATCH-FIX-UPSTREAM
Patch6:         use-local-cmake-modules-first.patch
# PATCH-FIX-UPSTREAM
Patch7:         Close-the-app-if-the-progress-dialog-is-closed.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  freetype2-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libpodofo-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JS)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(taglib)

%description
KRename is a batch renamer by KDE. It allows renaming many files in
one go. The filenames can be constructed from parts of the original
filename, an increasing number, or accessing file metadata, like
creation date or Exif information of an image.

%prep
%autosetup -p1
# GPLv2 only code, not really needed, lets avoid the license discussion
rm -rf src/modeltest.*

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -r -G "Batch File Renamer" org.kde.krename Qt KDE System FileManager

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md TODO
%{_kf5_applicationsdir}/org.kde.krename.desktop
%{_kf5_appstreamdir}/org.kde.krename.appdata.xml
%{_kf5_bindir}/krename
%{_kf5_iconsdir}/hicolor/*/apps/krename.png
%{_kf5_iconsdir}/locolor/*/apps/krename.png
%{_kf5_servicesdir}/ServiceMenus/

%changelog
