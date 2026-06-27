#
# spec file for package kf6-kmime
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.19.0
%define qt6_version 6.9.0

%define rname kmime
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kmime
Version:        6.27.0
Release:        0
Summary:        Library to assist handling MIME data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
Conflicts:      libKF5Mime5 < %{version}
# Renamed after frameworks 6.26 release
Provides:       kmime = %{version}
# 24.02.0 is the first Qt 6 based release
Obsoletes:      kmime >= 24.02.0

%description
KMime is a library for handling mail messages and newsgroup articles.

%package -n libKF6Mime6
Summary:        Library to assist handling MIME data
Requires:       kf6-kmime >= %{version}
Provides:       libKPim6mime = %{version}
Obsoletes:      libKPim6mime >= 24.02.0

%description  -n libKF6Mime6
KMime is a library for handling mail messages and newsgroup articles.

%package devel
Summary:        Build environment for the KF 6 MIME libraries
Requires:       libKF6Mime6 = %{version}
Provides:       kmime-devel = %{version}
Obsoletes:      kmime-devel >= 24.02.0

%description devel
KMime is a library for handling mail messages and newsgroup articles.
This package provides development files to use libKF6Mime6.

%lang_package -n libKF6Mime6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-qt

%ldconfig_scriptlets -n libKF6Mime6

%files
%{_kf6_debugdir}/kmime.categories
%{_kf6_debugdir}/kmime.renamecategories

%files -n libKF6Mime6
%license LICENSES/*
%{_kf6_libdir}/libKF6Mime.so.*

%files devel
%{_kf6_cmakedir}/KF6Mime/
%{_kf6_includedir}/KMime/
%{_kf6_libdir}/libKF6Mime.so

%files -n libKF6Mime6-lang -f %{name}.lang

%changelog
