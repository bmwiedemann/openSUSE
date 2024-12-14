#
# spec file for package kphotoalbum
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
Name:           kphotoalbum
Version:        6.0.0
Release:        0
Summary:        A photo administration utility
License:        GPL-2.0-or-later
URL:            https://www.kphotoalbum.org/
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kphotoalbum.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KDcrawQt6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Marble) >= 24.12.0
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libvlc)
Requires:       qt6-sql-sqlite >= %{qt6_version}
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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html

# Fix rpmlint warning text file has executable bits
chmod 644 %{buildroot}%{_kf6_applicationsdir}/org.kde.kphotoalbum.open-raw.desktop

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc CHANGELOG.md README.md
%{_kf6_applicationsdir}/*
%{_kf6_appstreamdir}/org.kde.kphotoalbum.appdata.xml
%{_kf6_bindir}/*
%{_kf6_configdir}/kphotoalbumrc
%{_kf6_htmldir}/en/kphotoalbum/
%{_kf6_iconsdir}/hicolor/*/*/*.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kphotoalbum.svg
%{_kf6_libdir}/libkpabase.so
%{_kf6_libdir}/libkpaexif.so
%{_kf6_libdir}/libkpathumbnails.so
%{_kf6_sharedir}/kphotoalbum/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kphotoalbum/

%changelog
