#
# spec file for package kphotoalbum
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kphotoalbum
Version:        5.5
Release:        0
Summary:        A photo administration utility
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            http://www.kphotoalbum.org/
Source:         http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.2.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons) >= 5.44.0
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KDcraw)
BuildRequires:  cmake(KF5KGeoMap)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kipi)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets) >= 5.9.0
BuildRequires:  cmake(Qt5Xml)
Requires:       kipi-plugins
Requires:       sqlite3

%description
KPhotoAlbum is a tool to help describe images, and to search in the pile
of images. With KPhotoAlbum it is today possible to find any image
in less than 5 seconds, let that be an image with a special person,
an image from a special place, or even both.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%find_lang %{name}
%kf5_find_htmldocs
%suse_update_desktop_file org.kde.%{name} Graphics Photography
%suse_update_desktop_file org.kde.%{name}-import Graphics Photography

%fdupes -s %{buildroot}

%files
%license COPYING
%doc ChangeLog README.md
%{_kf5_applicationsdir}/*
%{_kf5_bindir}/*
%{_kf5_iconsdir}/??color/*/*/*.png
%{_kf5_configdir}/kphotoalbumrc
%{_kf5_htmldir}/en/kphotoalbum/
%{_kf5_kxmlguidir}/kphotoalbum/
%{_kf5_sharedir}/kphotoalbum/
%{_kf5_appstreamdir}/org.kde.kphotoalbum.appdata.xml

%files lang -f %{name}.lang

%changelog
