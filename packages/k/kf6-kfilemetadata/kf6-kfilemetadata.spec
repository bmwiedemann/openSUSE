#
# spec file for package kf6-kfilemetadata
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


%define qt6_version 6.6.0

%define rname kfilemetadata
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without ffmpeg
%bcond_without released
Name:           kf6-kfilemetadata
Version:        6.3.0
Release:        0
Summary:        Library for extracting Metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  libattr-devel
BuildRequires:  libepub-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(exiv2) >= 0.21
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
# Not packaged yet
# BuildRequires:  cmake(QMobipocket6)
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib)
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif

%description
KFileMetaData provides plugins for extracting file metadata.

%package -n libKF6FileMetaData3
Summary:        Library for extracting Metadata
Requires:       kf6-kfilemetadata >= %{version}

%description -n libKF6FileMetaData3
A library for extracting file metadata.

%package devel
Summary:        Development package for kfilemetadata
Requires:       libKF6FileMetaData3 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
A library for extracting file metadata. Development files

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang kfilemetadata6 --all-name

%ldconfig_scriptlets -n libKF6FileMetaData3

%files
%{_kf6_debugdir}/kfilemetadata.categories
%{_kf6_debugdir}/kfilemetadata.renamecategories
%{_kf6_plugindir}/kf6/kfilemetadata/

%files -n libKF6FileMetaData3
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6FileMetaData.so.*

%files devel
%doc %{_kf6_qchdir}/KF6FileMetaData.*
%{_kf6_cmakedir}/KF6FileMetaData/
%{_kf6_includedir}/KFileMetaData/
%{_kf6_libdir}/libKF6FileMetaData.so

%files lang -f kfilemetadata6.lang

%changelog
