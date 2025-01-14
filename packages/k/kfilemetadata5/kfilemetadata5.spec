#
# spec file for package kfilemetadata5
#
# Copyright (c) 2021 SUSE LLC
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


# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without ffmpeg
%define qt5_version 5.15.2
%bcond_without released
Name:           kfilemetadata5
Version:        5.116.0
Release:        0
Summary:        Library for extracting Metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         kfilemetadata-%{version}.tar.xz
%if %{with released}
Source1:        kfilemetadata-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  libattr-devel
BuildRequires:  libepub-devel
BuildRequires:  libexiv2-devel >= 0.21
BuildRequires:  pkgconfig
BuildRequires:  taglib-devel >= 1.9
BuildRequires:  cmake(KF5Archive) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_version}
BuildRequires:  cmake(QMobipocket)
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
BuildRequires:  pkgconfig(poppler-qt5)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif

%description
A library for extracting file metadata.

%package devel
Summary:        Development package for kfilemetadata
Requires:       %{name} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
A library for extracting file metadata. Development files

%lang_package

%prep
%autosetup -p1 -n kfilemetadata-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build

%{kf5_find_lang}

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5FileMetaData.so.*
%{_kf5_plugindir}/

%files devel
%{_kf5_includedir}/KFileMetaData/
%{_kf5_libdir}/cmake/KF5FileMetaData/
%{_kf5_libdir}/libKF5FileMetaData.so
%{_kf5_mkspecsdir}/qt_KFileMetaData.pri

%files lang -f %{name}.lang

%changelog
