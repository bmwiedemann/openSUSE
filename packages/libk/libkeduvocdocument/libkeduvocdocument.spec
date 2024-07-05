#
# spec file for package libkeduvocdocument
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
Name:           libkeduvocdocument
Version:        24.05.2
Release:        0
Summary:        Library for KDE Education Applications
License:        GPL-2.0-or-later
URL:            https://edu.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
This package contains the library which is required by the KDE education
applications.

%package -n libKEduVocDocument5
Summary:        Library for KDE Education Applications
Recommends:     kdeedu-data
# Renamed
Obsoletes:      libkeduvocdocument-lang

%description -n libKEduVocDocument5
This package contains the library which is required by the KDE education
applications.

%package devel
Summary:        Library for KDE Education Applications: Build Environment
Requires:       libKEduVocDocument5 = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop KDE education applications.

%lang_package -n libKEduVocDocument5

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKEduVocDocument5

%files -n libKEduVocDocument5
%license LICENSES/*
%doc README
%{_kf6_libdir}/libKEduVocDocument.so.*

%files devel
%{_includedir}/libkeduvocdocument/
%{_kf6_cmakedir}/libkeduvocdocument/
%{_kf6_libdir}/libKEduVocDocument.so

%files -n libKEduVocDocument5-lang -f %{name}.lang

%changelog
