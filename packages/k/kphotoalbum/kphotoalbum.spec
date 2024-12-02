#
# spec file for package kphotoalbum
#
# Copyright (c) 2023 SUSE LLC
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


# Temporarily disabled until kphotoalbum gets a Qt6-based release
%bcond_with marble
#
%bcond_without released
Name:           kphotoalbum
Version:        5.13.0
Release:        0
Summary:        A photo administration utility
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.kphotoalbum.org/
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kphotoalbum.keyring
%endif
BuildRequires:  QtAV-devel
BuildRequires:  cmake >= 3.18.0
BuildRequires:  extra-cmake-modules > 5.92
BuildRequires:  fdupes
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons) >= 5.78.0
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KDcraw)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
%if %{with marble}
BuildRequires:  cmake(Marble)
%endif
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libvlc)
Requires:       sqlite3
Recommends:     marble

%description
KPhotoAlbum is a tool to help describe images, and to search in the pile
of images. With KPhotoAlbum it is today possible to find any image
in less than 5 seconds, let that be an image with a special person,
an image from a special place, or even both.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}
%{kf5_find_htmldocs}

# Fix rpmlint warning text file has executable bits
chmod 644 %{buildroot}%{_kf5_applicationsdir}/org.kde.kphotoalbum.open-raw.desktop

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc CHANGELOG.md README.md
%{_kf5_applicationsdir}/*
%{_kf5_appstreamdir}/org.kde.kphotoalbum.appdata.xml
%{_kf5_bindir}/*
%{_kf5_configdir}/kphotoalbumrc
%{_kf5_htmldir}/en/kphotoalbum/
%{_kf5_iconsdir}/hicolor/*/*/*.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kphotoalbum.svg
%{_kf5_libdir}/libkpabase.so
%{_kf5_libdir}/libkpaexif.so
%{_kf5_libdir}/libkpathumbnails.so
%{_kf5_sharedir}/kphotoalbum/

%files lang -f %{name}.lang

%changelog
